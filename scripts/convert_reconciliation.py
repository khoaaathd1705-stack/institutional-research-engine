# -*- coding: utf-8 -*-
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENTATION
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from document_formatter import (
    standardize_quarters,
    standardize_number_formatting,
    parse_inline_markdown,
    add_formatted_runs,
    safe_save_docx
)

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
        # Bỏ qua dòng separator | :--- | :---: |
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

    # Tính toán độ rộng cột dựa trên số lượng cột
    # Tổng độ rộng khả dụng khổ ngang A4 (11.69 - 1.0) = ~10.69 inches
    if col_count == 4:
        col_widths = [Inches(3.2), Inches(1.1), Inches(1.1), Inches(5.2)]
    elif col_count == 9:
        col_widths = [
            Inches(0.45), # STT
            Inches(1.85), # Chỉ tiêu
            Inches(0.60), # Kỳ
            Inches(1.60), # Slide
            Inches(0.85), # Vị trí Slide
            Inches(1.65), # Transcript
            Inches(0.95), # Vị trí Transcript
            Inches(1.05), # Trạng thái
            Inches(1.69), # Đánh giá
        ]
    else:
        unit = Inches(10.69 / col_count)
        col_widths = [unit] * col_count

    # Header Row
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

    # Data Rows
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

            # Canh lề
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

            # Xử lý text và status badge
            clean_val = cell_value.strip()
            status_match = None
            for tag in STATUS_COLORS:
                if tag in clean_val:
                    status_match = tag
                    break

            if status_match:
                # Render status tag with color
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

def markdown_to_reconciliation_docx(md_path: str, out_docx_path: str) -> str:
    """Chuyển đổi data_reconciliation.md sang DOCX khổ ngang A4 chuyên nghiệp."""
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

        # Kiểm tra bảng markdown
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

    return safe_save_docx(doc, out_docx_path)

if __name__ == "__main__":
    src_md = "workspace/tcx/output/data_reconciliation.md"
    dst_docx = "workspace/tcx/output/TCX_Data_Reconciliation_9M2026.docx"
    alias_docx = "workspace/tcx/output/data_reconciliation.docx"
    ws_docx = "workspace/tcx/data_reconciliation.docx"
    print(f"Bắt đầu chuyển đổi: {src_md} -> {dst_docx}")
    res = markdown_to_reconciliation_docx(src_md, dst_docx)
    import shutil
    shutil.copy2(dst_docx, alias_docx)
    shutil.copy2(dst_docx, ws_docx)
    print(f"[✓] Đã tạo thành công:")
    print(f"    - {dst_docx}")
    print(f"    - {alias_docx}")
    print(f"    - {ws_docx}")
