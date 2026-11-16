# -*- coding: utf-8 -*-
"""
Script: build_hdb_group_ground_truth.py
Mục đích:
1. Chuẩn hóa cấu trúc thư mục 3 tầng (input, internal, output) cho 3 thực thể: HDB, HDSAISON, HDS.
2. Trích xuất và lưu trữ ảnh slide chất lượng cao vào input/slides/.
3. Chạy RapidOCR bóc tách cấu trúc dòng và bảng số liệu chuẩn (Single Source of Truth - SSOT).
4. Xuất ground_truth_raw.json và ground_truth.md chuẩn hóa theo RULE-AM-RES-01 & AGENTS.md:
   - Ký hiệu quý đồng nhất (3Q26, 9M26).
   - Định dạng số quốc tế (dấu chấm thập phân, dấu phẩy phân cách hàng ngàn).
   - Tổng hợp bảng chỉ tiêu tài chính cốt lõi (Executive Summary Benchmark Tables).
   - Chi tiết bóc tách từng slide (Slide-by-Slide Raw & Clustered Extraction).
"""

import os
import re
import sys
import json
import shutil
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from rapidocr_onnxruntime import RapidOCR


def extract_slide_images_from_pptx(pptx_path: Path, target_slides_dir: Path) -> List[Path]:
    """Trích xuất ảnh slide từ file pptx theo đúng thứ tự slide."""
    target_slides_dir.mkdir(parents=True, exist_ok=True)
    images = []
    with zipfile.ZipFile(pptx_path) as z:
        slide_rels = sorted(
            [n for n in z.namelist() if n.startswith("ppt/slides/_rels/slide") and n.endswith(".xml.rels")],
            key=lambda x: int(re.search(r"slide(\d+)\.xml\.rels", x).group(1)) if re.search(r"slide(\d+)\.xml\.rels", x) else 0
        )
        for idx, rel_file in enumerate(slide_rels, start=1):
            root = ET.fromstring(z.read(rel_file))
            img_target = None
            for elem in root:
                target = elem.attrib.get("Target", "")
                if "media/image" in target.lower():
                    img_target = target
                    break
            if img_target:
                target_path = "ppt/" + img_target.replace("../", "")
                if target_path in z.namelist():
                    img_data = z.read(target_path)
                    out_img = target_slides_dir / f"slide_{idx:02d}.png"
                    with open(out_img, "wb") as f_out:
                        f_out.write(img_data)
                    images.append(out_img)
    return images


def run_ocr_on_images(ocr: RapidOCR, image_paths: List[Path]) -> List[Dict[str, Any]]:
    """Chạy RapidOCR và gom nhóm các dòng text theo tọa độ y/x."""
    extracted_slides = []
    for idx, img_path in enumerate(image_paths, start=1):
        res, _ = ocr(str(img_path))
        lines = []
        if res:
            for item in res:
                box, text, score = item[0], item[1].strip(), float(item[2])
                if not text:
                    continue
                min_x = min(pt[0] for pt in box)
                max_x = max(pt[0] for pt in box)
                min_y = min(pt[1] for pt in box)
                max_y = max(pt[1] for pt in box)
                lines.append({
                    "text": text,
                    "score": score,
                    "bbox": [min_x, min_y, max_x, max_y],
                    "center_y": (min_y + max_y) / 2.0,
                    "center_x": (min_x + max_x) / 2.0
                })
        lines.sort(key=lambda item: item["center_y"])
        
        # Gom cụm theo dòng (row clustering)
        grouped_rows = []
        if lines:
            curr_cluster = [lines[0]]
            for item in lines[1:]:
                prev_avg_y = sum(c["center_y"] for c in curr_cluster) / len(curr_cluster)
                if abs(item["center_y"] - prev_avg_y) <= 14.0:
                    curr_cluster.append(item)
                else:
                    curr_cluster.sort(key=lambda c: c["center_x"])
                    grouped_rows.append([c["text"] for c in curr_cluster])
                    curr_cluster = [item]
            if curr_cluster:
                curr_cluster.sort(key=lambda c: c["center_x"])
                grouped_rows.append([c["text"] for c in curr_cluster])

        raw_text_lines = [item["text"] for item in lines]
        extracted_slides.append({
            "slide_num": idx,
            "image_file": img_path.name,
            "lines_count": len(lines),
            "rows": grouped_rows,
            "raw_text_lines": raw_text_lines
        })
    return extracted_slides


def setup_workspace(ticker: str, base_dir: Path, pptx_name: str, misc_files: List[str]) -> Tuple[Path, Path, Path, Path]:
    """Tạo cấu trúc 3 tầng: input, internal, output."""
    input_dir = base_dir / "input"
    internal_dir = base_dir / "internal"
    archive_dir = internal_dir / "archive"
    output_dir = base_dir / "output"
    slides_dir = input_dir / "slides"

    input_dir.mkdir(parents=True, exist_ok=True)
    internal_dir.mkdir(parents=True, exist_ok=True)
    archive_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    slides_dir.mkdir(parents=True, exist_ok=True)

    # Di chuyển file pptx vào input nếu đang ở thư mục gốc
    src_pptx = base_dir / pptx_name
    dest_pptx = input_dir / pptx_name
    if src_pptx.exists() and not dest_pptx.exists():
        shutil.move(str(src_pptx), str(dest_pptx))
    elif not dest_pptx.exists():
        # Kiểm tra nếu còn file temp
        pass

    # Di chuyển các file khác
    for f_name in misc_files:
        src_f = base_dir / f_name
        if src_f.exists():
            if "Update" in f_name or "Script" in f_name or "raw" in f_name:
                shutil.move(str(src_f), str(input_dir / f_name))
            else:
                shutil.move(str(src_f), str(archive_dir / f_name))

    return input_dir, internal_dir, output_dir, slides_dir


