# -*- coding: utf-8 -*-
"""
Build standardized analyst_report.md and analyst_report.docx for BIDV (BID)
strictly adhering to the MSB Benchmark and AGENTS.md rules.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

REPORT_MD = """[Institutional Research] - Analyst Meeting BID (3Q26 và 9T26): Cập nhật hội nghị Nhà đầu tư

PHẦN I: Kết quả Hoạt động Kinh doanh 3Q26 và 9T26

1. Thu nhập Hoạt động (TOI), Thu nhập Lãi thuần (NII) & Thu nhập Ngoài lãi (NOII)

- Tổng thu nhập hoạt động (TOI): 67,541 tỷ VND trong 9T26 (+10.5% YoY, 3Q26 đạt 23,206 tỷ VND, +9.7% YoY), động lực cốt lõi đến từ mức tăng trưởng ổn định của thu nhập lãi thuần và hoạt động thu hồi nợ ngoại bảng.
- Thu nhập lãi thuần (NII): 50,594 tỷ VND trong 9T26 (+14.7% YoY, 3Q26 đạt 17,056 tỷ VND, +12.4% YoY), đóng góp 74.9% tổng thu nhập hoạt động nhờ quy mô tín dụng mở rộng và tối ưu hóa danh mục tài sản sinh lời trung dài hạn.
- Thu nhập ngoài lãi (NOII): 16,947 tỷ VND trong 9T26 (-0.5% YoY, 3Q26 đạt 6,150 tỷ VND, +2.8% YoY), phản ánh sự phân hóa mạnh giữa các cấu phần nghiệp vụ:
  * Thu nhập thuần từ phí dịch vụ (NFI): 5,442 tỷ VND (+5.5% YoY, 3Q26 đạt 1,858 tỷ VND, +7.2% YoY), dẫn dắt bởi nghiệp vụ Thanh toán & Tài trợ thương mại đạt 2,576 tỷ VND (+14.9% YoY); phí ngân hàng số chuyển từ lỗ -6.5 tỷ VND lên lãi 82.9 tỷ VND.
  * Thu nhập từ kinh doanh ngoại hối (FX): 2,955 tỷ VND (-7.2% YoY, riêng 3Q26 phục hồi đạt 1,139 tỷ VND, +18.0% YoY), do chênh lệch tỷ giá trung tâm và tỷ giá giao dịch thương mại bị thu hẹp đáng kể.
  * Thu nhập khác và thu hồi nợ: 7,789 tỷ VND (+16.8% YoY), nhờ tiến độ thu hồi nợ đã xử lý rủi ro đạt 8,266 tỷ VND (+14.1% YoY).
  * Lãi thuần từ chứng khoán kinh doanh và đầu tư: 231 tỷ VND (-86.0% YoY), chịu ảnh hưởng từ môi trường lợi suất trái phiếu biến động khiến quy mô chốt lời suy giảm.

2. Chi phí vốn (COF) và Biên lãi thuần (NIM)

- Chi phí vốn (COF): Chịu áp lực tăng nhẹ trong nửa đầu năm do cạnh tranh huy động tiền gửi dân cư trên thị trường 1, nhưng đã bắt đầu hạ nhiệt từ cuối 3Q26 khi lãi suất liên ngân hàng qua đêm giảm từ 4.25% xuống 3.41% và lãi suất huy động kỳ hạn 12 tháng được điều chỉnh giảm theo chỉ đạo điều hành.
- Biên lãi thuần (NIM): 2.10% trong 9T26 (đi ngang so với mức 2.07% tại cuối 2Q26 và thấp hơn mức bình quân 3.08% của 27 ngân hàng niêm yết), phản ánh sự bù trừ giữa đà cải thiện lợi suất cho vay khách hàng và chi phí vốn huy động tăng.
- Triển vọng NIM 4Q26 và 2027: Dự báo phục hồi nhẹ quanh mức 2.15% - 2.25% nhờ 3 động lực: (i) Tỷ lệ tiền gửi không kỳ hạn CASA phục hồi giúp ghìm chi phí vốn; (ii) Danh mục 62,000 tỷ VND dư nợ vay mua nhà bước vào chu kỳ điều chỉnh lãi suất thả nổi (+200 đến +300 bps); (iii) Tỷ trọng tín dụng trung và dài hạn sinh lời cao tiếp tục duy trì trên 40%.

