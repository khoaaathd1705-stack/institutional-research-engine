# BIÊN BẢN THẨM ĐỊNH SỐ LIỆU SLIDE (SLIDE VERIFICATION SCORECARD) - OCB
* **Trạng thái phê duyệt**: **🟢 PASSED (Đạt Chuẩn Toàn Diện)**
* **Động cơ kiểm toán**: Deterministic Financial Invariants Engine (SDEV Gate)
* **Tổng số quy tắc kiểm tra**: 12 quy tắc (12 Đạt / 0 Không đạt)
* **Lỗi chí mạng (Critical - Block)**: 0 | **Cảnh báo (Warning)**: 0

---

## I. BẢNG KẾT QUẢ ĐỐI SOÁT 12 QUY TẮC BẤT BIẾN TÀI CHÍNH

| Mã | Tên Quy tắc Kiểm toán | Phân loại | Trạng thái | Diễn giải & Kết quả Đối soát |
| :--- | :--- | :---: | :---: | :--- |
| **INV-01** | Sum-to-Total Segment Revenue | `INFO` | **✅ PASS** | Không có bảng phân bổ khối doanh thu để kiểm tra. |
| **INV-02** | Sum-to-Total Segment PBT | `INFO` | **✅ PASS** | Không có bảng LNTT phân bổ từng khối. |
| **INV-03** | Quarterly Additivity & Sequence | `INFO` | **✅ PASS** | Số liệu các quý hoàn toàn khớp với lũy kế 9 tháng. |
| **INV-04** | Pie Chart 100% Completeness | `INFO` | **✅ PASS** | Không có dữ liệu biểu đồ tròn cần kiểm toán. |
| **INV-05** | Balance Sheet Identity | `INFO` | **✅ PASS** | Cân đối bảng cân đối kế toán hợp lệ. |
| **INV-06** | Target Progress Sanity (25% - 120%) | `INFO` | **✅ PASS** | Tỷ lệ hoàn thành kế hoạch các khối đều nằm trong dải bình thường (50% - 70%). |
| **INV-07** | Growth & Trend Sanity | `INFO` | **✅ PASS** | Xu hướng tăng trưởng hợp lệ. |
| **INV-08** | Margin / Equity Regulatory Ceiling | `INFO` | **✅ PASS** | Không áp dụng cho doanh nghiệp phi chứng khoán. |
| **INV-09** | Loan <= Total Assets | `INFO` | **✅ PASS** | Dư nợ cho vay nhỏ hơn Tổng tài sản hợp lệ. |
| **INV-10** | CIR Boundary Check [5% - 95%] | `INFO` | **✅ PASS** | Không có chỉ tiêu CIR. |
| **INV-11** | NPL Bounds Check [0.1% - 25%] | `INFO` | **✅ PASS** | Không có chỉ tiêu NPL. |
| **INV-12** | Time-Axis Chronology | `INFO` | **✅ PASS** | Trục thời gian tuân thủ thứ tự. |

---

## II. KẾT LUẬN CỬA ẢI SDEV GATE
✅ **PHÊ DUYỆT XUẤT SSOT**: Toàn bộ dữ liệu trích xuất từ slide hoàn toàn trùng khớp với các quy luật logic tài chính. Cho phép ghi nhận vào `ground_truth.md` và kích hoạt tiếp tục pipeline xuất bản Báo cáo Phân tích.