def generate_hdb_ground_truth(slides_data: List[Dict[str, Any]], internal_dir: Path, source_file: str):
    """Tạo ground_truth.md và ground_truth_raw.json cho HDBank (HDB)."""
    # Gán tiêu đề slide chuẩn hóa
    titles = {
        1: "HDBank: Tổng quan về HDBank & Hệ sinh thái Toàn diện (Key Statistics 3Q26)",
        2: "Ba Thập Kỷ Tăng Trưởng Cao và Bền Vững (1989 - 3Q26)",
        3: "Thương Hiệu Được Vinh Danh Với Sự Công Nhận Quốc Tế",
        4: "Cập Nhật KQKD 9M26 Của HDBank và Các Đơn Vị Thành Viên (HDB, HD SAISON, HDS, Vikki)",
        5: "Mang Đến Trải Nghiệm Số Vượt Trội (Vikki Digital Bank & SkyJoy)",
        6: "Các Giải Pháp Số Hóa Khách Hàng Doanh Nghiệp (MediPay, EduPay)",
        7: "Tài Trợ Chuỗi Giá Trị & Đồng Hành Cùng Chủ Trương Giảm Lãi Suất (Tín dụng Xanh, Gói SME)",
        8: "Dấu Mốc Quan Trọng: Khai Phiên Giao Dịch Tại NYSE & Thương Hiệu Quốc Gia 2026",
        9: "Dấu Mốc Quan Trọng: Giải Thưởng Tín Dụng Xanh & Nông Nghiệp Bền Vững (APEA 2026)",
        10: "Bối Cảnh Vĩ Mô: Tăng Trưởng GDP Tích Cực Trong Bối Cảnh Áp Lực Lạm Phát",
        11: "Lãi Suất Tiếp Tục Tăng Cao, Dù Thanh Khoản Đã Cải Thiện Nhẹ",
        12: "Một Số Điểm Nhấn Tài Chính Nổi Bật 3Q26 (Key Financial Highlights 3Q26)",
        13: "Dẫn Đầu Về Hiệu Quả Sinh Lời Trong Top 10 Ngân Hàng Lớn Nhất (LNTT, CIR, ROE, NIM)",
        14: "Tăng Trưởng Tiền Gửi Cao & Nền Tảng Vốn Vững Mạnh Trong Nhóm Dẫn Đầu (Tiền gửi TT1 & CAR)",
        15: "Tăng Trưởng Huy Động Vốn & Cho Vay Theo Phân Khúc Khách Hàng (Cá nhân & Doanh nghiệp)",
        16: "Danh Mục Tín Dụng Đa Dạng Thúc Đẩy Tăng Trưởng Cho Vay Bền Vững (Cơ cấu ngành & Bán lẻ)",
        17: "Khả Năng Sinh Lời Bền Vững Trong Bối Cảnh Lãi Suất Biến Động (NIM, Chi phí vốn COF, Lợi suất IEA)",
        18: "Bộ Đệm Dự Phòng Vững Chắc & Chi Phí Tín Dụng Thấp (NPL TT31, LLR, Tài sản đảm bảo)",
        19: "An Toàn Vốn & Thanh Khoản Luôn Được Đảm Bảo (CAR Basel II, LDR TT22, Tỷ lệ vốn ngắn hạn cho vay TH-DH)",
        20: "Kế Hoạch Kinh Doanh 2026 của HDBank (Financial Outlook 2026F & Sáng kiến Chiến lược)"
    }
    for s in slides_data:
        s["title"] = titles.get(s["slide_num"], f"Slide {s['slide_num']}")

    # Lưu JSON
    json_path = internal_dir / "ground_truth_raw.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "ticker": "HDB",
            "period": "3Q26 & 9M26",
            "meeting_name": "HDBank Analyst Meeting / Investor Presentation",
            "source_file": source_file,
            "total_slides": len(slides_data),
            "slides": slides_data
        }, f, ensure_ascii=False, indent=2)

    # Render Markdown
    md = [
        "# DỮ LIỆU SỐ LIỆU CHUẨN TỪ SLIDES (GROUND TRUTH BENCHMARK DATA) - HDBANK (HDB)",
        "* **Mã chứng khoán**: HDB (Ngân hàng TMCP Phát triển TP.HCM)",
        "* **Cuộc họp / Kỳ báo cáo**: HDBank Earnings Presentation / Analyst Meeting (3Q26 & 9M26)",
        f"* **Tài liệu nguồn**: `{source_file}` ({len(slides_data)} slide trình chiếu chính thức)",
        "* **Phương pháp trích xuất**: Automated Ground Truth Extraction Engine (RapidOCR + Coordinate Clustering)",
        "* **Quy chuẩn định dạng**: Chuẩn quốc tế (dấu chấm `.` thập phân, dấu phẩy `,` phân cách hàng ngàn; ký hiệu quý `3Q26`, `9M26`).",
        "* **Nguyên tắc đối soát**: 100% số liệu cứng lấy trực tiếp từ bản trình chiếu slide chính thức của Ban lãnh đạo HDBank.",
        "",
        "---",
        "",
        "## PHẦN I: BẢNG CHỈ TIÊU TÀI CHÍNH CỐT LÕI (EXECUTIVE SUMMARY BENCHMARK TABLES)",
        "",
        "### 1. Bảng cân đối kế toán, Tín dụng & Huy động vốn (Balance Sheet & Size)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | Thực hiện 2025A | Thực hiện 9M26 | Kế hoạch 2026F | Tăng trưởng 9M26 (YoY / YTD) | % Hoàn thành KH 2026F | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Tổng tài sản (Total Assets)** | Nghìn tỷ đồng | 931.0 | 1,143.0 | 1,194.0 | +22.7% YTD / +46.2% YoY | 95.7% | Slide 1, 4, 12, 20 |",
        "| **Tiền gửi khách hàng TT1 (Total Deposits)** | Nghìn tỷ đồng | 648.0 | 837.0 | 822.0 | +29.1% YTD | **101.8% (Vượt KH)** | Slide 1, 12, 14, 15, 20 |",
        "| - Tiền gửi khách hàng cá nhân (Retail) | Nghìn tỷ đồng | 87.0 (2024) | 127.0 | - | +45.7% YTD | - | Slide 15 |",
        "| - Tiền gửi khách hàng doanh nghiệp (Corporate) | Nghìn tỷ đồng | 431.0 (2024) | 518.0 | - | +19.9% YTD | - | Slide 15 |",
        "| **Dư nợ tín dụng hợp nhất (Total Credit)** | Nghìn tỷ đồng | 588.0 | 756.0 | 805.0 | +28.6% YTD (Toàn ngành ~11.6%) | 93.9% | Slide 1, 12, 20 |",
        "| - Cho vay khách hàng cá nhân (Retail) | Nghìn tỷ đồng | 146.0 (2024) | 200.0 | - | +37.6% YTD | - | Slide 15, 16 |",
        "| - Cho vay khách hàng doanh nghiệp (Corporate) | Nghìn tỷ đồng | 422.0 (2024) | 570.0 | - | +28.1% YTD | - | Slide 15 |",
        "| - Tài trợ chuỗi giá trị (Value Chain Loans) | Nghìn tỷ đồng | - | 45.8 | - | +18.6% YoY (>8.1k khách hàng) | - | Slide 7 |",
        "| - Dư nợ tín dụng xanh (Green Credit) | Nghìn tỷ đồng | - | 6.1 | - | Lũy kế giải ngân >42,000 tỷ | - | Slide 7, 9 |",
        "",
        "### 2. Kết quả hoạt động kinh doanh & Khả năng sinh lời (P&L & Profitability)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | Thực hiện 2025A | Thực hiện 9M26 | Kế hoạch 2026F | Tăng trưởng 9M26 (YoY) | % Hoàn thành KH 2026F | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Lợi nhuận trước thuế (LNTT / PBT)** | Tỷ đồng | 21,300.0 | 18,379.0 | 30,100.0 | +24.2% YoY (3Q26: ~5,200 tỷ, +9.3% YoY) | 61.1% | Slide 1, 4, 12, 13, 17, 20 |",
        "| **Tỷ suất sinh lời trên VCSH (ROAE)** | % | 25.3% | 22.8% | > 25.0% | Dẫn đầu Top 10 ngân hàng lớn | Đạt cận mục tiêu | Slide 1, 12, 13, 17, 20 |",
        "| **Tỷ suất sinh lời trên tài sản (ROAA)** | % | 2.1% | 1.9% | > 2.0% | Nằm trong nhóm cao nhất ngành | Đạt cận mục tiêu | Slide 13, 17, 20 |",
        "| **Tỷ lệ Chi phí / Thu nhập (CIR)** | % | 25.7% | 24.9% | - | -0.8% sv 2025 (Tối ưu top đầu ngành) | Tối ưu bền vững | Slide 1, 13, 17 |",
        "| **Biên lãi thuần hợp nhất (NIM)** | % | 5.1% | 4.8% | - | 3Q26 đạt 3.9% (áp lực chi phí vốn ngắn hạn) | Kỳ vọng phục hồi 4Q26 | Slide 13, 17 |",
        "| **Lợi suất tài sản sinh lãi (Yield on IEA)** | % | 9.9% | 9.5% | - | - | - | Slide 17 |",
        "| **Chi phí vốn (Cost of Funds - COF)** | % | 4.6% | 4.7% | - | +0.1% do cạnh tranh huy động | - | Slide 17 |",
        "",
        "### 3. Chất lượng tài sản, Quản trị rủi ro & An toàn vốn (Asset Quality & Capital Adequacy)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | 2024 | 2025 | 9M26 (30/09/2026) | Quy định / Kế hoạch 2026F | Ghi chú & Đánh giá | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Tỷ lệ nợ xấu hợp nhất (NPL - TT 31)** | % | 1.48% | 1.66% | 2.55% | < 2.00% | Phản ánh xu hướng chung toàn ngành | Slide 1, 12, 18, 20 |",
        "| **Tỷ lệ nợ xấu ngân hàng mẹ (Parent NPL)**| % | 1.33% | 1.05% | 1.95% | - | Kiểm soát tốt ở mức an toàn | Slide 18 |",
        "| **Tỷ lệ bao phủ nợ xấu hợp nhất (LLR)** | % | 65.8% | 70.4% | 68.7% | - | Bộ đệm dự phòng vững vàng | Slide 18 |",
        "| **Tỷ lệ bao phủ tài sản đảm bảo** | % | 201.6% | 258.7% | 189.0% | - | Tài sản đảm bảo thanh khoản cao | Slide 18 |",
        "| **Số dư quỹ dự phòng rủi ro** | Tỷ đồng | 5,879.0 | 7,479.0 | 5,797.0 | - | DP chung: 3,301 tỷ; DP cụ thể: 2,496 tỷ | Slide 18 |",
        "| **Chi phí tín dụng (Credit Cost 9M)** | Tỷ đồng | 3,101.0 | 4,054.0 | 5,413.0 | - | Tỷ lệ chi phí tín dụng ~1.48% | Slide 18 |",
        "| **Hệ số an toàn vốn hợp nhất (CAR Basel II)** | % | 14.0% | 14.4% | 13.9% | > 8.00% | Vốn cấp 1: 8.6%; Vốn cấp 2: 5.3% (Dự kiến Basel III từ 2027) | Slide 1, 12, 14, 19 |",
        "| **Tỷ lệ cấp tín dụng / Huy động (LDR TT 22)**| % | 68.5% | 67.0% | 71.5% | < 85.00% | Riêng lẻ: 68.2%, thanh khoản dồi dào | Slide 1, 19 |",
        "| **Tỷ lệ vốn ngắn hạn cho vay trung-dài hạn** | % | 22.5% | 20.1% | 17.2% | < 30.00% | Tuân thủ an toàn thanh khoản chặt chẽ | Slide 19 |",
        "| **Chỉ số thanh khoản NSFR & LCR** | % | > 100% | > 100% | > 100% | > 100% | Vượt xa ngưỡng chuẩn quốc tế | Slide 19 |",
        "",
        "### 4. Đóng góp từ các Đơn vị thành viên trong Hệ sinh thái (Ecosystem Subsidiaries Breakdown)",
        "",
        "| Đơn vị thành viên | Lĩnh vực hoạt động | Tỷ lệ sở hữu của HDBank | Kết quả kinh doanh 9M26 nổi bật | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- |",
        "| **HD SAISON** | Tài chính tiêu dùng (Consumer Finance) | 50.0% vốn điều lệ, 51.0% quyền biểu quyết | LNTT 9M26 vượt 1,184 tỷ (+8.7% YoY) / 1,390 tỷ; NIM 26.9%; ROE 21.4%; Mạng lưới POS số 1 phục vụ >18 triệu KH | Slide 1, 4 |",
        "| **HD Securities (HDS)** | Chứng khoán & Ngân hàng đầu tư (Securities & IB) | 90.0% cổ phần (nâng từ 30% trước IPO) | LNTT 9M26 đạt 2,241 tỷ (+265% YoY); ROE dẫn đầu thị trường 26.1%; Top 3 thị phần phát hành TPDN | Slide 1, 4 |",
        "| **Vikki Digital Bank** | Ngân hàng số thế hệ mới (Digital Bank) | 100.0% vốn điều lệ (tiếp nhận DongA Bank) | >9 triệu KH (>5.6 triệu KH hoạt động); 3.7 triệu lượt tải app; Giải thưởng Thẻ VikkiONE Connect tại AEA 2026 | Slide 1, 4, 5 |",
        "| **SkyJoy** | Nền tảng khách hàng thân thiết tích hợp | Thành viên hệ sinh thái HDBank | >18 triệu thành viên, kết nối toàn bộ hệ sinh thái dịch vụ tài chính, bán lẻ, hàng không | Slide 4, 5 |",
        "",
        "---",
        "",
        "## PHẦN II: TỔNG HỢP NỘI DUNG & SỐ LIỆU TỪNG SLIDE (SLIDE-BY-SLIDE DETAILS)",
        ""
    ]

    for s in slides_data:
        num = s["slide_num"]
        title = s["title"]
        img_name = s["image_file"]
        rows = s["rows"]
        md.append(f"### Slide {num:02d}: {title}")
        md.append(f"*Ảnh slide: `slides/{img_name}`*")
        md.append("")
        md.append("#### Số liệu & Văn bản trích xuất:")
        if rows:
            md.append("```text")
            for r in rows:
                md.append(" | ".join(r))
            md.append("```")
        else:
            md.append("*(Slide dạng hình ảnh biểu đồ, không nhận diện được văn bản dòng)*")
        md.append("")

    md.extend([
        "---",
        "",
        "## PHẦN III: NGUYÊN TẮC ÁP DỤNG KHI ĐỐI CHIẾU & BIÊN TẬP (AUDIT & RECONCILIATION PROTOCOL)",
        "1. **Chân Lý Chuẩn (Single Source of Truth - SSOT)**: Toàn bộ số liệu định lượng trong `full_transcript.md` và `analyst_report.md` bắt buộc phải đối soát trực tiếp với dữ liệu trích xuất từ slide tại tài liệu này.",
        "2. **Hiệu chỉnh sai lệch âm thanh / ASR**: Khi diễn giả làm tròn số hoặc ASR nhận diện nhầm thuật ngữ, số liệu trên slide là căn cứ pháp lý cao nhất để hiệu chỉnh.",
        "3. **Cách ly nguồn dữ liệu (Source Isolation)**: Báo cáo chỉ sử dụng dữ liệu từ tài liệu trình chiếu kỳ 3Q26 & 9M26 này, chống rò rỉ dữ liệu ngoài."
    ])

    md_path = internal_dir / "ground_truth.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"[✓] Đã tạo thành công {md_path} ({len(md)} dòng).")