3. Chi phí dự phòng và Chi phí hoạt động

- Chi phí dự phòng rủi ro tín dụng: 15,959 tỷ VND trong 9T26 (-5.4% YoY, 3Q26 đạt 4,640 tỷ VND, -25.0% YoY), hoàn thành 63.2% kế hoạch trích lập cả năm (25,240 tỷ VND). Việc chủ động kiểm soát chi phí trích lập dự phòng nhờ tỷ lệ tài sản bảo đảm cao đã hỗ trợ trực tiếp cho tăng trưởng lợi nhuận trước thuế.
- Chi phí hoạt động (OPEX): 22,099 tỷ VND trong 9T26 (+7.0% YoY, 3Q26 đạt 7,987 tỷ VND, +8.3% YoY), được kiểm soát chặt chẽ với tốc độ tăng chi phí thấp hơn 3.5 điểm phần trăm so với tốc độ tăng doanh thu (Operating Leverage dương).
- Tỷ lệ Chi phí trên Thu nhập (CIR): 32.7% trong 9T26 (cải thiện 105 bps so với 33.8% tại 9T25; riêng 3Q26 đạt 34.4%), tiếp tục duy trì trong nhóm các ngân hàng có hiệu quả tối ưu chi phí vận hành dẫn đầu hệ thống nhờ tỷ lệ tự động hóa giao dịch số đạt 97.6%.

4. Lợi nhuận trước thuế (PBT) và Chỉ số sinh lời

- Lợi nhuận trước thuế hợp nhất (PBT): 29,483 tỷ VND trong 9T26 (+24.8% YoY, đạt 88.5% kế hoạch năm ĐHĐCĐ giao ~33,300 tỷ VND; riêng 3Q26 đạt 10,579 tỷ VND, +39.3% YoY). BIDV dự kiến sẽ hoàn thành và vượt chỉ tiêu lợi nhuận cả năm 2026 trong 4Q26 dựa trên đà mở rộng tín dụng và đẩy mạnh thu hồi nợ ngoại bảng.
- Lợi nhuận sau thuế của cổ đông ngân hàng mẹ: 23,278 tỷ VND trong 9T26 (+25.5% YoY, 3Q26 đạt 8,331 tỷ VND, +39.9% YoY).
- Chỉ số sinh lời (TTM): Tỷ suất sinh lời trên tổng tài sản bình quân ROAA đạt 0.92%; Tỷ suất sinh lời trên vốn chủ sở hữu bình quân ROAE đạt 17.00%, hoàn thành mục tiêu chiến lược giai đoạn 2026 - 2030 (ROAE >= 15.0%).

5. Quy mô tài sản, Tăng trưởng tín dụng & Tỷ lệ LDR

- Tổng tài sản: 3,493,271 tỷ VND tại ngày 30/09/2026 (+4.9% YTD, +13.7% YoY), tiếp tục củng cố vị thế định chế tài chính có quy mô tài sản lớn nhất hệ thống ngân hàng Việt Nam.
- Vốn chủ sở hữu: 197,163 tỷ VND tại ngày 30/09/2026 (+17.4% YTD, +21.3% YoY), tạo nền tảng nguồn vốn tự có vững chắc hỗ trợ mở rộng quy mô kinh doanh và gia tăng hệ số an toàn vốn.
- Dư nợ tín dụng khách hàng: 2,561,795 tỷ VND (+8.0% YTD, +14.5% YoY), hoàn thành 75.0% hạn mức tăng trưởng tín dụng cả năm được NHNN giao (10.66%). Tăng trưởng tín dụng tập trung chủ yếu vào phân khúc Khách hàng Bán buôn (Wholesale Banking) với mức tăng +11.5% YTD, đóng góp 76% vào tổng tăng trưởng dư nợ toàn ngân hàng:
  * Khách hàng Doanh nghiệp lớn (LC): 611,000 tỷ VND (+12.4% YTD, chiếm tỷ trọng 23.8%).
  * Doanh nghiệp FDI: 140,000 tỷ VND (+54.2% YTD, chiếm tỷ trọng 5.5%).
  * Doanh nghiệp quy mô vừa (MIDCOM): 386,000 tỷ VND (+30.3% YTD, chiếm tỷ trọng 15.1%).
  * Doanh nghiệp nhỏ và vừa (SME): 387,000 tỷ VND (-6.1% YTD, chiếm tỷ trọng 15.1%).
  * Khách hàng cá nhân (Retail): 1,146,805 tỷ VND (+4.0% YTD, chiếm tỷ trọng 45.6%), chịu ảnh hưởng do dư nợ vay mua nhà (-5.8% YTD) và vay sản xuất kinh doanh (-3.7% YTD) sụt giảm, bù trừ bởi cho vay tiêu dùng có TSBĐ tăng trưởng +37.3% YTD.
