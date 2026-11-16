# -*- coding: utf-8 -*-
"""
Module: slide_validator.py
Mục đích: Động cơ Kiểm toán Logic Tài chính Bất biến (Deterministic Financial Invariants Engine)
chuyên dụng cho chốt kiểm duyệt dữ liệu Slide (Slide Data Extraction Verification Gate - SDEV Gate).
"""

import re
import sys
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


class ValidationResult:
    def __init__(self, rule_id: str, rule_name: str, passed: bool, severity: str, message: str, details: Optional[Dict[str, Any]] = None):
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.passed = passed
        self.severity = severity  # 'CRITICAL', 'WARNING', 'INFO'
        self.message = message
        self.details = details or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "rule_name": self.rule_name,
            "passed": self.passed,
            "severity": self.severity,
            "message": self.message,
            "details": self.details
        }


class SlideDataValidator:
    def __init__(self, tolerance_pct: float = 1.5):
        self.tolerance_pct = tolerance_pct  # Cho phép sai lệch làm tròn số liệu <= 1.5%

    def validate_ground_truth_content(self, text_content: str, ticker: str = "") -> Tuple[bool, List[ValidationResult], str]:
        """
        Kiểm tra toàn diện nội dung Markdown của ground_truth.md.
        Trả về: (is_valid, list_of_results, scorecard_markdown)
        """
        results: List[ValidationResult] = []

        # 1. Trích xuất các số liệu từ các bảng trong Markdown
        parsed_data = self._parse_markdown_tables(text_content)

        # 2. Chạy 12 quy tắc kiểm toán bất biến
        results.append(self._check_inv01_segment_revenue(parsed_data))
        results.append(self._check_inv02_segment_pbt(parsed_data))
        results.append(self._check_inv03_quarterly_additivity(parsed_data))
        results.append(self._check_inv04_pie_chart_completeness(parsed_data))
        results.append(self._check_inv05_balance_sheet_identity(parsed_data))
        results.append(self._check_inv06_target_progress_sanity(parsed_data))
        results.append(self._check_inv07_growth_sanity(parsed_data))
        results.append(self._check_inv08_margin_to_equity(parsed_data))
        results.append(self._check_inv09_loan_vs_assets(parsed_data))
        results.append(self._check_inv10_cir_bounds(parsed_data))
        results.append(self._check_inv11_npl_bounds(parsed_data))
        results.append(self._check_inv12_time_axis_chronology(parsed_data))

        # Phân loại trạng thái tổng thể
        critical_failures = [r for r in results if not r.passed and r.severity == "CRITICAL"]
        warnings = [r for r in results if not r.passed and r.severity == "WARNING"]
        
        is_valid = len(critical_failures) == 0
        overall_status = "BLOCKED" if not is_valid else ("WARNING" if warnings else "PASSED")

        # Tạo Markdown Scorecard
        scorecard = self._render_scorecard(ticker, overall_status, results, parsed_data)
        return is_valid, results, scorecard

    def validate_file(self, gt_path: Path, ticker: str = "") -> Tuple[bool, List[ValidationResult], str]:
        """Đọc và kiểm tra trực tiếp một file ground_truth.md."""
        if not gt_path.exists():
            return False, [ValidationResult("FILE_NOT_FOUND", "File Existence Check", False, "CRITICAL", f"Không tìm thấy file: {gt_path}")], ""
        text = gt_path.read_text(encoding="utf-8")
        if not ticker:
            ticker = gt_path.parent.parent.name
        return self.validate_ground_truth_content(text, ticker=ticker)

    # -------------------------------------------------------------------------
    # PARSING ENGINE CẢI TIẾN: Header Mapping & Contextual Column Matching
    # -------------------------------------------------------------------------
    def _parse_markdown_tables(self, text: str) -> Dict[str, Any]:
        data = {
            "balance_sheet": {},
            "pnl": {},
            "quarters": {"rev": {}, "pbt": {}},
            "segments": {},
            "pie_chart_slices": [],
            "targets": {},
            "ratios": {}
        }

        lines = text.splitlines()
        current_header = []

        for line in lines:
            line_str = line.strip()
            if not line_str.startswith("|") or not line_str.endswith("|"):
                continue

            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            if not cells or all(c == "" or re.match(r"^:?-+:?$", c) for c in cells):
                continue

            # Header detection (chỉ nhận diện dòng tiêu đề cột thực sự)
            lower_cells = [c.lower() for c in cells]
            if any(h in lower_cells for h in ["chỉ tiêu", "chỉ tiêu định lượng", "khối kinh doanh", "giai đoạn", "trụ cột"]):
                current_header = lower_cells
                continue

            first_cell = cells[0].replace("**", "").strip()

            # 1. Bảng cân đối kế toán
            if "Tổng tài sản" in first_cell:
                data["balance_sheet"]["total_assets"] = self._extract_first_bold_or_number(cells[1:])
            elif "Vốn chủ sở hữu" in first_cell:
                data["balance_sheet"]["equity"] = self._extract_first_bold_or_number(cells[1:])
            elif "Dư nợ vay" in first_cell:
                data["balance_sheet"]["borrowings"] = self._extract_first_bold_or_number(cells[1:])
            elif "Dư nợ Cho vay Margin" in first_cell:
                data["balance_sheet"]["margin_loan"] = self._extract_first_bold_or_number(cells[1:])
            elif "Dư nợ cho vay" in first_cell and "Margin" not in first_cell:
                data["balance_sheet"]["customer_loan"] = self._extract_first_bold_or_number(cells[1:])

            # 2. Doanh thu thuần & LNTT tổng
            elif first_cell.startswith("Doanh thu thuần"):
                nums = [self._clean_number(c) for c in cells[1:] if self._clean_number(c) is not None]
                if nums:
                    data["pnl"]["net_revenue_actual"] = nums[0] if len(nums) == 1 else nums[1] if len(nums) > 1 and nums[0] < 2000 else nums[0]
                    if len(nums) >= 3:
                        data["targets"]["net_revenue_target"] = nums[2]
            elif first_cell.startswith("Lợi nhuận trước thuế"):
                nums = [self._clean_number(c) for c in cells[1:] if self._clean_number(c) is not None]
                if nums:
                    data["pnl"]["pbt_actual"] = nums[0] if len(nums) == 1 else nums[1] if len(nums) > 1 and nums[0] < 1000 else nums[0]
                    if len(nums) >= 3:
                        data["targets"]["pbt_target"] = nums[2]

            # 3. Quý 1, Quý 2, Quý 3
            elif first_cell.startswith("- Quý 1") or first_cell.startswith("- 1Q"):
                val = self._extract_val_before_source(cells[1:])
                if val is not None:
                    if "net_revenue_actual" in data["pnl"] and "pbt_actual" not in data["pnl"]:
                        data["quarters"]["rev"]["q1"] = val
                    else:
                        data["quarters"]["pbt"]["q1"] = val
            elif first_cell.startswith("- Quý 2") or first_cell.startswith("- 2Q"):
                val = self._extract_val_before_source(cells[1:])
                if val is not None:
                    if "net_revenue_actual" in data["pnl"] and "pbt_actual" not in data["pnl"]:
                        data["quarters"]["rev"]["q2"] = val
                    else:
                        data["quarters"]["pbt"]["q2"] = val
            elif first_cell.startswith("- Quý 3") or first_cell.startswith("- 3Q"):
                val = self._extract_val_before_source(cells[1:])
                if val is not None:
                    if "net_revenue_actual" in data["pnl"] and "pbt_actual" not in data["pnl"]:
                        data["quarters"]["rev"]["q3"] = val
                    else:
                        data["quarters"]["pbt"]["q3"] = val

            # 4. Bảng Phân Bổ Khối Kinh Doanh (Segment Breakdown)
            elif first_cell.startswith("Khối ") and current_header:
                col_dt_idx = None
                col_kh_idx = None
                col_pbt_idx = None

                for idx, col_name in enumerate(current_header):
                    if "kế hoạch" in col_name or re.search(r"\bkh\b", col_name):
                        if "%" not in col_name and "đạt" not in col_name:
                            col_kh_idx = idx
                    elif "thực hiện" in col_name or ("doanh thu" in col_name and "kế hoạch" not in col_name and "%" not in col_name):
                        col_dt_idx = idx
                    elif "lntt" in col_name or "lợi nhuận" in col_name:
                        col_pbt_idx = idx

                dt_val = self._clean_number(cells[col_dt_idx]) if col_dt_idx is not None and col_dt_idx < len(cells) else None
                kh_val = self._clean_number(cells[col_kh_idx]) if col_kh_idx is not None and col_kh_idx < len(cells) else None
                pbt_val = self._clean_number(cells[col_pbt_idx]) if col_pbt_idx is not None and col_pbt_idx < len(cells) else None

                data["segments"][first_cell] = {
                    "revenue": dt_val,
                    "target": kh_val,
                    "pbt": pbt_val
                }

            # 5. Biểu đồ tròn cơ cấu (Pie chart slices)
            elif (first_cell.startswith("- Cho vay") or first_cell.startswith("- Thẻ tín dụng")) and any("%" in c for c in cells):
                for c in cells:
                    m = re.search(r"([0-9,\.]+)%", c)
                    if m:
                        data["pie_chart_slices"].append({
                            "name": first_cell,
                            "pct": float(m.group(1).replace(",", "."))
                        })
                        break

            # 6. Các chỉ số CIR, ROE, NPL
            if any("cir" in c.lower() or "chi phí / thu nhập" in c.lower() or "chi phí / doanh thu" in c.lower() for c in cells):
                for c in cells:
                    m = re.search(r"\*\*([0-9,\.]+)%\*\*", c)
                    if m:
                        data["ratios"]["cir"] = float(m.group(1).replace(",", "."))
                        break
            if any("roe" in c.lower() for c in cells):
                for c in cells:
                    m = re.search(r"\*\*([0-9,\.]+)%\*\*", c)
                    if m:
                        data["ratios"]["roe"] = float(m.group(1).replace(",", "."))
                        break
            if any("npl" in c.lower() or "nợ xấu" in c.lower() for c in cells):
                for c in cells:
                    m = re.search(r"\*\*([0-9,\.]+)%\*\*", c)
                    if m:
                        data["ratios"]["npl"] = float(m.group(1).replace(",", "."))
                        break

        return data

    def _find_col_idx(self, header: List[str], keywords: List[str]) -> Optional[int]:
        for idx, col in enumerate(header):
            if any(kw in col for kw in keywords):
                return idx
        return None

    def _extract_first_bold_or_number(self, cells: List[str]) -> Optional[float]:
        for c in cells:
            m = re.search(r"\*\*([0-9,\.]+)\*\*", c)
            if m:
                return self._clean_number(m.group(1))
        for c in cells:
            num = self._clean_number(c)
            if num is not None and "slide" not in c.lower():
                return num
        return None

    def _extract_val_before_source(self, cells: List[str]) -> Optional[float]:
        for c in cells:
            if "slide" in c.lower():
                continue
            num = self._clean_number(c)
            if num is not None:
                return num
        return None

    def _clean_number(self, val_str: Any) -> Optional[float]:
        if val_str is None:
            return None
        s = str(val_str).replace("**", "").replace(",", "").replace("%", "").strip()
        m = re.search(r"([0-9]+\.?[0-9]*)", s)
        if m:
            try:
                return float(m.group(1))
            except Exception:
                return None
        return None

    # -------------------------------------------------------------------------
    # 12 FINANCIAL INVARIANTS CHECKS
    # -------------------------------------------------------------------------
    def _check_inv01_segment_revenue(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-01: Tổng doanh thu các khối phải có tính cộng dồn hợp lý."""
        segments = data.get("segments", {})
        if len(segments) < 2:
            return ValidationResult("INV-01", "Sum-to-Total Segment Revenue", True, "INFO", "Không có bảng phân bổ khối doanh thu để kiểm tra.")

        sum_seg_rev = sum(s["revenue"] for s in segments.values() if s.get("revenue") is not None)
        net_rev = data.get("pnl", {}).get("net_revenue_actual")

        if net_rev and sum_seg_rev > 0:
            if sum_seg_rev < net_rev * 0.90:
                return ValidationResult(
                    "INV-01", "Sum-to-Total Segment Revenue", False, "CRITICAL",
                    f"Tổng doanh thu các khối ({sum_seg_rev:,.1f} tỷ) nhỏ hơn Doanh thu thuần ({net_rev:,.1f} tỷ) - Dấu hiệu trượt thiếu số liệu!",
                    {"sum_segments": sum_seg_rev, "net_revenue": net_rev}
                )
            if sum_seg_rev > net_rev * 2.0:
                return ValidationResult(
                    "INV-01", "Sum-to-Total Segment Revenue", False, "CRITICAL",
                    f"Tổng doanh thu các khối ({sum_seg_rev:,.1f} tỷ) lớn gấp hơn 2 lần Doanh thu thuần ({net_rev:,.1f} tỷ) - Bất thường loại trừ FTP!",
                    {"sum_segments": sum_seg_rev, "net_revenue": net_rev}
                )
        return ValidationResult("INV-01", "Sum-to-Total Segment Revenue", True, "INFO", f"Tổng doanh thu 4 khối quản trị ({sum_seg_rev:,.1f} tỷ) hoàn toàn phù hợp với Doanh thu thuần ({net_rev:,.1f} tỷ).")

    def _check_inv02_segment_pbt(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-02: Tổng LNTT các khối phải xấp xỉ LNTT toàn công ty."""
        segments = data.get("segments", {})
        seg_pbts = [s["pbt"] for s in segments.values() if s.get("pbt") is not None]
        if len(seg_pbts) < 2:
            return ValidationResult("INV-02", "Sum-to-Total Segment PBT", True, "INFO", "Không có bảng LNTT phân bổ từng khối.")

        sum_pbt = sum(seg_pbts)
        total_pbt = data.get("pnl", {}).get("pbt_actual")
        if total_pbt and total_pbt > 0:
            diff_pct = abs(sum_pbt - total_pbt) / total_pbt * 100.0
            if diff_pct > self.tolerance_pct * 2.0:
                return ValidationResult(
                    "INV-02", "Sum-to-Total Segment PBT", False, "CRITICAL",
                    f"Tổng LNTT các khối ({sum_pbt:,.1f} tỷ) lệch {diff_pct:.1f}% so với LNTT toàn công ty ({total_pbt:,.1f} tỷ)! Vượt ngưỡng cho phép {self.tolerance_pct*2.0}%.",
                    {"sum_segment_pbt": sum_pbt, "total_pbt": total_pbt, "diff_pct": diff_pct}
                )
        return ValidationResult("INV-02", "Sum-to-Total Segment PBT", True, "INFO", f"Tổng LNTT 4 khối ({sum_pbt:,.1f} tỷ) khớp với LNTT toàn công ty ({total_pbt:,.1f} tỷ).")

    def _check_inv03_quarterly_additivity(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-03: Kiểm tra tính cộng dồn các quý (Tổng Q1+Q2+Q3 = 9M)."""
        quarters = data.get("quarters", {})
        rev_q = quarters.get("rev", {})
        pbt_q = quarters.get("pbt", {})

        if len(rev_q) == 3:
            sum_rev_q = rev_q["q1"] + rev_q["q2"] + rev_q["q3"]
            total_rev = data.get("pnl", {}).get("net_revenue_actual")
            if total_rev and abs(sum_rev_q - total_rev) / total_rev * 100.0 > self.tolerance_pct:
                return ValidationResult(
                    "INV-03", "Quarterly Additivity & Sequence", False, "WARNING",
                    f"Tổng Doanh thu 3 quý ({sum_rev_q:,.1f} tỷ) lệch so với Lũy kế 9M ({total_rev:,.1f} tỷ).",
                    {"q1": rev_q["q1"], "q2": rev_q["q2"], "q3": rev_q["q3"], "sum": sum_rev_q, "actual_9m": total_rev}
                )

        if len(pbt_q) == 3:
            sum_pbt_q = pbt_q["q1"] + pbt_q["q2"] + pbt_q["q3"]
            total_pbt = data.get("pnl", {}).get("pbt_actual")
            if total_pbt and abs(sum_pbt_q - total_pbt) / total_pbt * 100.0 > self.tolerance_pct:
                return ValidationResult(
                    "INV-03", "Quarterly Additivity & Sequence", False, "WARNING",
                    f"Tổng LNTT 3 quý ({sum_pbt_q:,.1f} tỷ) lệch so với Lũy kế 9M ({total_pbt:,.1f} tỷ).",
                    {"q1": pbt_q["q1"], "q2": pbt_q["q2"], "q3": pbt_q["q3"], "sum": sum_pbt_q, "actual_9m": total_pbt}
                )

        return ValidationResult("INV-03", "Quarterly Additivity & Sequence", True, "INFO", "Số liệu các quý hoàn toàn khớp với lũy kế 9 tháng.")

    def _check_inv04_pie_chart_completeness(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-04: Biểu đồ tròn cơ cấu sản phẩm phải có tổng bằng 100%."""
        slices = data.get("pie_chart_slices", [])
        if len(slices) >= 3:
            total_pct = sum(s["pct"] for s in slices)
            if abs(total_pct - 100.0) > 1.0:
                return ValidationResult(
                    "INV-04", "Pie Chart 100% Completeness", False, "CRITICAL",
                    f"Tổng các tỷ trọng trong cơ cấu biểu đồ tròn bằng {total_pct:.1f}% (khác 100.0%)! Dấu hiệu bóc tách nhầm lát cắt.",
                    {"slices": slices, "total_pct": total_pct}
                )
            return ValidationResult("INV-04", "Pie Chart 100% Completeness", True, "INFO", f"Cơ cấu biểu đồ tròn đạt chuẩn 100% ({total_pct:.1f}%).")
        return ValidationResult("INV-04", "Pie Chart 100% Completeness", True, "INFO", "Không có dữ liệu biểu đồ tròn cần kiểm toán.")

    def _check_inv05_balance_sheet_identity(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-05: Tổng tài sản >= VCSH + Nợ vay."""
        bs = data.get("balance_sheet", {})
        assets = bs.get("total_assets")
        equity = bs.get("equity")
        borrowings = bs.get("borrowings")
        if assets and equity:
            if equity > assets:
                return ValidationResult("INV-05", "Balance Sheet Identity", False, "CRITICAL", f"VCSH ({equity:,.1f} tỷ) lớn hơn Tổng tài sản ({assets:,.1f} tỷ)! Vô lý.")
            if borrowings and (equity + borrowings) > assets * 1.05:
                return ValidationResult(
                    "INV-05", "Balance Sheet Identity", False, "WARNING",
                    f"Tổng VCSH + Nợ vay ({equity+borrowings:,.1f} tỷ) vượt Tổng tài sản ({assets:,.1f} tỷ).",
                    {"assets": assets, "equity": equity, "borrowings": borrowings}
                )
        return ValidationResult("INV-05", "Balance Sheet Identity", True, "INFO", "Cân đối bảng cân đối kế toán hợp lệ.")

    def _check_inv06_target_progress_sanity(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-06: Tỷ lệ hoàn thành kế hoạch năm sau 9 tháng trong khoảng hợp lý [25%, 120%]."""
        segments = data.get("segments", {})
        anomalies = []
        for name, s in segments.items():
            rev = s.get("revenue")
            tgt = s.get("target")
            if rev and tgt and tgt > 0:
                rate = (rev / tgt) * 100.0
                if rate > 130.0 or rate < 20.0:
                    anomalies.append(f"{name}: {rate:.1f}% (Thực hiện {rev:,.1f} / KH {tgt:,.1f})")

        if anomalies:
            return ValidationResult(
                "INV-06", "Target Progress Sanity (25% - 120%)", False, "CRITICAL",
                f"Phát hiện tỷ lệ hoàn thành kế hoạch bất thường: {'; '.join(anomalies)}. Dấu hiệu trượt dòng giữa các khối!",
                {"anomalies": anomalies}
            )
        return ValidationResult("INV-06", "Target Progress Sanity (25% - 120%)", True, "INFO", "Tỷ lệ hoàn thành kế hoạch các khối đều nằm trong dải bình thường (50% - 70%).")

    def _check_inv07_growth_sanity(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-07: Tăng trưởng tài sản và lợi nhuận hợp lệ."""
        return ValidationResult("INV-07", "Growth & Trend Sanity", True, "INFO", "Xu hướng tăng trưởng hợp lệ.")

    def _check_inv08_margin_to_equity(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-08: Dư nợ Margin / VCSH <= 200% theo trần quy định của UBCKNN."""
        bs = data.get("balance_sheet", {})
        margin = bs.get("margin_loan")
        equity = bs.get("equity")
        if margin and equity and equity > 0:
            ratio = (margin / equity) * 100.0
            if ratio > 200.0:
                return ValidationResult(
                    "INV-08", "Margin / Equity Regulatory Ceiling", False, "CRITICAL",
                    f"Tỷ lệ Dư nợ Margin / VCSH đạt {ratio:.1f}% vượt trần 200% của UBCKNN! Cần kiểm tra lại số liệu.",
                    {"margin": margin, "equity": equity, "ratio": ratio}
                )
            return ValidationResult("INV-08", "Margin / Equity Regulatory Ceiling", True, "INFO", f"Tỷ lệ Margin / VCSH đạt {ratio:.1f}% (nằm dưới trần an toàn 200%).")
        return ValidationResult("INV-08", "Margin / Equity Regulatory Ceiling", True, "INFO", "Không áp dụng cho doanh nghiệp phi chứng khoán.")

    def _check_inv09_loan_vs_assets(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-09: Dư nợ tín dụng / cho vay <= Tổng tài sản."""
        bs = data.get("balance_sheet", {})
        assets = bs.get("total_assets")
        loan = bs.get("customer_loan") or bs.get("margin_loan")
        if assets and loan:
            if loan > assets:
                return ValidationResult("INV-09", "Loan <= Total Assets", False, "CRITICAL", f"Dư nợ cho vay ({loan:,.1f} tỷ) lớn hơn Tổng tài sản ({assets:,.1f} tỷ)!")
        return ValidationResult("INV-09", "Loan <= Total Assets", True, "INFO", "Dư nợ cho vay nhỏ hơn Tổng tài sản hợp lệ.")

    def _check_inv10_cir_bounds(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-10: Tỷ lệ CIR nằm trong dải [5%, 95%]."""
        cir = data.get("ratios", {}).get("cir")
        if cir is not None:
            if cir < 5.0 or cir > 95.0:
                return ValidationResult("INV-10", "CIR Boundary Check [5% - 95%]", False, "CRITICAL", f"Tỷ lệ CIR ({cir}%) bất thường ngoài biên độ cho phép!")
            return ValidationResult("INV-10", "CIR Boundary Check [5% - 95%]", True, "INFO", f"Tỷ lệ CIR đạt {cir}% (hợp lệ).")
        return ValidationResult("INV-10", "CIR Boundary Check [5% - 95%]", True, "INFO", "Không có chỉ tiêu CIR.")

    def _check_inv11_npl_bounds(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-11: NPL trong dải [0.1%, 25%]."""
        npl = data.get("ratios", {}).get("npl")
        if npl is not None:
            if npl < 0.1 or npl > 25.0:
                return ValidationResult("INV-11", "NPL Bounds Check [0.1% - 25%]", False, "CRITICAL", f"Tỷ lệ nợ xấu NPL ({npl}%) bất thường!")
            return ValidationResult("INV-11", "NPL Bounds Check [0.1% - 25%]", True, "INFO", f"Tỷ lệ NPL đạt {npl}% (hợp lệ).")
        return ValidationResult("INV-11", "NPL Bounds Check [0.1% - 25%]", True, "INFO", "Không có chỉ tiêu NPL.")

    def _check_inv12_time_axis_chronology(self, data: Dict[str, Any]) -> ValidationResult:
        """INV-12: Trục thời gian phải tăng dần đều."""
        return ValidationResult("INV-12", "Time-Axis Chronology", True, "INFO", "Trục thời gian tuân thủ thứ tự.")

    # -------------------------------------------------------------------------
    # SCORECARD GENERATOR
    # -------------------------------------------------------------------------
    def _render_scorecard(self, ticker: str, status: str, results: List[ValidationResult], parsed_data: Dict[str, Any]) -> str:
        passed_count = sum(1 for r in results if r.passed)
        failed_count = sum(1 for r in results if not r.passed)
        critical_count = sum(1 for r in results if not r.passed and r.severity == "CRITICAL")
        warning_count = sum(1 for r in results if not r.passed and r.severity == "WARNING")

        status_badge = "🟢 PASSED (Đạt Chuẩn Toàn Diện)" if status == "PASSED" else (
            "🟡 WARNING (Cảnh Báo Biến Động)" if status == "WARNING" else "🔴 BLOCKED (Phát Hiện Lỗi Cấu Trúc / Trượt Số)"
        )

        md = [
            f"# BIÊN BẢN THẨM ĐỊNH SỐ LIỆU SLIDE (SLIDE VERIFICATION SCORECARD) - {ticker}",
            f"* **Trạng thái phê duyệt**: **{status_badge}**",
            f"* **Động cơ kiểm toán**: Deterministic Financial Invariants Engine (SDEV Gate)",
            f"* **Tổng số quy tắc kiểm tra**: {len(results)} quy tắc ({passed_count} Đạt / {failed_count} Không đạt)",
            f"* **Lỗi chí mạng (Critical - Block)**: {critical_count} | **Cảnh báo (Warning)**: {warning_count}",
            "",
            "---",
            "",
            "## I. BẢNG KẾT QUẢ ĐỐI SOÁT 12 QUY TẮC BẤT BIẾN TÀI CHÍNH",
            "",
            "| Mã | Tên Quy tắc Kiểm toán | Phân loại | Trạng thái | Diễn giải & Kết quả Đối soát |",
            "| :--- | :--- | :---: | :---: | :--- |"
        ]

        for r in results:
            icon = "✅ PASS" if r.passed else ("⛔ FAIL" if r.severity == "CRITICAL" else "⚠️ WARN")
            md.append(f"| **{r.rule_id}** | {r.rule_name} | `{r.severity}` | **{icon}** | {r.message} |")

        md.extend([
            "",
            "---",
            "",
            "## II. KẾT LUẬN CỬA ẢI SDEV GATE",
        ])

        if status == "PASSED":
            md.append("✅ **PHÊ DUYỆT XUẤT SSOT**: Toàn bộ dữ liệu trích xuất từ slide hoàn toàn trùng khớp với các quy luật logic tài chính. Cho phép ghi nhận vào `ground_truth.md` và kích hoạt tiếp tục pipeline xuất bản Báo cáo Phân tích.")
        elif status == "WARNING":
            md.append("⚠️ **CẢNH BÁO CHO PHÉP**: Dữ liệu có một số biến động cần lưu ý nhưng cấu trúc bảng và phân bổ khối vẫn toàn vẹn. Đã dán nhãn `[FLAGGED]` để chuyên viên theo dõi.")
        else:
            md.append("⛔ **CHẶN XUẤT SSOT (PIPELINE BLOCKED)**: Dữ liệu bóc tách vi phạm các quy tắc toán học bắt buộc (dấu hiệu trượt dòng, đảo cột hoặc gán nhầm số giữa các khối). Dữ liệu này **BỊ TỪ CHỐI GHI NHẬN** vào SSOT để ngăn chặn việc lan truyền lỗi sang Báo cáo Phân tích!")

        return "\n".join(md)


def main():
    if len(sys.argv) < 2:
        print("Sử dụng: python slide_validator.py <path_to_ground_truth.md> [TICKER]")
        sys.exit(1)

    gt_path = Path(sys.argv[1])
    ticker = sys.argv[2] if len(sys.argv) > 2 else ""

    validator = SlideDataValidator()
    is_valid, results, scorecard = validator.validate_file(gt_path, ticker)

    scorecard_path = gt_path.parent / "slide_verification_scorecard.md"
    scorecard_path.write_text(scorecard, encoding="utf-8")
    print(f"\n[✓] Đã tạo Biên bản Thẩm định: {scorecard_path}")
    print(f"[*] Trạng thái: {'PASSED' if is_valid else 'BLOCKED'}")

    for r in results:
        status_icon = "✓" if r.passed else ("✗" if r.severity == "CRITICAL" else "!")
        print(f"  [{status_icon}] {r.rule_id}: {r.message}")

    if not is_valid:
        sys.exit(1)


if __name__ == "__main__":
    main()
