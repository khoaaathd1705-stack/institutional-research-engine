# -*- coding: utf-8 -*-
"""
Module: document_formatter.py
Mục đích: Đóng gói toàn bộ quy chuẩn định dạng tài liệu (Format Packager) theo chuẩn mực duy nhất: TCX (workspace/tcx/).
Cung cấp bộ công cụ tự động hóa hoàn chỉnh:
1. DocumentFormatter.markdown_to_transcript_docx(): Chuyển full_transcript.md sang DOCX chuẩn Corporate F88/TCX.
2. DocumentFormatter.markdown_to_report_docx(): Chuyển analyst_report.md sang DOCX chuẩn Institutional Research 3 phần.
3. DocumentFormatter.lint_document(): Kiểm định tuân thủ ngôn từ trung lập định chế tài chính theo AGENTS.md.
4. DocumentFormatter.compile_workspace(): Đóng gói định dạng một chạm cho toàn bộ thư mục workspace của doanh nghiệp.
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import docx
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.section import WD_ORIENTATION
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Đường dẫn template chuẩn mực duy nhất (Single Reference Benchmark)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR

TCX_BENCHMARK_TEMPLATE_PATHS = [
    PROJECT_ROOT / "workspace/TCX/output/TCX_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx",
    PROJECT_ROOT / "workspace/TCX/output/TCX_Earnings_Call_Q3_2026_Transcript_Bien_Tap.docx",
    PROJECT_ROOT / "workspace/F88/F88_Earnings_Call_Q3_2026_Transcript_Bien_Tap.docx",
]

# Danh mục từ ngữ cảm tính, PR, quảng cáo bị CẤM tuyệt đối theo AGENTS.md
FORBIDDEN_BUZZWORDS = [
    "bùng nổ",
    "bứt phá ngoạn mục",
    "xuất sắc",
    "đột phá",
    "vượt bậc",
    "thần tốc",
    "áp đảo",
    "vững như bàn thạch",
    "điểm sáng rực rỡ",
    "kỳ tích",
    "vô tiền khoáng hậu",
    "thống trị",
    "thắng lợi giòn giã",
    "tuyệt vời",
    "phi thường",
]

# Bảng thuật ngữ thay thế khách quan chuẩn mực tài chính
OBJECTIVE_REPLACEMENTS = {
    "bùng nổ": "tăng trưởng mạnh / tăng tốc",
    "bứt phá ngoạn mục": "tăng trưởng vượt trội / cải thiện đáng kể",
    "xuất sắc": "đạt hiệu quả cao / tích cực",
    "đột phá": "cải thiện rõ rệt / phát triển mới",
    "vượt bậc": "tăng trưởng cao hơn đáng kể",
    "thần tốc": "nhanh chóng / rút ngắn thời gian",
    "áp đảo": "chiếm tỷ trọng chủ đạo / dẫn đầu phân khúc",
    "vững như bàn thạch": "duy trì vị thế an toàn / ổn định",
    "điểm sáng rực rỡ": "chỉ số nổi bật / điểm nhấn tích cực",
    "kỳ tích": "mức cao kỷ lục / mức thực hiện cao",
}

# Quy chuẩn định dạng Quý thống nhất (Quarter Standardization: 3Q26, 4Q26, etc.)
QUARTER_REPLACEMENTS = [
    (r'\b[Qq]uý\s*([1-4])\s*/\s*20(\d{2})\b', r'\1Q\2'),
    (r'\b[Qq]uý\s*([1-4])\s+năm\s+20(\d{2})\b', r'\1Q\2'),
    (r'\b([1-4])Q20(\d{2})\b', r'\1Q\2'),
    (r'\bQ([1-4])/20(\d{2})\b', r'\1Q\2'),
    (r'\bQ([1-4])/(\d{2})\b', r'\1Q\2'),
    (r'\b[Qq]uý\s*([1-4])/(\d{2})\b', r'\1Q\2'),
    (r'\b[Qq]uý\s*3\b', '3Q26'),
    (r'\b[Qq]uý\s*4\b', '4Q26'),
    (r'\b[Qq]uý\s*1\b', '1Q26'),
    (r'\b[Qq]uý\s*2\b', '2Q26'),
    (r'\bQ3\b(?!\s*&|\s*A|\s*và\s*A)', '3Q26'),
    (r'\bQ4\b', '4Q26'),
    (r'\bQ1\b', '1Q26'),
    (r'\bQ2\b', '2Q26'),
]


def standardize_quarters(text: str) -> str:
    """Tự động chuẩn hóa toàn bộ ký hiệu quý về dạng duy nhất: 3Q26, 4Q26, 3Q25, 3Q27..."""
    out = text
    for pat, rep in QUARTER_REPLACEMENTS:
        out = re.sub(pat, rep, out)
    return out

def standardize_number_formatting(text: str) -> str:
    """
    Tự động chuẩn hóa định dạng số theo chuẩn quốc tế tài chính (AGENTS.md):
    - Dấu chấm (.) dùng cho phần thập phân (Decimal point)
    - Dấu phẩy (,) dùng cho phân cách hàng ngàn (Thousands separator)
    """
    # 1. Số có cả phân cách hàng ngàn bằng chấm và thập phân bằng phẩy: 4.057,6 -> 4,057.6; 11.438,2 -> 11,438.2
    def fix_thousands_decimal(m):
        int_part = m.group(1).replace('.', ',')
        dec_part = m.group(2)
        return f"{int_part}.{dec_part}"
    out = re.sub(r'\b(\d{1,3}(?:\.\d{3})+),(\d+)\b', fix_thousands_decimal, text)

    # 2. Phần trăm có dấu phẩy: 21,03% -> 21.03%, +18,1% -> +18.1%
    out = re.sub(r'([+\-–]?\b\d+),(\d+)(%)', r'\1.\2\3', out)

    # 3. Số hàng ngàn có dấu chấm trước các đơn vị: 18.000 tỷ -> 18,000 tỷ; 4.057 tỷ -> 4,057 tỷ; 1.000 tỷ -> 1,000 tỷ
    def fix_thousands_alone(m):
        int_part = m.group(1).replace('.', ',')
        unit = m.group(2)
        return f"{int_part}{unit}"
    out = re.sub(r'\b(\d{1,3}(?:\.\d{3})+)(\s*(?:tỷ|triệu|nghìn|ngàn|đồng|VND|USD|tấn|người|khách|cổ phiếu|điểm|đêm|phòng|con)\b)', fix_thousands_alone, out)

    # 4. Số thập phân có 1 hoặc 2 chữ số sau dấu phẩy (như 481,0 tỷ, 15,0 tỷ, 0,99 lần, 1,15x, 1,5%):
    def fix_decimal_comma(m):
        unit = m.group(3) if m.group(3) else ''
        return f"{m.group(1)}.{m.group(2)}{unit}"
    out = re.sub(r'\b(\d+),(\d{1,2})(?:(?=[^\w])|(?=[xX%])|$)(\s*(?:%|tỷ|triệu|nghìn|ngàn|đồng|VND|USD|tấn|người|khách|cổ phiếu|điểm|đêm|phòng|con|lần|x)\b)?', fix_decimal_comma, out)

    # 5. Xử lý trong bảng Markdown: | 18.000 | hoặc | 4.057,6 | hoặc | 21,03% |
    def fix_table_cell(m):
        val = m.group(2)
        if ',' in val:
            parts = val.split(',')
            return m.group(1) + parts[0].replace('.', ',') + '.' + parts[1] + m.group(3)
        return m.group(1) + val.replace('.', ',') + m.group(3)
    out = re.sub(r'(\|\s*)(\d{1,3}(?:\.\d{3})+(?:,\d+)?)([ \t]*\|)', fix_table_cell, out)

    return out





def safe_save_docx(doc, out_docx_path: str) -> str:
    """Lưu file Word an toàn, tự động tạo file fallback nếu file đang bị khóa bởi Microsoft Word."""
    Path(out_docx_path).parent.mkdir(parents=True, exist_ok=True)
    try:
        doc.save(out_docx_path)
        return out_docx_path
    except PermissionError:
        p = Path(out_docx_path)
        fallback = p.parent / f"{p.stem}_updated{p.suffix}"
        try:
            doc.save(str(fallback))
            print(f"[!] Chú ý: File {p.name} đang mở trong Word, đã lưu cập nhật tại: {fallback.name}")
            return str(fallback)
        except Exception:
            return out_docx_path
    except Exception as e:
        print(f"[!] Lỗi khi lưu file {out_docx_path}: {e}")
        return out_docx_path


def parse_inline_markdown(text: str) -> List[Tuple[str, bool, bool, bool]]:
    """
    Phân tích chuỗi markdown và tách thành các token:
    Return list of (text_segment, is_bold, is_italic, is_code)
    """
    tokens = []
    # Match `code`, **bold**, *italic*
    pattern = re.compile(r'(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)')
    pos = 0
    for match in pattern.finditer(text):
        start, end = match.span()
        if start > pos:
            tokens.append((text[pos:start], False, False, False))
        m_str = match.group()
        if m_str.startswith('`') and m_str.endswith('`'):
            tokens.append((m_str[1:-1], False, False, True))
        elif m_str.startswith('**') and m_str.endswith('**'):
            tokens.append((m_str[2:-2], True, False, False))
        elif m_str.startswith('*') and m_str.endswith('*'):
            tokens.append((m_str[1:-1], False, True, False))
        pos = end
    if pos < len(text):
        tokens.append((text[pos:], False, False, False))
    return tokens


def add_formatted_runs(
    paragraph,
    text: str,
    font_name: str = "Calibri",
    font_size: Pt = Pt(10),
    font_color: Optional[RGBColor] = None,
    bold_all: bool = False,
    italic_all: bool = False
):
    """Thêm text vào paragraph với phân tích inline formatting (bold, italic, code)."""
    tokens = parse_inline_markdown(text)
    for seg, is_b, is_i, is_c in tokens:
        run = paragraph.add_run(seg)
        run.font.name = font_name
        run.font.size = font_size
        run.font.bold = bold_all or is_b
        run.font.italic = italic_all or is_i
        if font_color:
            run.font.color.rgb = font_color
        if is_c:
            run.font.name = "Consolas"
            run.font.size = Pt(font_size.pt * 0.95)



STATUS_COLORS = {
    "[MATCH]": RGBColor(0x1B, 0x5E, 0x20),       # Dark Green
    "[VARIANCE]": RGBColor(0xE6, 0x51, 0x00),    # Orange/Amber
    "[SPEECH_ONLY]": RGBColor(0x0D, 0x47, 0xA1), # Navy Blue
    "[SLIDE_ONLY]": RGBColor(0x45, 0x5A, 0x64),  # Slate Grey
    "[FLAGGED]": RGBColor(0xB7, 0x1C, 0x1C),     # Dark Red
}

def set_cell_shading(cell, color_hex: str):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def parse_markdown_table(lines: List[str]) -> Tuple[List[str], List[List[str]]]:
    """Tách header và rows từ các dòng markdown table."""
    headers = []
    rows = []
    for line in lines:
        clean = line.strip()
        if not clean.startswith("|") or not clean.endswith("|"):
            continue
        cells = [c.strip() for c in clean[1:-1].split("|")]
        if all(re.match(r'^:?-+:?$', c) for c in cells if c):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows

def add_table_to_doc(doc, headers: List[str], rows: List[List[str]]):
    col_count = len(headers)
    table = doc.add_table(rows=len(rows) + 1, cols=col_count)
    table.autofit = False
    set_table_borders(table, "D3D3D3")

    if col_count == 4:
        col_widths = [Inches(3.2), Inches(1.1), Inches(1.1), Inches(5.2)]
    elif col_count == 9:
        col_widths = [
            Inches(0.45), Inches(1.85), Inches(0.60), Inches(1.60),
            Inches(0.85), Inches(1.65), Inches(0.95), Inches(1.05), Inches(1.69)
        ]
    else:
        unit = Inches(10.69 / col_count)
        col_widths = [unit] * col_count

    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i] if i < len(col_widths) else Inches(1.0)
        set_cell_shading(hdr_cells[i], "133F69")
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if (i in [0, 1, 2] and col_count == 4) or (i in [0, 2, 4, 6, 7] and col_count == 9) else WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(title.replace("**", ""))
        run.font.name = "Calibri"
        run.font.size = Pt(9)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for r_idx, row_data in enumerate(rows):
        row_cells = table.rows[r_idx + 1].cells
        bg_color = "F7F9FC" if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx, cell_value in enumerate(row_data):
            if c_idx >= col_count:
                break
            cell = row_cells[c_idx]
            cell.width = col_widths[c_idx] if c_idx < len(col_widths) else Inches(1.0)
            set_cell_shading(cell, bg_color)
            set_cell_margins(cell, top=70, bottom=70, left=90, right=90)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)

            if col_count == 9:
                if c_idx in [0, 2, 4, 6, 7]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            elif col_count == 4:
                if c_idx in [1, 2]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

            clean_val = cell_value.strip()
            status_match = None
            for tag in STATUS_COLORS:
                if tag in clean_val:
                    status_match = tag
                    break

            if status_match:
                r = p.add_run(status_match)
                r.font.name = "Calibri"
                r.font.size = Pt(8.5)
                r.font.bold = True
                r.font.color.rgb = STATUS_COLORS[status_match]
                rem = clean_val.replace(status_match, "").strip()
                if rem:
                    add_formatted_runs(p, " " + rem, font_name="Calibri", font_size=Pt(8.5))
            else:
                add_formatted_runs(p, clean_val, font_name="Calibri", font_size=Pt(8.5))

    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.space_before = Pt(4)
    p_spacer.paragraph_format.space_after = Pt(4)

class DocumentFormatter:
    """Đóng gói toàn bộ quy chuẩn định dạng cho Transcript và Analyst Report."""

    @staticmethod
    def setup_transcript_doc() -> docx.Document:
        """
        Khởi tạo Document cho Transcript theo chuẩn template TCX/F88:
        Ưu tiên clone style từ template gốc. Nếu không có file template,
        tự động tạo toàn bộ bộ style chuẩn bằng code không phụ thuộc file ngoài.
        """
        template_found = None
        for p in TCX_BENCHMARK_TEMPLATE_PATHS:
            if p.exists():
                template_found = p
                break

        if template_found:
            doc = docx.Document(str(template_found))
            # Xóa các paragraph cũ để tái sử dụng style
            for p in list(doc.paragraphs):
                p._p.getparent().remove(p._p)
            return doc

        # Tạo mới và định nghĩa đầy đủ style nếu không tìm thấy template
        doc = docx.Document()
        for sec in doc.sections:
            sec.top_margin = Inches(0.8)
            sec.bottom_margin = Inches(0.8)
            sec.left_margin = Inches(0.9)
            sec.right_margin = Inches(0.9)

        styles = doc.styles

        # 1. Title F88
        try:
            s_title = styles.add_style("Title F88", WD_STYLE_TYPE.PARAGRAPH)
            s_title.font.name = "Calibri"
            s_title.font.size = Pt(20)
            s_title.font.bold = True
            s_title.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
            s_title.paragraph_format.space_after = Pt(8)
        except Exception:
            pass

        # 2. Section F88
        try:
            s_sec = styles.add_style("Section F88", WD_STYLE_TYPE.PARAGRAPH)
            s_sec.font.name = "Calibri"
            s_sec.font.size = Pt(13)
            s_sec.font.bold = True
            s_sec.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
            s_sec.paragraph_format.space_before = Pt(14)
            s_sec.paragraph_format.space_after = Pt(6)
        except Exception:
            pass

        # 3. Speaker F88
        try:
            s_spk = styles.add_style("Speaker F88", WD_STYLE_TYPE.PARAGRAPH)
            s_spk.font.name = "Calibri"
            s_spk.font.size = Pt(10)
            s_spk.paragraph_format.line_spacing = 1.15
            s_spk.paragraph_format.space_after = Pt(4)
        except Exception:
            pass

        # 4. Note F88
        try:
            s_note = styles.add_style("Note F88", WD_STYLE_TYPE.PARAGRAPH)
            s_note.font.name = "Calibri"
            s_note.font.size = Pt(9.5)
            s_note.font.italic = True
            s_note.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
            s_note.paragraph_format.left_indent = Inches(0.25)
            s_note.paragraph_format.space_after = Pt(4)
        except Exception:
            pass

        return doc

    @staticmethod
    def setup_report_doc() -> docx.Document:
        """Khởi tạo Document cho Analyst Report theo chuẩn Institutional Research."""
        doc = docx.Document()
        for sec in doc.sections:
            sec.top_margin = Inches(0.8)
            sec.bottom_margin = Inches(0.8)
            sec.left_margin = Inches(0.9)
            sec.right_margin = Inches(0.9)
        return doc

    @staticmethod
    def lint_document(file_or_text: str) -> Dict[str, Any]:
        """
        Kiểm định tuân thủ ngôn từ trung lập của giới nghiên cứu tài chính theo AGENTS.md.
        Phát hiện các từ ngữ PR, phóng đại, cảm tính.
        """
        if os.path.exists(file_or_text):
            with open(file_or_text, "r", encoding="utf-8") as f:
                content = f.read()
            source_name = file_or_text
        else:
            content = file_or_text
            source_name = "<Text Buffer>"

        violations = []
        quarter_violations = []
        number_violations = []
        multiyear_violations = []
        table_violations = []
        is_analyst_report = ("analyst_report" in source_name.lower() or "[Institutional Research]" in content.lower()) and not ("data_reconciliation" in source_name.lower() or "ground_truth" in source_name.lower())
        lines = content.splitlines()
        for line_no, line in enumerate(lines, start=1):
            for word in FORBIDDEN_BUZZWORDS:
                # Tìm kiếm không phân biệt hoa thường
                pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
                matches = pattern.finditer(line)
                for m in matches:
                    replacement = OBJECTIVE_REPLACEMENTS.get(word.lower(), "từ ngữ định lượng trung tính")
                    violations.append({
                        "line": line_no,
                        "word": word,
                        "replacement": replacement,
                        "snippet": line.strip()[:100]
                    })

            # Kiểm tra quy chuẩn ký hiệu Quý (Bắt buộc dạng 3Q26, 4Q26...)
            bad_quarters = re.findall(r'(?:(?<![1-4])Q\d+|[Qq]uý\s*\d+|\b[1-4]Q\d{4}\b)', line)
            for bq in bad_quarters:
                quarter_violations.append({
                    "line": line_no,
                    "term": bq,
                    "suggested": "chuẩn hóa dạng 3Q26, 4Q26, 3Q25...",
                    "snippet": line.strip()[:100]
                })

                    # Kiểm tra định dạng số liệu (Dấu chấm cho thập phân, dấu phẩy cho hàng ngàn)
            bad_decimal_percentages = re.findall(r'(?:[+\-–]?\b\d+,\d+%)', line)
            for bp in bad_decimal_percentages:
                number_violations.append({
                    "line": line_no,
                    "term": bp,
                    "suggested": f"Đổi dấu phẩy sang dấu chấm: {bp.replace(',', '.')}",
                    "snippet": line.strip()[:100]
                })
            bad_thousands_decimal = re.findall(r'\b\d{1,3}(?:\.\d{3})+,\d+\b', line)
            for btd in bad_thousands_decimal:
                number_violations.append({
                    "line": line_no,
                    "term": btd,
                    "suggested": f"Đổi dấu chấm thành phẩy và phẩy thành chấm (e.g. {btd.replace('.', ',')})",
                    "snippet": line.strip()[:100]
                })

            # Kiểm tra liệt kê chuỗi dữ liệu đa năm cũ (Drop multi-year chronological listings: 2021-2024 raw data)
            multiyear_match = re.search(r'\b202[0-4]\b.*\b202[0-4]\b.*\b202[0-4]\b', line)
            if multiyear_match:
                multiyear_violations.append({
                    "line": line_no,
                    "term": multiyear_match.group(0)[:80],
                    "suggested": "Loại bỏ chuỗi số liệu đa năm (2021-2024); chỉ giữ lại kỳ hiện tại so với kỳ so sánh cơ sở (YoY/YTD/2025).",
                    "snippet": line.strip()[:100]
                })

            # Kiểm tra quy chuẩn cấm vẽ bảng trong Báo cáo Phân tích (Quy chuẩn 10 AGENTS.md)
            if is_analyst_report and line.strip().startswith("|") and line.strip().endswith("|"):
                if not re.match(r'^\|\s*[-:]+.*\|$', line.strip()):
                    table_violations.append({
                        "line": line_no,
                        "term": line.strip()[:80],
                        "suggested": "Báo cáo phân tích TUYỆT ĐỐI KHÔNG vẽ bảng; phải diễn đạt hoàn toàn bằng câu chữ văn xuôi & structured text bullet points theo AGENTS.md Quy chuẩn 10.",
                        "snippet": line.strip()[:100]
                    })

        is_compliant = (len(violations) == 0 and len(quarter_violations) == 0 and len(number_violations) == 0 and len(multiyear_violations) == 0 and len(table_violations) == 0)
        return {
            "source": source_name,
            "compliant": is_compliant,
            "violations_count": len(violations),
            "violations": violations,
            "quarter_violations_count": len(quarter_violations),
            "quarter_violations": quarter_violations,
            "number_violations_count": len(number_violations),
            "number_violations": number_violations,
            "multiyear_violations_count": len(multiyear_violations),
            "multiyear_violations": multiyear_violations,
            "table_violations_count": len(table_violations),
            "table_violations": table_violations
        }

    @staticmethod
    def markdown_to_transcript_docx(md_path: str, out_docx_path: str):
        """
        Tự động phân tích full_transcript.md và tạo file DOCX hoàn hảo theo template TCX/F88:
        - Chuẩn hóa header (Title F88, Subtitle, Speakers)
        - Đánh số Section 01, 02... | Tiêu đề với style Section F88
        - Gắn nhãn Diễn giả [Speaker]: vào đầu lượt thoại bằng màu Dark Navy #133F69 bold
        - Chuyển blockquote (> *[Diễn giải...]*) thành Note F88 màu xám nghiêng thụt lề
        - Phân tích và giữ nguyên in đậm/in nghiêng nội dòng
        """
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = standardize_quarters(content)
        content = standardize_number_formatting(content)
        lines = content.splitlines()
        doc = DocumentFormatter.setup_transcript_doc()

        # 1. Trích xuất metadata
        title = "Earnings Call Transcript"
        subtitle = "Financial Results & Strategic Update"
        speakers = "Board of Management & IR Team"

        for line in lines[:20]:
            l_str = line.strip()
            if l_str.startswith("# ") and "TRANSCRIPT" not in l_str and "BẢN GHI" not in l_str:
                title = l_str.replace("# ", "").strip()
            elif "Kỳ báo cáo" in l_str:
                subtitle = l_str.split(":", 1)[-1].strip().strip("*").strip()
            elif "Thành phần" in l_str:
                pass

        # 2. Add Header
        doc.add_paragraph(title, style="Title F88")

        p_sub = doc.add_paragraph(style="Normal")
        r_sub = p_sub.add_run(subtitle)
        r_sub.font.name = "Calibri"
        r_sub.font.size = Pt(12)
        r_sub.font.bold = True
        r_sub.font.color.rgb = RGBColor(0x3C, 0x5C, 0x7A)

        # Trích xuất danh sách diễn giả thực tế từ metadata
        spk_list = []
        in_spk_block = False
        for l in lines[:30]:
            if "Thành phần" in l:
                in_spk_block = True
                continue
            if in_spk_block:
                if l.strip().startswith("- "):
                    spk_list.append(l.strip()[2:].strip("* "))
                elif l.strip().startswith("*") or l.strip().startswith("#") or l.strip().startswith("---"):
                    in_spk_block = False

        if spk_list:
            speakers = "; ".join(spk_list)

        p_spk = doc.add_paragraph(style="Normal")
        r_label = p_spk.add_run("Speakers: ")
        r_label.font.name = "Calibri"
        r_label.font.bold = True
        p_spk.add_run(speakers)

        # 3. Phân tích nội dung chính
        current_speaker: Optional[str] = None
        in_header_meta = True
        note_buffer: List[str] = []

        def flush_note_buffer():
            nonlocal note_buffer
            if not note_buffer:
                return
            full_note = " ".join(note_buffer).strip()
            # Clean outer markdown symbols
            full_note = re.sub(r'^\*?\[?', '', full_note)
            full_note = re.sub(r'\]?\*?$', '', full_note)
            if not (full_note.startswith("Editorial Note:") or full_note.startswith("Ghi chú biên tập:")):
                if full_note.startswith("Diễn giải từ Slide"):
                    full_note = f"Editorial Note: Reference {full_note}"
                else:
                    full_note = f"Editorial Note: {full_note}"
            doc.add_paragraph(full_note, style="Note F88")
            note_buffer = []

        speaker_pattern = re.compile(r'^(?:\*\*(?:\[(.*?)\]|(.*?))\*\*|\[(.*?)\]):\s*(.*)$')
        section_pattern = re.compile(r'^##\s+(?:(\d+)\s*\|\s*|(?:PHẦN|PART)\s+(\d+)[:\s]+)(.*)', re.IGNORECASE)

        for line in lines:
            line_str = line.strip()

            # Quản lý Note buffer
            if line_str.startswith(">"):
                cl = line_str.lstrip("> *").rstrip("*]").strip()
                note_buffer.append(cl)
                continue
            else:
                if note_buffer:
                    flush_note_buffer()

            # Bỏ qua các dòng trống, đường kẻ ngang, hoặc comment
            if not line_str or line_str.startswith("---"):
                continue

            # Bỏ qua phần metadata ban đầu (sau dấu --- đầu tiên)
            if in_header_meta:
                if line_str.startswith("## "):
                    in_header_meta = False
                else:
                    continue

            # Section Header
            sec_match = section_pattern.match(line_str)
            if sec_match:
                current_speaker = None
                num = sec_match.group(1) or sec_match.group(2) or "01"
                sec_title = sec_match.group(3).strip()
                doc.add_paragraph(f"{int(num):02d}  |  {sec_title}", style="Section F88")
                continue

            # Kiểm tra dòng Speaker
            spk_match = speaker_pattern.match(line_str)
            if spk_match:
                spk_name = spk_match.group(1) or spk_match.group(2) or spk_match.group(3)
                rest_text = spk_match.group(4).strip()
                if not rest_text:
                    # Speaker đứng một mình trên dòng
                    current_speaker = spk_name.strip()
                    continue
                else:
                    # Speaker kèm luôn nội dung thoại
                    p = doc.add_paragraph(style="Speaker F88")
                    r_s = p.add_run(f"[{spk_name.strip()}]: ")
                    r_s.font.name = "Calibri"
                    r_s.font.bold = True
                    r_s.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
                    add_formatted_runs(p, rest_text)
                    current_speaker = None
                    continue

            # Dòng thoại thông thường
            p = doc.add_paragraph(style="Speaker F88")
            if current_speaker:
                r_s = p.add_run(f"[{current_speaker}]: ")
                r_s.font.name = "Calibri"
                r_s.font.bold = True
                r_s.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
                current_speaker = None

            # Xử lý bullets nếu có
            if line_str.startswith("- ") or line_str.startswith("* "):
                p.paragraph_format.left_indent = Inches(0.2)
                add_formatted_runs(p, f"•  {line_str[2:].strip()}")
            else:
                add_formatted_runs(p, line_str)

        # Flush buffer cuối cùng nếu còn
        if note_buffer:
            flush_note_buffer()

        actual_path = safe_save_docx(doc, out_docx_path)
        print(f"[✓] Đã tạo Full Transcript Word chuẩn định dạng: {actual_path}")

    @staticmethod
    def markdown_to_report_docx(md_path: str, out_docx_path: str):
        """
        Tự động phân tích analyst_report.md và tạo file DOCX hoàn hảo theo chuẩn Institutional Research 3 phần:
        - Title: 15.5pt bold Dark Navy #133F69
        - Heading 1 (Phần 1, 2, 3): 13pt bold #1E4E79
        - Heading 2 (Nhóm chỉ tiêu): 11pt bold #2E75B6
        - List Bullets: Bold lead text, regular body, spacing chuẩn
        - Q&A Blocks: Question bold #1F497D, Response indented with bold speaker prefix #333333
        """
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = standardize_quarters(content)
        content = standardize_number_formatting(content)
        lines = content.splitlines()
        doc = DocumentFormatter.setup_report_doc()

        def add_h1(text: str):
            p = doc.add_paragraph()
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(13)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0x1E, 0x4E, 0x79)
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            return p

        def add_h2(text: str):
            p = doc.add_paragraph()
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(11)
            r.font.bold = True
            r.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(3)
            return p

        def add_bullet(raw_line: str, indent_level: int = 0):
            clean_text = raw_line
            for prefix in ["- ", "* ", "+ "]:
                if clean_text.startswith(prefix):
                    clean_text = clean_text[len(prefix):].strip()
                    break

            p = doc.add_paragraph(style="List Bullet")
            if indent_level > 0:
                p.paragraph_format.left_indent = Inches(0.25 * (indent_level + 1))

            # Tách lead text in đậm nếu có cú pháp **Lead**:
            lead_match = re.match(r'^(?:\*\*(.*?)\*\*|(.*?)):(.*)$', clean_text)
            if lead_match and lead_match.group(1):
                lead = lead_match.group(1).strip()
                body = lead_match.group(3).strip()
                r_lead = p.add_run(f"{lead}: ")
                r_lead.font.name = "Calibri"
                r_lead.font.size = Pt(10)
                r_lead.font.bold = True
                add_formatted_runs(p, body, font_size=Pt(10))
            else:
                add_formatted_runs(p, clean_text, font_size=Pt(10))

            p.paragraph_format.space_after = Pt(3)
            return p

        first_line = True

        for line in lines:
            l = line.strip()
            if not l:
                continue

            # Tiêu đề báo cáo
            if (l.startswith("# ") or "[Institutional Research]" in l) and first_line:
                title_text = l.replace("# ", "").strip()
                p = doc.add_paragraph()
                r = p.add_run(title_text)
                r.font.name = "Calibri"
                r.font.size = Pt(15.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
                p.paragraph_format.space_after = Pt(12)
                first_line = False
                continue

            # Heading 1: Phần 1, Phần 2, Phần 3
            if re.match(r'^(?:##\s+)?(?:Phần|Part)\s+(?:\d+|[IVXLCDM]+)[:\s]+', l, re.IGNORECASE):
                clean_h1 = re.sub(r'^##\s*', '', l)
                add_h1(clean_h1)
                continue

            # Heading 2: Nhóm chỉ tiêu
            if l.startswith("### ") or (l.endswith(":") and not l.startswith("-") and not l.startswith("*") and not l.startswith("+") and not re.match(r'^\d+\.', l)):
                clean_h2 = l.replace("### ", "").strip()
                add_h2(clean_h2)
                continue

            # List Bullets (cấp 1 và cấp 2)
            if l.startswith("- ") or l.startswith("* ") or l.startswith("+ "):
                add_bullet(l, indent_level=0)
                continue
            elif line.startswith("    - ") or line.startswith("    * ") or line.startswith("  + "):
                add_bullet(line.strip(), indent_level=1)
                continue

            # Q&A Question
            qa_match = re.match(r'^(?:\*\*)?(\d+)\.\s+\*?\*?(.*?)\*?\*?:?$', l)
            if qa_match:
                p_q = doc.add_paragraph()
                r_num = p_q.add_run(f"{qa_match.group(1)}. {qa_match.group(2)}")
                r_num.font.name = "Calibri"
                r_num.font.size = Pt(10.5)
                r_num.font.bold = True
                r_num.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
                p_q.paragraph_format.space_before = Pt(8)
                p_q.paragraph_format.space_after = Pt(2)
                continue

            # Q&A Response
            if l.startswith("Phản hồi từ") or l.startswith("Management Response") or l.startswith("Ban Lãnh đạo:"):
                p_a = doc.add_paragraph()
                parts = l.split(":", 1)
                spk = parts[0].strip()
                body = parts[1].strip() if len(parts) > 1 else ""
                r_spk = p_a.add_run(f"{spk}: ")
                r_spk.font.name = "Calibri"
                r_spk.font.size = Pt(10)
                r_spk.font.bold = True
                r_spk.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
                add_formatted_runs(p_a, body, font_size=Pt(10))
                p_a.paragraph_format.left_indent = Inches(0.2)
                p_a.paragraph_format.space_after = Pt(6)
                continue

            # Đoạn văn bản bình thường
            p = doc.add_paragraph()
            add_formatted_runs(p, l, font_size=Pt(10))
            p.paragraph_format.space_after = Pt(4)

        actual_path = safe_save_docx(doc, out_docx_path)
        print(f"[✓] Đã tạo Analyst Report Word chuẩn định dạng: {actual_path}")


    @staticmethod
    def markdown_to_reconciliation_docx(md_path: str, out_docx_path: str) -> str:
        """
        Tự động phân tích data_reconciliation.md và tạo file DOCX khổ ngang A4 chuyên nghiệp:
        - Bảng ma trận đối soát số liệu chuẩn hóa.
        - Header bảng xanh đậm #133F69, text trắng bold.
        - Zebra shading xen kẽ dòng chẵn/lẻ.
        - Gắn nhãn màu sắc cho từng trạng thái [MATCH], [VARIANCE], [SPEECH_ONLY], [SLIDE_ONLY], [FLAGGED].
        """
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        content = standardize_quarters(content)
        content = standardize_number_formatting(content)
        lines = content.splitlines()

        doc = docx.Document()
        sec = doc.sections[0]
        sec.orientation = WD_ORIENTATION.LANDSCAPE
        sec.page_width = Inches(11.69)
        sec.page_height = Inches(8.27)
        sec.top_margin = Inches(0.5)
        sec.bottom_margin = Inches(0.5)
        sec.left_margin = Inches(0.5)
        sec.right_margin = Inches(0.5)

        table_buffer = []
        in_table = False

        i = 0
        while i < len(lines):
            line = lines[i]
            l = line.strip()

            if l.startswith("|") and l.endswith("|"):
                table_buffer.append(l)
                in_table = True
                i += 1
                continue
            else:
                if in_table and table_buffer:
                    headers, rows = parse_markdown_table(table_buffer)
                    if headers and rows:
                        add_table_to_doc(doc, headers, rows)
                    table_buffer = []
                    in_table = False

            if not l:
                i += 1
                continue

            if l.startswith("# "):
                title_text = l.replace("# ", "").strip()
                p = doc.add_paragraph()
                r = p.add_run(title_text)
                r.font.name = "Calibri"
                r.font.size = Pt(15)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(4)
            elif l.startswith("## "):
                h_text = l.replace("## ", "").strip()
                p = doc.add_paragraph()
                r = p.add_run(h_text)
                r.font.name = "Calibri"
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x4E, 0x79)
                p.paragraph_format.space_before = Pt(10)
                p.paragraph_format.space_after = Pt(4)
            elif l.startswith("### "):
                h_text = l.replace("### ", "").strip()
                p = doc.add_paragraph()
                r = p.add_run(h_text)
                r.font.name = "Calibri"
                r.font.size = Pt(10.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x2E, 0x75, 0xB6)
                p.paragraph_format.space_before = Pt(8)
                p.paragraph_format.space_after = Pt(3)
            elif l.startswith("- ") or l.startswith("* "):
                clean_text = l[2:].strip()
                p = doc.add_paragraph(style="List Bullet")
                p.paragraph_format.left_indent = Inches(0.2)
                p.paragraph_format.space_after = Pt(2)
                lead_match = re.match(r'^(?:\*\*(.*?)\*\*|(.*?)):(.*)$', clean_text)
                if lead_match and lead_match.group(1):
                    lead = lead_match.group(1).strip()
                    body = lead_match.group(3).strip()
                    r_lead = p.add_run(f"{lead}: ")
                    r_lead.font.name = "Calibri"
                    r_lead.font.size = Pt(9.5)
                    r_lead.font.bold = True
                    add_formatted_runs(p, body, font_name="Calibri", font_size=Pt(9.5))
                else:
                    add_formatted_runs(p, clean_text, font_name="Calibri", font_size=Pt(9.5))
            elif re.match(r'^\d+\.\s+', l):
                m = re.match(r'^(\d+)\.\s+(.*)$', l)
                num = m.group(1)
                body = m.group(2)
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Inches(0.2)
                p.paragraph_format.space_after = Pt(3)
                r_num = p.add_run(f"{num}. ")
                r_num.font.name = "Calibri"
                r_num.font.size = Pt(9.5)
                r_num.font.bold = True
                add_formatted_runs(p, body, font_name="Calibri", font_size=Pt(9.5))
            elif l.startswith("---"):
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(4)
            else:
                p = doc.add_paragraph()
                add_formatted_runs(p, l, font_name="Calibri", font_size=Pt(9.5))
                p.paragraph_format.space_after = Pt(3)

            i += 1

        if in_table and table_buffer:
            headers, rows = parse_markdown_table(table_buffer)
            if headers and rows:
                add_table_to_doc(doc, headers, rows)

        actual_path = safe_save_docx(doc, out_docx_path)
        print(f"[✓] Đã tạo Báo cáo Đối chiếu Dữ liệu Word: {actual_path}")
        return actual_path

    @staticmethod
    def compile_workspace(workspace_dir: str, ticker: Optional[str] = None, period: Optional[str] = None) -> Dict[str, Any]:
        """
        Đóng gói định dạng tự động cho toàn bộ thư mục workspace:
        1. Tìm full_transcript.md và analyst_report.md
        2. Tự động chuyển đổi thành DOCX chuẩn F88/TCX và Institutional Research
        3. Chạy kiểm định tuân thủ ngôn từ trung lập định chế tài chính
        """
        ws = Path(workspace_dir)
        if not ws.exists():
            raise FileNotFoundError(f"Không tìm thấy thư mục: {workspace_dir}")

        if not ticker:
            ticker = ws.name.upper()
        if not period:
            period = "9M2026"

        output_dir = ws / "output" if (ws / "output").exists() else ws
        generated_files = []

        print(f"\n=======================================================")
        print(f"  FORMAT PACKAGER — BỘ ĐÓNG GÓI ĐỊNH DẠNG CHUẨN MỰC TCX")
        print(f"  Mã doanh nghiệp: {ticker} | Kỳ báo cáo: {period}")
        print(f"  Thư mục: {ws}")
        print(f"=======================================================\n")

        internal_dir = ws / "internal"
        if not internal_dir.exists() and (ws / "input_docs").exists():
            internal_dir = ws / "input_docs"
        internal_dir.mkdir(parents=True, exist_ok=True)

        # 1. Transcript (Duy nhất 1 file Word chính thức trong output/)
        transcript_md = output_dir / "full_transcript.md"
        if not transcript_md.exists() and (ws / "full_transcript.md").exists():
            transcript_md = ws / "full_transcript.md"

        if transcript_md.exists():
            out_docx = output_dir / "full_transcript.docx"
            DocumentFormatter.markdown_to_transcript_docx(str(transcript_md), str(out_docx))
            generated_files.append(str(out_docx))
        else:
            print(f"[!] Không tìm thấy full_transcript.md trong {output_dir}")

        # 2. Data Reconciliation Report (Lưu trong internal/ để giữ output/ tinh gọn)
        recon_md = internal_dir / "data_reconciliation.md"
        if not recon_md.exists() and (output_dir / "data_reconciliation.md").exists():
            recon_md = output_dir / "data_reconciliation.md"
        elif not recon_md.exists() and (ws / "data_reconciliation.md").exists():
            recon_md = ws / "data_reconciliation.md"

        if recon_md.exists():
            if recon_md.parent == output_dir and internal_dir != output_dir:
                dest_recon = internal_dir / "data_reconciliation.md"
                import shutil
                try:
                    shutil.move(str(recon_md), str(dest_recon))
                    recon_md = dest_recon
                except Exception:
                    pass
            out_recon_docx = internal_dir / "data_reconciliation.docx"
            DocumentFormatter.markdown_to_reconciliation_docx(str(recon_md), str(out_recon_docx))
            generated_files.append(str(out_recon_docx))
        else:
            print(f"  [i] Chưa có data_reconciliation.md trong {internal_dir}")

        # 3. Analyst Report (Duy nhất 1 file Word chính thức trong output/)
        report_md = output_dir / "analyst_report.md"
        if not report_md.exists() and (ws / "analyst_report.md").exists():
            report_md = ws / "analyst_report.md"

        if report_md.exists():
            out_docx = output_dir / "analyst_report.docx"
            DocumentFormatter.markdown_to_report_docx(str(report_md), str(out_docx))
            generated_files.append(str(out_docx))
        else:
            print(f"[!] Không tìm thấy analyst_report.md trong {output_dir}")

        print(f"[✓] Đã hoàn tất đóng gói: Output chính tại {output_dir}, dữ liệu đối soát tại {internal_dir}")

        # 4. Kiểm định ngôn từ trung lập
        print(f"\n--- KIỂM ĐỊNH TUÂN THỦ NGÔN TỪ (FACT-BASED & NEUTRAL LINTER) ---")
        linter_results = []
        for md_file in [transcript_md, recon_md, report_md]:
            if md_file.exists():
                res = DocumentFormatter.lint_document(str(md_file))
                linter_results.append(res)
                if res["compliant"]:
                    print(f"[✓] {md_file.name}: 100% Tuân thủ chuẩn định chế tài chính & Chuẩn hóa Quý (3Q26).")
                else:
                    if res["violations_count"] > 0:
                        print(f"[!] {md_file.name}: Phát hiện {res['violations_count']} từ ngữ cảm tính:")
                        for v in res["violations"]:
                            print(f"    - Dòng {v['line']}: '{v['word']}' -> Đề xuất: '{v['replacement']}'")
                    if res.get("number_violations_count", 0) > 0:
                        print(f"[!] {md_file.name}: Phát hiện {res['number_violations_count']} lỗi định dạng Số (dấu . cho thập phân, dấu , cho hàng ngàn):")
                        for nv in res["number_violations"]:
                            print(f"    - Dòng {nv['line']}: '{nv['term']}' -> Cần đổi sang: {nv['suggested']}")
                    if res.get("quarter_violations_count", 0) > 0:
                        print(f"[!] {md_file.name}: Phát hiện {res['quarter_violations_count']} lỗi định dạng Quý:")
                        for qv in res["quarter_violations"]:
                            print(f"    - Dòng {qv['line']}: '{qv['term']}' -> Cần đổi sang: {qv['suggested']}")

        print(f"\n[✓] ĐÓNG GÓI ĐỊNH DẠNG HOÀN TẤT THÀNH CÔNG!")
        return {
            "status": "success",
            "ticker": ticker,
            "period": period,
            "files": generated_files,
            "linter": linter_results
        }


def main():
    parser = argparse.ArgumentParser(description="Format Packager: Đóng gói định dạng chuẩn Word / Markdown theo TCX Benchmark.")
    parser.add_argument("--workspace", "-w", type=str, help="Đường dẫn thư mục workspace (ví dụ: workspace/VPL)")
    parser.add_argument("--ticker", "-t", type=str, help="Mã cổ phiếu (ví dụ: VPL, TCX)")
    parser.add_argument("--period", "-p", type=str, default="9M2026", help="Kỳ báo cáo (mặc định: 9M2026)")
    parser.add_argument("--transcript-md", type=str, help="Đường dẫn file transcript markdown")
    parser.add_argument("--transcript-docx", type=str, help="Đường dẫn file transcript docx xuất ra")
    parser.add_argument("--report-md", type=str, help="Đường dẫn file report markdown")
    parser.add_argument("--report-docx", type=str, help="Đường dẫn file report docx xuất ra")
    parser.add_argument("--lint", type=str, help="Chạy kiểm định ngôn từ trung lập cho file chỉ định")

    args = parser.parse_args()

    if args.lint:
        res = DocumentFormatter.lint_document(args.lint)
        if res["compliant"]:
            print(f"[✓] {args.lint}: 100% Tuân thủ chuẩn định chế tài chính (Zero PR Buzzwords).")
        else:
            print(f"[!] {args.lint}: Phát hiện {res['violations_count']} từ ngữ cảm tính/PR:")
            for v in res["violations"]:
                print(f"    - Dòng {v['line']}: '{v['word']}' -> Đề xuất: '{v['replacement']}'")
        return

    if args.workspace:
        DocumentFormatter.compile_workspace(args.workspace, ticker=args.ticker, period=args.period)
        return

    if args.transcript_md and args.transcript_docx:
        DocumentFormatter.markdown_to_transcript_docx(args.transcript_md, args.transcript_docx)

    if args.report_md and args.report_docx:
        DocumentFormatter.markdown_to_report_docx(args.report_md, args.report_docx)


if __name__ == "__main__":
    main()
