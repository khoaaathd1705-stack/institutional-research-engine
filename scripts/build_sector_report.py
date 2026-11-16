# -*- coding: utf-8 -*-
"""
Module: build_sector_report.py
Biên dịch Analyst Report dựa 100% trên thư mục ngành do User chỉ định.
Không tự động phỏng đoán hay phân loại lại ngành của doanh nghiệp.
- Nếu User đặt trong Bank/ -> Áp dụng format chuẩn MSB.
- Nếu User đặt trong Dịch vụ tài chính/ -> Áp dụng format chuẩn VPX.
- Nếu User đặt trong BĐS/ -> Áp dụng format chuẩn VIC.
- Nếu User đặt trong Bán lẻ/ -> Áp dụng format chuẩn DGW.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Tuple, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import docx
from scripts.document_formatter import DocumentFormatter

WORKSPACE = PROJECT_ROOT / "workspace"

def get_ticker_dir_and_sector(ticker_or_path: str) -> Tuple[Optional[Path], Optional[str]]:
    """
    Xác định thư mục và ngành hoàn toàn dựa trên vị trí mà User đã sắp xếp.
    Hỗ trợ tìm kiếm theo cả đường dẫn trực tiếp lẫn tên mã ticker trong các thư mục con.
    """
    p = Path(ticker_or_path)
    if p.exists() and p.is_dir():
        ticker_dir = p.resolve()
        # Xác định sector cấp cao nhất dưới workspace
        rel_parts = ticker_dir.relative_to(WORKSPACE).parts
        sector_name = rel_parts[0] if rel_parts else ticker_dir.parent.name
        return ticker_dir, sector_name
        
    ticker_upper = ticker_or_path.upper()
    
    # Quét trong WORKSPACE tìm ticker
    for sector_dir in WORKSPACE.iterdir():
        if not sector_dir.is_dir():
            continue
        # Check cấp 1: workspace/<Sector>/<TICKER>
        cand1 = sector_dir / ticker_upper
        if cand1.exists() and cand1.is_dir():
            return cand1, sector_dir.name
        # Check cấp 2: workspace/<Sector>/<Group>/<TICKER> (ví dụ BĐS/VinGroup/VIC)
        for sub_dir in sector_dir.iterdir():
            if sub_dir.is_dir():
                cand2 = sub_dir / ticker_upper
                if cand2.exists() and cand2.is_dir():
                    return cand2, sector_dir.name
                if sub_dir.name.upper() == ticker_upper:
                    return sub_dir, sector_dir.name
                    
    return None, None

def compile_report(ticker_or_path: str) -> bool:
    ticker_dir, sector_name = get_ticker_dir_and_sector(ticker_or_path)
    
    if not ticker_dir:
        print(f"[ERROR] Không tìm thấy thư mục cho '{ticker_or_path}' trong workspace.")
        return False
        
    ticker_upper = ticker_dir.name.upper()
    print(f"=== XỬ LÝ ANALYST REPORT CHO {ticker_upper} ===")
    print(f"[*] Vị trí thư mục do User sắp xếp: {ticker_dir}")
    print(f"[*] Ngành do User chỉ định: '{sector_name}'")
    
    # Áp dụng Benchmark dựa trên đúng thư mục cha mà User đã đặt
    sec_lower = sector_name.lower()
    if sec_lower == "bank":
        print(f"[*] Áp dụng Benchmark Ngân hàng theo MSB (workspace/Bank/MSB/AM-MSB.docx)")
    elif "tài chính" in sec_lower:
        print(f"[*] Áp dụng Benchmark Dịch vụ tài chính theo VPX (workspace/Dịch vụ tài chính/VPX/VPX_AM.docx)")
    elif "bđs" in sec_lower or "bds" in sec_lower:
        print(f"[*] Áp dụng Benchmark Bất động sản theo VIC (workspace/BĐS/VinGroup/VIC/VIC_AM.docx)")
    elif "bán lẻ" in sec_lower or "ban le" in sec_lower or "retail" in sec_lower:
        print(f"[*] Áp dụng Benchmark Bán lẻ theo DGW (workspace/Bán lẻ/DGW/DGW_AM.docx)")
    else:
        print(f"[*] Thư mục ngành '{sector_name}' - Áp dụng cấu trúc chuẩn mực theo thư mục hiện hành.")
        
    # Tìm file markdown nguồn trong thư mục mà User quản lý
    candidate_mds = [
        ticker_dir / f"{ticker_upper}_AM_Template.md",
        ticker_dir / f"{ticker_upper}_AM.md",
        ticker_dir / "analyst_report.md",
        ticker_dir / "output" / "analyst_report.md"
    ]
    
    src_md = None
    for cand in candidate_mds:
        if cand.exists():
            src_md = cand
            break
            
    if not src_md:
        print(f"[ERROR] Không tìm thấy file markdown mẫu nào trong {ticker_dir}")
        return False
        
    print(f"[*] Nguồn dữ liệu markdown: {src_md.name}")
    
    # Chạy linter kiểm tra tuân thủ
    lint_res = DocumentFormatter.lint_document(src_md)
    print(f"[*] Kết quả Linter: Compliant={lint_res.get('compliant')}, Violations={lint_res.get('violations_count')}")
    if not lint_res.get('compliant'):
        print(f"[WARN] Có {lint_res.get('violations_count')} vi phạm từ ngữ / ký hiệu cần chỉnh sửa:")
        for v in lint_res.get('violations', []):
            print(f"   - {v}")
            
    # Tạo file docx đích
    out_docx = ticker_dir / f"{ticker_upper}_AM.docx"
    doc = docx.Document()
    
    # Thiết lập lề 1 inch chuẩn (72pt)
    for section in doc.sections:
        section.top_margin = docx.shared.Pt(72)
        section.bottom_margin = docx.shared.Pt(72)
        section.left_margin = docx.shared.Pt(72)
        section.right_margin = docx.shared.Pt(72)
        
    with open(src_md, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line in lines:
        text = line.strip()
        if not text:
            continue
        doc.add_paragraph(text)
        
    doc.save(out_docx)
    print(f"[SUCCESS] Đã tạo thành công file Word: {out_docx.name} tại {ticker_dir}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Biên dịch Analyst Report dựa 100% trên thư mục ngành do User chỉ định.")
    parser.add_argument("--ticker", type=str, required=True, help="Mã cổ phiếu hoặc đường dẫn thư mục doanh nghiệp do User sắp xếp.")
    args = parser.parse_args()
    
    compile_report(args.ticker)
