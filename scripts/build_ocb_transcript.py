# -*- coding: utf-8 -*-
"""
Build standardized full_transcript.md and full_transcript.docx for OCB.
Includes:
- Section 01: Lời Mở đầu & Bối cảnh Kinh tế Vĩ mô 9M26
- Section 02: Khái quát Kết quả Kinh doanh OCB 9M26
- Section 03: Chi tiết Bức tranh Tài chính 9M26 & Kế hoạch FY26
- Section 04: Chiến lược Chuyển đổi Số & Phát triển Ngân hàng AI-Native
- Section 05: Tầm nhìn Chiến lược Dài hạn & Ba Trọng tâm Thực thi
- Section 06: Phiên Thảo luận và Hỏi đáp Toàn diện (Q&A Session - 13 câu hỏi)
- Section 07: Bế mạc Hội nghị Trình bày Kết quả Kinh doanh 9M26
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

TRANSCRIPT_MD = """# NGÂN HÀNG THƯƠNG MẠI CỔ PHẦN PHƯƠNG ĐÔNG (OCB)
# BẢN GHI ĐẦY ĐỦ CUỘC HỌP (FULL STANDARDIZED TRANSCRIPT)

* **Kỳ báo cáo**: 3Q26 & 9 tháng đầu năm 2026 (9M26) – Định hướng 4Q26 & Kế hoạch Cả năm FY26 & Triển vọng 2027
* **Thời gian tổ chức**: Ngày 12/11/2026 (Performance Announcement 9M2026 & Earnings Call Q&A)
* **Đơn vị tổ chức**: Ngân hàng TMCP Phương Đông (Mã chứng khoán: OCB)
* **Thành phần Ban Lãnh đạo chủ trì**:
  - **Bà Thúy Quỳnh** – Bộ phận Quan hệ Nhà đầu tư OCB (Host / Điều phối viên)
  - **Ông Dương Đức Hùng** – Tổng Giám đốc OCB
  - **Ông Quách Thành Long** – Giám đốc Trung tâm Quản lý Tài chính OCB
  - **Mr. Chris Shayan** – Giám đốc Điều hành OCB (Managing Director)
  - **Các định chế tài chính & quỹ đầu tư đặt câu hỏi**: VCBF, PVSC, Horizon Capital, Arisco, MBIS, FPTS, VIS Rating, TCBS, TPS, DVSG, OCBS, SHS, BVSC