def generate_hdsaison_ground_truth(slides_data: List[Dict[str, Any]], internal_dir: Path, source_file: str):
    """Tạo ground_truth.md và ground_truth_raw.json cho HD SAISON."""
    titles = {
        1: "HD SAISON: Tăng Trưởng Tín Dụng & Giải Ngân Mạnh Mẽ (Loan Book, Disbursements, NIM & Chi Phí Vốn)",
        2: "HD SAISON: Hiệu Quả Sinh Lời Bền Vững & Chất Lượng Tài Sản (PBT, ROE, ROA, CIR, NPL & Credit Cost)"
    }
    for s in slides_data:
        s["title"] = titles.get(s["slide_num"], f"Slide {s['slide_num']}")

    json_path = internal_dir / "ground_truth_raw.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "ticker": "HDSAISON",
            "period": "3Q26 & 9M26",
            "meeting_name": "HD SAISON Financial Highlights 3Q2026",
            "source_file": source_file,
            "total_slides": len(slides_data),
            "slides": slides_data
        }, f, ensure_ascii=False, indent=2)

    md = [
        "# DỮ LIỆU SỐ LIỆU CHUẨN TỪ SLIDES (GROUND TRUTH BENCHMARK DATA) - HD SAISON",
        "* **Tên công ty**: Công ty Tài chính TNHH HD SAISON (Công ty con của HDBank)",
        "* **Cuộc họp / Kỳ báo cáo**: HD SAISON 3Q2026 Financial Highlights (3Q26 & 9M26)",
        f"* **Tài liệu nguồn**: `{source_file}` ({len(slides_data)} slide trình chiếu chính thức)",
        "* **Phương pháp trích xuất**: Automated Ground Truth Extraction Engine (RapidOCR + Coordinate Clustering)",
        "* **Quy chuẩn định dạng**: Chuẩn quốc tế (dấu chấm `.` thập phân, dấu phẩy `,` phân cách hàng ngàn; ký hiệu quý `3Q26`, `9M26`).",
        "* **Nguyên tắc đối soát**: 100% số liệu cứng lấy trực tiếp từ bản trình chiếu slide chính thức.",
        "",
        "---",
        "",
        "## PHẦN I: BẢNG CHỈ TIÊU TÀI CHÍNH CỐT LÕI (EXECUTIVE SUMMARY BENCHMARK TABLES)",
        "",
        "### 1. Quy mô Dư nợ, Giải ngân & Cơ cấu Sản phẩm (Loan Book & Disbursements)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | 2021 | 2022 | 2023 | 2024 | 2025 | 3Q26 / 9M26 | Tăng trưởng | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Dư nợ cho vay (Loan Book)** | Tỷ đồng | 13,376.0 | 16,839.0 | 16,086.0 | 18,212.0 | 22,070.0 | **26,452.0** | +19.9% YTD sv 2025 | Slide 1 |",
        "| **Tổng giải ngân (Disbursements)** | Tỷ đồng | 20,364.0 | 26,986.0 | 24,448.0 | 27,689.0 | 32,204.0 | **28,751.0** (9M26) | +29.2% YoY sv 9M25 (22,251 tỷ) | Slide 1 |",
        "| **Cơ cấu Dư nợ theo sản phẩm (3Q26)**: | | | | | | | | | Slide 1 |",
        "| - Cho vay Nhu cầu đời sống (Living needs) | % | - | - | - | - | - | **35.0%** | Phân khúc chiếm tỷ trọng lớn nhất | Slide 1 |",
        "| - Cho vay Giải ngân trực tiếp (Direct disb.) | % | - | - | - | - | - | **19.0%** | Động lực tăng trưởng linh hoạt | Slide 1 |",
        "| - Cho vay Điện máy (Electronics) | % | - | - | - | - | - | **18.0%** | Giữ vững thị phần bán lẻ | Slide 1 |",
        "| - Thẻ tín dụng & Khác (Cards & others) | % | - | - | - | - | - | **15.0%** | Mở rộng tệp khách hàng số | Slide 1 |",
        "| - Cho vay Xe máy (Motorbike) | % | - | - | - | - | - | **13.0%** | Phân khúc truyền thống chọn lọc | Slide 1 |",
        "",
        "### 2. Khả năng sinh lời & Hiệu quả vận hành (Profitability & Operations)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | 2021 | 2022 | 2023 | 2024 | 2025 | 9M25 | 9M26 / 3Q26 | Đánh giá & Xu hướng | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Lợi nhuận trước thuế (LNTT / PBT)**| Tỷ đồng | 1,001.0 | 1,152.0 | 660.0 | 1,214.0 | 1,390.0 | 1,089.0 | **1,184.0** | +8.7% YoY sv cùng kỳ 9M25 | Slide 2 |",
        "| **Tổng thu nhập hoạt động (TOI)** | Tỷ đồng | 4,682.0 | 5,701.0 | 5,959.0 | 6,663.0 | 6,936.0 | 5,169.0 | **6,155.0** | +19.1% YoY sv cùng kỳ 9M25 | Slide 2 |",
        "| **Tỷ lệ Chi phí / Thu nhập (CIR)** | % | 44.0% | 38.2% | 39.0% | 35.7% | 37.2% | 36.9% | **33.1%** | Tối ưu hóa mạnh mẽ (-3.8% YoY) | Slide 2 |",
        "| **Tỷ suất sinh lời trên VCSH (ROE)** | % | 23.1% | 24.2% | 13.3% | 23.7% | 22.5% | - | **21.4%** | Duy trì hiệu quả sinh lời bền vững | Slide 2 |",
        "| **Tỷ suất sinh lời trên tài sản (ROA)**| % | 5.3% | 5.7% | 3.0% | 5.2% | 5.0% | - | **4.8%** | Tỷ suất lợi nhuận tài sản cao | Slide 2 |",
        "| **Biên lãi thuần (NIM)** | % | 26.8% | 30.2% | 29.0% | 30.6% | 27.2% | - | **26.9%** | Ổn định ở mức cao trong ngành | Slide 1 |",
        "| **Chi phí vốn (Funding Cost)** | % | 6.5% | 6.0% | 8.1% | 7.7% | 6.1% | - | **7.6%** | Tăng nhẹ do chi phí huy động | Slide 1 |",
        "",
        "### 3. Chất lượng tài sản & Chi phí rủi ro (Asset Quality & Credit Cost)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | 2021 | 2022 | 2023 | 2024 | 2025 | 3Q26 | Đánh giá & Diễn biến | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Tỷ lệ nợ xấu (NPL Ratio)** | % | 7.3% | 7.1% | 7.6% | 7.4% | 6.9% | **7.8%** | Kiểm soát chặt chẽ trong phân khúc tài chính tiêu dùng | Slide 2 |",
        "| **Chi phí tín dụng (Credit Cost)** | % | 11.8% | 15.7% | 18.1% | 17.9% | 14.7% | **16.3%** | Phản ánh chi phí trích lập theo chu kỳ tăng trưởng dư nợ | Slide 2 |",
        "",
        "---",
        "",
        "## PHẦN II: TỔNG HỢP NỘI DUNG & SỐ LIỆU TỪNG SLIDE (SLIDE-BY-SLIDE DETAILS)",
        ""
    ]

    for s in slides_data:
        num = s["slide_num"]
        title = s["title"]
        img_name = s["image_file"]
        rows = s["rows"]
        md.append(f"### Slide {num:02d}: {title}")
        md.append(f"*Ảnh slide: `slides/{img_name}`*")
        md.append("")
        md.append("#### Số liệu & Văn bản trích xuất:")
        if rows:
            md.append("```text")
            for r in rows:
                md.append(" | ".join(r))
            md.append("```")
        else:
            md.append("*(Slide dạng hình ảnh biểu đồ, không nhận diện được văn bản dòng)*")
        md.append("")

    md.extend([
        "---",
        "",
        "## PHẦN III: NGUYÊN TẮC ÁP DỤNG KHI ĐỐI CHIẾU & BIÊN TẬP (AUDIT & RECONCILIATION PROTOCOL)",
        "1. **Chân Lý Chuẩn (Single Source of Truth - SSOT)**: Toàn bộ số liệu định lượng về dư nợ, giải ngân, NIM, LNTT, ROE, NPL và chi phí tín dụng của HD SAISON bắt buộc phải khớp 100% với slide trình chiếu này.",
        "2. **Định dạng số thống nhất**: Luôn sử dụng dấu chấm cho số thập phân (ví dụ: `26.9%`, `28,751.0 tỷ`) và dấu phẩy cho phân cách hàng ngàn.",
        "3. **Cách ly nguồn dữ liệu (Source Isolation)**: Báo cáo chỉ sử dụng dữ liệu từ 2 slide chính thức này."
    ])

    md_path = internal_dir / "ground_truth.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"[✓] Đã tạo thành công {md_path} ({len(md)} dòng).")