- Cơ cấu tín dụng theo ngành kinh tế: Ngành Dịch vụ đạt 740,000 tỷ VND (+30.7% YTD, chiếm 28.9% tổng dư nợ); Ngành Công nghiệp chế biến chế tạo đạt 580,000 tỷ VND (+10.3% YTD, chiếm 22.7%); Ngành Bán buôn và bán lẻ đạt 386,000 tỷ VND (-6.0% YTD, chiếm 15.1%).
- Huy động vốn khách hàng (Gross): 2,680,223 tỷ VND (+9.2% YTD, +16.6% YoY), trong đó tiền gửi khách hàng đạt 2,360,525 tỷ VND (+6.2% YTD) và phát hành giấy tờ có giá đạt 311,000 tỷ VND (+38.0% YTD). Tốc độ tăng trưởng huy động vốn trong 3Q26 đã vượt tốc độ tăng trưởng tín dụng.
- Tỷ lệ CASA hợp nhất: 19.9% tại 30/09/2026 (giảm nhẹ so với 21.1% tại cuối 2025, nhưng cao hơn mức trung vị 19.5% của toàn ngành), tương ứng quy mô số dư CASA đạt 470,000 tỷ VND. Tiền gửi online của khách hàng cá nhân tăng trưởng +47% YTD lên 315,000 tỷ VND, chiếm 26% tổng nguồn vốn huy động bán lẻ.
- Tỷ lệ Cho vay trên Huy động (LDR quy chuẩn): Được kiểm soát an toàn dưới trần 85% của NHNN. Việc áp dụng Quyết định 1743/QĐ-NHNN (tính 50% tiền gửi Kho bạc Nhà nước vào nguồn vốn huy động đến tháng 07/2028) đã giúp tỷ lệ LDR của BIDV giảm thêm khoảng 1.6 - 1.7 điểm phần trăm.
- Hệ số an toàn vốn (CAR hợp nhất): Đạt 10.13% tại 30/09/2026 (tăng 80 bps so với mức 9.33% tại cuối 2025; tỷ lệ Vốn cấp 1 đạt 7.14%), vượt quy chuẩn an toàn tối thiểu 8.0% theo Thông tư 41.
- Tỷ lệ vốn ngắn hạn cho vay trung và dài hạn (MTLT): Duy trì ở mức 24.49% tại cuối 3Q26, cách biệt an toàn so với trần quy định 40% của Thông tư 25/2026/TT-NHNN.

6. Chất lượng Tài sản

- Tỷ lệ nợ xấu NPL (BCTC hợp nhất): 1.85% tại 30/09/2026 (giảm 2 bps so với 1.87% tại 3Q25, tăng nhẹ từ mức 1.83% tại 2Q26 và 1.47% tại cuối 2025), thấp hơn mức trung vị 2.11% của 27 ngân hàng niêm yết.
- Tỷ lệ nợ xấu theo Thông tư 31 (Ngân hàng mẹ): 1.58% tại 30/09/2026, tiếp tục duy trì dưới trần cam kết ĐHĐCĐ (<= 1.60%). Nợ xấu gia tăng chủ yếu chịu tác động phân loại chéo nhóm nợ qua CIC, áp lực dòng tiền của nhóm nhà thầu xây dựng - VLXD và Thông tư 02 hết hiệu lực.
- Tỷ lệ nợ nhóm 2 (Nợ cần chú ý): Ghi nhận 1.54% (+32 bps QoQ so với 1.22% tại 2Q26); tỷ lệ nợ quá hạn ở mức 2.43%.
- Tỷ lệ nợ xấu phân theo phân khúc: Khách hàng SME ghi nhận tỷ lệ NPL cao nhất khoảng 2.2%; Khách hàng Doanh nghiệp lớn ở mức ~2.0%; Khách hàng cá nhân được kiểm soát ở mức 1.22% với 97.5% tổng dư nợ có tài sản bảo đảm (tỷ lệ LTV bình quân an toàn 59.35%).
- Tỷ lệ bao phủ nợ xấu (LLR): Đạt 73.4% tại ngày 30/09/2026 (thu hẹp so với 99.9% tại cuối 2025 do nợ nhóm 3 tăng trong khi quỹ dự phòng duy trì ổn định). Số dư quỹ dự phòng rủi ro cho vay đạt 34,871 tỷ VND (-0.2% YoY).
- Chi phí tín dụng (Credit Cost quy năm): Đạt 0.73% trong 3Q26 (giảm so với 0.94% trong 2Q26 và 1.12% trong 3Q25; lũy kế 9T26 đạt 0.92%).

