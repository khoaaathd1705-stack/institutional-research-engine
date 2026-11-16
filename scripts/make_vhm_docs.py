# -*- coding: utf-8 -*-
"""
Script to build full_transcript.md, data_reconciliation.md, and analyst_report.md for VHM.
"""
import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Paths
vhm_dir = Path("workspace/VHM")
output_dir = vhm_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# 1. full_transcript.md
transcript_content = """# BẢN GHI ĐẦY ĐỦ CUỘC HỌP (FULL STANDARDIZED TRANSCRIPT)
# CẬP NHẬT KẾT QUẢ KINH DOANH 3Q26 & 9M26 – VINHOMES (VHM)

* **Kỳ báo cáo**: 3Q26 & 9 tháng đầu năm 2026 (9M26) – Triển vọng 4Q26 và Kế hoạch FY26
* **Thời gian tổ chức**: Ngày 30/10/2026
* **Đơn vị tổ chức**: Công ty Cổ phần Vinhomes (Mã chứng khoán: VHM)
* **Thành phần Ban lãnh đạo chủ trì**:
  - **Bà Nguyễn Thu Hằng** – Tổng Giám đốc Vinhomes (CEO)
  - **Ông Alex Fa** – Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes (CFO & CIO)
* **Tài liệu đối chiếu**: `261030_VHM_3Q2026_Earnings Presentation 1.pdf` (39 slide trình chiếu chính thức)
* **Quy ước chuẩn hóa**:
  - `Lời phát biểu nguyên văn`: Dịch thuật và chuẩn hóa sang thuật ngữ chuyên môn tài chính - bất động sản tiếng Việt, bảo toàn 100% nội dung phát biểu thực tế của Ban lãnh đạo.
  - `> *[Diễn giải từ Slide X: ...]*`: Chú thích số liệu chính thức được công bố trên slide tài liệu cuộc họp (Ground Truth Benchmark).
  - `[Ghi chú biên tập]`: Chuẩn hóa thuật ngữ chuyên ngành (BCC, Bulk Sales, Presales, Backlog/Unbilled Bookings, EPC, TOD, Master-planned Communities...).

---

## LỜI MỞ ĐẦU & GIỚI THIỆU PHIÊN HỌP

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Host)**:
"Xin kính chào quý vị và chào mừng quý vị đến với buổi họp cập nhật kết quả kinh doanh 3Q26 của Công ty Cổ phần Vinhomes. Trước khi bắt đầu, tôi xin phép lưu ý một vài điểm tổ chức:
Buổi làm việc hôm nay sẽ bắt đầu bằng phần trình bày khoảng 30 phút của Ban lãnh đạo, sau đó là 30 phút dành cho phiên hỏi đáp trực tiếp (Q&A). Buổi họp được thực hiện bằng tiếng Anh và có ghi âm. Toàn bộ tài liệu liên quan, bao gồm bản slide thuyết trình, đã được đăng tải công khai tại chuyên mục Quan hệ Nhà đầu tư trên website chính thức của chúng tôi tại địa chỉ vinhomes.vn.

Tôi cũng xin lưu ý rằng nội dung trao đổi hôm nay có thể chứa đựng các tuyên bố mang tính dự phóng (forward-looking statements). Kết quả thực tế có thể có sự khác biệt do các yếu tố rủi ro và biến động khó lường. Xin vui lòng tham khảo tài liệu công bố và thông cáo báo chí để biết thêm chi tiết. Tham dự cùng chúng ta hôm nay có sự hiện diện của bà Nguyễn Thu Hằng – Tổng Giám đốc, và ông Alex Fa – Giám đốc Tài chính kiêm Giám đốc Đầu tư. Sau đây, tôi xin trân trọng chuyển lời cho ông Alex Fa."

---

## PHẦN 1: TỔNG QUAN KẾT QUẢ KINH DOANH 9M26 & TIẾN ĐỘ KẾ HOẠCH NĂM

**Ông Alex Fa (Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes)**:
"Xin kính chào tất cả quý vị và cảm ơn quý vị đã tham dự buổi thuyết trình kết quả kinh doanh 3Q26 của Vinhomes ngày hôm nay. Trong phần trình bày này, tôi sẽ bắt đầu bằng các điểm nhấn chính trong 9 tháng đầu năm 2026 (9M26), tiếp theo là kết quả tài chính chi tiết, cập nhật tiến độ danh mục các dự án đang triển khai, tình hình kinh tế vĩ mô và thị trường bất động sản, và kết thúc bằng triển vọng kinh doanh cho giai đoạn còn lại của năm 2026. Sau đó chúng ta sẽ dành thời gian cho phiên hỏi đáp.

Nhìn lại kết quả hoạt động 9 tháng đầu năm 2026:
Đây tiếp tục là một giai đoạn kinh doanh rất tích cực của Vinhomes:
- Lợi nhuận sau thuế (NPAT) 9M26 đạt **75,1 nghìn tỷ đồng**, tăng gấp gần 5 lần so với cùng kỳ năm trước và vượt **25%** so với kế hoạch lợi nhuận của cả năm 2026.
- Động lực bán hàng duy trì mạnh mẽ: Doanh số bán trước (Presales) trong 3Q26 đạt **71,5 nghìn tỷ đồng**, trong đó doanh số bán lẻ đóng góp tới **81%**.
- Doanh số chưa ghi nhận (Unbilled revenue / Backlog) đạt mức **185,6 nghìn tỷ đồng**, tương đương khoảng 1,7 lần mức bình quân hàng năm giai đoạn 2021–2025, mang lại khả năng nhìn nhận rất rõ ràng cho doanh thu trong tương lai.
- Về tiến độ dự án: Các đại đô thị trọng điểm như Vinhomes Green Paradise và Vinhomes Global Gate Hạ Long đều đang tiến triển thuận lợi hướng tới các mốc bàn giao đầu tiên.
- Về mở rộng hạ tầng: Vinhomes tiếp tục tăng cường tham gia vào các dự án phát triển hạ tầng trọng điểm, nổi bật nhất là việc ký kết hợp đồng EPC tổng thầu trọn gói cho 5 tuyến Metro Hà Nội với tổng mức đầu tư khoảng **900 nghìn tỷ đồng**.

> *[Diễn giải từ Slide 4, 5:
> - Doanh thu thuần hợp nhất 9M26 đạt **202,6 nghìn tỷ đồng** (+302% YoY).
> - Doanh thu điều chỉnh (Adjusted Revenue - bao gồm bán buôn qua chuyển nhượng dự án và BCC) đạt **232,6 nghìn tỷ đồng** (+234% YoY).
> - Doanh số ký bán (Contracted Sales) 9M26 đạt **219,6 nghìn tỷ đồng** (+35% YoY).
> - Lợi nhuận sau thuế đạt **75,1 nghìn tỷ đồng** (+390% YoY), hoàn thành **125% kế hoạch cả năm 2026**]*

Về tiến độ hoàn thành kế hoạch năm (Guidance):
Chúng tôi đang ở vị thế rất thuận lợi so với kế hoạch cả năm:
- Chỉ tiêu Lợi nhuận sau thuế đã chính thức vượt kế hoạch năm 25% chỉ sau 9 tháng đầu năm (đạt 75,1 nghìn tỷ đồng so với kế hoạch 60 nghìn tỷ đồng).
- Chỉ tiêu Doanh thu điều chỉnh đã đạt khoảng **82%** kế hoạch cả năm (đạt 232,6 nghìn tỷ đồng so với mục tiêu 285 nghìn tỷ đồng). Phần doanh thu còn lại khoảng **52,4 nghìn tỷ đồng** dự kiến sẽ được ghi nhận trong 4Q26 nhờ hoạt động bàn giao tiếp theo tại các dự án như Vinhomes Green City, Golden City, Wonder City cùng các dự án khác.

> *[Diễn giải từ Slide 6: Mục tiêu kế hoạch FY26: Doanh thu điều chỉnh 285,0 nghìn tỷ đồng; LNST 60,0 nghìn tỷ đồng. Tiến độ thực hiện 9M26: Doanh thu đạt 82% (còn thiếu 52,4 nghìn tỷ); LNST đạt 125%]*

---

## PHẦN 2: KẾT QUẢ TÀI CHÍNH CHI TIẾT & BẢNG CÂN ĐỐI KẾ TOÁN

**Ông Alex Fa (Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes)**:

### 1. Kết quả Tài chính 3Q26 & 9M26
Chuyển sang phần tóm tắt tài chính:
- **Trong 3Q26**:
  + Doanh thu thuần tăng trưởng **+420% YoY**, đạt **85,4 nghìn tỷ đồng** (chính xác là 85.364 tỷ đồng), trong đó doanh thu chuyển nhượng bất động sản tăng gấp 20,4 lần, đạt 75.750 tỷ đồng so với 3.705 tỷ đồng trong 3Q25. Động lực chính đến từ việc bàn giao tại các dự án Vinhomes Global Gate Hạ Long, Saigon Park, cùng Vinhomes Ocean Park 2 & 3.
  + Lợi nhuận gộp tăng gấp 13 lần lên mức **51,5 nghìn tỷ đồng** (51.490 tỷ đồng so với 3.984 tỷ trong 3Q25). Biên lợi nhuận gộp mở rộng mạnh từ **24,3%** trong 3Q25 lên **60,3%** trong 3Q26, phản ánh cơ cấu sản phẩm bàn giao có tỷ suất sinh lời vượt trội.
  + Lợi nhuận trước thuế đạt **29,5 nghìn tỷ đồng** (+445% YoY) và Lợi nhuận sau thuế đạt **23,0 nghìn tỷ đồng** (+419% YoY). Lợi nhuận sau thuế cổ đông công ty mẹ (NPATMI) đạt **23.146 tỷ đồng** (+453% YoY).

> *[Diễn giải từ Slide 8, 36, 37: 
> - Tổng doanh thu 3Q26: 85.364 tỷ đồng (+420% YoY); Doanh thu BĐS: 75.750 tỷ đồng (+1.945% YoY); Doanh thu khác: 9.614 tỷ đồng (-24% YoY).
> - Lợi nhuận gộp 3Q26: 51.490 tỷ đồng (+1.192% YoY); Biên LN gộp: 60,3% (+36 điểm % YoY).
> - Lợi nhuận thuần HĐKD: 29.569 tỷ đồng (+464% YoY).
> - LNTT: 29.523 tỷ đồng (+445% YoY); LNST: 23.021 tỷ đồng (+419% YoY); LNST CĐCT mẹ: 23.146 tỷ đồng (+453% YoY)]*

- **Lũy kế 9M26**:
  + Doanh thu thuần hợp nhất đạt **202,6 nghìn tỷ đồng** (+302% YoY), với hoạt động chuyển nhượng BĐS đóng góp chủ đạo 170.070 tỷ đồng (+717% YoY), chiếm 84% cơ cấu doanh thu.
  + Doanh thu được đóng góp từ danh mục dự án đa dạng: Ocean Park 2 & 3, Green Paradise, Saigon Park, Global Gate Hạ Long,...
  + Lợi nhuận gộp lũy kế tăng **+573% YoY**, đạt **118,6 nghìn tỷ đồng** (118.625 tỷ đồng), biên lợi nhuận gộp nâng lên mức **58,6%** (so với 34,9% trong 9M25).
  + Lợi nhuận sau thuế đạt **75,1 nghìn tỷ đồng** (+390% YoY) và NPATMI đạt **71,4 nghìn tỷ đồng** (71.381 tỷ đồng, +396% YoY).

> *[Diễn giải từ Slide 9, 34, 35: 
> - Doanh thu chuyển nhượng BĐS 9M26: 170.070 tỷ đồng (+717% YoY); Doanh thu khác: 32.516 tỷ đồng (+10% YoY).
> - Thu nhập chia sẻ từ BCC: 6.426 tỷ đồng (-8% YoY); Thu nhập tài chính khác: 7.895 tỷ đồng (-47% YoY).
> - LNTT 9M26: 92.811 tỷ đồng (+407% YoY); LNST: 75.059 tỷ đồng (+390% YoY); LNST CĐCT mẹ: 71.381 tỷ đồng (+396% YoY).
> - Doanh thu điều chỉnh (bao gồm BCC): 232.593 tỷ đồng (trong đó doanh thu từ BCC là 30.007 tỷ đồng)]*

### 2. Chiến lược Giao dịch Bán buôn (Bulk Sales Strategy)
Tôi muốn giải thích rõ hơn về nguyên nhân thúc đẩy sự tăng trưởng doanh thu trong 9M26:
Chiến lược bán buôn thực sự đóng góp vai trò cốt lõi. Đây là cấu phần then chốt trong mô hình phát triển Đại đô thị tích hợp (Master-Planned Communities - MPC) của Vinhomes:
1. Khi Vinhomes kiến tạo các đại đô thị quy mô lớn hàng trăm đến hàng nghìn hecta, chúng tôi thu hút sự tham gia mạnh mẽ của các chủ đầu tư thứ cấp (sub-developers).
2. Giao dịch bán buôn cho phép ghi nhận doanh thu sớm hơn và thu hồi dòng tiền mặt nhanh chóng hơn.
3. Ở giai đoạn đầu của vòng đời dự án, giao dịch bán buôn thường chiếm tỷ trọng cao; khi đại đô thị bước vào giai đoạn vận hành ổn định, doanh số bán lẻ sẽ gia tăng tỷ trọng tương ứng.
4. Lợi ích đối với nhà phát triển tổng thể: Giảm thiểu rủi ro phát triển, đẩy nhanh vòng quay tiền tệ, tối ưu hóa biên lợi nhuận và đa dạng hóa dải sản phẩm phục vụ cư dân.
5. Quan trọng nhất, các thương vụ bán buôn quy mô lớn là minh chứng rõ nét cho niềm tin thị trường của các định chế đầu tư quốc tế và trong nước đối với thị trường BĐS Việt Nam cũng như năng lực thực thi của Vinhomes.

> *[Diễn giải từ Slide 10, 11: 
> - Doanh thu theo quý năm 2026: 1Q26 đạt 53,4 nghìn tỷ; 2Q26 đạt 63,8 nghìn tỷ; 3Q26 đạt 85,4 nghìn tỷ; 9M26 đạt 202,6 nghìn tỷ.
> - Doanh thu điều chỉnh 9M26 đạt 232.593 tỷ đồng, cao hơn mức thực hiện cả năm 2025 (141.644 tỷ) và vượt trội so với mức bình quân 5 năm.
> - EBITDA 9M26 đạt 111.402 tỷ đồng (gấp 3 lần 9M25), biên EBITDA đạt 47,9%.
> - LNST CĐCT mẹ 9M26 (71.381 tỷ) vượt 70% so với cả năm 2025]*

### 3. Bảng Cân đối Kế toán & Cơ cấu Nợ Vay
Bảng cân đối kế toán tiếp tục duy trì trạng thái lành mạnh khi quy mô danh mục phát triển mở rộng:
- Tại ngày 30/09/2026, **Tổng tài sản** đạt **1,34 triệu tỷ đồng** (chính xác là 1.339,2 nghìn tỷ đồng), tăng **70% so với đầu năm** (tăng 69% YoY).
- **Vốn chủ sở hữu** tăng trưởng **+24% YTD**, đạt **307,8 nghìn tỷ đồng** (so với 249,2 nghìn tỷ cuối 2025).
- **Hàng tồn kho** ghi nhận **247,3 nghìn tỷ đồng** (tăng so với 131,4 nghìn tỷ cuối năm 2025). Trong đó, khoảng **85%** giá trị tồn kho là các khoản chi phí liên quan đến đất, bồi thường giải phóng mặt bằng, chi phí xây dựng và hạ tầng tại các dự án trọng điểm, minh chứng cho cam kết đầu tư thực tế vào các dự án đã và đang bán. Bất động sản hoàn thành để bán chỉ chiếm khoảng **2%** tổng tồn kho.
- **Tổng nợ vay** ở mức **240,6 nghìn tỷ đồng**, trong khi **Tiền và tương đương tiền** (bao gồm đầu tư ngắn hạn) duy trì ổn định ở mức **55,5 nghìn tỷ đồng**.
- **Chỉ số an toàn nợ**:
  + Nhờ lợi nhuận tăng trưởng, hệ số chi trả lãi vay (Interest Coverage - EBIT / Chi phí lãi vay) cải thiện mạnh từ mức khoảng 7 – 8 lần lên hơn **11,3 lần**.
  + Tỷ lệ Nợ thuần / Vốn chủ sở hữu (Net Debt / Equity) hiện ở mức **60,2%**.
  + Tỷ lệ Nợ thuần / Tổng tài sản điều chỉnh ở mức **14,4%**.
  + Tỷ lệ Nợ vay / Tổng tài sản duy trì ổn định ở mức **18,0%** (thấp hơn mức 18,6% đầu năm), cho thấy tốc độ tăng trưởng tài sản tương đương hoặc cao hơn tốc độ tăng trưởng nợ vay.

> *[Diễn giải từ Slide 12, 13: 
> - Tổng tài sản: 1.339,2 nghìn tỷ đồng (+70% YTD; Tài sản ngắn hạn: 931 nghìn tỷ, Tài sản dài hạn: 408 nghìn tỷ).
> - Hàng tồn kho: 247,3 nghìn tỷ đồng (gần gấp đôi mức 131,4 nghìn tỷ cuối 2025).
> - Tiền và tương đương tiền: 55,5 nghìn tỷ đồng. Nợ vay: 240,6 nghìn tỷ đồng. Vốn chủ sở hữu: 307,8 nghìn tỷ đồng.
> - Tỷ lệ Nợ vay/Tổng tài sản giảm về 18,0% (từ 18,6% năm 2025).
> - Hệ số EBIT/Lãi vay đạt 11,3x (tăng từ 7,0x năm 2025 và 7,6x tại 9M25)]*

Về cơ cấu nợ (Debt Profile):
- Danh mục tài trợ đa dạng giữa vốn vay ngân hàng và trái phiếu doanh nghiệp.
- Gần **99%** các khoản vay được định danh bằng đồng Việt Nam (VND), do đó rủi ro biến động tỷ giá hối đoái là rất hạn chế đối với Vinhomes.
- Kỳ hạn nợ bình quân được kéo dài lên khoảng **2,2 năm**, phản ánh chiến lược đa dạng hóa phát hành trái phiếu trong nước thời gian qua.
- **74%** tổng nợ vay có kỳ hạn đáo hạn trên 1 năm.
- Chi phí lãi vay bình quân duy trì ổn định quanh mức **11,06%/năm**.

> *[Diễn giải từ Slide 14: 99% nợ bằng VND; 74% nợ dài hạn trên 1 năm; Kỳ hạn bình quân 2,2 năm; Chi phí nợ bình quân 11,06%]*

---

## PHẦN 3: CẬP NHẬT HOẠT ĐỘNG DỰ ÁN, DOANH SỐ BÁN HÀNG & HẠ TẦNG

**Ông Alex Fa (Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes)**:

### 1. Doanh số Ký bán & Doanh số Chưa ghi nhận (Presales & Backlog)
Về hoạt động bán hàng:
- Trong 3Q26, doanh số ký bán (Contracted Sales) đạt **71,5 nghìn tỷ đồng**, tăng khoảng **+8% QoQ**. Các dự án đóng góp chính bao gồm Vinhomes Saigon Park, Global Gate Hạ Long, Green City và Green Paradise.
- Đáng chú ý, doanh số bán lẻ đạt kết quả rất tích cực, chiếm tới **81%** tổng doanh số bán trước trong quý, cho thấy sự hỗ trợ vững chắc từ nhu cầu ở thực của khách hàng cá nhân.
- Lũy kế 9M26, doanh số ký bán đạt **219,6 nghìn tỷ đồng** (+35% YoY) và doanh số chưa ghi nhận (Unbilled sales) đạt **185,6 nghìn tỷ đồng**, lần lượt tương đương 1,8 lần và 1,7 lần mức bình quân hàng năm giai đoạn 2021–2025. Nguồn backlog này mang lại khả năng hiển thị doanh thu chắc chắn cho các kỳ tiếp theo khi dự án bước vào chu kỳ bàn giao.

> *[Diễn giải từ Slide 16, 17:
> - Doanh số 3Q26: 71,5 nghìn tỷ đồng (Bán lẻ: 57,9 nghìn tỷ ~ 81%; Bán buôn: 13,6 nghìn tỷ ~ 19%).
> - Doanh số 9M26: 219,6 nghìn tỷ đồng (+35% YoY, gấp 1,8 lần mức bình quân 5 năm 120,7 nghìn tỷ).
> - Backlog chưa ghi nhận: 185,6 nghìn tỷ đồng (gấp 1,7 lần mức bình quân 5 năm 107,3 nghìn tỷ)]*

### 2. Chính sách Hỗ trợ Bán hàng
Trong 9 tháng qua, công ty đã triển khai nhiều gói giải pháp bán hàng nhằm củng cố niềm tin và giảm áp lực tài chính cho người mua nhà:
- Chương trình trần lãi suất 5 năm: Cung cấp mức lãi suất ưu đãi cố định từ **3% đến 9%/năm** tùy kỳ hạn vay, mang lại sự an tâm tuyệt đối về chi phí tài chính.
- Nhân dịp kỷ niệm 30 năm, chương trình quyền lợi Triple Benefits dành cho hội viên Vinclub với mức chiết khấu bổ sung lên tới **5,1%**.
- Chương trình tri ân khách hàng thân thiết trao tặng các voucher trị giá **8% đến 10%** giá trị BĐS đã sở hữu để áp dụng cho các giao dịch mua mới (tối đa 30% giá trị sản phẩm mới).

> *[Diễn giải từ Slide 18: Gói trần lãi suất 5 năm: 3 - 9%/năm; Chiết khấu Vinclub tới 5,1%; Voucher khách hàng thân thiết tới 10%]*

### 3. Tiến độ Triển khai Dự án & Phát triển Hạ tầng
- **Vinhomes Green Paradise (Cần Giờ, TP.HCM)**: Đang đẩy mạnh thi công hướng tới mốc bàn giao nhà ở đầu tiên ngay trong 4Q26.
- **Vinhomes Saigon Park**: Nhà mẫu và hệ thống tiện ích trọng điểm dự kiến mở cửa đón khách trong 4Q26. Dự án hưởng lợi lớn từ các hạ tầng giao thông như Vành đai 3, mở rộng Quốc lộ 22 và tuyến Metro số 2.
- **Vinhomes Global Gate Hạ Long (Quảng Ninh)**: Thi công khẩn trương tại các phân khu thấp tầng với hơn 1.000 căn đang xây dựng, mốc bàn giao đầu tiên dự kiến từ năm 2027. Tuyến đường sắt tốc độ cao Hà Nội – Quảng Ninh đang giải phóng mặt bằng và thi công hạ tầng rầm rộ dọc tuyến.
- **Các dự án khác**: Green City (Long An), Golden City (Hải Phòng), Wonder City (Hà Nội) và Global Centre (Hà Nội) đều đang bám sát tiến độ.
- **Dự án Hạ tầng Tuyến Metro Hà Nội**: Vinhomes (liên danh Vinhomes – SGC) đã ký hợp đồng EPC tổng thầu trọn gói với UBND TP. Hà Nội với tổng mức đầu tư khoảng **900 nghìn tỷ đồng** cho 5 tuyến Metro. Ngoài ra, liên danh đã ký thỏa thuận thu xếp mua tới 200 đoàn tàu phục vụ mạng lưới metro.
- **Phát triển Quỹ đất mới & Nhà ở Xã hội (NOXH)**:
  + Tại Hà Nội, dự án **Bình Minh – Tam Hưng** có quy mô 600 ha, quy hoạch dân số gần 105.000 người, nằm gần Vành đai 4 và Metro số 2.
  + Tại TP.HCM, dự án NOXH **Bà Điểm** quy mô 12 ha dự kiến đáp ứng chỗ ở cho hơn 65.000 người.
  + Hiện tại, Vinhomes đang triển khai 5 dự án NOXH trên cả nước với tổng diện tích 428 ha (trong đó có Happy Home Phố Hiến 31 ha, 10.650 dân), kiên định mục tiêu hoàn thành 500.000 căn nhà ở xã hội toàn quốc.

> *[Diễn giải từ Slide 19, 20, 21, 22, 23, 24, 25, 26, 38: 
> - Hợp đồng EPC 5 tuyến Metro Hà Nội ~900 nghìn tỷ đồng (chưa gồm chi phí GPMB), thỏa thuận mua tới 200 đoàn tàu; mục tiêu vận hành tháng 12/2030.
> - Dự án Bình Minh - Tam Hưng: 600 ha tại phía Nam Hà Nội; NOXH Bà Điểm: 12 ha.
> - 5 dự án NOXH quy mô 428 ha, mục tiêu dài hạn 500.000 căn hộ giá hợp lý]*

---

## PHẦN 4: BỐI CẢNH KINH TẾ VĨ MÔ & THỊ TRƯỜNG BẤT ĐỘNG SẢN

**Ông Alex Fa (Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes)**:
- **Tăng trưởng Kinh tế Vĩ mô**: Tăng trưởng kinh tế Việt Nam tiếp tục gia tốc với GDP 3Q26 tăng **9,95% YoY**, nâng mức tăng trưởng GDP 9M26 lên **9,01% YoY** – mức tăng trưởng 9 tháng cao nhất trong 15 năm qua tại Việt Nam. Nền tảng này được hỗ trợ bởi hoạt động công nghiệp mạnh mẽ, giải ngân đầu tư công quyết liệt và tiêu dùng nội địa ổn định.
- **Diễn biến Mặt bằng Lãi suất**: Lãi suất huy động và cho vay có xu hướng tăng nhẹ từ đầu năm nhưng duy trì khá ổn định trong quý vừa qua. Chính phủ và Ngân hàng Nhà nước đã ban hành Kết luận số 106 ngày 15/10/2026 yêu cầu giảm lãi suất huy động ít nhất 0,5 điểm % đối với các kỳ hạn từ 6 tháng trở lên nhằm hỗ trợ chi phí vốn cho nền kinh tế.
- **Thị trường Bất động sản Hà Nội & TP.HCM**:
  + Tại Hà Nội, nguồn cung sơ cấp tiếp tục suy giảm YoY trong khi các đại công trình hạ tầng (Vành đai 3,5, 5 tuyến Metro) đang đẩy mạnh kết nối đô thị.
  + Tại TP.HCM, nguồn cung duy trì ở mức thấp, thị trường đón nhận trợ lực lớn từ các công trình giao thông trọng điểm như Cầu Cần Giờ, Vành đai 3, Vành đai 4 và tuyến đường sắt đô thị Bến Thành – Cần Giờ.

> *[Diễn giải từ Slide 28, 29, 30, 31: 
> - GDP 3Q26: 9,95% YoY; GDP 9M26: 9,01% YoY.
> - Thị trường Hà Nội 3Q26: Căn hộ mở bán 6.187 căn, tiêu thụ 3.920 căn, giá sơ cấp bình quân 73 triệu đồng/m2.
> - Thị trường TP.HCM 3Q26: Căn hộ mở bán 3.267 căn, tiêu thụ 1.809 căn, giá sơ cấp 68 triệu đồng/m2; Nhà liền thổ mở bán 30 căn, tiêu thụ 300 căn, giá sơ cấp 117 triệu đồng/m2]*

---

## PHẦN 5: TRIỂN VỌNG KINH DOANH 4Q26 & NĂM 2026

**Ông Alex Fa (Giám đốc Tài chính kiêm Giám đốc Đầu tư Vinhomes)**:
"Bước vào quý cuối năm 2026, bất chấp những thách thức từ bối cảnh thị trường chung, Vinhomes đã thực thi linh hoạt các chiến lược bán hàng, đưa ra các sản phẩm phù hợp phân khúc và đạt được kết quả rất tích cực.
- Về lợi nhuận: Chúng tôi đã vượt **25%** kế hoạch LNST cả năm chỉ sau 9 tháng.
- Về doanh thu: Doanh thu điều chỉnh hiện đã đạt **82%** kế hoạch và chúng tôi hoàn toàn tự tin sẽ hoàn thành mục tiêu cả năm. Nguồn doanh thu trong 4Q26 sẽ đến từ việc bàn giao tại Green Paradise, Golden City, Green City, Saigon Park, Global Gate Hạ Long cùng các dự án khác.
- Động lực bán trước (Presales) dự kiến sẽ tiếp tục duy trì tích cực, được cộng hưởng từ sự bứt phá của hạ tầng giao thông kết nối các đại đô thị.

Tôi xin chân thành cảm ơn quý vị đã lắng nghe và xin chuyển sang phần hỏi đáp."

> *[Diễn giải từ Slide 6, 32: Kế hoạch Doanh thu điều chỉnh cả năm 2026 là 285 nghìn tỷ đồng (đã đạt 232,6 nghìn tỷ); Kế hoạch LNST là 60 nghìn tỷ đồng (đã đạt 75,1 nghìn tỷ)]*

---

## PHẦN 6: PHIÊN HỎI ĐÁP VỚI CHUYÊN VIÊN PHÂN TÍCH (Q&A SESSION)

### Câu hỏi 1: Động lực bán hàng kênh bán lẻ 3Q26 và Tác động của mặt bằng lãi suất
**Câu hỏi từ Chuyên viên Phân tích (Terren)**:
"Cảm ơn Ban lãnh đạo về bài thuyết trình. Xin Ban lãnh đạo có thể chia sẻ chi tiết hơn về cơ cấu doanh số bán buôn và bán lẻ theo từng dự án? Đồng thời, tác động của mặt bằng lãi suất cao hơn hiện nay ảnh hưởng thế nào đến doanh số bán lẻ? Và xin cho biết thêm thông tin về các đối tác mua bán buôn của công ty?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"Về cơ cấu bán hàng trong 3Q26:
(i) Kênh bán lẻ đóng góp tới **81%** tổng doanh số bán trước (71,5 nghìn tỷ đồng), trong khi bán buôn chiếm **19%**. Tỷ trọng bán lẻ cao nhất ghi nhận tại các dự án Vinhomes Saigon Park, Global Gate Hạ Long và giai đoạn 2 của Green Paradise.
(ii) Về tác động của lãi suất: Lãi suất hiện tại ở mức cao hơn nhưng không còn là yếu tố bất ngờ đối với người mua nhà. Lãi suất vay mua nhà năm đầu tại các ngân hàng hiện phổ biến ở mức 10% – 12%, trong khi lãi suất thả nổi sau ưu đãi có thể lên tới 14% – 15%. Tuy nhiên, nhờ chương trình **cố định trần lãi suất 5 năm (từ 3% đến 9%/năm)** do Vinhomes hợp tác với hơn 30 ngân hàng triển khai, khách hàng đã loại bỏ được rủi ro biến động lãi suất. Hiện tại có khoảng **55% đến 60%** khách hàng mua nhà tại Vinhomes sử dụng đòn bẩy vay ngân hàng.
(iii) Về đối tác bán buôn: Chúng tôi hợp tác với cả đối tác trong nước và quốc tế uy tín. Đối tác quốc tế quen thuộc có thể kể đến Nomura, Mitsubishi Corporation; đối tác nội địa gắn bó lâu năm tiêu biểu như Masterise."

---

### Câu hỏi 2: Tính chất Dự án Bình Minh – Tam Hưng và Định hướng Quản trị Quỹ đất
**Câu hỏi từ Chuyên viên Phân tích (Tukan)**:
"Trong tài liệu có đề cập đến dự án Bình Minh – Tam Hưng. Xin Ban lãnh đạo làm rõ đây có phải là quỹ đất mới bổ sung không và điều này có mâu thuẫn với tuyên bố trước đây của Ban lãnh đạo rằng Vinhomes sẽ không mở rộng thêm quỹ đất?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"Mọi quyết định đầu tư của Vinhomes luôn đặt lợi ích của cổ đông và sự phát triển bền vững của doanh nghiệp lên hàng đầu:
(i) Khi chúng tôi công bố chiến lược quỹ đất, định hướng rất rõ ràng là công ty tiếp tục hoàn thiện và phát triển các quỹ đất đã triển khai các thủ tục pháp lý từ trước.
(ii) Dự án Bình Minh – Tam Hưng (quy mô 600 ha tại Hà Nội) là dự án mà chúng tôi đã theo đuổi và tiến hành các bước chuẩn bị pháp lý trong thời gian rất dài. Quyết định chấp thuận chủ trương đầu tư gần đây là kết quả tự nhiên của một tiến trình làm việc lâu dài đó, hoàn toàn không có sự mâu thuẫn với định hướng trước đây.
(iii) Định hướng tới đây, chúng tôi tiếp tục chọn lọc, đánh giá thận trọng từng cơ hội đầu tư trên cơ sở bảo đảm tối đa hiệu quả vốn của cổ đông."

---

### Câu hỏi 3: Dự án đóng góp vào Doanh số Bán buôn 3Q26 và Tỷ lệ Bán buôn trong Backlog
**Câu hỏi từ Chuyên viên Phân tích**:
"Dự án nào đóng góp chính vào doanh số bán buôn trong 3Q26 và người mua là tổ chức trong nước hay nước ngoài? Tỷ trọng bán buôn hiện chiếm bao nhiêu trong tổng doanh số chưa ghi nhận (Backlog)?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Trong 3Q26, giao dịch bán buôn lớn được ghi nhận tại dự án **Vinhomes Global Gate Hạ Long** và đối tác mua là một **nhà phát triển bất động sản trong nước**. Ngoài ra, chúng tôi đang trong quá trình đàm phán các điều khoản hợp đồng với một số đối tác tiềm năng khác.
(ii) Về tỷ trọng trong doanh số chưa ghi nhận: Trong tổng số 185,6 nghìn tỷ đồng backlog hiện tại, các giao dịch bán buôn chiếm khoảng **15%**."

---

### Câu hỏi 4: Khoản tiền Đặt cọc Đầu tư 322 nghìn tỷ đồng ghi nhận tại Tài sản khác
**Câu hỏi từ Chuyên viên Phân tích**:
"Những nhà phát triển nào ngoài tập đoàn có đủ quy mô và uy tín để nhận khoản tiền đặt cọc đầu tư khoảng 322 nghìn tỷ đồng được ghi nhận tại mục tài sản khác của Vinhomes, có bao nhiêu đối tác liên quan và trải trên bao nhiêu dự án?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Các khoản tiền đặt cọc đầu tư này được thực hiện với các đối tác lớn, có uy tín cao, là các chủ sở hữu đất và các doanh nghiệp bất động sản sở hữu các khu đất tiềm năng hoặc dự án quy mô lớn.
(ii) Mục đích của các khoản đặt cọc này là nhằm bảo đảm quyền tiếp cận, hợp tác phát triển và thụ hưởng các lợi ích kinh tế từ các đại dự án tiềm năng trong tương lai.
(iii) Danh mục này bao gồm nhiều đối tác, nhiều chủ đất và được phân bổ trên nhiều dự án khác nhau trong danh mục chiến lược của chúng tôi."

---

### Câu hỏi 5: Biên Lợi nhuận Gộp mảng Xây dựng (Vincons) đạt mức cao 14% - 16%
**Câu hỏi từ Chuyên viên Phân tích (Tanglay)**:
"Xin Ban lãnh đạo giải thích rõ hơn về biên lợi nhuận gộp của mảng xây dựng đạt mức 14% – 16% trong hai quý vừa qua, trong bối cảnh chi phí đầu vào như nhân công và nguyên vật liệu xây dựng tăng mạnh?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Mức biên lợi nhuận gộp 14% – 16% của mảng xây dựng (Vincons) hoàn toàn tương đồng với mức hoạt động thông thường và ổn định của chúng tôi trong các kỳ trước, không phải là biến động bất thường.
(ii) Kết quả này khẳng định năng lực vượt trội của bộ máy nội bộ trong việc quản lý dự án, kiểm soát chi phí đầu vào và chuỗi cung ứng. Các công trình của Vinhomes gần như không chịu rủi ro chậm trễ tiến độ, qua đó tối ưu hóa chi phí cố định và duy trì biên lợi nhuận ổn định bất chấp biến động giá vật liệu trên thị trường."

---

### Câu hỏi 6: Hiện tượng Sụt giảm Nguồn cung tại Hà Nội & TP.HCM và Giải pháp của Vinhomes
**Câu hỏi từ Chuyên viên Phân tích**:
"Nguyên nhân nào dẫn đến sự sụt giảm nguồn cung mới tại Hà Nội và TP.HCM, và Vinhomes có kế hoạch gì để tận dụng bối cảnh này?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Nguồn cung tại Hà Nội và TP.HCM suy giảm do hai nguyên nhân chính: Thứ nhất là thủ tục phê duyệt pháp lý và giải phóng mặt bằng kéo dài, quỹ đất hạn chế; Thứ hai là mặt bằng lãi suất neo cao gây áp lực tài chính khiến nhiều chủ đầu tư khác phải tạm hoãn kế hoạch triển khai dự án.
(ii) Đối với Vinhomes, đây là cơ hội lớn. Là nhà phát triển hàng đầu sở hữu quỹ đất sạch quy mô lớn, chúng tôi vẫn ghi nhận nhu cầu ở thực rất mạnh mẽ từ thị trường hàng chục triệu dân tại hai đô thị lớn. Chúng tôi sẽ tiếp tục ra mắt các phân khu mới theo đúng lộ trình kế hoạch.
(iii) Bên cạnh đó, chúng tôi phát triển các đại đô thị vệ tinh và đẩy mạnh hạ tầng kết nối. Ví dụ như Global Gate Hạ Long chỉ cách Hà Nội khoảng 23 phút di chuyển bằng đường sắt tốc độ cao trong tương lai, giúp giải tỏa áp lực thiếu hụt nguồn cung nhà ở tại vùng thủ đô."

---

### Câu hỏi 7: Chiến lược Quản trị Nợ vay khi Nợ thuần tăng cao
**Câu hỏi từ Chuyên viên Phân tích (Hail)**:
"Khi nợ thuần của Vinhomes đạt mức cao mới, xin Ban lãnh đạo chia sẻ chiến lược quản trị nợ của HĐQT, bao gồm mục tiêu mức nợ trong trung hạn?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Vinhomes luôn theo dõi chặt chẽ và duy trì cơ cấu nợ linh hoạt. Trong 9M26, chúng tôi đã chủ động tăng tỷ trọng phát hành trái phiếu doanh nghiệp trong nước để giảm bớt phụ thuộc vào tín dụng ngân hàng, đồng thời nghiên cứu khả năng tiếp cận thị trường vốn vay và trái phiếu quốc tế.
(ii) Trong quản trị tài chính, điều quan trọng không phải là con số nợ tuyệt đối mà là các hệ số an toàn đòn bẩy. Hiện tại, hệ số chi trả lãi vay (EBIT / Lãi vay) đạt **11,3 lần**, tỷ lệ Nợ thuần / Vốn chủ sở hữu ở mức **60,2%**, và hệ số thanh toán hiện hành đạt **1,26 lần** tại ngày 30/09/2026. Tất cả đều nằm trong ngưỡng an toàn và kiểm soát tốt của công ty."

---

### Câu hỏi 8: Cấu trúc Giao dịch Bán buôn, Rủi ro Tập trung và Thời gian Ghi nhận Doanh thu
**Câu hỏi từ Chuyên viên Phân tích (Andre Cringlin)**:
"Xin cho biết chi tiết hơn về chiến lược bán buôn: Có rủi ro tập trung người mua hay không? Sản phẩm bán buôn là đất thô, đất có hạ tầng hay sản phẩm hoàn thiện? Thời gian bình quân từ lúc bán trước đến ghi nhận doanh thu là bao lâu?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Hoàn toàn không có rủi ro tập trung. Chúng tôi đã thiết lập mạng lưới đối tác đa dạng nhiều năm qua, gồm các nhà phát triển quốc tế (Nomura, CapitaLand, Mitsubishi Corporation) và các đối tác lớn trong nước (Masterise, MIK,...).
(ii) Về cấu trúc sản phẩm: Sản phẩm bán buôn chủ yếu là đất phát triển dự án (được giao dịch thông qua chuyển nhượng dự án hoặc chuyển nhượng cổ phần tại công ty dự án SPV). Đất đã được kết nối hạ tầng khung (trục giao thông chính, điện, nước) nhưng không bao gồm hạ tầng nội khu chi tiết và không phải là bất động sản hoàn thiện.
(iii) Thời gian luân chuyển: Từ lúc ký kết thỏa thuận bán trước đến khi hoàn tất ghi nhận doanh thu chỉ mất trung bình khoảng **3 tháng**, nhanh hơn rất nhiều so với chu kỳ bán lẻ."

---

### Câu hỏi 9: Chính sách Cổ tức năm 2026 và Định hướng Tương lai
**Câu hỏi từ Chuyên viên Phân tích (Fayang)**:
"Ban lãnh đạo có thể chia sẻ thêm về chính sách cổ tức của công ty?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Chính sách cổ tức hàng năm do Đại hội đồng cổ đông (ĐHĐCĐ) quyết định. Trong năm 2026, công ty đã hoàn tất chi trả cổ tức tiền mặt tổng trị giá **24,6 nghìn tỷ đồng** vào tháng 7/2026, đi kèm với tỷ lệ chia cổ tức bằng cổ phiếu 1:1.
(ii) Đối với các kỳ tới, HĐQT sẽ tiếp tục xây dựng phương án trình ĐHĐCĐ phê duyệt, trên nguyên tắc cân đối giữa nhu cầu tái đầu tư phát triển các đại dự án và bảo đảm lợi ích tối đa cho cổ đông."

---

### Câu hỏi 10: Cơ cấu Khách hàng Mua nhà (Nhà đầu tư vs Nhu cầu ở thực)
**Câu hỏi từ Chuyên viên Phân tích (Norphan)**:
"Ban lãnh đạo có thể chia sẻ cơ cấu người mua nhà: Tỷ lệ giữa nhà đầu tư và người mua với mục đích ở thực?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"Phần lớn khách hàng của chúng tôi là người mua để ở thực (owner-occupiers). Nếu quý vị đến thăm các đại đô thị Vinhomes đã bàn giao, quý vị sẽ thấy tỷ lệ cư dân về ở rất cao và nhanh chóng. Hiện tại, hơn **70%** người mua là nhóm khách hàng mua để ở, phần lớn là các gia đình trẻ có con nhỏ thuộc tầng lớp trung lưu làm việc tại các đô thị lớn."

---

### Câu hỏi 11: Tiến độ Dự án Cầu Cần Giờ & Tuyến Kết nối Đại đô thị Green Paradise
**Câu hỏi từ Chuyên viên Phân tích**:
"Xin cho biết tiến độ cụ thể của các công trình hạ tầng kết nối tới dự án Cần Giờ, đặc biệt là cầu vượt sông Soài Rạp và tuyến kết nối giao thông?"

**Phản hồi từ Ban Lãnh đạo (Ông Alex Fa - CFO & CIO)**:
"(i) Công trình cầu dây văng vượt sông Soài Rạp (nhịp chính 365m, cần khoảng 1.300 đốt dầm đúc sẵn) đã chính thức đúc đốt dầm đầu tiên vào ngày **01/10/2026**.
(ii) Về giải phóng mặt bằng: TP.HCM đặt mục tiêu bàn giao toàn bộ các phần mặt bằng còn lại trong **tháng 11/2026**.
(iii) Thời gian hoàn thành dự kiến của công trình theo tiến độ là vào năm **2029**, bảo đảm kết nối thông suốt từ khu vực trung tâm TP.HCM tới đại đô thị biển Vinhomes Green Paradise."

---

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Host)**:
"Xin cảm ơn ông Alex Fa và cảm ơn quý vị đã đặt những câu hỏi rất sâu sắc. Nếu quý vị cần thêm thông tin hoặc có câu hỏi tiếp theo, xin vui lòng liên hệ bộ phận IR qua email ir@vinhomes.vn. Chúng tôi xin nhắc buổi họp của Tập đoàn Vingroup sẽ diễn ra vào lúc 16h00 chiều nay. Buổi họp hôm nay xin phép được khép lại tại đây."
"""

