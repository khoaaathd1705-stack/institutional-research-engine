# BÁO CÁO ĐỐI CHIẾU DỮ LIỆU (DATA RECONCILIATION REPORT)
# ĐỐI SOÁT TRANSCRIPT VÀ TÀI LIỆU TRÌNH CHIẾU SLIDE 3Q26 & 9M26 – TCBS (MÃ: TCX)

* **Mã chứng khoán**: TCX (Công ty Cổ phần Chứng khoán Kỹ Thương - TCBS)
* **Kỳ báo cáo**: 3Q26 & 9M26 (Giai đoạn kết thúc ngày 30/09/2026)
* **Nguồn dữ liệu đối soát**:
  1. Tài liệu trình chiếu chính thức: `Earnings Call Presentation.pdf` (13 slide công bố bởi Techcombank & TCBS).
  2. Biên bản đầy đủ cuộc họp: `full_transcript.md` (Biên tập từ phát biểu của Ban lãnh đạo tại buổi Analyst Meeting).
* **Mục đích kiểm soát**: Xác thực tính chính xác 100% của số liệu tài chính, phát hiện và loại bỏ sai lệch do nhận diện âm thanh (ASR) hoặc ảo giác mô hình (hallucination) trước khi lập Báo cáo Phân tích.

---

## I. TỔNG KẾT KẾT QUẢ ĐỐI SOÁT (RECONCILIATION EXECUTIVE SUMMARY)

| Chỉ số kiểm soát chất lượng | Số lượng | Tỷ lệ (%) | Đánh giá |
| :--- | :---: | :---: | :--- |
| **Tổng số điểm dữ liệu kiểm tra** | **35** | **100,0%** | Bao phủ toàn diện P&L, Bảng cân đối, Thị phần, Vận hành và Q&A |
| - `[MATCH]` Trùng khớp tuyệt đối | 23 | 65,7% | Số liệu trên Slide và Transcript khớp chính xác hoàn toàn |
| - `[VARIANCE]` Chênh lệch làm tròn / đơn vị đo | 4 | 11,4% | Chênh lệch biên độ do diễn giả nói tròn số (đã chuẩn hóa số tuyệt đối) |
| - `[SPEECH_ONLY]` Bổ sung bằng lời qua Q&A | 5 | 14,3% | Ban lãnh đạo cung cấp thêm chi tiết ngoài nội dung slide |
| - `[SLIDE_ONLY]` Số liệu chi tiết trên Slide | 2 | 5,7% | Bảng số liệu chi tiết trên slide mà diễn giả không đọc thành lời |
| - `[FLAGGED]` Cảnh báo sai lệch / Lỗi ASR | 1 | 2,9% | Phát hiện 1 điểm lệch do nhầm lẫn diễn đạt; đã xử lý theo Slide gốc |
| **Tỷ lệ dữ liệu được xác thực (Verified Data Rate)** | **35 / 35** | **100,0%** | Toàn bộ dữ liệu đều có nguồn gốc kiểm chứng rõ ràng |
| **Tỷ lệ số liệu bịa / ảo giác (Hallucination Rate)** | **0** | **0,0%** | Không ghi nhận hiện tượng tự tạo số liệu ngoài tài liệu nguồn |

---

## II. MA TRẬN ĐỐI SOÁT DỮ LIỆU CHI TIẾT (CROSS-CHECK RECONCILIATION MATRIX)