---

PHẦN II: Định hướng và Triển vọng của BIDV (BID) trong 2026 và Sắp tới

1. Kế hoạch Tăng vốn Điều lệ & Tiềm lực Vốn:
- Hoàn tất tăng vốn điều lệ lên 77,782 tỷ VND (+10.8% YTD) thông qua chi trả cổ tức bằng cổ phiếu tỷ lệ 21% trong năm 2025 và tiền mặt 4.5% trong năm 2026.
- Lộ trình tăng vốn giai đoạn 2026 - 2027: Kế hoạch chào bán riêng lẻ và/hoặc phát hành ra công chúng 780,000,000 cổ phần mới (~10.71% lượng cổ phiếu lưu hành tại tháng 03/2026) nhằm huy động thêm khoảng 40,400 tỷ VND thặng dư vốn, nâng vốn điều lệ sau hoàn tất lên 107,517 tỷ VND (+47.68%). Ngân hàng đã lựa chọn thêm đơn vị tư vấn tài chính quốc tế và đang trực tiếp đàm phán với các nhà đầu tư tổ chức chiến lược tiềm năng.
- Tái cơ cấu vốn Nhà nước: Nghị quyết ĐHĐCĐ và Quyết định 2054/QĐ-TTg xác định tỷ lệ sở hữu Nhà nước tại BIDV tiếp tục duy trì tối thiểu >= 65% trong giai đoạn 2026 - 2030 (hiện tại tỷ lệ sở hữu Nhà nước là 76.73%).

2. Kế hoạch Huy động vốn Dài hạn Quốc tế & Trái phiếu Vốn Cấp 2:
- Quy mô giấy tờ có giá lưu hành: Số dư trái phiếu vốn cấp 2 đạt 67,524 tỷ VND (+16.6% YTD) tại 30/09/2026.
- Kế hoạch phát hành 2026 - 2027: Lên kế hoạch phát hành bổ sung khoảng 25,000 đến 28,000 tỷ VND trái phiếu thâm niên và trái phiếu vốn cấp 2 nhằm tăng cường hệ số an toàn vốn, gia tăng nguồn vốn trung dài hạn tài trợ cho các dự án kinh tế trọng điểm quốc gia.

3. Mở rộng Hệ sinh thái Tài chính & Tài trợ Hạ tầng Trọng điểm:
- Danh mục tín dụng hạ tầng giao thông và logistics: Duy trì 18,400 tỷ VND dư nợ tài trợ các dự án BOT giao thông và 4,500 tỷ VND tài trợ cảng biển nước sâu.
- Cơ chế tín dụng đặc thù: Đã hoàn tất phê duyệt cam kết hạn mức 2,000 tỷ VND cho 1 đại dự án giao thông trọng điểm quốc gia theo cơ chế tín dụng chuyên biệt (được loại trừ khỏi giới hạn trần room tín dụng hàng năm của NHNN). Sẵn sàng đồng hành cùng 18 dự án hạ tầng quốc gia dự kiến đóng góp khoảng +1.0 điểm phần trăm tăng trưởng tín dụng năm 2027.