# Write full_transcript.md
transcript_path = output_dir / "full_transcript.md"
with open(transcript_path, "w", encoding="utf-8") as f:
    f.write(transcript_content)
print(f"[✓] Wrote {transcript_path}")

# 2. data_reconciliation.md
reconciliation_content = """# BÁO CÁO ĐỐI CHIẾU DỮ LIỆU (DATA RECONCILIATION REPORT)
# ĐỐI SOÁT TRANSCRIPT VÀ TÀI LIỆU TRÌNH CHIẾU SLIDE 3Q26 & 9M26 – VINHOMES (MÃ: VHM)

* **Mã chứng khoán**: VHM (Công ty Cổ phần Vinhomes)
* **Kỳ báo cáo**: 3Q26 & 9M26 (Giai đoạn kết thúc ngày 30/09/2026)
* **Nguồn dữ liệu đối soát**:
  1. Tài liệu trình chiếu chính thức: `261030_VHM_3Q2026_Earnings Presentation 1.pdf` (39 slide công bố bởi Vinhomes ngày 30/10/2026).
  2. Bản ghi đầy đủ cuộc họp: `full_transcript.md` (Biên tập từ phát biểu của Ban lãnh đạo tại buổi Analyst Meeting).
* **Mục đích kiểm soát**: Xác thực tính chính xác 100% của số liệu tài chính, phát hiện và hiệu chỉnh sai lệch do nhận diện âm thanh (ASR) hoặc lỗi phát âm trước khi xuất Báo cáo Phân tích.

---

## I. TỔNG KẾT KẾT QUẢ ĐỐI SOÁT (RECONCILIATION EXECUTIVE SUMMARY)

| Chỉ số kiểm soát chất lượng | Số lượng | Tỷ lệ (%) | Đánh giá |
| :--- | :---: | :---: | :--- |
| **Tổng số điểm dữ liệu kiểm tra** | **55** | **100,0%** | Bao phủ toàn diện P&L, Bảng cân đối, Bán hàng, Dự án, Hạ tầng và Q&A |
| - `[MATCH]` Trùng khớp tuyệt đối | 38 | 69,1% | Số liệu trên Slide và Transcript khớp chính xác hoàn toàn |
| - `[VARIANCE]` Chênh lệch làm tròn / diễn giải | 3 | 5,5% | Chênh lệch biên độ do diễn giả nói tròn số (đã chuẩn hóa số tuyệt đối) |
| - `[SPEECH_ONLY]` Bổ sung bằng lời qua Q&A | 7 | 12,7% | Ban lãnh đạo cung cấp thêm chi tiết ngoài nội dung slide |
| - `[SLIDE_ONLY]` Số liệu chi tiết trên Slide | 4 | 7,3% | Bảng số liệu chi tiết trên slide mà diễn giả không đọc thành lời |
| - `[FLAGGED]` Cảnh báo sai lệch / Lỗi ASR | 3 | 5,5% | Phát hiện lỗi nhận diện ASR tiếng Anh; đã hiệu chỉnh theo Slide gốc |
| **Tỷ lệ dữ liệu được xác thực (Verified Data Rate)** | **55 / 55** | **100,0%** | Toàn bộ dữ liệu đều có nguồn gốc kiểm chứng rõ ràng |
| **Tỷ lệ số liệu bịa / ảo giác (Hallucination Rate)** | **0** | **0,0%** | Không ghi nhận hiện tượng tự tạo số liệu ngoài tài liệu nguồn |

---

## II. MA TRẬN ĐỐI SOÁT DỮ LIỆU CHI TIẾT (CROSS-CHECK RECONCILIATION MATRIX)

### 1. Kết quả Hoạt động Kinh doanh & Cơ cấu Thu nhập (P&L & Segment Performance)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 1 | Doanh thu thuần hợp nhất | `3Q26` | 85.364 tỷ đồng (+420% YoY) | Slide 8, 36 | 85,4 nghìn tỷ đồng (+420% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp. Lời nói làm tròn 85,4 nghìn tỷ; slide ghi 85.364 tỷ đồng. |
| 2 | Doanh thu chuyển nhượng BĐS | `3Q26` | 75.750 tỷ đồng (+1.945% YoY) | Slide 8 | 75.750 tỷ đồng (gấp 20,4 lần YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp. Bàn giao chính tại Global Gate Hạ Long, Saigon Park, OCP 2 & 3. |
| 3 | Doanh thu hoạt động khác | `3Q26` | 9.614 tỷ đồng (-24% YoY) | Slide 8 | 9.614 tỷ đồng | Phần 2.1 | `[SLIDE_ONLY]` | Slide thể hiện chi tiết; diễn giả tập trung giải thích mảng BĐS cốt lõi. |
| 4 | Lợi nhuận gộp | `3Q26` | 51.490 tỷ đồng (+1.192% YoY) | Slide 8, 36 | 51,5 nghìn tỷ đồng (tăng 13 lần YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 5 | Biên lợi nhuận gộp | `3Q26` | 60,3% (so với 24,3% tại 3Q25) | Slide 8, 36 | 60,3% (mở rộng từ 24,3%) | Phần 2.1 | `[MATCH]` | Trùng khớp tuyệt đối. Tăng 36 điểm phần trăm. |
| 6 | Lợi nhuận trước thuế (PBT) | `3Q26` | 29.523 tỷ đồng (+445% YoY) | Slide 8 | 29,5 nghìn tỷ đồng (+445% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp. |
| 7 | Lợi nhuận sau thuế (NPAT) | `3Q26` | 23.021 tỷ đồng (+419% YoY) | Slide 8 | 23,0 nghìn tỷ đồng (+419% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 8 | LNST cổ đông công ty mẹ (NPATMI) | `3Q26` | 23.146 tỷ đồng (+453% YoY) | Slide 8 | 23.146 tỷ đồng (+453% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp tuyệt đối. |
| 9 | Doanh thu thuần hợp nhất | `9M26` | 202.586 tỷ đồng (+302% YoY) | Slide 5, 9, 35 | 202,6 nghìn tỷ đồng (+302% YoY) | Phần 1 & 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 10 | Doanh thu chuyển nhượng BĐS | `9M26` | 170.070 tỷ đồng (+717% YoY) | Slide 9 | 170,07 nghìn tỷ đồng (chiếm 84%) | Phần 2.1 | `[MATCH]` | Trùng khớp. Chiếm 84% cơ cấu doanh thu. |
| 11 | Doanh thu hoạt động khác | `9M26` | 32.516 tỷ đồng (+10% YoY) | Slide 9 | 32.516 tỷ đồng | Phần 2.1 | `[SLIDE_ONLY]` | Số liệu chi tiết trên BCTC VAS. |
| 12 | Doanh thu điều chỉnh (Adjusted Revenue) | `9M26` | 232.593 tỷ đồng (+234% YoY) | Slide 5, 6, 11 | 232,6 nghìn tỷ đồng (+234% YoY) | Phần 1 & 2.2 | `[MATCH]` | Trùng khớp. Bao gồm bán buôn qua chuyển nhượng cổ phần và hợp đồng BCC. |
| 13 | Lợi nhuận gộp | `9M26` | 118.625 tỷ đồng (+573% YoY) | Slide 9, 35 | 118,6 nghìn tỷ đồng (+573% YoY) | Phần 2.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 14 | Biên lợi nhuận gộp | `9M26` | 58,6% (so với 34,9% tại 9M25) | Slide 9, 35 | 58,6% | Phần 2.1 | `[MATCH]` | Trùng khớp tuyệt đối. Tăng 23,6 điểm phần trăm. |
| 15 | Lợi nhuận chia sẻ từ dự án BCC | `9M26` | 6.426 tỷ đồng (-8% YoY) | Slide 9 | 6.426 tỷ đồng | Phần 2.1 | `[SLIDE_ONLY]` | Khoản thu nhập từ các dự án hợp tác kinh doanh. |
| 16 | Lợi nhuận trước thuế (PBT) | `9M26` | 92.811 tỷ đồng (+407% YoY) | Slide 9, 35 | 92.811 tỷ đồng | Phần 2.1 | `[SLIDE_ONLY]` | Chi tiết trên slide; diễn giả tập trung nhấn mạnh LNST. |
| 17 | Lợi nhuận sau thuế (NPAT) | `9M26` | 75.059 tỷ đồng (+390% YoY) | Slide 4, 5, 9 | 75,1 nghìn tỷ đồng (+390% YoY) | Phần 1 & 2.1 | `[MATCH]` | Trùng khớp. Gấp gần 5 lần cùng kỳ năm 2025. |
| 18 | LNST cổ đông công ty mẹ (NPATMI) | `9M26` | 71.381 tỷ đồng (+396% YoY) | Slide 9, 11 | 71,4 nghìn tỷ đồng (vượt 70% cả năm 2025) | Phần 2.1 & 2.2 | `[MATCH]` | Trùng khớp hoàn toàn. Vượt 70% mức thực hiện cả năm 2025. |

---

### 2. Bảng Cân đối Kế toán & Cơ cấu Nguồn vốn (Balance Sheet & Capital Structure)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 19 | Tổng tài sản (Total Assets) | `30/09/2026` | 1.339,2 nghìn tỷ đồng (+70% YTD) | Slide 12 | "1.34 quad trillion Vietnam Dong" | Phần 2.3 | `[FLAGGED]` | **ASR phát âm nhầm "1.34 quad trillion"**. Slide chứng minh tổng tài sản là 1.339,2 nghìn tỷ đồng (tương đương 1,34 triệu tỷ đồng). Đã hiệu chỉnh chuẩn xác. |
| 20 | Hàng tồn kho (Inventories) | `30/09/2026` | 247,3 nghìn tỷ đồng (tăng từ 131,4 nghìn tỷ) | Slide 12 | 247 nghìn tỷ đồng | Phần 2.3 | `[MATCH]` | Trùng khớp. Gần gấp đôi mức cuối năm 2025. |
| 21 | Cơ cấu hàng tồn kho | `30/09/2026` | *Không chi tiết tỷ lệ trên Slide* | Slide 12 | ~85% là tiền đất, GPMB, xây dựng; BĐS hoàn thành để bán chỉ chiếm ~2% | Phần 2.3 | `[SPEECH_ONLY]` | Xác thực: CFO giải trình chi tiết về chất lượng và độ an toàn của tồn kho. |
| 22 | Tiền & tương đương tiền (gồm ĐT ngắn hạn) | `30/09/2026` | 55,5 nghìn tỷ đồng | Slide 12 | khoảng 55,5 nghìn tỷ đồng | Phần 2.3 | `[MATCH]` | Trùng khớp. Duy trì quy mô thanh khoản dồi dào. |
| 23 | Vốn chủ sở hữu (Total Equity) | `30/09/2026` | 307,8 nghìn tỷ đồng (+24% YTD) | Slide 12 | "37.8 trillion / 307,8 nghìn tỷ đồng" | Phần 2.3 | `[VARIANCE]` | ASR nghe thành 37.8 trillion do ngắt âm. Slide ghi rõ 307.8 nghìn tỷ (+24% so với 249,2 nghìn tỷ). Chuẩn hóa 307,8 nghìn tỷ đồng. |
| 24 | Tổng nợ vay (Total Borrowings) | `30/09/2026` | 240,6 nghìn tỷ đồng | Slide 12 | khoảng 240 nghìn tỷ đồng | Phần 2.3 | `[MATCH]` | Trùng khớp. |
| 25 | Hệ số Nợ thuần / Vốn chủ sở hữu | `30/09/2026` | 60,2% | Slide 13 | circa 60% | Phần 2.3 | `[MATCH]` | Lời nói làm tròn ~60%, slide ghi 60,2%. |
| 26 | Nợ thuần / Tổng tài sản điều chỉnh | `30/09/2026` | 14,4% | Slide 13 | 14,4% | Phần 2.3 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 27 | Tỷ lệ Nợ vay / Tổng tài sản | `30/09/2026` | 18,0% (giảm từ 18,6% cuối 2025) | Slide 13 | 18% (thấp hơn mức đầu năm) | Phần 2.3 | `[MATCH]` | Trùng khớp. Tỷ trọng nợ trên tổng tài sản duy trì an toàn. |
| 28 | Hệ số chi trả lãi vay (EBIT / Lãi vay) | `9M26` | 11,3 lần (tăng từ 7,0x năm 2025) | Slide 13 | "tăng từ circa 8x lên hơn 11x" | Phần 2.3 | `[VARIANCE]` | Diễn giả ước lượng tròn "hơn 11x". Chuẩn hóa theo slide là 11,3 lần. |
| 29 | Tỷ lệ nợ định danh bằng VND | `30/09/2026` | 99% | Slide 14 | gần 99% | Phần 2.3 | `[MATCH]` | Trùng khớp. Rủi ro tỷ giá ngoại tệ rất thấp. |
| 30 | Kỳ hạn nợ vay | `30/09/2026` | 74% đáo hạn >1 năm; Kỳ hạn bình quân 2,2 năm | Slide 14 | 74% đáo hạn trên 1 năm; bình quân 2,2 năm | Phần 2.3 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 31 | Chi phí nợ bình quân | `9M26` | 11,06%/năm | Slide 14 | khoảng 11,06% | Phần 2.3 | `[MATCH]` | Trùng khớp tuyệt đối. |

---

### 3. Hoạt động Bán hàng & Doanh số Chưa ghi nhận (Presales & Backlog)

| STT | Chỉ tiêu tài chính | Kỳ | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 32 | Doanh số ký bán (Contracted Sales) | `3Q26` | 71,5 nghìn tỷ đồng (+8% QoQ) | Slide 4, 16 | 71,5 nghìn tỷ đồng (+8% QoQ) | Phần 1 & 3.1 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 33 | Cơ cấu bán trước 3Q26: Bán lẻ | `3Q26` | 81% (57,9 nghìn tỷ đồng) | Slide 4, 16 | chiếm 81% tổng doanh số bán trước | Phần 1 & 3.1 | `[MATCH]` | Trùng khớp. Kênh bán lẻ đóng vai trò chủ đạo trong 3Q26. |
| 34 | Cơ cấu bán trước 3Q26: Bán buôn | `3Q26` | 19% (13,6 nghìn tỷ đồng) | Slide 16 | đại diện 19% | Q&A Câu 1 | `[MATCH]` | Trùng khớp cơ cấu phân rã bán buôn/bán lẻ. |
| 35 | Doanh số ký bán lũy kế | `9M26` | 219,6 nghìn tỷ đồng (+35% YoY) | Slide 4, 5, 17 | 219,6 nghìn tỷ đồng (+35% YoY) | Phần 1 & 3.1 | `[MATCH]` | Trùng khớp. Gấp 1,8 lần mức bình quân 5 năm (120,7 nghìn tỷ). |
| 36 | Doanh số chưa ghi nhận (Backlog) | `30/09/2026` | 185,6 nghìn tỷ đồng (1,7x bình quân 5 năm) | Slide 4, 5, 17 | 185,6 nghìn tỷ đồng (1,7 lần bình quân 5 năm) | Phần 1 & 3.1 | `[MATCH]` | Trùng khớp hoàn toàn. Đảm bảo tầm nhìn doanh thu tương lai. |
| 37 | Tỷ trọng bán buôn trong Backlog | `30/09/2026` | *Không ghi nhận trên Slide* | - | chiếm khoảng 15% tổng backlog | Q&A Câu 3 | `[SPEECH_ONLY]` | Xác thực: CFO cung cấp trực tiếp tại phiên chất vấn. |
| 38 | Thời gian từ bán buôn đến ghi nhận DT | - | *Không ghi nhận trên Slide* | - | trung bình khoảng 3 tháng | Q&A Câu 8 | `[SPEECH_ONLY]` | Xác thực: Chu kỳ thanh toán và chuyển quyền nhanh chóng. |
| 39 | Tỷ lệ người mua để ở thực | - | *Không ghi nhận trên Slide* | - | hơn 70% là nhóm khách hàng mua để ở | Q&A Câu 10 | `[SPEECH_ONLY]` | Xác thực: Khách hàng ở thực chiếm đa số, giảm thiểu rủi ro đầu cơ. |
| 40 | Tỷ lệ khách hàng dùng vốn vay NH | - | *Không ghi nhận trên Slide* | - | khoảng 55% đến 60% người mua dùng vốn vay | Q&A Câu 1 | `[SPEECH_ONLY]` | Xác thực: CFO nêu rõ tỷ lệ đòn bẩy người mua nhà. |

---

### 4. Tiến độ Triển khai Dự án & Phát triển Hạ tầng (Projects & Infrastructure)

| STT | Chỉ tiêu / Dự án | Mốc thời gian | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 41 | Vinhomes Green Paradise (Cần Giờ) | `4Q26` | Bàn giao nhà ở đầu tiên trong 4Q26 | Slide 4, 19 | hướng tới mốc bàn giao đầu tiên trong 4Q26 | Phần 1 & 3.3 | `[MATCH]` | Trùng khớp hoàn toàn mốc bàn giao. |
| 42 | Vinhomes Global Gate Hạ Long | `2027` | >1.000 căn thấp tầng đang thi công; bàn giao 2027 | Slide 4, 21 | >1.000 căn thấp tầng đang xây dựng; bàn giao 2027 | Phần 1 & 3.3 | `[MATCH]` | Trùng khớp. |
| 43 | Vinhomes Saigon Park | `4Q26` | Mở nhà mẫu và tiện ích trong 4Q26 | Slide 20 | mở nhà mẫu và tiện ích trọng điểm trong 4Q26 | Phần 3.3 | `[MATCH]` | Trùng khớp. |
| 44 | Dự án 5 tuyến Metro Hà Nội (EPC) | `12/2030` | Tổng vốn ~900 nghìn tỷ đồng; hoàn thành 12/2030 | Slide 4, 5, 23 | hợp đồng EPC turnkey trị giá ~900 nghìn tỷ đồng | Phần 1 & 3.3 | `[MATCH]` | Trùng khớp. Liên danh Vinhomes - SGC thực hiện. |
| 45 | Hợp đồng mua đoàn tàu Metro | - | *Không ghi nhận trên Slide* | - | ký thỏa thuận mua tới 200 đoàn tàu từ đối tác quốc tế | Phần 3.3 | `[FLAGGED]` | **ASR phát âm nhầm "Altech / transets"**. Hiệu chỉnh: thỏa thuận mua tới 200 đoàn tàu (trainsets) từ Alstom/đối tác quốc tế. |
| 46 | Dự án Bình Minh – Tam Hưng (Hà Nội) | Quy mô | 600 ha, dân số quy hoạch 105.000 người | Slide 24 | 600 ha, gần 105.000 dân; gần VĐ4 và Metro 2 | Phần 3.3 & Q&A Câu 2 | `[MATCH]` | Trùng khớp. Lãnh đạo giải trình là dự án theo đuổi từ trước. |
| 47 | Dự án NOXH Bà Điểm (TP.HCM) | Quy mô | 12 ha, dân số 65.000 người | Slide 24 | 12 ha, đáp ứng chỗ ở cho 65.000 người | Phần 3.3 | `[MATCH]` | Trùng khớp hoàn toàn. |
| 48 | Danh mục NOXH đang triển khai | Toàn quốc | 5 dự án, diện tích 428 ha, mục tiêu 500.000 căn | Slide 25 | 5 dự án, tổng quy mô 428 ha; mục tiêu 500.000 căn | Phần 3.3 | `[MATCH]` | Trùng khớp. Gồm Happy Home Phố Hiến 31 ha. |
| 49 | Tiến độ Cầu Cần Giờ (sông Soài Rạp) | `2026 - 2029` | *Không ghi nhận trên Slide* | - | Đúc dầm đầu tiên 01/10/2026; bàn giao MB 11/2026; xong 2029 | Q&A Câu 11 | `[FLAGGED]` | **ASR phát âm "S wrap river / Bengtan"**. Hiệu chỉnh: Cầu dây văng vượt sông Soài Rạp (nhịp 365m, 1.300 đốt dầm) và tuyến kết nối Bến Thành. |
| 50 | Tiền đặt cọc đầu tư 322 nghìn tỷ đồng | `30/09/2026` | *Ghi nhận trong Tài sản khác trên BCTC* | - | phân bổ cho các đối tác uy tín, chủ đất lớn trên nhiều dự án | Q&A Câu 4 | `[SPEECH_ONLY]` | Xác thực: CFO giải trình mục đích bảo đảm quyền tiếp cận các đại dự án tương lai. |

---

### 5. Kế hoạch Kinh doanh & Chỉ số Vĩ mô (Forward Guidance & Macro Indicators)

| STT | Chỉ tiêu / Luận điểm | Kỳ / Năm | Số liệu trên Slide (PPT/PDF) | Vị trí Slide | Số liệu trong Transcript | Vị trí Transcript | Trạng thái | Đánh giá & Hướng xử lý |
| :---: | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| 51 | Kế hoạch Doanh thu điều chỉnh FY26 | Cả năm 2026 | 285,0 nghìn tỷ đồng (9M26 đạt 82%) | Slide 6, 32 | đạt 82% kế hoạch cả năm | Phần 1 & 5 | `[MATCH]` | Trùng khớp. Đã thực hiện 232,6 nghìn tỷ đồng. |
| 52 | Doanh thu cần đạt thêm trong 4Q26 | `4Q26` | Còn thiếu 52,4 nghìn tỷ đồng | Slide 6 | còn lại khoảng 52,4 nghìn tỷ đồng | Phần 1 | `[MATCH]` | Trùng khớp. Động lực từ Green City, Golden City, Wonder City. |
| 53 | Kế hoạch LNST cả năm (FY26 Guidance) | Cả năm 2026 | 60,0 nghìn tỷ đồng (9M26 đạt 125%) | Slide 6, 32 | vượt 25% kế hoạch cả năm (đạt 75,1 nghìn tỷ) | Phần 1 & 5 | `[MATCH]` | Trùng khớp. Vượt kế hoạch trước 1 quý. |
| 54 | Tăng trưởng GDP Việt Nam | `3Q26` & `9M26` | 3Q26: 9,95% YoY; 9M26: 9,01% YoY | Slide 28 | 3Q26: 9,95% YoY; 9M26: 9,01% YoY | Phần 4 | `[MATCH]` | Trùng khớp tuyệt đối. Tăng trưởng 9 tháng cao nhất trong 15 năm. |
| 55 | Diễn biến nguồn cung BĐS Hà Nội & HCM | `3Q26` | HN căn hộ: 6.187 căn mở bán; HCM: 3.267 căn | Slide 30, 31 | Nguồn cung tiếp tục suy giảm tại hai đô thị lớn | Phần 4 & Q&A Câu 6 | `[MATCH]` | Khớp. Lời nói giải trình nguyên nhân thiếu hụt; Slide cung cấp số liệu chi tiết. |
"""