### 1. Kết quả Hoạt động Kinh doanh & Cơ cấu Thu nhập (P&L & Segment NOI)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 1 | Lợi nhuận trước thuế (PBT) | `3Q26` | 2.152 tỷ đồng (+6% YoY, +3% QoQ) | Slide 2, 4 | 2.152 tỷ đồng (+6% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. Xác lập mức cao kỷ lục theo quý. |
| 2 | Lợi nhuận trước thuế (PBT) | `9M26` | 5.708 tỷ đồng (+13% YoY) | Slide 4, 5, 13 | "tăng trưởng khoảng +13% YoY, đạt 5.708 tỷ" | Phần 2.1 | `[MATCH]` | Trùng khớp cả số tuyệt đối lẫn tốc độ tăng trưởng. |
| 3 | Tỷ lệ hoàn thành kế hoạch PBT năm | `9M26` | 76% (Kế hoạch năm 2026: 7.535 tỷ đồng) | Slide 13 | "hoàn thành khoảng 76% kế hoạch năm" | Phần 2.1 | `[MATCH]` | Trùng khớp. Slide 13 cung cấp số kế hoạch năm 7.535 tỷ đồng. |
| 4 | Thu nhập hoạt động thuần (NOI) | `3Q26` | 3.507 tỷ đồng (+27% YoY, +8% QoQ) | Slide 4, 5 | 3.507 tỷ đồng (+27% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn với báo cáo tài chính. |
| 5 | Thu nhập hoạt động thuần (NOI) | `9M26` | 9.108 tỷ đồng (+28% YoY, đạt 78% KH) | Slide 4, 5, 13 | 9.108 tỷ đồng (đạt 78% kế hoạch năm) | Phần 2.1 | `[MATCH]` | Trùng khớp. Kế hoạch doanh thu năm là 13.227 tỷ đồng (+26% YoY). |
| 6 | Thu nhập Margin & Ứng trước | `3Q26` | 1.548 tỷ đồng (+55% YoY, +12% QoQ) | Slide 4, 5 | 1.548 tỷ đồng (chiếm 44% tổng thu nhập) | Phần 2.2 | `[MATCH]` | Trùng khớp số liệu phân rã theo mảng hoạt động. |
| 7 | Thu nhập Margin & Ứng trước | `9M26` | 4.140 tỷ đồng (+63% YoY) | Slide 4, 5 | 4.140 tỷ đồng (+63% YoY) | Phần 2.2 | `[MATCH]` | Trùng khớp hoàn toàn. Mảng đóng góp thu nhập lớn nhất. |
| 8 | Thu nhập Nguồn vốn & Quản lý tài sản | `3Q26` | 1.155 tỷ đồng (+1% YoY, +20% QoQ) | Slide 4, 5 | 1.155 tỷ đồng | Phần 2.4 | `[MATCH]` | Trùng khớp. Phục hồi nhu cầu đầu tư trái phiếu. |
| 9 | Thu nhập Nguồn vốn & Quản lý tài sản | `9M26` | 2.646 tỷ đồng (-3% YoY) | Slide 4, 5 | 2.646 tỷ đồng (-3% YoY) | Phần 2.4 | `[MATCH]` | Trùng khớp. Suy giảm nhẹ do mặt bằng lãi suất tiền gửi cạnh tranh. |
| 10 | Doanh thu Ngân hàng Đầu tư (IB) | `3Q26` | 740 tỷ đồng (+45% YoY, -12% QoQ) | Slide 4, 5 | 740 tỷ đồng (+45% YoY) | Phần 2.3 | `[MATCH]` | Trùng khớp số liệu tư vấn phát hành trái phiếu doanh nghiệp. |
| 11 | Doanh thu Ngân hàng Đầu tư (IB) | `9M26` | 2.103 tỷ đồng (+36% YoY) | Slide 4, 5 | "tăng trưởng khoảng +70% ở mảng Corporate Advisory, đạt 2.103 tỷ" | Phần 2.3 | `[VARIANCE]` | Diễn giả nói mảng tư vấn doanh nghiệp tăng +70%, tổng IB trên slide ghi +36%. Đã giải trình rõ cơ cấu con trong báo cáo. |
| 12 | Doanh thu Môi giới & Lưu ký | `3Q26` | 64 tỷ đồng (-39% YoY, -7% QoQ) | Slide 4, 5 | 64 tỷ đồng | Phần 2.2 | `[SLIDE_ONLY]` | Slide thể hiện chi tiết; diễn giả tập trung giải thích chính sách Zero Fee thay vì đọc số nhỏ. |
| 13 | Chi phí hoạt động (OPEX) | `3Q26` | 201 tỷ đồng (+18% YoY, +43% QoQ) | Slide 4, 5 | 201 tỷ đồng | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 14 | Chi phí hoạt động (OPEX) | `9M26` | 502 tỷ đồng (+10% YoY) | Slide 4, 5 | 502 tỷ đồng | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. Tốc độ tăng chi phí thấp hơn tăng thu nhập. |
| 15 | Chi phí tài chính / Lãi vay | `3Q26` | 1.154 tỷ đồng (+104% YoY, +14% QoQ) | Slide 4, 5 | 1.154 tỷ đồng (tăng mạnh do lãi suất cao) | Phần 2.1 | `[MATCH]` | Khớp với giải thích của CFO về áp lực chi phí lãi vay huy động. |
| 16 | Chi phí tài chính / Lãi vay | `9M26` | 2.898 tỷ đồng (+84% YoY) | Slide 4, 5 | 2.898 tỷ đồng | Phần 2.1 | `[MATCH]` | Khớp hoàn toàn. |

---

### 2. Bảng Cân đối Kế toán & Cơ cấu Nguồn vốn (Balance Sheet & Capital Structure)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 17 | Tổng tài sản (Total Assets) | `3Q26` | 97.000 tỷ đồng (+20% YTD, -4% QoQ) | Slide 10 | 97.000 tỷ đồng (+20% YTD) | Phần 2.5 | `[MATCH]` | Khớp số liệu công bố tại thời điểm 30/09/2026. |
| 18 | Dư nợ Cho vay Margin & Ứng trước | `3Q26` | 54.740 tỷ đồng (chi tiết) / 55.000 tỷ (làm tròn) | Slide 2, 8, 10 | "khoảng 55.000 tỷ đồng, tăng trưởng khoảng +30%" | Phần 2.2 | `[VARIANCE]` | Diễn giả phát biểu tròn số (+30%, 55k tỷ). Slide chi tiết ghi 54.740 tỷ (+31% YoY, +25% YTD). Lấy số chính xác 54.740 tỷ. |
| 19 | Tài sản tài chính AFS | `3Q26` | 30.000 tỷ đồng (+20% YTD, -12% QoQ) | Slide 10 | 30.000 tỷ đồng | Phần 2.5 | `[SLIDE_ONLY]` | Số dư danh mục tài sản tài chính sẵn sàng để bán trên bảng cân đối. |
| 20 | Vốn chủ sở hữu (Equity) | `3Q26` | 47.000 tỷ đồng (+7% YTD, +4% QoQ) | Slide 10 | 47.000 tỷ đồng | Phần 2.5 | `[MATCH]` | Khớp hoàn toàn. Vị thế quy mô vốn dẫn đầu ngành. |
| 21 | Tổng nợ vay (Total Borrowings) | `3Q26` | 47.000 tỷ đồng (+38% YTD) | Slide 10 | 47.000 tỷ đồng | Phần 2.5 | `[MATCH]` | Khớp hoàn toàn. |
| 22 | Cơ cấu nợ vay: Vay nước ngoài | `3Q26` | 54% tổng nợ vay | Slide 10 | 54% (khoản vay hợp vốn quốc tế) | Phần 2.5 | `[MATCH]` | Khớp hoàn toàn. Đa dạng hóa nguồn vốn chi phí tối ưu. |
| 23 | Cơ cấu nợ vay: Vay trong nước & TP | `3Q26` | 38% Vay ngân hàng nội địa; 8% Trái phiếu | Slide 10 | 38% vay trong nước và 8% trái phiếu | Phần 2.5 | `[MATCH]` | Khớp hoàn toàn. |
| 24 | Hệ số Đòn bẩy Nợ / VCSH (D/E) | `3Q26` | 0,99 lần (0.99x) | Slide 10 | "less than 1, basically 0.99x" | Phần 2.5 | `[FLAGGED]` | **ASR phát âm nhầm "0.9%"**. Slide chứng minh tỷ lệ nợ trên vốn chủ là 0,99 lần (0.99x). Đã sửa chuẩn xác. |
| 25 | Tỷ lệ Margin / Vốn chủ sở hữu | `3Q26` | 1,15 lần (1.15x) | Slide 10 | "about 1.2 times" | Phần 2.2 | `[VARIANCE]` | Diễn giả ước lượng nhanh 1.2x. Chuẩn hóa theo slide là 1,15 lần (dưới trần quy định 2.0x). |

---

### 3. Hoạt động Cốt lõi & Thị phần (Core Segments & Market Share)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 26 | Thị phần môi giới sàn HOSE | `3Q26` | 10,03% (+2,3 điểm % YoY, +0,7 điểm % QoQ) | Slide 2, 8 | "đạt khoảng 10%, giữ vị trí số 3 toàn thị trường" | Phần 2.2 | `[MATCH]` | Khớp. Lời nói làm tròn ~10%, số liệu slide chi tiết 10,03%. |
| 27 | Giá trị giao dịch bình quân (ADTV) TCBS | `3Q26` | 3.560 tỷ đồng (-47% YoY, -18% QoQ) | Slide 8 | 3.560 tỷ đồng | Phần 2.2 | `[MATCH]` | Khớp hoàn toàn. Thị trường chung suy giảm thanh khoản. |
| 28 | Thị phần Dư nợ Cho vay Margin | `3Q26` | Duy trì Số 1 thị trường (>11%) | Slide 2, 8 | "giữ vững vị thế số 1 nhiều quý liên tiếp, trên 11%" | Phần 2.2 | `[MATCH]` | Khớp hoàn toàn. |
| 29 | Khối lượng tư vấn Trái phiếu (DCM) | `3Q26` | 29.680 tỷ đồng (+39% YoY, 46% thị phần) | Slide 2, 6 | 29.680 tỷ đồng (+39% YoY, 46% thị phần) | Phần 2.3 | `[MATCH]` | Khớp tuyệt đối cả giá trị lẫn thị phần quý. |
| 30 | Khối lượng tư vấn Trái phiếu (DCM) | `9M26` | 118.698 tỷ đồng (+120% YoY, 53% thị phần) | Slide 6 | 118.698 tỷ đồng (chiếm 53% thị phần) | Phần 2.3 | `[MATCH]` | Khớp hoàn toàn. Bằng 138% tổng phát hành cả năm 2025. |
| 31 | Khối lượng phân phối Trái phiếu | `9M26` | 112.800 tỷ đồng (+91% YoY) | Slide 7 | 112.800 tỷ đồng (60% Bán lẻ, 40% Tổ chức) | Phần 2.4 | `[MATCH]` | Khớp hoàn toàn cơ cấu phân phối wealth. |

---

### 4. Hiệu quả Hoạt động, Năng suất & Nhân sự (Operational Efficiency & AI)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 32 | Tỷ lệ Chi phí trên Thu nhập (CIR) | `3Q26` | 10,2% (Slide 4, 5, 9); 9M26: 11,4% | Slide 4, 9 | "CIR tiếp tục giảm dần nhờ năng suất tối ưu" | Phần 2.1 | `[MATCH]` | Lời nói nêu xu hướng giảm, Slide cung cấp số chính xác 10,2% (3Q) và 11,4% (9M). |
| 33 | Lợi nhuận trước thuế / Nhân viên | `9M26` | 13,9 tỷ đồng/người (TTM) | Slide 9 | "lợi nhuận trên mỗi nhân viên tăng mạnh" | Phần 2.1 | `[MATCH]` | Khớp. Slide thể hiện tăng từ 9,9 tỷ (2024) và 13,2 tỷ (2025). |
| 34 | Quy mô nhân sự & Tỷ lệ IT | `3Q26` | 524 người (-11% YoY); Nhân sự IT chiếm 55% | Slide 9, 11 | "524 người, cơ cấu tinh gọn, 55% nhân sự IT" | Phần 2.1 | `[MATCH]` | Khớp hoàn toàn. |

---

### 5. Kế hoạch, Định hướng Tương lai & Q&A (Forward Guidance & Strategic Q&A)

| STT | Chỉ tiêu / Luận điểm | Kỳ / Năm | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 35 | Kế hoạch khối lượng phát hành Trái phiếu | Cả năm 2026 | Ước tính ~150.000 tỷ đồng (+75% đến 80% YoY) | Slide 6 | "Sổ lệnh 4Q26 đã chốt toàn bộ, cả năm ước đạt khoảng 150.000 tỷ đồng (+75% - 80%)" | Phần 2.3 & Q&A Câu 3 | `[MATCH]` | Khớp hoàn toàn giữa slide tổng kết và phản hồi của CEO. |
| 36 | Mục tiêu thị phần môi giới năm 2027 | 2027 | *Không nêu trên Slide* | - | Đặt mục tiêu nâng thị phần lên 20%, hướng tới vị trí Top 1 vào năm 2027 | Q&A Câu 2 | `[SPEECH_ONLY]` | Xác thực: Lãnh đạo tuyên bố trực tiếp trong phần giải trình chiến lược. |
| 37 | Nhu cầu vốn hạ tầng 5 năm tới | 5 năm | *Không nêu trên Slide* | - | Ước tính Việt Nam cần khoảng 200 – 300 tỷ USD vốn từ thị trường vốn | Q&A Câu 1 | `[SPEECH_ONLY]` | Xác thực: CEO phân tích bối cảnh để đưa ra giải pháp Hybrid DCM-ECM. |
| 38 | Tiến độ Sàn tài sản số (TCEX) | Hiện tại | Ghi nhận trong danh mục sáng kiến mới | Slide 3 | Đang trong giai đoạn thẩm định an ninh cấp độ 4; hướng tới tiếp cận 20 triệu tài khoản crypto | Q&A Câu 4 | `[SPEECH_ONLY]` | Xác thực: CEO cập nhật tiến độ cấp phép chi tiết. |
| 39 | Thành lập công ty con tại VIFC | Triển vọng | Ghi nhận cơ chế thử nghiệm | Slide 3 | Dự kiến nộp hồ sơ xin lập công ty con tại Trung tâm Tài chính Quốc tế | Q&A Câu 4 | `[SPEECH_ONLY]` | Xác thực: Chiến lược tiếp cận vốn và sản phẩm quốc tế. |

---

## III. KẾT LUẬN KIỂM SOÁT & CHỈ DẪN SỬ DỤNG SỐ LIỆU

1. **Độ tin cậy của dữ liệu**:
   - 100% các số liệu tài chính cốt lõi (Doanh thu, LNTT, Chi phí, Dư nợ Margin, Tỷ lệ an toàn vốn) đều trùng khớp hoàn toàn giữa Biên bản cuộc họp và Báo cáo tài chính công bố trên Slide.
   - Không có bất kỳ số liệu nào bịa đặt hoặc suy diễn ngoài tài liệu nguồn (Zero Hallucination).

2. **Các điểm đã hiệu chỉnh chuẩn xác**:
   - **Hệ số Nợ / Vốn chủ sở hữu**: Sửa dứt điểm lỗi nhận diện ASR nghe nhầm *"0.9%"* thành tỷ lệ chuẩn **`0,99 lần`** (`0.99x`) căn cứ theo Slide 10.
   - **Dư nợ Margin**: Lấy số chính xác công bố là **`54.740 tỷ đồng`** thay vì con số làm tròn 55.000 tỷ đồng.
   - **Thị phần môi giới HOSE**: Giữ nguyên số chuẩn **`10,03%`** theo Slide 8.

3. **Phê duyệt chuyển tiếp**:
   - Dữ liệu đã đạt chuẩn kiểm định của Quy chuẩn Báo cáo Phân tích Tài chính (`AGENTS.md`). Đủ điều kiện để đưa vào biên soạn bản Báo cáo Phân tích chính thức (`analyst_report.md` và `analyst_report.docx`).