4. Bứt phá từ Ngân hàng số & Công nghệ AI Toàn diện:
- Đóng góp từ kênh số: Thu nhập thuần từ hoạt động ngân hàng số đạt 11,152 tỷ VND trong 9T26, chiếm tỷ trọng 17.3% tổng thu nhập thuần toàn ngân hàng.
- Quy mô người dùng: Số lượng khách hàng cá nhân đạt 27.4 triệu (+2.4 triệu khách hàng YTD); số người dùng SmartBanking hoạt động giao dịch thường xuyên đạt 10.6 triệu (+29% YoY); khách hàng tổ chức BIDV Direct đạt ~207,000 doanh nghiệp. Tỷ trọng giao dịch bán lẻ xử lý tự động trên kênh số đạt 97.6%.
- Ứng dụng Trí tuệ Nhân tạo (AI): Đem lại doanh thu định lượng 65.7 tỷ VND trong 9T26; 54.17% số đơn vị kinh doanh đã áp dụng AI vào vận hành thực tế (vượt xa chỉ tiêu năm là 20%); 98.65% nhân sự toàn hệ thống được đào tạo kỹ năng AI. Triển khai sâu rộng trợ lý ảo BSaleChat, RM Assistant Phase 2, Lending Hub IDP và hệ thống AI kiểm soát chất lượng tại Contact Center.
- Nền tảng mở Open API & Hệ sinh thái kết nối: Kết nối 504 đối tác đăng ký (96 đối tác vận hành chính thức như Masan/CP Vietnam, Jetpay, Thế Giới Di Động, SSI); ứng dụng BIDV Home vượt 550,000 người dùng với quy trình cho vay 100% không giấy tờ tích hợp VNeID.

5. Quản trị Rủi ro & Chủ động Đón đầu Chuẩn mực Quốc tế:
- Lộ trình Basel III: Đặt mục tiêu áp dụng Phương pháp Tiêu chuẩn (Standardised Approach - SA) từ 1Q27 và hoàn thiện triển khai Phương pháp Nội bộ (IRB) vào năm 2030.
- Chủ động thích ứng Thông tư 50/2026/TT-NHNN: Bắt đầu áp dụng bắt buộc chỉ số LCR và NSFR từ 01/10/2028; tỷ lệ trần LDR sẽ được nâng lên 95% đối với các ngân hàng đáp ứng chuẩn Basel III (thay thế trần 85% hiện tại), mở ra dư địa mở rộng bảng cân đối tài sản sinh lời quy mô lớn cho BIDV.

---

PHẦN III: Q&A BAN LÃNH ĐẠO

1. Kế hoạch Lợi nhuận 4Q26 và Triển vọng Tín dụng 2027 – Question from MBIS, Horizon Capital and HD Securities:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Kết quả lợi nhuận 4Q26 phụ thuộc vào tiến độ giải ngân tín dụng cuối năm, quy mô thu hồi nợ ngoại bảng (mục tiêu cả năm ~14,000 tỷ VND) và chi phí trích lập dự phòng theo mùa vụ.
- (2) Mitigating factor/buffer: Lũy kế 9T26 lợi nhuận trước thuế đã đạt 29,483 tỷ VND (+24.8% YoY), hoàn thành 88.5% kế hoạch ĐHĐCĐ giao, tạo vùng đệm hoàn thành kế hoạch năm rất vững chắc.
- (3) Forward guidance: Định hướng tăng trưởng tín dụng toàn hệ thống năm 2027 đạt khoảng 16% nhờ đầu tư công và FDI; BIDV đặt mục tiêu tăng trưởng tín dụng năm 2027 trong khoảng 15% - 16% tương đương mức tăng trưởng toàn ngành, kế hoạch chi tiết đang hoàn thiện để trình HĐQT phê duyệt.

2. Động lực Phân hóa Tín dụng Bán buôn và Bán lẻ – Question from Vietcap and VPBankS:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Tín dụng bán buôn tăng trưởng +11.5% YTD (đóng góp 76% mức tăng dư nợ) nhờ phân khúc Khách hàng lớn (+12.4%), FDI (+54.2%) và MIDCOM (+33.6%) hấp thụ vốn tốt trong các ngành Dịch vụ (+30.7%) và Chế biến chế tạo (+10.3%); trong khi tín dụng bán lẻ chỉ tăng +4.0% YTD do dư nợ vay mua nhà (-5.8%) và vay sản xuất kinh doanh (-3.7%) chịu áp lực trả nợ trước hạn.
- (2) Mitigating factor/buffer: Phân khúc cho vay tiêu dùng có TSBĐ của khách hàng cá nhân vẫn duy trì đà tăng trưởng +37.3% YTD; tỷ lệ tài sản bảo đảm của khối bán lẻ đạt 97.5% với tỷ lệ LTV bình quân an toàn 59.35%.
- (3) Forward guidance: Tiếp tục đẩy mạnh giải ngân tài trợ vốn lưu động cho doanh nghiệp FDI, doanh nghiệp xuất khẩu lớn; đồng thời kích hoạt lại phân khúc vay mua nhà bán lẻ thông qua gói lãi suất cho vay mới quanh mức 9.5%.