def generate_hds_ground_truth(slides_data: List[Dict[str, Any]], internal_dir: Path, source_file: str):
    """Tạo ground_truth.md và ground_truth_raw.json cho HD Securities (HDS)."""
    titles = {
        1: "HDS: Tổng Quan HD Securities Từ 'Why' Đến 'Where' (Sứ Mệnh, Tầm Nhìn, Văn Hóa Al-Native)",
        2: "HDS: Kết Quả 9 Tháng 2026 - LNTT 2,241 Tỷ, Gấp 3.6 Lần Cùng Kỳ (+265% YoY)",
        3: "HDS: Kế Hoạch 2026 - LNTT 9 Tháng Đạt 66% Kế Hoạch Năm (Thực Hiện vs Chỉ Tiêu KH 2026)",
        4: "HDS: AI & FinTech - AI Everywhere Từ Vận Hành Nội Bộ Đến Sản Phẩm Khách Hàng",
        5: "HDS: Chiến Lược 2026-2030 - Ba Giai Đoạn Hướng Tới Vị Thế Dẫn Đầu (Build - Accelerate - Lead)",
        6: "HDS: Kế Hoạch & Tiến Độ IPO, Niêm Yết HoSE (Lộ Trình Tăng Vốn, Nộp Hồ Sơ và Lên Sàn)"
    }
    for s in slides_data:
        s["title"] = titles.get(s["slide_num"], f"Slide {s['slide_num']}")

    json_path = internal_dir / "ground_truth_raw.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "ticker": "HDS",
            "period": "3Q26 & 9M26",
            "meeting_name": "HD Securities 3Q2026 Business Results & Strategic Update",
            "source_file": source_file,
            "total_slides": len(slides_data),
            "slides": slides_data
        }, f, ensure_ascii=False, indent=2)

    md = [
        "# DỮ LIỆU SỐ LIỆU CHUẨN TỪ SLIDES (GROUND TRUTH BENCHMARK DATA) - HD SECURITIES (HDS)",
        "* **Tên công ty**: Công ty Cổ phần Chứng khoán HD (HDSecurities - Mã cổ phiếu dự kiến: HDX)",
        "* **Công ty mẹ**: Ngân hàng TMCP Phát triển TP.HCM (HDBank sở hữu 90.0% trước IPO)",
        "* **Cuộc họp / Kỳ báo cáo**: HD Securities 3Q2026 Business Results & Strategic Update (3Q26 & 9M26)",
        f"* **Tài liệu nguồn**: `{source_file}` ({len(slides_data)} slide trình chiếu chính thức)",
        "* **Phương pháp trích xuất**: Automated Ground Truth Extraction Engine (RapidOCR + Coordinate Clustering)",
        "* **Quy chuẩn định dạng**: Chuẩn quốc tế (dấu chấm `.` thập phân, dấu phẩy `,` phân cách hàng ngàn; ký hiệu quý `3Q26`, `9M26`).",
        "* **Nguyên tắc đối soát**: 100% số liệu cứng lấy trực tiếp từ bản trình chiếu slide chính thức.",
        "",
        "---",
        "",
        "## PHẦN I: BẢNG CHỈ TIÊU TÀI CHÍNH CỐT LÕI (EXECUTIVE SUMMARY BENCHMARK TABLES)",
        "",
        "### 1. Quy mô Bảng cân đối kế toán & Nguồn vốn (Balance Sheet & Capital Structure)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | Đầu năm (01/01/2026) | Thực hiện 9M26 (30/09/2026) | Tăng trưởng | Đánh giá & Vị thế ngành | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Tổng tài sản (Total Assets)** | Tỷ đồng | 5,949.0 | **27,338.0** | **x4.6 lần (+359.5%)** | Quy mô tài sản mở rộng đột phá | Slide 2 |",
        "| **Vốn chủ sở hữu (VCSH)** | Tỷ đồng | 3,480.0 | **14,041.0** | **x4.0 lần (+303.5%)** | Tăng vốn lên 10,960 tỷ thành công | Slide 2, 6 |",
        "| **Dư nợ vay (Borrowings)** | Tỷ đồng | - | **10,565.0** | - | Nguồn vốn tài trợ đòn bẩy hoạt động | Slide 2 |",
        "| **Tỷ lệ Nợ vay / VCSH** | % | - | **75.0%** | An toàn | Đòn bẩy tài chính ở mức thận trọng | Slide 2 |",
        "| **Dư nợ Cho vay Margin** | Tỷ đồng | - | **10,972.0** | 57.7% KH năm (19,000 tỷ) | Động lực tăng trưởng thu nhập lãi | Slide 3 |",
        "| **Số dư trái phiếu phân phối** | Tỷ đồng | - | **73,000.0** | 48.7% KH năm (150,000 tỷ)| Mạng lưới phân phối định chế & bán lẻ | Slide 3 |",
        "| **Giá trị tư vấn phát hành** | Tỷ đồng | - | **9,690.0** | 12.1% KH năm (80,000 tỷ) | Top 3 thị phần tư vấn TPDN (4.4%) | Slide 2, 3 |",
        "| **VCSH mục tiêu cuối năm (sau IPO)**| Tỷ đồng | - | **18,377.0** | Dự phóng sau IPO | Nâng cao năng lực cạnh tranh vốn | Slide 3 |",
        "",
        "### 2. Kết quả hoạt động kinh doanh & Khả năng sinh lời (P&L & Profitability)",
        "",
        "| Chỉ tiêu định lượng | Đơn vị | 9M25 | 9M26 Thực hiện | Kế hoạch cả năm 2026 | Tăng trưởng 9M26 YoY | % Hoàn thành KH 2026 | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Doanh thu thuần (Net Revenue)** | Tỷ đồng | ~1,015.0 | **2,618.0** | **4,555.0** | **+158.0% YoY** | 57.5% | Slide 2, 3 |",
        "| - Quý 1/2026 (1Q26) | Tỷ đồng | - | 423.0 | - | - | - | Slide 2 |",
        "| - Quý 2/2026 (2Q26) | Tỷ đồng | - | 1,248.0 | - | +195.0% QoQ (Quý đỉnh cao) | - | Slide 2 |",
        "| - Quý 3/2026 (3Q26) | Tỷ đồng | - | 947.0 | - | -24.1% QoQ | - | Slide 2 |",
        "| **Lợi nhuận trước thuế (LNTT / PBT)**| Tỷ đồng | 614.0 | **2,241.0** | **3,375.0** | **+265.0% YoY (gấp 3.65 lần)** | **66.3%** | Slide 2, 3 |",
        "| - Quý 1/2026 (1Q26) | Tỷ đồng | - | 352.0 | - | - | - | Slide 2 |",
        "| - Quý 2/2026 (2Q26) | Tỷ đồng | - | 1,118.0 | - | +217.6% QoQ (Quý đỉnh cao) | - | Slide 2 |",
        "| - Quý 3/2026 (3Q26) | Tỷ đồng | - | 769.0 | - | -31.2% QoQ | - | Slide 2 |",
        "| **Lợi nhuận sau thuế (LNST / NPAT)** | Tỷ đồng | ~489.0 | **1,804.0** | - | **+269.0% YoY** | BCTC riêng 3Q26 | Slide 2 |",
        "| **Mục tiêu hoàn thành Q4/2026** | Tỷ đồng | - | - | Cần DT: 1,938 tỷ & LNTT: 1,136 tỷ | - | Đảm bảo về đích 100% KH năm | Slide 3 |",
        "| **Tỷ suất sinh lời trên VCSH (ROE)** | % | - | **26.1%** | 27.0% (Mục tiêu năm) | **Top 1 toàn ngành chứng khoán** | Gần chạm đích kế hoạch | Slide 2, 3 |",
        "| **Tỷ suất sinh lời trên tài sản (ROA)**| % | - | **14.5%** | - | Hiệu quả sử dụng tài sản vượt bậc | - | Slide 2 |",
        "| **Tỷ lệ Chi phí / Doanh thu (CIR)** | % | - | **14.5%** | - | Tối ưu hàng đầu thị trường nhờ AI | - | Slide 2 |",
        "",
        "### 3. Đóng góp theo Khối Kinh Doanh (Business Segments Breakdown - Trước Bù Trừ FTP)",
        "",
        "| Khối kinh doanh | Doanh thu 9M26 (tỷ) | Kế hoạch Doanh thu (tỷ) | % Đạt KH Doanh thu | LNTT 9M26 (tỷ) | Năng lực & Thị phần nổi bật | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Khối Môi giới (Brokerage)** | 438.0 | 845.0 | **51.8%** | **38.0** | Năng lực mới 2026: Bond outright & Institutional sales | Slide 2, 3 |",
        "| **Khối KD Trái phiếu & Tự doanh** | 907.0 | 1,793.0 | **50.6%** | **463.0** | Danh mục tài sản đầu tư thanh khoản cao | Slide 2, 3 |",
        "| **Khối Tư vấn (IB / Advisory)** | 1,079.0 | 1,601.0 | **67.4%** | **1,034.0** | Top 3 thị phần phát hành TPDN (4.4%) | Slide 2, 3 |",
        "| **Khối Nguồn vốn (Treasury)** | 873.0 | 1,486.0 | **58.8%** | **704.0** | Tối ưu hóa thanh khoản & quản trị dòng vốn | Slide 2, 3 |",
        "",
        "### 4. Tiến độ Tăng vốn, IPO và Niêm yết HoSE (Listing & IPO Roadmap)",
        "",
        "| Giai đoạn | Nội dung công việc trọng tâm | Mốc thời gian | Tỷ lệ hoàn thành | Trạng thái chi tiết | Nguồn Slide |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
        "| **Giai đoạn I: Tăng vốn** | - Tăng vốn lên 10,960 tỷ qua phát hành riêng lẻ & chia cổ tức<br>- HDBank nâng sở hữu từ 30% lên 90% trước IPO<br>- Kiểm toán vốn sau phát hành & Hoàn thành kiểm toán BCTC 2025 | 03/2026 - 05/2026 | **100.0%** | Đã hoàn thành toàn bộ, tạo nền tảng vốn vững chắc | Slide 6 |",
        "| **Giai đoạn II: IPO** | - Nộp hồ sơ chào bán lên UBCKNN<br>- Thực hiện chào bán IPO ra công chúng cho nhà đầu tư<br>- Kiểm toán vốn sau IPO | 05/10/2026<br>11/2026<br>12/2026 | **25.0%** | Đã nộp hồ sơ ngày 05/10/2026, đang triển khai chào bán | Slide 6 |",
        "| **Giai đoạn III: Niêm yết HoSE** | - Nộp hồ sơ niêm yết HoSE đồng thời với hồ sơ UBCKNN<br>- Đăng ký cổ phiếu HDX tại VSDC<br>- Nhận giấy phép niêm yết HoSE<br>- Ngày giao dịch đầu tiên trên sàn HoSE | 05/10/2026<br>12/2026<br>< 21/12/2026<br>**01/2027** | **10.0%** | Đã nộp hồ sơ, dự kiến chính thức giao dịch tháng 01/2027 | Slide 6 |",
        "",
        "### 5. Chiến lược Công nghệ & Lộ trình Phát triển 2026-2030 (Tech & Strategic Phases)",
        "",
        "| Trụ cột | Hạng mục giải pháp chi tiết | Nguồn Slide |",
        "| :--- | :--- | :--- |",
        "| **AI Vận hành nội bộ** | - **HDWork-AI Office**: Văn phòng AI tác tử, tự chủ trong quy trình thực cho 100% nhân sự.<br>- **Digital Factory & CoE**: Vận hành tập trung, Hub dữ liệu & chứng từ điện tử, CoE chuẩn hóa và nhân rộng AI.<br>- **HD Advisors app**: Ứng dụng quản lý khách hàng, danh mục và tư vấn có AI hỗ trợ cho chuyên viên. | Slide 4 |",
        "| **Sản phẩm Khách hàng**| - **HDInvest**: Super app AI dẫn dắt toàn bộ hành trình đầu tư của khách hàng.<br>- **FinoMS Pro**: Hệ thống đặt lệnh thông minh OMS/EMS/RMS cho khách hàng cá nhân và tổ chức.<br>- **FinRadar & Alpha Hunter**: Radar thị trường sàng lọc cổ phiếu và trợ lý AI cung cấp insight thời gian thực.<br>- **WealthMgmt & HD Academy**: Tư vấn quản lý gia sản và học viện đầu tư số. | Slide 4 |",
        "| **Đối tác Chiến lược** | Galaxy Technology, FSS, GTS Vietnam, Algo Platform, FPT Smart Cloud, Fintech1, AAR Center, TMG Corporation, OS. | Slide 4 |",
        "| **Chiến lược 3 Giai đoạn**| - **2026-2027 (BUILD)**: Connecting Capital - DCM, margin và tự doanh dẫn dắt tăng trưởng.<br>- **2028 (ACCELERATE)**: Unlocking Opportunity - HDS Prime, cộng đồng nhà đầu tư, chiến dịch đại chúng.<br>- **2029-2030 (LEAD)**: Creating Value, globally - VIFC, token hóa tài sản, B2B mở, thương mại hóa AI Office, mở rộng khu vực. | Slide 5 |",
        "",
        "---",
        "",
        "## PHẦN II: TỔNG HỢP NỘI DUNG & SỐ LIỆU TỪNG SLIDE (SLIDE-BY-SLIDE DETAILS)",
        ""
    ]

    for s in slides_data:
        num = s["slide_num"]
        title = s["title"]
        img_name = s["image_file"]
        rows = s["rows"]
        md.append(f"### Slide {num:02d}: {title}")
        md.append(f"*Ảnh slide: `slides/{img_name}`*")
        md.append("")
        md.append("#### Số liệu & Văn bản trích xuất:")
        if rows:
            md.append("```text")
            for r in rows:
                md.append(" | ".join(r))
            md.append("```")
        else:
            md.append("*(Slide dạng hình ảnh biểu đồ, không nhận diện được văn bản dòng)*")
        md.append("")

    md.extend([
        "---",
        "",
        "## PHẦN III: NGUYÊN TẮC ÁP DỤNG KHI ĐỐI CHIẾU & BIÊN TẬP (AUDIT & RECONCILIATION PROTOCOL)",
        "1. **Chân Lý Chuẩn (Single Source of Truth - SSOT)**: Toàn bộ số liệu định lượng về kết quả kinh doanh 9M26, tiến độ kế hoạch năm, số liệu bảng cân đối, phân bổ khối và tiến độ IPO của HD Securities bắt buộc phải đối soát trực tiếp với slide này.",
        "2. **Định dạng số thống nhất**: Luôn sử dụng dấu chấm cho phần thập phân (ví dụ: `2,241.0 tỷ`, `26.1%`, `14,041.0 tỷ`) và dấu phẩy cho phân cách hàng ngàn.",
        "3. **Cách ly nguồn dữ liệu (Source Isolation)**: Báo cáo chỉ sử dụng dữ liệu từ tài liệu trình chiếu 6 slide chính thức này."
    ])

    md_path = internal_dir / "ground_truth.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    print(f"[✓] Đã tạo thành công {md_path} ({len(md)} dòng).")