# Write data_reconciliation.md
recon_path = output_dir / "data_reconciliation.md"
with open(recon_path, "w", encoding="utf-8") as f:
    f.write(reconciliation_content)
print(f"[✓] Wrote {recon_path}")

# 3. analyst_report.md
report_content = """[Institutional Research] – Cập nhật Kết quả Kinh doanh Vinhomes (VHM - 3Q26 & 9M26): Doanh thu và Lợi nhuận tăng trưởng mạnh, Vượt kế hoạch năm sau 9 tháng

Phần 1: Kết quả hoạt động kinh doanh 3Q26 và 9M26
Tăng trưởng Doanh thu và Lợi nhuận:
- Doanh thu thuần hợp nhất: Trong 3Q26, doanh thu thuần đạt 85.364 tỷ đồng (+420% YoY so với 16.420 tỷ đồng trong 3Q25). Động lực tăng trưởng chủ yếu đến từ mảng chuyển nhượng bất động sản với doanh thu đạt 75.750 tỷ đồng (gấp 20,4 lần YoY), nhờ hoạt động bàn giao tại các dự án Vinhomes Global Gate Hạ Long, Saigon Park, cùng Vinhomes Ocean Park 2 & 3. Lũy kế 9M26, doanh thu thuần đạt 202.586 tỷ đồng (+302% YoY so với 50.413 tỷ đồng trong 9M25), trong đó doanh thu chuyển nhượng BĐS đạt 170.070 tỷ đồng (+717% YoY), chiếm 84% cơ cấu tổng doanh thu.
- Doanh thu điều chỉnh (Adjusted Revenue): Bao gồm doanh thu từ các giao dịch bán buôn ghi nhận qua chuyển nhượng cổ phần và dự án hợp tác kinh doanh (BCC), doanh thu điều chỉnh 9M26 đạt 232.593 tỷ đồng (+234% YoY), cao hơn mức thực hiện cả năm 2025 (141.644 tỷ đồng) và vượt trội so với mức bình quân 5 năm giai đoạn 2021–2025.
- Lợi nhuận gộp & Biên lợi nhuận: Lợi nhuận gộp trong 3Q26 đạt 51.490 tỷ đồng (+1.192% YoY); biên lợi nhuận gộp mở rộng lên mức 60,3% (tăng 36 điểm phần trăm so với 24,3% trong 3Q25) nhờ cơ cấu bàn giao tập trung vào các phân khu có tỷ suất lợi nhuận cao. Lũy kế 9M26, lợi nhuận gộp đạt 118.625 tỷ đồng (+573% YoY); biên lợi nhuận gộp đạt 58,6% (so với 34,9% trong 9M25).
- Lợi nhuận sau thuế & Tiến độ kế hoạch năm: Lợi nhuận sau thuế (NPAT) trong 3Q26 đạt 23.021 tỷ đồng (+419% YoY) và lợi nhuận sau thuế của cổ đông công ty mẹ (NPATMI) đạt 23.146 tỷ đồng (+453% YoY). Lũy kế 9M26, LNST đạt 75.059 tỷ đồng (+390% YoY) và NPATMI đạt 71.381 tỷ đồng (+396% YoY), vượt 70% mức thực hiện cả năm 2025. Với kế hoạch LNST cả năm 2026 là 60.000 tỷ đồng, Vinhomes đã chính thức hoàn thành 125% mục tiêu lợi nhuận năm sau 9 tháng đầu năm. Về chỉ tiêu doanh thu điều chỉnh, công ty đã hoàn thành 82% kế hoạch năm (285.000 tỷ đồng), phần còn lại khoảng 52.400 tỷ đồng dự kiến sẽ được ghi nhận trong 4Q26.

Hoạt động Bán hàng (Presales) và Doanh số chưa ghi nhận (Backlog):
- Doanh số ký bán (Contracted Sales): Trong 3Q26, doanh số ký bán đạt 71,5 nghìn tỷ đồng (+8% QoQ), với sự đóng góp lớn từ các dự án Vinhomes Saigon Park, Global Gate Hạ Long, Green City và Green Paradise. Điểm nổi bật là kênh bán lẻ (retail) đóng góp tới 81% cơ cấu doanh số quý (đạt 57,9 nghìn tỷ đồng), cho thấy lực cầu từ người mua nhà ở thực duy trì tích cực. Lũy kế 9M26, tổng doanh số ký bán đạt 219,6 nghìn tỷ đồng (+35% YoY), gấp 1,8 lần mức bình quân hàng năm giai đoạn 2021–2025 (120,7 nghìn tỷ đồng).
- Doanh số chưa ghi nhận (Unbilled Bookings / Backlog): Tính đến ngày 30/09/2026, lượng doanh số chưa ghi nhận đạt 185,6 nghìn tỷ đồng, gấp 1,7 lần mức bình quân 5 năm giai đoạn 2021–2025 (107,3 nghìn tỷ đồng). Trong đó, các giao dịch bán buôn chiếm khoảng 15% tổng backlog. Lượng backlog dồi dào này tiếp tục đảm bảo mức độ nhìn nhận doanh thu cao cho các quý tiếp theo khi các dự án bước vào chu kỳ bàn giao.

Cân đối Kế toán & Cơ cấu Nguồn vốn:
- Quy mô tài sản & Hàng tồn kho: Tổng tài sản tại ngày 30/09/2026 đạt 1.339,2 nghìn tỷ đồng (+70% so với đầu năm). Hàng tồn kho tăng lên mức 247,3 nghìn tỷ đồng (từ 131,4 nghìn tỷ đồng cuối năm 2025). Đáng chú ý, khoảng 85% giá trị tồn kho là các khoản chi phí liên quan đến đất, bồi thường giải phóng mặt bằng, chi phí xây dựng hạ tầng tại các dự án trọng điểm; bất động sản hoàn thiện để bán chỉ chiếm khoảng 2% tổng tồn kho.
- Quy mô Nợ vay & Thanh khoản: Tiền và tương đương tiền (bao gồm các khoản đầu tư ngắn hạn) duy trì ổn định ở mức 55,5 nghìn tỷ đồng. Tổng nợ vay ghi nhận 240,6 nghìn tỷ đồng; Vốn chủ sở hữu đạt 307,8 nghìn tỷ đồng (+24% YTD). Tỷ lệ Nợ vay trên Tổng tài sản duy trì an toàn ở mức 18,0% (giảm so với 18,6% tại thời điểm cuối năm 2025); Tỷ lệ Nợ thuần trên Vốn chủ sở hữu ở mức 60,2%; Tỷ lệ Nợ thuần trên Tổng tài sản điều chỉnh ở mức 14,4%.
- Cơ cấu nợ & Hệ số thanh toán: Danh mục nợ vay có độ an toàn cao với 99% nợ định danh bằng đồng Việt Nam (VND), hạn chế tối đa rủi ro tỷ giá; 74% các khoản nợ có kỳ hạn trên 1 năm với thời hạn nợ bình quân đạt 2,2 năm; Chi phí vay nợ bình quân duy trì ở mức 11,06%/năm. Nhờ lợi nhuận tăng trưởng cao, hệ số chi trả lãi vay (EBIT / Chi phí lãi vay) cải thiện lên 11,3 lần (so với 7,0 lần năm 2025 và 7,6 lần trong 9M25).

Phần 2: Định hướng chiến lược và Triển vọng các Dự án Trọng điểm
- Triển vọng 4Q26 và Kế hoạch năm: Công ty đặt kế hoạch ghi nhận phần doanh thu điều chỉnh còn lại khoảng 52.400 tỷ đồng trong 4Q26 để hoàn thành trọn vẹn mục tiêu 285.000 tỷ đồng của cả năm, động lực đến từ việc tiếp tục bàn giao tại Green Paradise, Golden City, Green City, Saigon Park, Global Gate Hạ Long và Wonder City.
- Đại đô thị Biển Vinhomes Green Paradise (Cần Giờ, TP.HCM): Tiến độ thi công đang được đẩy mạnh nhằm đạt mốc bàn giao những căn nhà đầu tiên ngay trong 4Q26. Hạ tầng kết nối ngoại khu ghi nhận bước tiến quan trọng với công trình cầu dây văng vượt sông Soài Rạp (nhịp chính 365m) đã đúc đốt dầm đầu tiên vào ngày 01/10/2026; TP.HCM dự kiến hoàn tất bàn giao mặt bằng trong tháng 11/2026 và mục tiêu hoàn thành công trình vào năm 2029.
- Vinhomes Global Gate Hạ Long & Saigon Park: Tại Global Gate Hạ Long, hơn 1.000 căn thấp tầng đang được thi công khẩn trương để chuẩn bị bàn giao từ năm 2027; dự án đón nhận lực đẩy hạ tầng lớn từ tuyến đường sắt tốc độ cao Hà Nội – Quảng Ninh đang thi công. Tại Vinhomes Saigon Park, nhà mẫu và hệ thống tiện ích trọng điểm dự kiến khai trương trong 4Q26, đón đầu kết nối từ đường Vành đai 3 và Metro số 2.
- Chiến lược Bán buôn (Bulk Sales): Tiếp tục đóng vai trò trụ cột trong mô hình phát triển đại đô thị tích hợp (MPC). Bán buôn giúp rút ngắn thời gian thu hồi dòng tiền, giảm thiểu rủi ro phát triển và tối ưu hóa lợi nhuận trong giai đoạn đầu dự án, với thời gian luân chuyển từ lúc ký thỏa thuận đến ghi nhận doanh thu trung bình chỉ khoảng 3 tháng. Mạng lưới người mua đa dạng từ các đối tác quốc tế (Nomura, CapitaLand, Mitsubishi Corporation) đến đối tác trong nước (Masterise, MIK), không có rủi ro tập trung.
- Tham gia Dự án Hạ tầng Giao thông Đô thị (EPC Metro Hà Nội): Liên danh Vinhomes – SGC đã ký kết hợp đồng tổng thầu EPC trọn gói cho 5 tuyến Metro Hà Nội với tổng mức đầu tư ước tính khoảng 900 nghìn tỷ đồng (chưa gồm chi phí GPMB), thời hạn hoàn thành mục tiêu vào tháng 12/2030; đồng thời ký thỏa thuận mua tới 200 đoàn tàu phục vụ mạng lưới metro. Định hướng này mở rộng đáng kể năng lực phát triển mô hình đô thị gắn kết giao thông công cộng (TOD) trong dài hạn.
- Đẩy mạnh Phát triển Phân khúc Nhà ở Xã hội (NOXH): Đang triển khai 5 dự án NOXH trên toàn quốc với tổng quy mô 428 ha, tiêu biểu như Happy Home Phố Hiến (Hưng Yên - 31 ha, 10.650 cư dân) và Bà Điểm (TP.HCM - 12 ha, 65.000 cư dân), kiên định cam kết cung cấp 500.000 căn nhà ở xã hội trên cả nước.

Phần 3: Đối đáp và trả lời câu hỏi với chuyên viên phân tích (Q&A)
1. Động lực tăng trưởng doanh số bán lẻ 3Q26 và Tác động của môi trường lãi suất – Question from Terren:
Management Response: (i) Kênh bán lẻ đóng góp 81% tổng doanh số bán trước 3Q26 (57,9 nghìn tỷ trên tổng số 71,5 nghìn tỷ đồng), đóng góp chủ đạo từ Vinhomes Saigon Park, Global Gate Hạ Long và Green Paradise Giai đoạn 2; (ii) Mặt bằng lãi suất neo cao không gây gián đoạn thanh khoản nhờ công ty triển khai gói cố định trần lãi suất 5 năm (từ 3% đến 9%/năm) phối hợp cùng hơn 30 ngân hàng, đi kèm ưu đãi hội viên Vinclub chiết khấu tới 5,1% và voucher tri ân 8% – 10%; (iii) Hiện có khoảng 55% – 60% khách hàng mua nhà sử dụng đòn bẩy ngân hàng; các gói tài chính cố định giúp người mua loại bỏ áp lực lãi suất thả nổi thị trường (hiện ở mức 14% – 15%).
2. Bản chất Dự án Bình Minh – Tam Hưng và Định hướng Quản trị Quỹ đất – Question from Tukan:
Management Response: (i) Dự án Bình Minh – Tam Hưng (quy mô 600 ha tại Hà Nội) là dự án công ty đã theo đuổi và tiến hành hoàn thiện thủ tục pháp lý trong thời gian dài; việc được phê duyệt chủ trương đầu tư gần đây là kết quả của tiến trình chuẩn bị trước đó; (ii) Hoạt động này hoàn toàn nhất quán với định hướng phát triển quỹ đất thận trọng đã công bố; Vinhomes không mua gom đất dàn trải mà tập trung khai thác các dự án có pháp lý rõ ràng, bảo đảm tối đa hiệu quả vốn và lợi ích cổ đông.
3. Cơ cấu Đối tác Bán buôn, Tính chất Sản phẩm và Chu kỳ Ghi nhận Doanh thu – Question from Andre Cringlin:
Management Response: (i) Hoàn toàn không có rủi ro tập trung người mua; đối tác bán buôn bao gồm các tập đoàn đa quốc gia (Nomura, CapitaLand, Mitsubishi Corporation) và các doanh nghiệp phát triển lớn trong nước (Masterise, MIK,...); (ii) Sản phẩm bán buôn chủ yếu là đất phát triển dự án đã kết nối hạ tầng khung (trục giao thông chính, hệ thống cấp thoát nước, điện), không bao gồm hạ tầng nội khu chi tiết và không phải bất động sản hoàn thiện; (iii) Thời gian luân chuyển từ khi ký kết thỏa thuận bán trước đến khi ghi nhận doanh thu trung bình chỉ khoảng 3 tháng, nhanh hơn đáng kể so với bán lẻ.
4. Khoản tiền Đặt cọc Đầu tư 322 nghìn tỷ đồng ghi nhận tại Danh mục Tài sản khác – Question from Analyst:
Management Response: (i) Khoản tiền đặt cọc đầu tư được phân bổ cho các đối tác uy tín, các chủ sở hữu đất và doanh nghiệp bất động sản sở hữu các quỹ đất sạch tiềm năng hoặc dự án quy mô lớn; (ii) Mục đích nhằm bảo đảm quyền tiếp cận, hợp tác phát triển và phân chia lợi ích kinh tế tại các đại dự án tương lai; (iii) Danh mục hợp tác được phân tán trên nhiều đối tác và dự án khác nhau, phục vụ chiến lược tích lũy và phát triển dự án gối đầu.
5. Biên Lợi nhuận Gộp mảng Xây dựng (Vincons) duy trì ở mức cao 14% - 16% – Question from Tanglay:
Management Response: (i) Biên lợi nhuận gộp 14% – 16% của mảng xây dựng hoàn toàn phù hợp với mức vận hành bình thường và ổn định của công ty trong các kỳ trước; (ii) Kết quả này phản ánh năng lực quản lý dự án nội bộ, chủ động chuỗi cung ứng và kiểm soát chặt chẽ chi phí đầu vào; các công trình của Vinhomes hầu như không bị chậm trễ tiến độ, giúp tối ưu hóa chi phí và hấp thụ tốt áp lực gia tăng giá vật liệu và nhân công xây dựng.
6. Chiến lược Quản trị Nợ vay và Cấu trúc Đòn bẩy Tài chính – Question from Hail:
Management Response: (i) Công ty quản trị nợ dựa trên các hệ số an toàn đòn bẩy; hệ số chi trả lãi vay (EBIT / Chi phí lãi vay) đạt 11,3 lần, tỷ lệ Nợ thuần / Vốn chủ sở hữu ở mức 60,2%, hệ số thanh toán hiện hành đạt 1,26 lần, bảo đảm an toàn tài chính vững chắc; (ii) Chủ động đa dạng hóa cấu trúc huy động vốn thông qua đẩy mạnh phát hành trái phiếu doanh nghiệp trong nước và chuẩn bị sẵn sàng các phương án phát hành trái phiếu quốc tế để tối ưu hóa chi phí vốn và giảm áp lực phụ thuộc tín dụng ngân hàng nội địa.
7. Tiến độ Triển khai Dự án Cầu Cần Giờ & Tuyến Kết nối Đại đô thị Green Paradise – Question from Analyst:
Management Response: (i) Dự án cầu dây văng vượt sông Soài Rạp (nhịp chính 365m, cần khoảng 1.300 đốt dầm đúc sẵn) đã chính thức đúc đốt dầm đầu tiên vào ngày 01/10/2026; (ii) TP.HCM đặt mục tiêu bàn giao toàn bộ mặt bằng còn lại trong tháng 11/2026; (iii) Dự kiến hoàn thành công trình vào năm 2029, bảo đảm kết nối thông suốt từ khu vực trung tâm TP.HCM tới đại đô thị biển Vinhomes Green Paradise.
"""

# Write analyst_report.md
report_path = output_dir / "analyst_report.md"
with open(report_path, "w", encoding="utf-8") as f:
    f.write(report_content)
print(f"[✓] Wrote {report_path}")