3. Tín dụng Dự án Hạ tầng Giao thông và Cơ chế Đặc thù – Question from VPS, Shinhan Securities and VCBF:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Nhu cầu vốn phát triển hạ tầng giao thông và logistics quốc gia tăng cao, nhưng việc cấp tín dụng đòi hỏi thẩm định khắt khe về tính khả thi tài chính và quy chế trần an toàn vốn.
- (2) Mitigating factor/buffer: Dư nợ tài trợ hạ tầng hiện hữu đạt 18,400 tỷ VND (BOT giao thông) và 4,500 tỷ VND (cảng biển); ngân hàng kiểm soát chặt chẽ qua 3 cấp độ thẩm định: xem xét sơ bộ, phê duyệt cam kết và giải ngân thực tế.
- (3) Forward guidance: Đã phê duyệt cam kết hạn mức 2,000 tỷ VND cho 1 dự án giao thông trọng điểm theo cơ chế tín dụng đặc thù nằm ngoài room tín dụng hàng năm; sẵn sàng tham gia thu xếp vốn cho danh mục 18 dự án hạ tầng quốc gia giai đoạn 2026 - 2027.

4. Nguyên nhân Nợ Nhóm 2 Tăng và Áp lực Nợ xấu – Question from MBS, Shinhan Securities and VCBF:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Tỷ lệ nợ nhóm 2 tăng 32 bps QoQ lên 1.54% trong 3Q26 xuất phát từ 3 nguyên nhân: (i) Phân loại chéo nhóm nợ từ hệ thống thông tin tín dụng CIC; (ii) Khó khăn dòng tiền tạm thời của một số doanh nghiệp xây dựng; (iii) Thông tư 02 hết hiệu lực khiến các khoản nợ cơ cấu chuyển về đúng nhóm nợ thực tế.
- (2) Mitigating factor/buffer: Dư nợ bán lẻ có tỷ lệ nợ xấu thấp (1.22%) với 97.5% có tài sản bảo đảm; nợ xấu ngân hàng mẹ theo Thông tư 31 chỉ ở mức 1.58% (thấp hơn trần cam kết ĐHĐCĐ <= 1.60%).
- (3) Forward guidance: Tăng cường rà soát dòng tiền của các khách hàng có nợ nhóm 2, đẩy mạnh xử lý nợ xấu qua thu hồi nợ bằng tiền mặt; kiên định mục tiêu kiểm soát NPL hợp nhất cuối năm 2026 dưới 1.60%.

5. Triển vọng Biên lãi thuần NIM và Điều chỉnh Lãi suất Cho vay Mua nhà – Question from Institutional Investors:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: NIM 9T26 duy trì ở mức 2.10% (đi ngang QoQ) do áp lực chi phí vốn đầu vào tăng nhẹ trong các tháng đầu năm triệt tiêu đà cải thiện của lợi suất tài sản sinh lời.
- (2) Mitigating factor/buffer: Tỷ lệ vốn ngắn hạn cho vay trung dài hạn ở mức 24.49% (thấp hơn trần 40% của Thông tư 25); chi phí vốn COF đang giảm dần theo xu hướng giảm lãi suất liên ngân hàng và lãi suất huy động 12 tháng.
- (3) Forward guidance: Dự báo NIM cải thiện dần trong 4Q26 và năm 2027 nhờ cơ cấu lại tài sản sinh lời sang kỳ hạn trung dài hạn (>40% tổng dư nợ), mở rộng tiền gửi CASA chi phí thấp và điều chỉnh tăng lãi suất (+200 đến +300 bps) đối với danh mục 62,000 tỷ VND dư nợ vay mua nhà hết hạn ưu đãi trong 12 tháng tới.