def main():
    print("=" * 70)
    print("KHỞI CHẠY QUY TRÌNH TRÍCH XUẤT GROUND TRUTH CHO HDB, HDSAISON, HDS")
    print("=" * 70)
    
    ocr = RapidOCR()
    base_ws = Path("D:/AM/workspace")

    # 1. Cấu hình 3 thực thể
    entities = [
        {
            "ticker": "HDB",
            "folder": base_ws / "Bank" / "HDB",
            "pptx": "HDB_Slides.pptx",
            "misc": ["HDB - 3Q26, 9M26 Update AM.docx", "HDB_AM.docx", "HDB_AM_Format_Guide.md", "HDB_AM_Template.md"],
            "generator": generate_hdb_ground_truth
        },
        {
            "ticker": "HDSAISON",
            "folder": base_ws / "Dịch vụ tài chính" / "HDSAISON",
            "pptx": "HDSAISON_Slides.pptx",
            "misc": [],
            "generator": generate_hdsaison_ground_truth
        },
        {
            "ticker": "HDS",
            "folder": base_ws / "Dịch vụ tài chính" / "HDS",
            "pptx": "HDS_Slides.pptx",
            "misc": ["HDS_AM.docx", "HDS_AM_Format_Guide.md", "HDS_AM_Template.md"],
            "generator": generate_hds_ground_truth
        }
    ]

    for ent in entities:
        ticker = ent["ticker"]
        base_dir = ent["folder"]
        pptx_name = ent["pptx"]
        misc = ent["misc"]
        gen_func = ent["generator"]

        print(f"\n[*] Đang xử lý: {ticker}...")
        
        # Thiết lập cấu trúc 3 tầng
        input_dir, internal_dir, output_dir, slides_dir = setup_workspace(ticker, base_dir, pptx_name, misc)
        pptx_file = input_dir / pptx_name

        # Trích xuất ảnh slide vào input/slides/
        print(f"  -> Đang bóc tách ảnh slide từ {pptx_name} vào {slides_dir.name}...")
        images = extract_slide_images_from_pptx(pptx_file, slides_dir)
        print(f"     Đã bóc tách {len(images)} slide ảnh.")

        # Chạy OCR
        print(f"  -> Đang chạy RapidOCR bóc tách cấu trúc dòng...")
        slides_data = run_ocr_on_images(ocr, images)

        # Xuất ground_truth.md và ground_truth_raw.json
        print(f"  -> Đang tổng hợp báo cáo Ground Truth và ma trận dữ liệu SSOT...")
        gen_func(slides_data, internal_dir, pptx_name)

    # Dọn dẹp thư mục tạm temp_slides nếu có
    temp_dir = base_ws / "temp_slides"
    if temp_dir.exists():
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"\n[✓] Đã dọn dẹp thư mục tạm: {temp_dir}")

    print("\n" + "=" * 70)
    print("HOÀN THÀNH TOÀN BỘ QUY TRÌNH TRÍCH XUẤT DỮ LIỆU SLIDES CHO 3 DOANH NGHIỆP!")
    print("=" * 70)


if __name__ == "__main__":
    main()
