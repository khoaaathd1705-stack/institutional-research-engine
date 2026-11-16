# -*- coding: utf-8 -*-
"""
Script: am_pipeline.py
Mục đích: Pipeline tổng điều phối toàn bộ quy trình xử lý Analyst Meeting / Earnings Call (One-Stop Master Runner).
Tự động thực hiện toàn bộ các bước:
- Giai đoạn 1.5: Trích xuất Ground Truth siêu tốc từ Slide PDF (extract_ground_truth.py, ~0.15s).
- Giai đoạn 3 & 4: Đóng gói định dạng toàn diện Full Transcript & Analyst Report sang Word (.docx) chuẩn TCX.
- Linter: Kiểm định tuân thủ ngôn từ trung lập định chế tài chính (AGENTS.md).
"""

import os
import sys
import time
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from document_formatter import DocumentFormatter
from script_cleaner import ScriptCleaner
from metric_harvester import MetricHarvester


class AMPipeline:
    """Master Pipeline điều phối toàn bộ quy trình xử lý cuộc họp Analyst Meeting."""

    def __init__(self, workspace_dir: str, ticker: Optional[str] = None, period: Optional[str] = None, force: bool = False, skip_ocr_if_vector: bool = True):
        self.workspace = Path(workspace_dir).resolve()
        if not self.workspace.exists():
            raise FileNotFoundError(f"Thư mục không tồn tại: {workspace_dir}")

        self.ticker = ticker or self.workspace.name.upper()
        self.period = period or "9M2026"
        self.force = force
        self.skip_ocr_if_vector = skip_ocr_if_vector
        self.output_dir = self.workspace / "output"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.input_dir = self.workspace / "input" if (self.workspace / "input").exists() else (self.workspace / "input_docs")
        self.internal_dir = self.workspace / "internal" if (self.workspace / "internal").exists() else self.workspace / "input_docs"
        self.input_docs_dir = self.internal_dir

    def run_stage_ground_truth(self) -> bool:
        """Giai đoạn 1.5: Trích xuất Ground Truth siêu tốc từ Slide PDF (Vector Native Text + Caching)."""
        print("\n[GIAI ĐOẠN 1.5] Trích xuất Ground Truth từ Slide...")
        t0 = time.time()

        gt_md = self.input_docs_dir / "ground_truth.md"
        # 1. Kiểm tra cache thông minh trước
        if not self.force and gt_md.exists() and gt_md.stat().st_size > 500:
            print(f"  [✓] Sử dụng Ground Truth từ cache: {gt_md.name} ({gt_md.stat().st_size / 1024:.1f} KB)")
            print(f"      Bỏ qua bóc tách lại slide (0.001s). Dùng cờ --force nếu muốn trích xuất lại!")
            return True

        # Tìm file slide trong input/, input_docs/ hoặc workspace
        slide_pdf = None
        for cand_dir in [self.input_dir, self.workspace / "input_docs", self.workspace]:
            if cand_dir and cand_dir.exists():
                for f in cand_dir.glob("*.pdf"):
                    slide_pdf = f
                    break
            if slide_pdf:
                break

        if not slide_pdf:
            print(f"  [i] Không tìm thấy file Slide PDF trong {self.input_docs_dir} hoặc {self.workspace}. Bỏ qua trích xuất slide.")
            return False

        print(f"  --> Phát hiện file slide: {slide_pdf.name}")
        script_dir = Path(__file__).resolve().parent
        cmd = [
            sys.executable,
            str(script_dir / "extract_ground_truth.py"),
            "--input", str(slide_pdf),
            "--out-dir", str(self.input_docs_dir),
            "--ticker", self.ticker,
            "--period", self.period,
            "--meeting", f"{self.ticker} {self.period} Earnings Call"
        ]
        if self.force:
            cmd.append("--force")
        if self.skip_ocr_if_vector:
            cmd.append("--skip-ocr-if-vector")

        try:
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", check=True)
            if res.stdout:
                for line in res.stdout.strip().splitlines():
                    print(f"  {line}")
            elapsed = time.time() - t0
            print(f"  [✓] Hoàn tất bước Ground Truth trong {elapsed:.2f}s!")
            print(f"      File tạo ra: {gt_md} ({gt_md.stat().st_size / 1024:.1f} KB)")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  [!] Lỗi khi chạy extract_ground_truth.py: {e.stderr}")
            return False


    def run_stage_clean_script(self) -> Optional[Dict[str, Any]]:
        """Giai đoạn 1.8: Tiền xử lý Raw Script siêu tốc (<15ms) qua ScriptCleaner."""
        print(f"\n[GIAI ĐOẠN 1.8] Tiền xử lý Raw Script siêu tốc (Heuristic Cleaner)...")
        t0 = time.time()
        raw_file = None
        for cand in [self.workspace / "raw_transcript.txt", self.workspace / "input_docs" / "raw_transcript.txt"]:
            if cand.exists():
                raw_file = cand
                break
        if not raw_file:
            print(f"  [i] Chưa có raw_transcript.txt trong {self.workspace}, bỏ qua tiền xử lý thô.")
            return None

        res = ScriptCleaner.process_file(str(raw_file))
        elapsed = time.time() - t0
        print(f"  [✓] Dọn dẹp disfluencies & Chuẩn hóa quý hoàn tất trong {elapsed*1000:.2f} ms!")
        print(f"      Dung lượng: {res['raw_chars']} -> {res['cleaned_chars']} ký tự (Giảm {res['compression_ratio']})")

        qa_count = res['segments'].get('qa_items_count', 0)
        if qa_count > 0:
            print(f"  [⚡] Phát hiện {qa_count} câu hỏi Q&A từ Transcript:")
            for idx, q_item in enumerate(res['segments']['qa_items'][:8], start=1):
                q_text = q_item['question'][:75] + ("..." if len(q_item['question']) > 75 else "")
                print(f"      {idx}. {q_text}")
        return res

    def run_stage_reconciliation(self) -> bool:
        """Giai đoạn 2.5: Bóc tách & Đối chiếu số liệu siêu tốc (<5ms) qua MetricHarvester."""
        print(f"\n[GIAI ĐOẠN 2.5] Đối soát chéo số liệu Slide vs Transcript (Metric Harvester)...")
        t0 = time.time()
        gt_file = self.input_docs_dir / "ground_truth.md"
        if not gt_file.exists():
            print(f"  [i] Chưa có ground_truth.md, bỏ qua đối soát số liệu.")
            return False

        res_path = MetricHarvester.reconcile(str(self.workspace), ticker=self.ticker, period=self.period)
        elapsed = time.time() - t0
        print(f"  [✓] Xuất ma trận đối chiếu hoàn tất trong {elapsed*1000:.2f} ms: {res_path}")
        return True

    def run_stage_formatting(self) -> Dict[str, Any]:
        """Giai đoạn 3 & 4: Đóng gói định dạng chuẩn Word DOCX & Linter tuân thủ."""
        print(f"\n[GIAI ĐOẠN 3 & 4] Đóng gói định dạng (Format Packager) theo TCX Benchmark...")
        t0 = time.time()
        result = DocumentFormatter.compile_workspace(
            workspace_dir=str(self.workspace),
            ticker=self.ticker,
            period=self.period
        )
        elapsed = time.time() - t0
        print(f"  [✓] Đóng gói định dạng hoàn tất trong {elapsed:.2f}s!")
        return result

    def print_executive_snapshot(self):
        """In bảng tóm tắt chỉ số tài chính cốt lõi (Executive Financial Snapshot) từ ground_truth.md."""
        gt_file = self.internal_dir / "ground_truth.md"
        if not gt_file.exists():
            return
        try:
            with open(gt_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            tables_found = []
            current_table = []
            in_table = False
            for line in lines:
                l_str = line.strip()
                if l_str.startswith("|") and l_str.endswith("|"):
                    current_table.append(l_str)
                    in_table = True
                else:
                    if in_table and len(current_table) >= 3:
                        tables_found.append(current_table)
                    current_table = []
                    in_table = False
            if in_table and len(current_table) >= 3:
                tables_found.append(current_table)

            if not tables_found:
                return

            print("\n" + "-" * 70)
            print("  EXECUTIVE FINANCIAL SNAPSHOT (TÓM TẮT CHỈ SỐ CỐT LÕI TỪ SLIDES)")
            print("-" * 70)
            for tbl in tables_found[:2]:
                for row in tbl[:10]:
                    print(f"  {row}")
                print()
            print("-" * 70)
        except Exception as e:
            print(f"  [!] Không thể sinh bảng snapshot: {e}")

    def print_summary(self, result: Dict[str, Any]):
        """In bảng tổng kết kết quả thực hiện."""
        print(f"\n" + "=" * 70)
        print(f"       TỔNG KẾT PIPELINE HOÀN TẤT: {self.ticker} ({self.period})")
        print(f"=" * 70)
        print(f"  Thư mục làm việc: {self.workspace}")
        print(f"  Thư mục kết quả:  {self.output_dir}\n")

        print(f"  DANH SÁCH SẢN PHẨM ĐẦU RA:")
        files_to_check = [
            ("ground_truth.md", self.internal_dir / "ground_truth.md", "Số liệu chuẩn từ Slide (SSOT)"),
            ("slide_verification_scorecard.md", self.internal_dir / "slide_verification_scorecard.md", "Biên bản thẩm định SDEV Gate"),
            ("data_reconciliation.md", self.internal_dir / "data_reconciliation.md", "Ma trận đối chiếu Slide vs Transcript (MD)"),
            ("data_reconciliation.docx", self.internal_dir / "data_reconciliation.docx", "Word Đối chiếu nội bộ khổ ngang A4"),
            ("full_transcript.md", self.output_dir / "full_transcript.md", "Bản ghi đầy đủ theo ngôn ngữ Speaker (MD)"),
            ("full_transcript.docx", self.output_dir / "full_transcript.docx", "Word Transcript chuẩn Corporate"),
            ("analyst_report.md", self.output_dir / "analyst_report.md", "Báo cáo phân tích tiếng Việt 3 phần (MD)"),
            ("analyst_report.docx", self.output_dir / "analyst_report.docx", "Word Report chuẩn Institutional Research (Tiếng Việt)"),
        ]

        for fname, path, desc in files_to_check:
            if path.exists():
                size_kb = path.stat().st_size / 1024
                print(f"  [✓] {fname:<36} | {size_kb:>6.1f} KB | {desc}")
            else:
                print(f"  [-] {fname:<36} |   N/A    | {desc} (Chưa tạo)")

        print(f"\n  KIỂM ĐỊNH TUÂN THỦ QUY CHUẨN ĐỊNH CHẾ TÀI CHÍNH:")
        linters = result.get("linter", [])
        all_compliant = True
        for l in linters:
            status = "100% TUÂN THỦ (Zero PR Buzzwords)" if l["compliant"] else f"CÓ {l['violations_count']} TỪ NGỮ CẦN ĐỔI"
            print(f"  - {Path(l['source']).name:<25}: {status}")
            if not l["compliant"]:
                all_compliant = False

        print(f"=" * 70)
        if all_compliant:
            print(f"  >>> TRẠNG THÁI: TOÀN BỘ OUTPUT ĐẠT CHUẨN NGHIÊN CỨU ĐỊNH CHẾ CAO NHẤT <<<")
        else:
            print(f"  >>> TRẠNG THÁI: ĐÃ ĐÓNG GÓI XONG, CẦN RÀ SOÁT TỪ NGỮ CẢM TÍNH ĐƯỢC BÁO BỞI LINTER <<<")
        print(f"=" * 70 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Master Analyst Meeting Pipeline: Tự động hóa toàn diện từ Slide đến Word Report.")
    parser.add_argument("workspace", type=str, help="Thư mục workspace của doanh nghiệp (ví dụ: workspace/VPL)")
    parser.add_argument("--ticker", "-t", type=str, help="Mã cổ phiếu (ví dụ: VPL, TCX)")
    parser.add_argument("--period", "-p", type=str, default="9M2026", help="Kỳ báo cáo (mặc định: 9M2026)")
    parser.add_argument("--skip-ground-truth", action="store_true", help="Bỏ qua bước trích xuất slide")
    parser.add_argument("--skip-docx", action="store_true", help="Bỏ qua bước tạo file Word")
    parser.add_argument("--lint-only", action="store_true", help="Chỉ chạy kiểm định ngôn từ trung lập")
    parser.add_argument("--fast", action="store_true", help="Kích hoạt chế độ Fast-Track siêu tốc (< 2 giây)")
    parser.add_argument("--force", "-f", action="store_true", help="Bỏ qua cache, ép trích xuất lại Slide và đối soát từ đầu")
    parser.add_argument("--skip-ocr-if-vector", action="store_true", default=True, help="Tự động nhận diện PDF vector bỏ qua OCR")
    parser.add_argument("--slides-only", action="store_true", help="Pha 1: Chỉ đọc slide, kiểm duyệt SDEV Gate và xuất ground_truth.md + scorecard.md")
    parser.add_argument("--report-only", action="store_true", help="Pha 2: Bỏ qua đọc slide, sử dụng SSOT có sẵn và raw_script để ra report")

    args = parser.parse_args()

    pipeline = AMPipeline(args.workspace, ticker=args.ticker, period=args.period, force=getattr(args, "force", False), skip_ocr_if_vector=getattr(args, "skip_ocr_if_vector", True))

    if args.slides_only:
        print("\n" + "=" * 70)
        print("  [PHA 1] TIỀN THẨM ĐỊNH SLIDE & THIẾT LẬP DỮ LIỆU CHUẨN SSOT")
        print("=" * 70)
        pipeline.run_stage_ground_truth()
        scorecard = pipeline.internal_dir / "slide_verification_scorecard.md"
        gt_file = pipeline.internal_dir / "ground_truth.md"
        pipeline.print_executive_snapshot()
        print(f"\n[✓] Hoàn tất Pha 1! Dữ liệu đã được kiểm duyệt tại:")
        print(f"    - SSOT:      {gt_file}")
        if scorecard.exists():
            print(f"    - Scorecard: {scorecard}")
        print(f"    --> Bây giờ bạn có thể hoàn thiện raw_script và nạp vào để chạy tiếp Pha 2.")
        print("=" * 70 + "\n")
        return

    if args.report_only:
        print("\n" + "=" * 70)
        print("  [PHA 2] KHỚP NỐI RAW SCRIPT & XUẤT BẢN TOÀN DIỆN (REPORT & TRANSCRIPT)")
        print("=" * 70)
        pipeline.run_stage_clean_script()
        pipeline.run_stage_reconciliation()
        if not args.skip_docx:
            result = pipeline.run_stage_formatting()
            pipeline.print_summary(result)
        return

    if args.fast:
        print("\n⚡ KÍCH HOẠT CHẾ ĐỘ FAST PIPELINE (TỔNG THỜI GIAN < 2 GIÂY) ⚡")
        # 1. Slide Ground Truth (< 0.2s nếu vector / 0.001s nếu cache)
        if not args.skip_ground_truth:
            pipeline.run_stage_ground_truth()
        # 2. Clean Script (<15ms)
        pipeline.run_stage_clean_script()
        # 2. Reconcile Metrics (<5ms)
        pipeline.run_stage_reconciliation()
        # 3. Format Packaging & DOCX Compilation (<0.6s)
        result = pipeline.run_stage_formatting()
        pipeline.print_summary(result)
        return


    if args.lint_only:
        DocumentFormatter.compile_workspace(args.workspace, ticker=args.ticker, period=args.period)
        return

    # 1. Slide Ground Truth
    if not args.skip_ground_truth:
        pipeline.run_stage_ground_truth()

    # 2. Format Packaging & DOCX Compilation
    if not args.skip_docx:
        result = pipeline.run_stage_formatting()
        pipeline.print_summary(result)


if __name__ == "__main__":
    main()