6. Thực trạng Nợ xấu Khách hàng Doanh nghiệp lớn và Chất lượng TSBĐ – Question from Vietcap:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Nợ xấu khối khách hàng doanh nghiệp lớn (NPL ~2.0%) tập trung chủ yếu tại các doanh nghiệp hoạt động trong lĩnh vực Xây dựng và Sản xuất vật liệu xây dựng do chu kỳ thanh toán các dự án kéo dài.
- (2) Mitigating factor/buffer: Hầu hết các khoản cấp tín dụng cho phân khúc này đều có tài sản bảo đảm giá trị lớn là dự án, nhà xưởng, máy móc thiết bị và bất động sản có tính pháp lý đầy đủ.
- (3) Forward guidance: Tích cực cơ cấu lại kỳ hạn trả nợ phù hợp với dòng tiền nghiệm thu dự án của nhà thầu; đặt mục tiêu kéo giảm tỷ lệ NPL phân khúc Doanh nghiệp lớn về mức 2.0% trong các quý tới.

7. Mục tiêu Tỷ lệ Bao phủ Nợ xấu LLR và Ngân sách Dự phòng 4Q26 – Question from Institutional Investors:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Tỷ lệ bao phủ nợ xấu (LLR) giảm xuống 73.4% tại cuối 3Q26 do quy mô nợ nhóm 3 tăng trong khi tốc độ trích lập dự phòng 9T26 được giữ ở mức thận trọng (-5.4% YoY).
- (2) Mitigating factor/buffer: Quỹ dự phòng rủi ro lũy kế duy trì mức cao 34,871 tỷ VND; tỷ lệ nợ xấu có TSBĐ của toàn ngân hàng ở mức rất cao, giảm thiểu rủi ro mất vốn thực tế.
- (3) Forward guidance: Lên kế hoạch tăng cường trích lập trong 4Q26 với ngân sách cả năm duy trì khoảng 24,000 - 25,000 tỷ VND (tương đương mức 25,240 tỷ VND năm 2025), qua đó phục hồi tỷ lệ bao phủ nợ xấu LLR lên mức mục tiêu khoảng 85% vào thời điểm 31/12/2026.

8. Tiến độ Phát hành Riêng lẻ và Kế hoạch Tăng Vốn Tự có – Question from FPTS and Institutional Investors:
Phản hồi từ Ban lãnh đạo:
- (1) Core root cause: Nhu cầu củng cố vốn tự có để mở rộng quy mô tín dụng và chuẩn bị cho việc áp dụng sớm các tiêu chuẩn Basel III (Thông tư 50/2026/TT-NHNN).
- (2) Mitigating factor/buffer: CAR hợp nhất hiện đạt 10.13% (+80 bps YTD); vốn điều lệ đã tăng lên 77,782 tỷ VND (+10.8% YTD) và số dư trái phiếu vốn cấp 2 đạt 67,524 tỷ VND.
- (3) Forward guidance: Tiếp tục triển khai phương án phát hành riêng lẻ 780,000,000 cổ phần mới (~10.71% vốn điều lệ) để nâng vốn điều lệ lên 107,517 tỷ VND, hiện đang phối hợp chặt chẽ với đơn vị tư vấn tài chính quốc tế để tiếp xúc nhà đầu tư; song song đó lên kế hoạch phát hành thêm 25,000 - 28,000 tỷ VND trái phiếu vốn cấp 2 trong giai đoạn 2026 - 2027.
"""

def main():
    out_dir = PROJECT_ROOT / "workspace/Bank/BID/output"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    md_path = out_dir / "analyst_report.md"
    docx_path = out_dir / "analyst_report.docx"
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(REPORT_MD.strip() + "\n")
    print(f"[✓] Đã tạo file Markdown Analyst Report: {md_path} ({len(REPORT_MD)} chars)")
    
    from scripts.document_formatter import DocumentFormatter
    DocumentFormatter.markdown_to_report_docx(str(md_path), str(docx_path))
    print(f"[✓] Đã biên dịch file DOCX Institutional Research Report: {docx_path} ({docx_path.stat().st_size / 1024:.1f} KB)")

    # Run Linter
    res = DocumentFormatter.lint_document(str(md_path))
    print(f"[*] Kết quả Linter: Compliant={res['compliant']}, Violations={res['violations_count']}, Quarters={res['quarter_violations_count']}, Tables={res['table_violations_count']}")
    if not res['compliant']:
        print("[!] Vi phạm:")
        for v in res.get('violations', []):
            print("  -", v)
        for q in res.get('quarter_violations', []):
            print("  - Quarter:", q)
        for t in res.get('table_violations', []):
            print("  - Table:", t)

if __name__ == "__main__":
    main()