* **Tài liệu đối chiếu**: `OCB Presentation.pdf` (24 slide trình chiếu chính thức)
* **Quy ước biên tập chuẩn mực định chế**:
  - `Ngôn ngữ phát biểu`: Giữ nguyên ngôn ngữ gốc của người thuyết trình (Speaker's Language) – tiếng Việt cho Ban điều hành và tiếng Anh cho Khối Chuyển đổi số.
  - `Chuẩn hóa bản ghi ASR`: Loại bỏ toàn bộ từ ngập ngừng, từ đệm (à, ừ...), chuẩn hóa lỗi nhận diện âm thanh, bảo toàn 100% số liệu thực tế và luận điểm của Ban lãnh đạo.
  - `> *[Diễn giải từ Slide X: ...]*`: Chú thích đối chiếu số liệu công bố chính thức trên slide tài liệu cuộc họp (Ground Truth Benchmark).
  - `Quy chuẩn số liệu`: Định dạng quốc tế chuẩn mực (dấu chấm `.` cho phần thập phân, dấu phẩy `,` cho phân cách hàng ngàn).
  - `Quy chuẩn ký hiệu kỳ`: Thống nhất đồng bộ định dạng `3Q26`, `9M26`, `4Q26`, `FY26`, `FY27`.

---

## 01  |  Lời Mở đầu và Cập nhật Bối cảnh Kinh tế Vĩ mô 9M26

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin kính chào quý cổ đông, quý nhà đầu tư và các anh chị chuyên viên phân tích. Quý vị đang tham dự chương trình Hội nghị công bố kết quả kinh doanh 9 tháng đầu năm 2026 (9M26) được thực hiện bởi Ngân hàng TMCP Phương Đông (OCB) ngày hôm nay.

Đầu tiên, tôi xin được trân trọng giới thiệu thành phần Ban lãnh đạo OCB tham dự buổi làm việc:
- Ông Dương Đức Hùng – Tổng Giám đốc;
- Mr. Chris Shayan – Giám đốc Điều hành (Managing Director);
- Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính.

Thưa quý vị, chương trình của chúng ta ngày hôm nay bao gồm hai phần:
- Phần thứ nhất: Ban lãnh đạo OCB sẽ trình bày các hoạt động nổi bật, kết quả kinh doanh đạt được trong 9M26 cũng như các định hướng và chiến lược hành động sắp tới.
- Phần thứ hai: Chúng ta sẽ bước vào phiên thảo luận và trả lời câu hỏi (Q&A).

Để mở đầu cho phần trình bày hôm nay, chúng tôi xin trân trọng kính mời Ông Dương Đức Hùng – Tổng Giám đốc sẽ chia sẻ bức tranh vĩ mô cùng những hoạt động nổi bật của OCB trong 9M26. Xin trân trọng kính mời anh."

> *[Diễn giải từ Slide 01, 02: Performance Announcement 9M2026, tổ chức ngày 12/11/2026 tại TP.HCM. Chương trình nghị sự gồm 5 phần: (01) 9M2026 Highlights - CEO; (02) 9M2026 Financial Results & FY2026 Guidance - CFO/Head of Financial Management Center; (03) Digital Transformation & Strategic Initiatives - Managing Director; (04) Strategic Vision & Execution Priorities - CEO; (05) Q&A Session]*

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Cảm ơn chị Quỳnh. Xin kính chào tất cả các anh chị chuyên viên phân tích, các quỹ đầu tư và quý nhà đầu tư. Như chị Quỳnh đã giới thiệu, tôi là Dương Đức Hùng – Tổng Giám đốc Ngân hàng OCB. Rất vui mừng được gặp gỡ và chia sẻ thông tin cập nhật đến các anh chị ngày hôm nay.

Trước hết, tôi xin chia sẻ nhanh một số cập nhật về bối cảnh kinh tế vĩ mô trong 9M26.

Về kinh tế thế giới: Cú sốc giá năng lượng trong thời gian qua đã khiến Cục Dự trữ Liên bang Mỹ (Fed) quay trở lại lập trường thắt chặt chính sách tiền tệ. Cụ thể, tại cuộc họp ngày 16/09/2026, Fed đã quyết định tăng lãi suất cơ bản USD thêm 25 điểm cơ bản (bps), đưa lãi suất quỹ liên bang (Fed funds rate) lên biên độ 3.75% – 4.00%. Tính đến ngày 30/09/2026, lợi suất trái phiếu Chính phủ Mỹ kỳ hạn 10 năm (UST 10Y) neo ở mức 5.29% và giá dầu Brent duy trì trên ngưỡng 100 USD/thùng.

Về kinh tế Việt Nam: Tăng trưởng GDP trong 3Q26 ghi nhận mức tăng tốc mạnh mẽ 9.95% YoY. Đà tăng này đã đưa tăng trưởng GDP chung của 9M26 đạt mức 9.01% YoY – mức tăng trưởng 9 tháng cao nhất trong vòng 15 năm qua. Hoạt động xuất khẩu diễn biến rất tích cực, tăng 39% trong tháng 9 so với tháng trước; riêng tháng 9 đã ghi nhận xuất siêu hơn 1 tỷ USD. Tuy nhiên, tính chung toàn bộ 9M26, cán cân thương mại hàng hóa của Việt Nam vẫn ghi nhận mức nhập siêu 19.42 tỷ USD. Về diễn biến lạm phát, chỉ số giá tiêu dùng (CPI) tháng 9 đạt 5.08% YoY do giá xăng dầu vẫn ở vùng cao; tính bình quân 9M26, CPI ở mức 4.52%, nhỉnh hơn một chút so với mục tiêu điều hành cả năm của Chính phủ là 4.50%.

> *[Diễn giải từ Slide 03: Lãi suất Fed funds 3.75% - 4.00%, lợi suất UST 10Y đạt 5.29% tại 30/09/2026, giá dầu Brent >100 USD/thùng. GDP Việt Nam 3Q26 tăng 9.95% YoY, GDP 9M26 đạt 9.01% YoY (cao nhất 15 năm). CPI bình quân 9M26 ở mức 4.52%, nhập siêu 9M26 là 19.42 tỷ USD]*

Về thị trường tiền tệ và ngoại hối:
Thanh khoản trên thị trường liên ngân hàng đã ghi nhận sự cải thiện rõ nét. Số dư nghiệp vụ thị trường mở (OMO) bình quân trong 3Q26 giảm mạnh xuống mức 192,000 tỷ VND, thu hẹp đáng kể so với mức bình quân 288,000 tỷ VND trong 2Q26. Yếu tố hỗ trợ then chốt ở đây là dòng tiền gửi của Kho bạc Nhà nước tại hệ thống các ngân hàng thương mại đã gia tăng, giúp giảm mức độ phụ thuộc vào kênh OMO. Bên cạnh đó, trong tháng 9, Ngân hàng Nhà nước (NHNN) cũng đã bổ sung công cụ hỗ trợ thanh khoản thông qua nghiệp vụ hoán đổi ngoại tệ (FX Swap). Lãi suất liên ngân hàng bình quân kỳ hạn qua đêm (Overnight) và 1 tháng (1M) trong 3Q26 đều hạ nhiệt đáng kể so với 2Q26 (kỳ hạn 1M chốt tại ngày 30/09 ở mức 6.30%). Tỷ giá USD/VND duy trì ở trạng thái tương đối ổn định, giảm 1.1% trong 3Q26 so với 2Q26, giao dịch ở mức 25,959 VND/USD tại ngày 30/09.

Về tương quan tăng trưởng tín dụng và huy động:
Trong 9M26, tăng trưởng tín dụng toàn hệ thống đạt 11.59% YTD, trong khi tăng trưởng huy động vốn đạt 10.60% YTD. Độ chênh lệch giữa tín dụng và huy động (credit-deposit gap) đã thu hẹp xuống chỉ còn 0.99 điểm % (so với mức chênh lệch 2.17 điểm % trong 2Q26). Nguyên nhân cốt lõi là do tốc độ huy động tiền gửi toàn hệ thống đã có sự tăng tốc mạnh mẽ trong 3Q26.

> *[Diễn giải từ Slide 04: Số dư OMO bình quân 3Q26 đạt 192 nghìn tỷ VND; lãi suất liên ngân hàng 1M tại 30/09 là 6.30%; tỷ giá USD/VND tại 30/09 là 25,959. Tín dụng toàn ngành 9M26 tăng 11.59% YTD, huy động vốn tăng 10.60% YTD; khoảng cách chênh lệch tín dụng - huy động thu hẹp về 0.99 điểm %]*

Về triển vọng vĩ mô 4Q26:
Tại cuộc họp chính sách ngày 28/10/2026, Fed đã quyết định giữ nguyên lãi suất USD. Biến số thị trường lúc này chịu sự chi phối giữa một bên là sức ép lạm phát và một bên là trạng thái phòng vệ né tránh rủi ro (risk-off) xuất phát từ đợt điều chỉnh giảm của nhóm cổ phiếu công nghệ/AI. Diễn biến bán tháo nhóm cổ phiếu AI vừa qua đã làm giảm xác suất Fed tiếp tục tăng lãi suất trong kỳ họp tháng 12/2026 tới.

Tại Việt Nam, bước sang tháng 10, chỉ số CPI bình quân 10 tháng ghi nhận ở mức 4.57%, cao hơn mức 4.52% của 9 tháng và cao hơn mục tiêu trần 4.50% của Chính phủ. Tuy nhiên, một tín hiệu rất tích cực là giá xăng RON 95 đã giảm 17.8% kể từ cuối tháng 10. Đồng thời, Chính phủ đã ban hành quyết định giảm giá điện bình quân 2% và hạ mức thuế tiêu thụ đặc biệt đối với xăng dầu xuống 0% kể từ ngày 01/11/2026 cho đến hết tháng 5/2027. Chúng tôi ước tính gói giải pháp này sẽ hỗ trợ kéo giảm CPI tháng 11 khoảng 0.5 điểm % so với tháng 10, dù tác động bình quân lên cả 10 tháng là khoảng 0.08 điểm %.

Về tiền tệ và tỷ giá trong tháng 10 và đầu tháng 11:
Lãi suất liên ngân hàng qua đêm (bình quân tháng 10 đạt 3.60%) và kỳ hạn 1 tháng (bình quân đạt 5.52%) tiếp tục duy trì xu hướng giảm. Tỷ giá USD/VND duy trì ổn định, ghi nhận quanh mức 25,680 VND/USD tại ngày 05/11/2026.

Dựa trên kịch bản cơ sở là xác suất Fed nâng lãi suất USD vào cuối năm giảm xuống và tỷ giá USD/VND tiếp tục duy trì trạng thái ổn định, dư địa nới lỏng chính sách tiền tệ của NHNN có thể sẽ được mở ra. Dù vậy, yếu tố rủi ro lớn nhất cần theo dõi sát sao vẫn là tỷ giá. Nếu dòng giải ngân vốn vay nước ngoài (offshore borrowing) có dấu hiệu chững lại, thị trường sẽ mất đi một nguồn lực hỗ trợ tỷ giá rất quan trọng. Đồng thời, trong tháng 10 vừa qua, toàn bộ kim ngạch nhập siêu của Việt Nam tập trung chủ yếu vào nhóm linh kiện điện tử và máy tính; do đó, sự suy yếu của chu kỳ công nghệ toàn cầu có thể tác động tiêu cực đến xuất khẩu và cán cân thanh toán, qua đó tạo áp lực trở lại lên tỷ giá. Khi rủi ro tỷ giá quay trở lại, dư địa điều hành nới lỏng của NHNN sẽ chịu sự thu hẹp tương ứng."

> *[Diễn giải từ Slide 05: Fed funds rate 3.75% - 4.00%; lợi suất UST 10Y giảm về 4.84% tại ngày 05/11; giá dầu Brent hạ về 98 USD/thùng. CPI bình quân 10 tháng tại 4.57%; giá xăng RON 95 giảm 17.8% từ cuối tháng 10. Lãi suất qua đêm bình quân tháng 10 là 3.60%, lãi suất 1M là 5.52%; tỷ giá USD/VND tại 05/11 là 25,680]*

---

## 02  |  Khái quát Kết quả Hoạt động Kinh doanh OCB 9M26

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Chuyển sang kết quả hoạt động kinh doanh của OCB: Như quý vị có thể quan sát trên slide, trong 9M26, OCB tiếp tục duy trì đà tăng trưởng tích cực trên toàn bộ các chỉ tiêu kinh doanh trọng yếu:
- Lợi nhuận trước thuế (PBT): Đạt 4,123 tỷ VND, tăng trưởng 20.2% YoY so với cùng kỳ năm trước.
- Quy mô tổng tài sản: Đạt 363,726 tỷ VND (xấp xỉ 364 nghìn tỷ VND), tăng trưởng hai chữ số 12.6% YTD so với đầu năm và tăng 15.4% YoY so với cùng kỳ.
- Dư nợ tín dụng thị trường 1: Đạt 227,183 tỷ VND (xấp xỉ 227 nghìn tỷ VND), tăng trưởng 10.8% YTD (tăng 12.0% YoY).
- Tổng doanh thu và thu nhập: Tăng trưởng vững chắc, trong đó Thu nhập lãi thuần (NII) đạt 7,676 tỷ VND (+13.4% YoY). Đặc biệt, Thu nhập ngoài lãi (Non-NII) tăng trưởng bứt phá 42.9% YoY (hơn +43%), đạt 1,543 tỷ VND (vượt mốc 1,500 tỷ VND). Kết quả này minh chứng chiến lược đa dạng hóa cơ cấu nguồn thu của OCB đang đi rất đúng hướng.
- Hiệu quả hoạt động: Tỷ lệ chi phí trên thu nhập (CIR) được cải thiện rõ nét, giảm hơn 4.5 điểm % YoY xuống mức 34.8% (so với 39.3% cùng kỳ).

Lát nữa, anh Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính sẽ chia sẻ chi tiết hơn bức tranh tài chính chuyên sâu của ngân hàng trong 9M26.

Ngoài ra, trong năm vừa qua, OCB tiếp tục được các định chế tài chính uy tín trong nước và quốc tế như The Asian Banker, FinanceAsia, Global Banking & Finance Review vinh danh thông qua nhiều giải thưởng danh giá. Đây là minh chứng vững chắc cho vị thế thương hiệu và năng lực cạnh tranh ngày càng nâng cao của OCB trên thị trường tài chính ngân hàng.

Tôi xin trân trọng cảm ơn quý vị và xin chuyển lời lại cho ban tổ chức."

> *[Diễn giải từ Slide 06: PBT 9M26 đạt 4,123 tỷ VND (+20.2% YoY). Tổng tài sản đạt 364 nghìn tỷ VND (+12.6% YTD, +15.4% YoY). Tín dụng thị trường 1 đạt 227 nghìn tỷ VND (+10.8% YTD, +12.0% YoY). Thu nhập lãi thuần (NII) đạt 7,676 tỷ VND (+13.4% YoY). Thu nhập ngoài lãi đạt 1,543 tỷ VND (+42.9% YoY). Tỷ lệ CIR đạt 34.8% (giảm 4.5 điểm % YoY)]*

---

## 03  |  Chi tiết Bức tranh Tài chính 9M26 và Định hướng Kế hoạch FY26

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin được trân trọng cảm ơn phần chia sẻ tổng quan của Ông Dương Đức Hùng. Tiếp theo chương trình, chúng tôi xin trân trọng kính mời Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB sẽ trình bày chi tiết về kết quả tài chính 9M26 và các mục tiêu, định hướng kinh doanh cho 4Q26 cũng như cả năm 2026. Xin trân trọng kính mời anh."

> *[Diễn giải từ Slide 07: Phần 02 - 9M2026 Financial Results & FY2026 Guidance do Mr. Quách Thành Long – Head of Financial Management Center trình bày]*

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Vâng, xin cảm ơn chị Quỳnh. Kính chào quý nhà đầu tư và quý chuyên viên phân tích. Sau đây tôi xin phép đi sâu vào các số liệu tài chính chi tiết của OCB trong 9M26 cũng như các định hướng điều hành trong 4Q26.

Như Tổng Giám đốc vừa chia sẻ, trong 9M26, OCB tiếp tục duy trì đà tăng trưởng tích cực cả về quy mô hoạt động lẫn hiệu quả kinh doanh nhằm hướng tới hoàn thành các mục tiêu mà Đại hội đồng cổ đông (ĐHĐCĐ) đã giao cho Ban điều hành.

Về quy mô hoạt động và bảng cân đối kế toán:
- Tổng tài sản: Tính đến ngày 30/09/2026, tổng tài sản của OCB đạt 363,726 tỷ VND, tăng trưởng 12.6% so với đầu năm và tăng 15.4% YoY so với cùng kỳ năm 2025. Quy mô tổng tài sản hiện tại đã chính thức vượt kế hoạch cả năm 2026 được ĐHĐCĐ giao (kế hoạch năm là 354,214 tỷ VND, đạt 102.7% kế hoạch).
- Dư nợ tín dụng thị trường 1: Đạt 227,183 tỷ VND, tăng trưởng 10.8% YTD so với đầu năm (tăng 12.0% YoY, hoàn thành 96.3% kế hoạch năm là 235,875 tỷ VND). Tăng trưởng tín dụng của OCB được điều hành bám sát hạn mức (quota) do NHNN cấp, ưu tiên tập trung vào các phân khúc khách hàng có biên lợi suất tốt và thuộc lĩnh vực ngành nghề ưu tiên của Hội đồng Quản trị.
- Huy động vốn thị trường 1: Đạt 226,111 tỷ VND, tăng 2.3% YTD so với đầu năm (tăng 2.8% YoY, đạt 89.8% kế hoạch năm là 251,919 tỷ VND). Trong đó, mảng huy động bán lẻ tiếp tục tăng trưởng mạnh mẽ và mở rộng quy mô, đảm bảo nền tảng thanh khoản và các tỷ lệ an toàn luôn được duy trì ở mức thận trọng, tuân thủ nghiêm ngặt các quy định của NHNN.

> *[Diễn giải từ Slide 08: Tổng tài sản đạt 363,726 tỷ VND (+12.6% YTD, +15.4% YoY; kế hoạch năm 354,214 tỷ VND). Dư nợ tín dụng thị trường 1 đạt 227,183 tỷ VND (+10.8% YTD, +12.0% YoY; kế hoạch năm 235,875 tỷ VND). Huy động vốn thị trường 1 đạt 226,111 tỷ VND (+2.3% YTD, +2.8% YoY; kế hoạch năm 251,919 tỷ VND)]*

Phân tích chi tiết về cơ cấu danh mục tín dụng:
Tín dụng 9M26 đạt mức tăng 10.8% YTD. Chúng tôi chủ trương tăng trưởng có chọn lọc và tối ưu hóa hiệu quả trên hạn mức được cấp, tập trung giải ngân cho các khách hàng hiện hữu có chất lượng tốt cũng như tái cơ cấu danh mục để đạt biên lợi suất sinh lời cao hơn.
- Phân khúc Khách hàng Doanh nghiệp (Corporate): Dư nợ tăng trưởng 13.0% YTD, tiếp tục đáp ứng kịp thời nhu cầu vốn phục vụ sản xuất kinh doanh và thương mại của cộng đồng doanh nghiệp.
- Phân khúc Khách hàng Cá nhân (Retail): Ghi nhận tăng trưởng 5.2% YTD. Kết quả này đánh dấu sự phục hồi bước đầu của mảng bán lẻ; OCB duy trì tốc độ giải ngân thận trọng trong bối cảnh thị trường bán lẻ nói chung vẫn đối mặt với khó khăn, tập trung ưu tiên vào tệp khách hàng phân khúc Affluent và Mass Affluent.
- Tín dụng xanh (Green Financing): Tỷ lệ tín dụng xanh của OCB hiện đạt mức 9.5% trên tổng dư nợ – giữ vững vị thế là một trong những định chế có tỷ trọng tài trợ tín dụng xanh cao hàng đầu trong toàn ngành ngân hàng.
- Đa dạng hóa danh mục theo ngành nghề: Nhằm hạn chế rủi ro tập trung, OCB phân bổ danh mục cho vay đồng đều qua nhiều lĩnh vực then chốt. Cụ thể: Bất động sản chiếm 24%, Bán buôn & bán lẻ chiếm 14%, Dịch vụ lưu trú & ăn uống chiếm 11%, Các ngành trọng điểm khác chiếm 11%, Xây dựng chiếm 7%, Hoạt động chuyên môn KH&CN chiếm 6%, Công nghiệp chế biến chế tạo chiếm 5%, Logistics & kho bãi chiếm 3%, Sản xuất và phân phối điện, khí đốt chiếm 2%. Cơ cấu đa dạng này là bệ đỡ vững chắc giúp OCB tăng trưởng tín dụng bền vững và hạn chế rủi ro chu kỳ ngành.

> *[Diễn giải từ Slide 09: Dư nợ Khách hàng Doanh nghiệp tăng 13.0% YTD, Khách hàng Cá nhân tăng 5.2% YTD. Tỷ trọng tài trợ tín dụng xanh đạt 9.5% tổng dư nợ. Cơ cấu tín dụng theo ngành nghề: BĐS 24%, Bán buôn & bán lẻ 14%, Lưu trú & ăn uống 11%, Ngành khác 11%, Xây dựng 7%, KH&CN 6%, Chế biến chế tạo 5%, Logistics 3%, Điện/khí đốt 2%]*

Về cơ cấu nguồn vốn huy động:
OCB chủ động điều hành huy động vốn nhịp nhàng với tiến độ tăng trưởng tín dụng, chú trọng cải thiện cơ cấu nguồn vốn giá rẻ để tối ưu hóa chi phí vốn (COF).
- Tăng trưởng CASA: Số dư tiền gửi không kỳ hạn (CASA) tăng trưởng ấn tượng 18.7% YTD. Về cơ cấu huy động: Tiền gửi có kỳ hạn chiếm 59%, Giấy tờ có giá (Valuable papers) chiếm 30%, Tiền gửi CASA chiếm 8%, và Quỹ ủy thác (Trusted funds) chiếm 3%.
- Đóng góp từ kênh số hóa: Các sản phẩm huy động được phân phối linh hoạt qua kênh ngân hàng số Liobank và ứng dụng OCB OMNI. Trong 9M26, số dư huy động tiền gửi qua Liobank tăng vọt 105% YTD; số dư tiền gửi trực tuyến của khách hàng cá nhân (RB online FD) tăng mạnh 68.9% YTD. Riêng mảng bán lẻ, tổng nguồn vốn huy động tăng 16% so với đầu năm. Đây là minh chứng rõ nét cho năng lực tiếp cận sâu rộng tệp khách hàng số hóa và khả năng đa dạng hóa nguồn vốn của OCB.

> *[Diễn giải từ Slide 10: Tiền gửi CASA tăng 18.7% YTD; huy động tiền gửi Liobank tăng 105% YTD; tiền gửi online mảng bán lẻ (RB online FD) tăng 68.9% YTD. Cơ cấu nguồn vốn: Tiền gửi có kỳ hạn 59%, Giấy tờ có giá 30%, CASA 8%, Quỹ ủy thác 3%]*

Về xếp hạng tín nhiệm và các chỉ số an toàn, thanh khoản:
- Xếp hạng tín nhiệm Moody's: Trong kỳ đánh giá công bố ngày 20/09/2026, Tổ chức xếp hạng tín nhiệm quốc tế Moody's đã khẳng định duy trì xếp hạng tiền gửi và nhà phát hành dài hạn của OCB ở mức Ba3 với Triển vọng Ổn định (Rating outlook: Stable); đánh giá sức mạnh nội tại (Baseline Credit Assessment - BCA) duy trì ở mức B1. Kết quả này củng cố mạnh mẽ uy tín của OCB trên thị trường tài chính quốc tế, tạo tiền đề thuận lợi cho việc huy động vốn trung và dài hạn.
- Hệ số an toàn vốn (CAR): Báo cáo của Moody's cũng khẳng định hệ số CAR của OCB đạt mức rất tốt là 12.2% – vượt xa mức quy định tối thiểu của NHNN (8.0%) và cao hơn mặt bằng chung của các ngân hàng thương mại.
- Tỷ lệ nợ xấu (NPL): Tại ngày 30/09/2026, tỷ lệ nợ xấu theo quy định của NHNN ở mức 2.8%, nằm trong giới hạn kiểm soát cho phép (<3.0%). Tỷ lệ này có sự tăng nhẹ so với cuối quý 2 và cuối năm 2025 (2.3%), phản ánh đúng áp lực chất lượng tài sản chung của toàn ngành. OCB đang kiểm soát chặt chẽ danh mục và kỳ vọng tỷ lệ nợ xấu sẽ giảm trở lại trong 4Q26 nhờ đẩy mạnh thu hồi và xử lý nợ.
- Tỷ lệ vốn ngắn hạn cho vay trung và dài hạn (MTLT): OCB duy trì ở mức 34.9%, tuân thủ an toàn so với trần quy định của NHNN (ngưỡng 40% / 30%).
- Tỷ lệ cấp tín dụng trên huy động (LDR): Đạt mức 70.5%, duy trì khoảng đệm an toàn rất xa so với trần quy định 80% (hoặc trần 85% theo Thông tư mới).
Các chỉ số trên khẳng định bên cạnh mục tiêu phát triển kinh doanh, OCB luôn đặt an toàn hoạt động và thanh khoản lên hàng đầu, tạo nền tảng vững vàng cho sự phát triển của bảng cân đối trong thời gian tới.

> *[Diễn giải từ Slide 11: Moody's xếp hạng OCB ngày 20/09/2026 ở mức Ba3 (Triển vọng Ổn định), BCA mức B1. Hệ số CAR đạt 12.2% (tuân thủ tốt). Tỷ lệ nợ xấu NPL đạt 2.8% (tuân thủ mục tiêu <3.0%). Tỷ lệ vốn ngắn hạn cho vay trung dài hạn (MTLT) đạt 34.9% (tuân thủ quy định). Tỷ lệ LDR đạt 70.5% (dưới trần 80%)]*

Phân tích kết quả kinh doanh và cấu phần P&L 9M26:
- Tổng thu nhập hoạt động (TOI): Đạt 9,219 tỷ VND, tăng trưởng 17.5% YoY so với mức 7,844 tỷ VND cùng kỳ năm trước.
- Thu nhập lãi thuần (NII): Đạt 7,676 tỷ VND, tăng trưởng 13.4% YoY (so với 6,767 tỷ VND trong 9M25), tốc độ tăng trưởng NII cao hơn tốc độ mở rộng của quy mô tín dụng (10.8% YTD). Biên lãi thuần (NIM trượt 4 quý gần nhất) duy trì ổn định ở mức 3.02% trong 3Q26 (so với 3.01% trong 2Q26 và 3.08% tại 4Q25). Điểm này rất đáng ghi nhận vì trong khi mặt bằng chung toàn ngành đang chịu áp lực nén NIM, OCB vẫn bảo vệ và duy trì được biên lãi thuần trên 3.0%.
- Thu nhập ngoài lãi (Non-NII): Đạt 1,543 tỷ VND, tăng trưởng bứt phá 42.9% YoY (so với 1,079 tỷ VND cùng kỳ), chiếm tỷ trọng 16.7% trong cơ cấu TOI:
  + Thu nhập thuần từ phí dịch vụ (NFI): Đạt 856 tỷ VND (+39.6% YoY), trong đó thu từ phí kinh doanh thẻ tăng vọt 57% YoY và tư vấn tài chính tăng 37% YoY.
  + Lãi thuần từ kinh doanh ngoại hối (FX): Đạt 195 tỷ VND (+9.7% YoY / doanh số FX Sales tăng 37% YoY).
  + Lãi thuần từ hoạt động khác (bao gồm thu hồi nợ xấu đã xử lý rủi ro và phí bảo lãnh): Đạt 492 tỷ VND (+70.3% YoY).
  + Hoạt động kinh doanh chứng khoán đầu tư: Ghi nhận mức -21 tỷ VND, cải thiện mạnh so với mức lỗ -206 tỷ VND trong 9M25.
- Quản trị chi phí hoạt động (OPEX): Chi phí hoạt động 9M26 chỉ tăng 4.1% YoY, đạt 3,207 tỷ VND (so với 3,080 tỷ VND cùng kỳ). Do tốc độ tăng doanh thu (+17.5%) vượt xa tốc độ tăng chi phí (+4.1%), tỷ lệ CIR của OCB giảm mạnh 4.5 điểm % YoY xuống mức 34.8% (so với 39.3% cùng kỳ). Đây là chỉ số rất quan trọng giúp OCB đạt điểm đánh giá tối đa trong hệ thống chấm điểm tổ chức tín dụng của NHNN theo Thông tư 21/TT-NHNN.
- Chi phí dự phòng rủi ro tín dụng: Do chất lượng tín dụng thị trường chung biến động và số dư nợ xấu tăng tuyệt đối, OCB đã chủ động trích lập dự phòng thận trọng. Chi phí dự phòng 9M26 ghi nhận 1,888 tỷ VND, tăng 41.4% YoY (so với 1,335 tỷ VND cùng kỳ), nhằm tuân thủ tuyệt đối quy định phân loại nợ và trích lập cho các tài sản có thời gian xử lý quá 2 năm. Đệm dự phòng rủi ro được củng cố với tỷ lệ bao phủ nợ xấu (LLR) nâng lên tiệm cận 60% vào cuối 3Q26.
- Lợi nhuận trước thuế (PBT): Đạt 4,123 tỷ VND, tăng trưởng 20.2% YoY (so với 3,429 tỷ VND trong 9M25).
- Tỷ suất sinh lời: Tỷ suất sinh lời trên vốn chủ sở hữu bình quân (ROAE trượt 12 tháng) đạt 12.8% và tỷ suất sinh lời trên tài sản (ROAA trượt 12 tháng) đạt 1.3%. Ban điều hành kỳ vọng ROAE sẽ tiếp tục cải thiện cao hơn nữa trong 4Q26.

> *[Diễn giải từ Slide 12, 13: Cấu phần PBT Bridge 9M26: TOI đạt 9,219 tỷ VND (+17.5% YoY), gồm NII đạt 7,676 tỷ VND (+13.4% YoY), NFI đạt 856 tỷ VND (+39.6% YoY), FX đạt 195 tỷ VND (+9.7% YoY), Khác đạt 492 tỷ VND (+70.3% YoY), Đầu tư CK đạt -21 tỷ VND. Chi phí OPEX đạt 3,207 tỷ VND (+4.1% YoY). Tỷ lệ CIR đạt 34.8% (-4.5 điểm % YoY). Chi phí dự phòng đạt 1,888 tỷ VND (+41.4% YoY). LNTT đạt 4,123 tỷ VND (+20.2% YoY). NIM TTM đạt 3.02%. ROAE đạt 12.8%, ROAA đạt 1.3%]*

Về đánh giá tiến độ kế hoạch năm FY26 và định hướng điều hành 4Q26:
- Tiến độ kế hoạch năm 2026: Kế hoạch lợi nhuận trước thuế cả năm ĐHĐCĐ giao là 6,960 tỷ VND (+38% so với năm 2025). Kết thúc 9M26, OCB đã hoàn thành 4,123 tỷ VND, tương ứng đạt 59.2% kế hoạch cả năm. Ban điều hành nhận định quý 4 sẽ là một quý đầy thách thức và đòi hỏi toàn hệ thống phải có sự tăng tốc rất lớn để hoàn thành cam kết với Đại hội đồng cổ đông.
- Các định hướng hành động trọng tâm trong 4Q26:
  + Về bảng cân đối: Tiếp tục điều hành tăng trưởng linh hoạt, bám sát hạn mức tín dụng của NHNN; ưu tiên giải ngân cho các phân khúc khách hàng chiến lược, cải thiện chất lượng nợ và nâng cao hiệu quả sinh lời của danh mục tài sản.
  + Về nguồn vốn huy động: Đa dạng hóa nguồn vốn, đẩy mạnh thu hút nguồn vốn giá rẻ như CASA và tiền gửi trực tuyến, đảm bảo thanh khoản và tối ưu hóa chi phí huy động (COF). Bám sát chỉ đạo điều hành giảm lãi suất huy động khoảng 0.5 điểm % của NHNN.
  + Về chất lượng tài sản: Kiên quyết duy trì tỷ lệ nợ xấu dưới 3.0% theo quy định, đẩy mạnh quyết liệt các chiến dịch thu hồi và xử lý nợ có vấn đề.
  + Về kiểm soát chi phí: Giữ vững kỷ luật chi phí nghiêm ngặt, tối ưu hóa năng suất vận hành nhằm duy trì chỉ số CIR ở mức tối ưu.

Toàn thể Ban điều hành OCB cam kết sẽ nỗ lực tối đa để hiện thực hóa các mục tiêu kinh doanh năm 2026 đã được ĐHĐCĐ phê duyệt. Xin trân trọng cảm ơn quý vị."

> *[Diễn giải từ Slide 14: Kế hoạch FY26 vs Thực hiện 9M26: Tổng tài sản đạt 363,726 / 354,214 tỷ VND (đạt 102.7% KH năm); Dư nợ tín dụng M1 đạt 227,183 / 235,875 tỷ VND (đạt 96.3% KH năm); Huy động vốn M1 đạt 226,111 / 251,919 tỷ VND (đạt 89.8% KH năm); Tỷ lệ NPL đạt 2.8% (mục tiêu <3.0%); LNTT đạt 4,123 / 6,960 tỷ VND (đạt 59.2% KH năm). Định hướng 4Q26: Đẩy mạnh kinh doanh cốt lõi, tối ưu chi phí, tăng tốc thu hồi nợ để hoàn thành kế hoạch]*

---

## 04  |  Chiến lược Chuyển đổi Số và Phát triển Ngân hàng AI-Native

**[Mr. Chris Shayan – Managing Director, OCB]**:
"Thank you, and good afternoon, everyone. It is a great pleasure to join our third quarter earnings call today.

Before diving into the detailed presentation slides, I would like to emphasize that we have embarked on a journey of placing Artificial Intelligence (AI) at the very center of everything we do. It is a humble beginning, but in the subsequent slides, I will outline our step-by-step progress and how we are executing this strategy.

At OCB, we recognize that the foundation of any enduring prosperity is trust. In Vietnam, trust is structured and shaped deeply around the concept of family. We understand that the balance sheets of an individual, their family, and their business are deeply interconnected. Our strategic direction is focused on understanding these relationships, building deeper bonds with our customers, and deploying all the technology capabilities at our disposal to deliver compounding value for the individual, the family, and the business.

> *[Diễn giải từ Slide 15, 16, 17: Mr. Chris Shayan – Managing Director trình bày Khối Chuyển đổi số. Tầm nhìn xây dựng ngân hàng AI-Native: 'The bank that knows you and grows with you'. Triết lý 'The Bank for Me, My Family, My Business' – kết nối 3 bảng cân đối tài chính cá nhân, gia đình và doanh nghiệp thành một mối quan hệ duy nhất]*

From a strategic perspective, we approach our AI transformation through three fundamental pillars:

First, democratizing Data and AI for our workforce:
We empower our employees to leverage AI tools in their daily workflows, automating mundane and repetitive tasks. This enables them to reclaim time and focus on higher-value, creative, and meaningful endeavors. To date, we have realized an average time saving of 20 hours per month per user, and our software engineering teams have achieved a 40% reduction in development cycle times through AI-assisted tooling. Across the bank, we have successfully implemented 110 distinct AI use cases spanning 16 operating divisions and centers.

Second, enhancing credit risk appetite and risk quality:
We utilize advanced models to ensure we extend the right credit facilities to the right customers at the appropriate limits, coupled with continuous, dynamic risk monitoring. Crucially, our approach is not confined solely to modern Large Language Models (LLMs). While we actively deploy LLMs, autonomous agents, and multi-agent workflows, we also heavily leverage classic and predictive machine learning models for propensity scoring, predictive analytics, and upsell modeling. Combining these techniques allows OCB to serve customer financing needs prudently and efficiently.

Third, delivering hyper-personalization across digital touchpoints:
Every customer interaction within the OCB OMNI application is becoming increasingly individualized. Depending on the time of day, customer persona, and behavioral patterns, users receive customized in-app messaging, dynamic banners, and tailored product recommendations. All of these creative assets are AI-generated, subject to rigorous human-in-the-loop oversight to ensure full compliance with internal governance and brand regulations. This initiative has driven a remarkable 23% to 25% uplift in click-through rates (CTR) for promotional campaigns.

> *[Diễn giải từ Slide 18: Ba trụ cột chuyển đổi AI: (01) Dân chủ hóa Dữ liệu & AI: tiết kiệm 20 giờ/người dùng/tháng, giảm 40% thời gian phát triển của kỹ sư, triển khai 110 ca sử dụng AI tại 16 khối/trung tâm; (02) Mở rộng khẩu vị tín dụng thận trọng kết hợp ML truyền thống, LLMs và Agentic workflows; (03) Siêu cá nhân hóa (Hyper-personalization) trên OCB OMNI với nội dung do AI tạo có kiểm soát human-in-the-loop, tăng CTR từ 23% đến 25%]*

Turning to our digital performance indicators:
While labeled as digital results, these achievements reflect an enterprise-wide collaboration across Retail Banking, Risk Management, Data, Digital, and Treasury divisions.

Key operating highlights include:
- Digital transaction adoption reached 98% (+112% YoY), and digital onboarding reached 98% (+114% YoY). Average unique user logins per month increased by 19% YoY, and monthly active OMNI users expanded by 17% YoY.
- Retail online deposits: Customers are increasingly conducting deposit and saving transactions online 24/7. Retail online fixed deposit (FD) balances expanded by 40% YoY, and our online FD customer base increased by 35% YoY.
- Pre-approved digital credit model: In our last earnings call, we outlined our transition toward a pre-approved credit underwriting model to maintain strict credit quality control. In 3Q26, this program achieved extraordinary momentum: issuance of MasterCard 2-in-1 cards to our affluent segment expanded by 15 times (15x), and digital card issuance via OMNI surged 63% YoY. Following this success, we expanded the pre-approved credit card program to mass customers during the third quarter.
- FlexFund (Automated Digital Lending): Developed through close inter-departmental collaboration between Data, Risk, and Digital teams, FlexFund enables one-time automated underwriting and instant credit disbursement directly onto any digital device. Launched in August 2026, the product has already disbursed over 2,200 loans, receiving exceptionally positive customer reception. We will progressively expand eligibility to broader qualified customer pools.
- FlexiSavings: Collaboratively engineered by Treasury, Digital, and Retail Banking teams, FlexiSavings is a 100% in-app digital savings proposition. In 3Q26, deposit balances grew by 87% quarter-on-quarter, scale-up surpassed 390 times, and penetration among Affluent and Mass Affluent customer segments exceeded 90%.

I would like to extend my heartfelt congratulations and gratitude to all teams across the bank for their relentless dedication in delivering these strong digital outcomes. Thank you very much."

> *[Diễn giải từ Slide 19, 20, 21: Giao dịch số và mở tài khoản số đạt 98% (+112% và +114% YoY); Active OMNI users +17% YoY. Số dư tiền gửi online bán lẻ +40% YoY. Thẻ tín dụng MasterCard 2-in-1 qua mô hình Pre-approved cho khách hàng Affluent tăng gấp 15 lần trong 3Q26, mở thẻ trên kênh OMNI tăng +63% YoY. Sản phẩm vay số FlexFund giải ngân hơn 2,200 khoản vay từ khi ra mắt tháng 08/2026. Tiền gửi FlexiSavings tăng trưởng 87% QoQ, quy mô tăng >390 lần, thâm nhập >90% phân khúc Affluent & Mass Affluent]*

---

## 05  |  Tầm nhìn Chiến lược Dài hạn và Ba Trọng tâm Thực thi

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin được cảm ơn phần trình bày rất ấn tượng về chiến lược ngân hàng số và AI của Mr. Chris Shayan. Nối tiếp chương trình ngày hôm nay, chúng tôi xin được trân trọng kính mời Ông Dương Đức Hùng – Tổng Giám đốc sẽ quay trở lại để chia sẻ về tầm nhìn chiến lược dài hạn và các trọng tâm thực thi cốt lõi của OCB. Xin trân trọng kính mời anh."

> *[Diễn giải từ Slide 22: Phần 04 - Strategic Vision & Execution Priorities do Mr. Dương Đức Hùng – Chief Executive Officer trình bày]*

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Cảm ơn chị Quỳnh.

Về trọng tâm thực thi trước mắt: Mục tiêu cấp thiết hàng đầu của Ban điều hành và toàn thể cán bộ nhân viên OCB trong giai đoạn này là nỗ lực hết sức để hiện thực hóa chỉ tiêu kế hoạch kinh doanh năm 2026 do ĐHĐCĐ giao phó – cụ thể là mục tiêu lợi nhuận trước thuế (PBT) 6,960 tỷ VND như anh Long vừa trình bày.

Về định hướng chiến lược dài hạn:
OCB kiên định và nhất quán với tầm nhìn chiến lược trở thành Top 5 ngân hàng thương mại cổ phần tư nhân hàng đầu tại Việt Nam về:
- Hiệu quả sinh lời trên vốn chủ sở hữu (ROE);
- Năng lực số hóa và ứng dụng công nghệ AI;
- Cam kết thực thi chuẩn mực ESG và phát triển bền vững.

Để hiện thực hóa tầm nhìn trên, OCB tiếp tục theo đuổi các sáng kiến chiến lược cốt lõi tại ba mảng kinh doanh: Khối Khách hàng Cá nhân (Retail Banking), Khối Doanh nghiệp vừa và nhỏ (SMEs), và Khối Ngân hàng Giao dịch (Transaction Banking). Toàn bộ các sáng kiến này được xây dựng vững chắc trên 4 trụ cột nền tảng:
1. Con người (People)
2. Năng lực Quản trị Rủi ro (Risk Management)
3. Văn hóa tổ chức OCB (Culture)
4. Năng lực Số hóa và Trí tuệ Nhân tạo (AI & Digital Capabilities)

> *[Diễn giải từ Slide 22: Tầm nhìn OCB: Top 5 NHTMCP tư nhân về ROE, Năng lực số, và ESG. Sáng kiến chiến lược: Retail banking, SMEs, Transaction banking. 4 trụ cột nền tảng: Con người, Quản trị rủi ro, Văn hóa OCB, Năng lực AI & Số hóa]*

Về nền tảng vững chắc cho giai đoạn phát triển tiếp theo:
OCB hiện đang sở hữu một bệ phóng kinh doanh vững mạnh và có khả năng mở rộng quy mô (scalable):
- Cơ sở khách hàng quy mô lớn với hơn 5 triệu khách hàng tin tưởng sử dụng dịch vụ;
- Tiềm lực tài chính vững chắc với tổng tài sản đạt 363,726 tỷ VND, vốn chủ sở hữu đạt 37,000 tỷ VND;
- Mạng lưới vật lý gồm 176 điểm giao dịch và chi nhánh trên toàn quốc, kết hợp cùng hệ sinh thái đối tác ngày càng mở rộng trong các lĩnh vực kinh tế trọng yếu.
- Năng lực chuyển đổi số và phát triển ngân hàng số AI-Native Bank: Như anh Chris Shayan vừa chia sẻ, ngân hàng đang từng bước hoàn thiện mô hình AI-Native Bank nhằm thấu hiểu khách hàng sâu sắc hơn, đưa ra các gói giải pháp may đo kịp thời hơn, nâng cao trải nghiệm khách hàng ở quy mô lớn với hiệu quả chi phí tối ưu.
- Cam kết ESG và phát triển bền vững: Đây là cam kết mang tính chiến lược dài hạn của OCB, tạo tiền đề vững vàng cho mảng tài trợ tín dụng xanh nhằm đồng hành cùng cộng đồng doanh nghiệp trong hành trình chuyển đổi xanh.
- Động lực phục hồi kinh doanh rõ nét: Tốc độ tăng trưởng lợi nhuận 9M26 đạt 20.2%, biên thu nhập từ lãi và ngoài lãi cải thiện mạnh, hệ số CIR tối ưu sâu... tạo tiền đề vững chắc cho sự bứt phá của OCB trong những năm tới.

> *[Diễn giải từ Slide 23: Nền tảng phát triển OCB: Nền tảng kinh doanh vững chắc, quy mô lớn (>5 triệu khách hàng, 364 nghìn tỷ tổng tài sản, 37 nghìn tỷ VCSH, 176 điểm giao dịch); Mô hình vận hành tiên phong số hóa AI-Native; Năng lực ESG và phát triển bền vững; Quản trị rủi ro kỷ luật; Động lực phục hồi lợi nhuận rõ nét]*

Về 3 trọng tâm thực thi hành động (Key Execution Priorities):
Để hiện thực hóa các mục tiêu chiến lược, OCB tập trung vào ba trọng tâm hành động cụ thể sau:

1. Tăng cường gắn kết và mở rộng hệ sinh thái khách hàng:
OCB chuyển dịch mạnh mẽ từ mô hình bán sản phẩm ngân hàng đơn lẻ sang cung cấp giải pháp tài chính toàn diện. Chúng tôi nâng cao vai trò tư vấn tài chính chuyên sâu của OCB, đẩy mạnh mảng Ngân hàng Giao dịch (Transaction Banking) thông qua các gói giải pháp may đo riêng cho từng phân khúc. Song song đó, ngân hàng không ngừng mở rộng hệ sinh thái liên kết đối tác nhằm đào sâu mối quan hệ khách hàng và gia tăng tối đa giá trị vòng đời khách hàng (Customer Lifetime Value).

2. Kiện toàn năng lực quản trị rủi ro toàn diện:
OCB chủ động đẩy nhanh tiến độ triển khai chuẩn mực Basel III và áp dụng Thông tư 14/2025/TT-NHNN trước thời hạn bắt buộc của NHNN. Ngân hàng nâng cấp hệ thống mô hình cảnh báo sớm (Early Warning System - EWS) để nhận diện rủi ro tín dụng từ sớm, chủ động tái cấu trúc danh mục và gắn chặt quản trị rủi ro với hoạt động kinh doanh hàng ngày. Mục tiêu là đảm bảo tăng trưởng tín dụng có chọn lọc, bảo toàn chất lượng tài sản và duy trì kỷ luật kinh doanh nghiêm ngặt.

3. Củng cố và nhúng sâu năng lực AI và Dữ liệu:
Đưa dữ liệu và trí tuệ nhân tạo vào sâu trong quy trình ra quyết định ở mọi cấp độ quản trị, đồng thời tích hợp toàn diện công nghệ vào toàn bộ hành trình trải nghiệm của khách hàng. Mục tiêu cốt lõi không chỉ dừng ở ứng dụng công nghệ, mà là chuyển hóa các khoản đầu tư công nghệ thành giá trị gia tăng thiết thực và trải nghiệm vượt trội cho khách hàng, đồng thời mang lại năng suất lao động cao hơn và hiệu quả chi phí vượt trội cho toàn tổ chức OCB.

Đó là toàn bộ định hướng chiến lược dài hạn và các trọng tâm hành động trước mắt mà Ban lãnh đạo muốn truyền tải tới quý vị ngày hôm nay. Xin trân trọng cảm ơn các anh chị."

> *[Diễn giải từ Slide 24: Ba ưu tiên thực thi chiến lược: (01) Tăng cường & mở rộng hệ sinh thái khách hàng (giải pháp toàn diện, tư vấn sâu, transaction banking, gia tăng giá trị vòng đời khách hàng); (02) Kiện toàn năng lực quản trị rủi ro (áp dụng sớm Basel III và Thông tư 14/2025/TT-NHNN, mô hình cảnh báo sớm EWS, quản trị danh mục chủ động); (03) Củng cố năng lực Số & AI (áp dụng dữ liệu/AI vào ra quyết định, nhúng AI vào hành trình khách hàng, mở rộng hệ sinh thái số)]*

---

## 06  |  Phiên Thảo luận và Hỏi đáp Toàn diện (Q&A Session)

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin được cảm ơn anh Hùng. Thưa quý vị, phần đầu của chương trình công bố kết quả kinh doanh 9M26 của OCB xin được phép khép lại. Sau đây chúng ta sẽ bước ngay vào Phần thứ hai: Phiên thảo luận và trả lời câu hỏi (Q&A Session).

Chúng tôi xin mở đầu với câu hỏi thứ nhất: Ban lãnh đạo đánh giá mặt bằng lãi suất và diễn biến tỷ giá trong những tháng cuối năm 2026 và năm 2027 như thế nào; những biến động này có ảnh hưởng ra sao đến nhu cầu tín dụng, chi phí vốn, NIM, hoạt động ngoại hối và chất lượng tài sản của OCB? Xin trân trọng kính mời anh Hùng."

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Về mặt bằng lãi suất và tỷ giá những tháng cuối năm 2026, chúng tôi dự báo sẽ tiếp tục xoay quanh mặt bằng hiện tại. Sang năm 2027, thị trường sẽ chịu sự tác động từ các yếu tố bên ngoài như áp lực lạm phát toàn cầu và xu hướng lãi suất điều hành của các ngân hàng trung ương lớn. Những yếu tố này có thể tạo áp lực lên mặt bằng lãi suất và tỷ giá trong nước, từ đó ảnh hưởng đến NIM và chất lượng tài sản của toàn ngành.

Trong bối cảnh đó, OCB chủ động cơ cấu nguồn vốn một cách linh hoạt để bảo vệ NIM ổn định. Đồng thời, nhận thấy nhu cầu tín dụng trong nước vẫn duy trì ở mức cao, OCB chủ trương tăng trưởng tín dụng có chọn lọc, cung cấp vốn cho những khách hàng có chất lượng tín dụng tốt, phù hợp với khẩu vị rủi ro. Mặt khác, biến động tỷ giá cũng mở ra cơ hội kinh doanh ngoại tệ và các sản phẩm phòng ngừa rủi ro tỷ giá cho tệp khách hàng xuất nhập khẩu của ngân hàng."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Hùng. Câu hỏi số hai xin được dành cho anh Chris Shayan: Số lượng khách hàng hoàn tất quy trình số hóa onboarding tăng mạnh trong năm 2026; vậy bao nhiêu phần trăm trong số này đã trở thành khách hàng hoạt động (active customers) tạo doanh thu cho ngân hàng, và OCB kỳ vọng sẽ tiếp tục cải thiện tỷ lệ chuyển đổi này như thế nào? Mr. Chris, please."

**[Mr. Chris Shayan – Managing Director, OCB]**:
"Thank you. More than 40% of our customers acquired online have become active customers with us. Among them, 30% of these customers are affluent and mass affluent individuals who have passed the threshold of holding three or more products, with the broader mass segment progressively approaching that threshold.

As we continue onboarding more customers, we have instituted an AI-enabled program covering the first 90 days post-onboarding. During these critical 90 days, we leverage automated intelligence to guide customers toward relevant banking products and services, ensuring we deliver exactly what they need while accurately identifying their customer segment. This continuous engagement systematically uplifts our product holding ratio across our rapidly expanding customer franchise."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn Mr. Chris. Câu hỏi tiếp theo được gửi đến từ VCBF, PVSC, Horizon Capital và Arisco: Ban lãnh đạo vui lòng đánh giá khả năng hoàn thành kế hoạch lợi nhuận của OCB trong năm 2026 như thế nào; các động lực và rủi ro chính trong quý 4 là gì; và OCB có thể chia sẻ định hướng sơ bộ cho năm 2027 được không? Xin kính mời anh Hùng."

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Như đã chia sẻ, sau 9M26, lợi nhuận trước thuế của OCB tăng trưởng 20.2% YoY, đạt 4,123 tỷ VND, tương đương khoảng 60% kế hoạch cả năm (59.2%). Nhìn chung, bối cảnh kinh doanh năm 2026 chứa đựng nhiều thách thức: thị trường bất động sản phục hồi chậm hơn dự kiến ban đầu, mặt bằng lãi suất neo cao hơn cùng kỳ tạo trở lực cho công tác thu hồi và xử lý nợ.

Tuy nhiên, OCB đã đạt được những cải thiện rõ nét về hiệu quả kinh doanh cốt lõi: doanh thu tăng trưởng vững, tỷ lệ CIR tối ưu sâu, quy mô tài sản và dư nợ cho vay mở rộng an toàn. Vì vậy, Ban điều hành kiên định với mục tiêu hoàn thành chỉ tiêu LNTT 6,960 tỷ VND được ĐHĐCĐ giao. Quý 4 này là giai đoạn chạy nước rút toàn lực: đẩy mạnh các mảng kinh doanh cốt lõi, bảo vệ biên lợi nhuận, giữ vững kỷ luật chi phí và đôn đốc quyết liệt các hoạt động thu hồi, xử lý nợ xấu ngoại bảng. Về định hướng sơ bộ năm 2027, hiện ngân hàng đang hoàn thiện số liệu chi tiết để trình HĐQT; phương châm xuyên suốt vẫn là tăng trưởng có chọn lọc, tập trung vào phân khúc mục tiêu và kiểm soát chặt chẽ chất lượng tài sản."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Hùng. Câu hỏi tiếp theo đến từ MBIS, FPTS và VIS Rating: So với quý 2, vì sao tăng trưởng tín dụng giảm tốc mạnh trong quý 3; và động lực chính thúc đẩy tăng trưởng tín dụng của OCB trong 9M26 là gì? Xin kính mời anh Long."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Trong quý 2, OCB đã chủ động đẩy mạnh tốc độ tăng trưởng tín dụng theo định hướng điều hành của NHNN nhằm sớm hiện thực hóa thu nhập lãi thuần (NII) ngay từ những tháng đầu năm. Nhờ danh mục tín dụng quý 2 tăng trưởng sớm, NII của OCB trong 9M26 đã đạt mức tăng trưởng 13.4% YoY, cao hơn tốc độ tăng trưởng dư nợ 10.8% YTD. Bước sang quý 3, quy mô dư nợ nhìn chung đi ngang so với quý 2 để đảm bảo tuân thủ chặt chẽ hạn mức tín dụng được phân bổ.

Về cấu trúc tăng trưởng, dư nợ tài trợ sản xuất kinh doanh của khối Khách hàng Doanh nghiệp tăng 13.0% YTD, cao hơn mặt bằng chung. Đối với khối Khách hàng Cá nhân, chúng tôi tập trung giải ngân vào phân khúc ưu tiên Affluent và Mass Affluent, đẩy mạnh cho vay mua nhà dự án, cho vay tiêu dùng có TSBĐ và dòng sản phẩm số FlexFund, đồng thời tích cực thu hồi nợ xấu. Nhờ đó, cấu trúc danh mục tín dụng đã chuyển dịch tích cực hơn theo hướng tối ưu hóa biên lợi suất."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Long. Tiếp theo là câu hỏi từ FPTS, SHS và VIS Rating: Liệu OCB có thể hoàn thành mục tiêu tăng trưởng tín dụng năm 2026 hay không; phân khúc khách hàng và ngành kinh tế nào sẽ dẫn dắt tăng trưởng tín dụng của OCB trong quý 4 và năm 2027; và OCB sẽ cân bằng giữa doanh nghiệp SME và bán lẻ như thế nào? Xin kính mời anh Hùng."

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"OCB luôn điều hành tăng trưởng tín dụng bám sát định hướng của NHNN và trong phạm vi hạn mức được giao để đảm bảo tăng trưởng an toàn và bền vững. Trong quý 4 năm nay, ngân hàng tiếp tục tăng trưởng tín dụng thận trọng, có chọn lọc, ưu tiên những khách hàng có chất lượng tín dụng tốt trong tệp hiện hữu, phù hợp khẩu vị rủi ro, đồng thời ưu tiên lĩnh vực sản xuất kinh doanh và gói tín dụng nhà ở xã hội theo Nghị quyết 33.

Bước sang năm 2027, OCB tiếp tục tối ưu hóa hạn mức tín dụng được cấp, mở rộng cho vay các khách hàng có lịch sử hợp tác lâu dài. Đối với mảng bán lẻ, chúng tôi tập trung vào phân khúc bất động sản tiêu dùng phục vụ nhu cầu mua nhà để ở của nhóm khách hàng có thu nhập ổn định từ lương. Tổng thể, ngân hàng cân đối tăng trưởng đồng đều trên ba mảng: Sản xuất kinh doanh, Khối SME và Khối Bán lẻ nhằm đảm bảo an toàn tuyệt đối cho bảng cân đối."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Hùng. Tiếp theo là câu hỏi từ TCBS, TPS, DVSG, OCBS, SHS và VIS Rating dành cho anh Long: Nguyên nhân lợi suất cho vay (Yield) và NIM quý 3 của OCB cải thiện là gì; OCB có ghi nhận lãi treo thu hồi hoặc khoản thu lãi không thường xuyên nào không; và triển vọng NIM trong quý 4 cũng như năm 2027 ra sao trong bối cảnh cạnh tranh lãi suất huy động và định hướng giảm lãi suất cho vay? Xin kính mời anh Long."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Động lực chính giúp lợi suất cho vay và NIM của OCB cải thiện trong quý 3 là việc tái cơ cấu danh mục tài sản sinh lời. Trong bối cảnh hạn mức tín dụng được kiểm soát chặt chẽ, chúng tôi tập trung nguồn vốn cấp tín dụng trung và dài hạn cho các khách hàng có phương án kinh doanh khả thi với biên lợi suất tốt hơn. Ngoài ra, NIM được hỗ trợ thêm từ các khoản thu bảo lãnh và kinh doanh tín dụng ổn định. Về câu hỏi lãi treo: OCB không ghi nhận bất kỳ khoản lãi treo thu hồi hay thu nhập lãi bất thường nào; tỷ lệ lãi dồn tích trên bảng cân đối của ngân hàng được duy trì ở mức rất thấp theo đúng chuẩn mực thận trọng.

Về triển vọng NIM quý 4: Thực hiện chỉ đạo của Thống đốc NHNN, chúng tôi dự kiến điều chỉnh giảm khoảng 0.5 điểm phần trăm lãi suất huy động trong quý 4 để tạo dư địa hỗ trợ giảm lãi suất cho vay cho các lĩnh vực sản xuất kinh doanh ưu tiên. NIM quý 4 có thể chịu áp lực thu hẹp nhẹ nhưng OCB tự tin sẽ kiểm soát vững chắc trên ngưỡng 3.0%. Sang năm 2027, dù đối mặt áp lực giảm lãi suất cho vay hỗ trợ nền kinh tế, OCB vẫn sẽ duy trì NIM ổn định trên 3.0% nhờ tối ưu hóa cơ cấu danh mục, đa dạng hóa nguồn vốn giá rẻ và mở rộng nghiệp vụ bảo lãnh."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Long. Tiếp tục một câu hỏi dành cho anh: Tăng trưởng tiền gửi khách hàng giảm tốc trong quý 3 dù tỷ lệ LDR vẫn cải thiện so với quý trước; OCB có gặp khó khăn gì trong huy động thị trường 1 hay không và ngân hàng có kế hoạch đẩy mạnh huy động thị trường 1 trong quý 4 không? Xin kính mời anh."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Trong quý 3, tốc độ tăng trưởng huy động của OCB không cao do ngân hàng chủ động điều hành huy động bám sát định hướng của NHNN về kiểm soát và hạ nhiệt mặt bằng lãi suất đầu vào. Chúng tôi không tham gia cuộc đua cạnh tranh lãi suất cao để tránh tạo áp lực lên chi phí vốn và thanh khoản thị trường, qua đó tạo dư địa giảm lãi suất cho vay.

Đồng thời, OCB tận dụng hiệu quả nguồn vốn liên ngân hàng có chi phí thấp trong hạn mức và khẩu vị rủi ro nghiêm ngặt do Ủy ban ALCO kiểm soát. Về phía khách hàng, chúng tôi ghi nhận sự chuyển dịch tích cực từ tiền gửi truyền thống ngắn hạn sang các giải pháp tiết kiệm số linh hoạt như FlexiSavings và chứng chỉ tiền gửi. Điều này giúp OCB duy trì cấu trúc nguồn vốn linh hoạt, giảm thiểu chi phí huy động và bảo vệ biên lãi thuần. Trong quý 4, OCB tiếp tục đa dạng hóa kênh huy động và tối ưu hóa chi phí vốn trên thị trường 1, kết hợp thanh khoản liên ngân hàng để giữ vững thanh khoản và an toàn hoạt động."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Long. Câu hỏi tiếp theo xin dành cho anh Chris Shayan: Đến nay, các chương trình chuyển đổi số và AI của OCB đã mang lại những khoản tiết kiệm chi phí và cải thiện năng suất có thể đo lường cụ thể nào? Xin kính mời anh."

**[Mr. Chris Shayan – Managing Director, OCB]**:
"Thank you. At OCB, the ultimate metric we track for our digital and AI transformation is the Cost-to-Income Ratio (CIR). We view our employees as our greatest talent and core engine of growth. Therefore, we have empowered our entire workforce with AI capabilities integrated into the Microsoft ecosystem. For employees handling complex workflows, we have deployed advanced AI models such as Claude Code to enhance their day-to-day output. As shared earlier, this has unlocked nearly 2,000 hours of cumulative time savings per month, with 77% of routine tasks enhanced or automated.

For our software engineering and technology teams, the deployment of specialized AI development tools like Kiro and Claude Code has dramatically shortened delivery cycles. A clear indicator of this acceleration is our deployment cadence: we now achieve four to five production releases per month across our app stores, customer journeys, and internal employee portals. This rapid iteration has driven substantial digital engagement and underpinned the surge in our online deposit ratios. Moving forward, we are advancing two large-scale machine learning initiatives: an end-to-end automated credit underwriting engine, and an intelligent debt collection system designed to elevate asset recovery while boosting frontline sales productivity."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn Mr. Chris. Câu hỏi tiếp theo từ TCBS và BVSC dành cho anh Long: Vì sao chi phí dự phòng tín dụng 9M26 tăng khoảng 41% YoY; trong quý 4 và năm 2027, OCB kỳ vọng chi phí tín dụng, tỷ lệ bao phủ nợ xấu, nguồn thu từ xử lý nợ và chi phí dự phòng sẽ diễn biến như thế nào; ngân hàng sẽ triển khai giải pháp gì để đẩy nhanh công tác thu hồi nợ trong quý 4? Xin kính mời anh."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Như đã báo cáo, chi phí dự phòng 9M26 tăng 41.4% YoY lên 1,888 tỷ VND. Trước hết, tỷ lệ nợ xấu NPL của OCB tại ngày 30/09/2026 là 2.81%, tiếp tục được kiểm soát dưới trần 3.0% theo quy định của NHNN. Về giá trị tuyệt đối, nợ xấu nội bảng ghi nhận 8,700 tỷ VND, tăng nhẹ so với đầu năm phản ánh khó khăn chung của thị trường bất động sản và sự phục hồi dòng tiền không đồng đều giữa các nhóm ngành. Tuy nhiên, tốc độ tăng dòng nợ xấu của OCB chỉ ở mức 29%, thấp hơn nhiều so với tốc độ tăng nợ xấu bình quân của các ngân hàng đối thủ.

Trong số 1,888 tỷ VND chi phí dự phòng trích lập trong 9M26, OCB đã chủ động trích lập 100% giá trị không tính trừ tài sản bảo đảm đối với toàn bộ các khoản nợ có thời gian xử lý quá 2 năm theo đúng quy định phân loại nợ của NHNN. Đây chính là khoản 'lương khô' dự phòng vững chắc cho tương lai. Nhờ đó, tỷ lệ bao phủ nợ xấu (LLR) đã được nâng lên tiệm cận 60% vào cuối quý 3. Trong quý 4, OCB tiếp tục tăng cường quyết liệt công tác thu nợ; nếu cần thiết, ngân hàng sẽ trích lập bổ sung ít nhất 400 đến 500 tỷ VND để duy trì tỷ lệ bao phủ nợ xấu quanh mức 60%. Định hướng năm 2027, OCB sẽ duy trì chính sách trích lập dự phòng thận trọng để củng cố sức chống chịu trước mọi biến động thị trường."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Long. Tiếp theo là câu hỏi: Điều gì thúc đẩy thu nhập phí thuần 9M26 tăng 39.6% YoY (riêng quý 3 tăng 62.3% YoY); OCB có kế hoạch mở rộng mảng quản lý tài sản, bảo hiểm hay tư vấn để gia tăng nguồn thu phí hay không? Xin kính mời anh Long."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"Tăng trưởng thu nhập phí và thu ngoài lãi là kết quả của chiến lược chuyển dịch bền bỉ từ năm 2025 nhằm đa dạng hóa cơ cấu nguồn thu. Động lực chính đến từ: nghiệp vụ thẻ tăng trưởng 57%, phí tư vấn tăng 37%, kinh doanh ngoại hối tăng 37% và các khoản thu hồi từ nợ đã xử lý rủi ro. Riêng mảng bảo hiểm (Bancassurance) có sự chững lại do tác động chung từ Thông tư 67/TT-BTC siết chặt quy định bán chéo. Trước bối cảnh đó, OCB đã chủ động dịch chuyển sang các sản phẩm bảo hiểm phi nhân thọ và bảo hiểm sức khỏe (hợp tác với OPES...), đồng thời tái cấu trúc quy trình phân phối bảo hiểm nhân thọ theo mô hình tư vấn chuyên biệt để tạo đà tăng trưởng trở lại trong quý 4 và năm 2027."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Long. Xin kính mời anh Hùng chia sẻ thêm: Ban lãnh đạo đánh giá thế nào về tính bền vững của tăng trưởng thu nhập phí trong quý 4 và năm 2027; những mảng nào sẽ là động lực chính của OCB?"

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Chúng tôi hoàn toàn tin tưởng vào tính bền vững của thu nhập ngoài lãi trong năm 2027. Nền tảng vững chắc ở đây là cơ cấu thu phí của OCB hiện nay xuất phát từ các giao dịch thường xuyên của tệp khách hàng gắn bó lâu năm, chứ không còn phụ thuộc vào các khoản phí mang tính thời điểm (one-off).

Có ba động lực tăng trưởng thu phí chủ lực:
1. Ngân hàng Giao dịch và Quản lý dòng tiền (Transaction Banking & Cash Management);
2. Tài trợ thương mại và Tài trợ chuỗi cung ứng (Supply Chain Finance);
3. Dịch vụ thanh toán, thẻ, ngoại hối và tư vấn tài chính.
OCB tập trung xây dựng hệ sinh thái kết nối các tập đoàn, doanh nghiệp lớn hạt nhân với các nhà cung cấp, đối tác, cán bộ nhân viên và khách hàng cá nhân. Ngân hàng giao dịch đóng vai trò huyết mạch luân chuyển dòng tiền trong toàn bộ hệ sinh thái này, tạo ra nguồn thu phí dịch vụ ổn định và bền vững cho OCB."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Hùng. Câu hỏi tiếp theo dành cho anh Chris Shayan: Trong chiến lược trở thành ngân hàng AI-Native, OCB ưu tiên những lĩnh vực nào để tạo ra tác động rõ nhất lên trải nghiệm khách hàng, năng suất và hiệu quả tài chính; khi nào nhà đầu tư có thể nhìn thấy những đóng góp cụ thể đo lường bằng doanh thu và chi phí? Mr. Chris, please."

**[Mr. Chris Shayan – Managing Director, OCB]**:
"Thank you. I would like to reiterate that 'AI-Native' is a profound and ambitious concept, and we approach it with deep humility. We are in the active process of becoming AI-native, which means we focus rigorously on tangible quick wins where AI directly moves the needle. Our initial focus has centered on workforce productivity, digital marketing optimization, intelligent copywriting, and dynamic customer communication across our web and mobile applications.

The next phase of our journey is leveraging the vast data footprint we generate. Every dynamic banner, personalized message, and in-app interaction generates behavioral data, enabling us to continuously refine our product recommendations and offerings. Simultaneously, as a regulated bank, disciplined risk management remains paramount. We are deploying machine learning models to strengthen our credit underwriting and portfolio monitoring. A prime example is FlexFund, where risk management and digital teams collaborated to deliver instant, automated credit decisions while keeping the bank thoroughly safeguarded. We look forward to presenting further quantified impacts in our upcoming earnings calls. Thank you."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn Mr. Chris. Câu hỏi tiếp theo dành cho CEO Dương Đức Hùng: Ban lãnh đạo đánh giá Thông tư 50/2026/TT-NHNN sẽ ảnh hưởng thế nào đến cơ cấu tài sản, nguồn vốn, thanh khoản, chi phí vốn và tăng trưởng tín dụng năm 2027 của OCB; tình trạng đáp ứng và kế hoạch áp dụng Thông tư 50 tại ngân hàng ra sao? Xin kính mời anh."

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Thông tư 50/2026/TT-NHNN đặt ra những chuẩn mực rất cao về quản trị thanh khoản theo thông lệ Basel III và quy trình đánh giá an toàn thanh khoản nội bộ (ILAAP). Những quy chuẩn này đòi hỏi các ngân hàng phải liên tục nâng cấp hệ thống và văn hóa quản trị rủi ro.

Thuận lợi lớn của OCB là chúng tôi đã chủ động triển khai Basel III và ILAAP từ rất sớm, ngay từ năm 2022. Do đó, khi Thông tư 50 được ban hành, OCB đã hoàn toàn sẵn sàng đáp ứng toàn bộ các chỉ tiêu quy định với biên độ an toàn cao:
- Tỷ lệ nguồn vốn ổn định ròng (NSFR): Quy định yêu cầu đạt từ 90% trở lên đến năm 2028; OCB hiện đã đáp ứng vượt mức này.
- Tỷ lệ đảm bảo khả năng thanh khoản (LCR): Yêu cầu từ 50% trở lên; OCB duy trì ở biên độ rất an toàn.
- Tỷ lệ cấp tín dụng trên huy động (LDR chuẩn mới): Yêu cầu nhỏ hơn hoặc bằng 95%; OCB hiện kiểm soát ở mức 70.5%.
Nhìn chung, Thông tư 50 không tạo ra áp lực tiêu cực lên chi phí vốn hay bảng cân đối của OCB, mà trái lại còn củng cố vị thế an toàn thanh khoản vững chắc của ngân hàng trên thị trường."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin cảm ơn anh Hùng. Do thời lượng chương trình có hạn, chúng tôi xin chuyển đến câu hỏi cuối cùng dành cho anh Long: OCB có kế hoạch tăng vốn chủ sở hữu trong năm 2027 không; các phương án nào đang được xem xét và sẽ ảnh hưởng thế nào đến CAR, năng lực tăng trưởng và chỉ tiêu ROE? Xin kính mời anh."

**[Ông Quách Thành Long – Giám đốc Trung tâm Quản lý Tài chính OCB]**:
"OCB sở hữu nền tảng vốn tự có vững mạnh và luôn chủ động xây dựng kế hoạch tăng vốn định kỳ phù hợp với nhu cầu mở rộng quy mô. Trong năm 2026, ngân hàng đã hoàn thành kế hoạch tăng vốn được ĐHĐCĐ phê duyệt, nâng vốn điều lệ lên trên 30,000 tỷ VND, đưa hệ số an toàn vốn CAR tại ngày 30/09/2026 đạt 12.2% – cao hơn rất nhiều so với ngưỡng quy định tối thiểu (8.0%). Nền tảng vốn hiện tại tạo dư địa dồi dào để OCB tiếp tục tăng trưởng tài sản có trọng số rủi ro (RWA), củng cố bộ đệm rủi ro và đầu tư cho các năng lực số hóa chiến lược.

Đối với năm 2027, OCB đang đánh giá toàn diện nhu cầu vốn trong kế hoạch kinh doanh trung hạn. Các phương án cụ thể đang được xây dựng để trình Hội đồng Quản trị xem xét, đảm bảo hài hòa giữa yêu cầu an toàn vốn CAR và mục tiêu trọng tâm là cải thiện tỷ suất sinh lời ROAE, tránh pha loãng giá trị cổ phiếu. Kế hoạch tăng vốn năm 2027 chi tiết sẽ được công bố chính thức sau khi HĐQT phê duyệt và dự kiến sẽ trình Đại hội đồng cổ đông trong cuộc họp thường niên vào quý 1 năm 2027. Xin trân trọng cảm ơn quý vị."

---

## 07  |  Bế mạc Hội nghị Trình bày Kết quả Kinh doanh 9M26

**[Ông Dương Đức Hùng – Tổng Giám đốc OCB]**:
"Trước hết, thay mặt Ban điều hành OCB, tôi xin chân thành cảm ơn tất cả các anh chị chuyên viên phân tích, các quỹ đầu tư và quý nhà đầu tư đã dành thời gian theo dõi buổi cập nhật hôm nay. OCB đã đạt được những kết quả phục hồi rất tích cực trong 9M26. Thời gian tới, chúng tôi tiếp tục kiên định với chiến lược: đẩy mạnh chuyển đổi số và phát triển ngân hàng AI-Native, kiện toàn năng lực quản trị rủi ro chuẩn quốc tế, và tăng tốc các sáng kiến kinh doanh cốt lõi trong mảng SME, Bán lẻ và Ngân hàng Giao dịch. Mục tiêu tối thượng là mang lại giá trị bền vững lâu dài cho khách hàng, cổ đông và cộng đồng. Xin trân trọng cảm ơn."

**[Bà Thúy Quỳnh – Host / Bộ phận Quan hệ Nhà đầu tư]**:
"Xin được trân trọng cảm ơn phần chia sẻ của Ông Dương Đức Hùng và toàn thể Ban lãnh đạo OCB. Những câu hỏi chưa kịp giải đáp trực tiếp tại hội nghị, Bộ phận Quan hệ Nhà đầu tư (IR) của OCB sẽ tổng hợp và phản hồi chi tiết qua email. Kính chúc quý vị thật nhiều sức khỏe, hạnh phúc và thành công. Xin kính chào và hẹn gặp lại trong các sự kiện tiếp theo!"
"""

def main():
    out_dir = PROJECT_ROOT / "workspace/Bank/OCB/output"
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / "full_transcript.md"
    docx_path = out_dir / "full_transcript.docx"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(TRANSCRIPT_MD.strip() + "\n")
    print(f"[✓] Đã tạo file Markdown Transcript: {md_path} ({len(TRANSCRIPT_MD)} bytes)")

    from scripts.document_formatter import DocumentFormatter
    DocumentFormatter.markdown_to_transcript_docx(str(md_path), str(docx_path))
    print(f"[✓] Đã biên dịch file DOCX Corporate Transcript: {docx_path} ({docx_path.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    main()
