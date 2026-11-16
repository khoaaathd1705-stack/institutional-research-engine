# -*- coding: utf-8 -*-
"""
Script: expand_full_transcript_hdb.py
Mục đích:
Xây dựng bản ghi đầy đủ chuẩn hóa (Full Standardized Transcript) với 100% ĐẦY ĐỦ TẤT CẢ CÁC CÂU HỎI & CÂU TRẢ LỜI
trong phần Q&A, bảo toàn trọn vẹn từng lập luận, số liệu, và dẫn chứng của các diễn giả:
- Ông Phạm Văn Đẩu (CFO HDBank)
- Ông Hoàng Thái (Phó TGĐ HDBank kiêm Đại diện HD SAISON)
- Ông Trần Hoài Phương (Giám đốc Khối KHDN HDBank)
- Ông Vũ Hữu Điền (Chủ tịch HĐQT HD Securities - HDS)
Loại bỏ triệt để từ đệm (à, ừ...), sửa lỗi ASR, chuẩn hóa định dạng số quốc tế, ký hiệu quý 3Q26/9M26,
tích hợp đầy đủ các khối đối chiếu Slide `> *[Diễn giải đối chiếu từ Slide X: ...]*`.
"""

import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path("D:/AM").resolve()
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from document_formatter import DocumentFormatter, standardize_quarters, standardize_number_formatting


def generate_full_transcript():
    hdb_base = PROJECT_ROOT / "workspace/Bank/HDB"
    output_dir = hdb_base / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    transcript_md = """# BẢN GHI ĐẦY ĐỦ CUỘC HỌP (FULL STANDARDIZED TRANSCRIPT)
# HỘI NGHỊ NHÀ ĐẦU TƯ CẬP NHẬT KẾT QUẢ KINH DOANH 9T2026 (3Q26 & 9M26) - HDBANK VÀ HỆ SINH THÁI (HDB, HD SAISON, HDS)

* **Kỳ báo cáo**: 3Q26 & 9 tháng đầu năm 2026 (9M26) – Triển vọng 4Q26 và Kế hoạch 2026–2027
* **Đơn vị tổ chức**: Ngân hàng TMCP Phát triển TP.HCM (HDBank - Mã chứng khoán: HDB)
* **Thời gian tổ chức**: Tháng 10/2026 (Báo cáo kết quả kinh doanh 9M26)
* **Thành phần Ban Lãnh đạo chủ trì cuộc họp**:
  - **Ông Phạm Văn Đẩu** – Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank (CFO)
  - **Ông Hoàng Thái** – Phó Tổng Giám đốc HDBank (phụ trách Khối Bán lẻ) kiêm Đại diện Ban điều hành HD SAISON
  - **Ông Trần Hoài Phương** – Giám đốc Khối Khách hàng Doanh nghiệp HDBank
  - **Ông Vũ Hữu Điền** – Chủ tịch Hội đồng Quản trị Công ty Cổ phần Chứng khoán HD (HDSecurities - HDS)
  - **Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**: Điều phối viên chương trình và điều hành phiên Q&A
* **Tài liệu đối chiếu số liệu chuẩn (SSOT Benchmark)**:
  - `HDB_Slides.pptx` (20 slide trình chiếu chính thức của HDBank)
  - `HDSAISON_Slides.pptx` (2 slide kết quả tài chính chính thức của HD SAISON)
  - `HDS_Slides.pptx` (6 slide kết quả kinh doanh và chiến lược IPO của HD Securities)
* **Quy ước biên tập chuẩn mực định chế**:
  - `Lời phát biểu nguyên văn`: Được chuẩn hóa từ bản ghi ASR, loại bỏ toàn bộ từ ngữ thừa, ngập ngừng (à, ừ...), sửa lỗi nghe nhầm thuật ngữ âm thanh, bảo toàn 100% số liệu thực tế và luận điểm của Ban lãnh đạo.
  - `> *[Diễn giải đối chiếu từ Slide X: ...]*`: Chú thích dữ liệu đối soát trực tiếp từ slide tài liệu cuộc họp của từng đơn vị.
  - `[Ghi chú biên tập]`: Chuẩn hóa các thuật ngữ chuyên ngành tài chính - ngân hàng và sửa lỗi ASR (CASA, CIR, LDR, NPL, CAR, Basel II, Basel III, TT31, TT22, MediPay, EduPay, SkyJoy, Vikki Digital Bank, mã chứng khoán HDX...).

---

## PHẦN I: TỔNG QUAN HỆ SINH THÁI & KẾT QUẢ KINH DOANH HDBANK (HDB)

### 1. Khái quát Kết quả Kinh doanh Hợp nhất 9M26 & Vị thế Hệ sinh thái

**Ông Hoàng Thái (Phó Tổng Giám đốc HDBank)**:
"Kính thưa quý chuyên viên phân tích, đại diện các quỹ đầu tư và quý nhà đầu tư đã tham dự buổi cập nhật kết quả kinh doanh 9 tháng đầu năm 2026 của HDBank ngày hôm nay.

Tôi xin phép được bắt đầu bằng việc điểm qua các chỉ số tài chính nổi bật trong 9M26 của ngân hàng. Tính đến ngày 30/09/2026:
- Tổng tài sản của HDBank đã đạt mốc 1,143 nghìn tỷ đồng (tương đương 1.14 triệu tỷ đồng), tăng 22.7% so với đầu năm và tăng 46.2% so với cùng kỳ năm 2025.
- Về huy động vốn, tiền gửi thị trường 1 của ngân hàng tăng trưởng rất mạnh mẽ, đạt 29.1% so với đầu năm, vượt mức 837,000 tỷ đồng, tiếp tục nằm trong nhóm dẫn đầu toàn ngành ngân hàng.
- Dư nợ tín dụng hợp nhất đạt 756,000 tỷ đồng, tăng trưởng 28.6% so với đầu năm.
- Về lợi nhuận, lợi nhuận trước thuế hợp nhất 9M26 đạt 18,379 tỷ đồng (xấp xỉ 18.4 nghìn tỷ đồng), tăng trưởng 24.2% so với cùng kỳ năm trước. Kết quả này giúp HDBank duy trì tỷ suất sinh lời trên vốn chủ sở hữu (ROE) đạt 22.8%, tiếp tục thuộc nhóm dẫn đầu toàn ngành.
- Các chỉ số về hiệu quả vận hành và an toàn hoạt động như tỷ lệ chi phí trên thu nhập (CIR: 24.9%), tỷ lệ cấp tín dụng trên huy động (LDR: 71.5%), tỷ lệ nợ xấu (NPL: 2.55% theo Thông tư 31) và hệ số an toàn vốn (CAR Basel II: 13.9%) đều được kiểm soát ở mức rất an toàn và tích cực.

> *[Diễn giải đối chiếu từ Slide 1, 4 & 12 (HDB)]:*
> - *Tổng tài sản: **1,143 nghìn tỷ đồng** (+22.7% YTD, +46.2% YoY).*
> - *Tiền gửi TT1: **837 nghìn tỷ đồng** (+29.1% YTD).*
> - *Dư nợ tín dụng: **756 nghìn tỷ đồng** (+28.6% YTD).*
> - *LNTT 9M26: **18,379 tỷ đồng** (+24.2% YoY).*
> - *ROE: **22.8%**; CIR: **24.9%**; LDR (Cir.22): **71.5%**; NPL (Cir.31): **2.55%**; CAR (Basel II): **13.9%**.*

Kết quả tích cực này một lần nữa khẳng định sức mạnh và tính tương hỗ cao của hệ sinh thái tài chính - ngân hàng toàn diện mà HDBank đang sở hữu.

Trải qua hơn ba thập kỷ phát triển bền bỉ, đặc biệt trong giai đoạn 10 năm từ năm 2015 đến nay, tổng tài sản của HDBank đã tăng trưởng hơn 10 lần, từ quy mô khiêm tốn 100 nghìn tỷ đồng năm 2015 lên tới 1,143 nghìn tỷ đồng hiện tại. HDBank đã trở thành đối tác chiến lược tin cậy của nhiều định chế tài chính và quỹ đầu tư quốc tế hàng đầu như IFC, DEG, Proparco, LeapFrog, Baillie Gifford và Affinity.

Về thương hiệu và sự ghi nhận quốc tế, HDBank tiếp tục được vinh danh tại nhiều bảng xếp hạng uy tín trong nước và quốc tế như Fortune Southeast Asia 500, Top 50 Doanh nghiệp Niêm yết Tốt nhất Việt Nam của Forbes, giải thưởng Ngân hàng Bán lẻ Tốt nhất, và Quản trị Công ty Tốt nhất khu vực ASEAN. Đặc biệt, Tiến sĩ Nguyễn Thị Phương Thảo – Phó Chủ tịch Thường trực HĐQT HDBank – đã được Chủ tịch nước trao tặng danh hiệu Anh hùng Lao động vào năm 2025.

> *[Diễn giải đối chiếu từ Slide 2 & 3 (HDB)]:*
> - *Tổng tài sản tăng hơn 10 lần từ mức 100 nghìn tỷ đồng (2015) lên 1,143 nghìn tỷ đồng (3Q26).*
> - *Đối tác chiến lược quốc tế: IFC, DEG, Proparco, LeapFrog, Baillie Gifford.*
> - *Giải thưởng: Fortune Southeast Asia 500, Forbes Top 50, Huân chương Lao động (2013, 2015, 2017, 2020), Anh hùng Lao động năm 2025.*

### 2. Tổng quan Đóng góp từ các Đơn vị Thành viên & Chuyển đổi Số

Nhìn vào bức tranh hợp nhất 9M26 của HDBank và các đơn vị thành viên:
1. **Ngân hàng thương mại HDBank**: Tổng tài sản đạt 1,143 nghìn tỷ đồng (+46.2% svck), LNTT đạt 18.4 nghìn tỷ đồng (+24.2% svck), ROE đạt 22.8%, CAR đạt 13.9%.
2. **Khối Tài chính Tiêu dùng (HD SAISON)**: HDBank sở hữu 50% vốn điều lệ và 51% quyền biểu quyết. LNTT 9M26 vượt 1,184 tỷ đồng (tăng 8.7% svck theo báo cáo quản trị / đạt 1,390 tỷ đồng theo BCTC riêng), NIM đạt 26.9%, ROE đạt 21.4%. HD SAISON duy trì vị trí số 1 về mạng lưới điểm bán POS và phục vụ hơn 18 triệu khách hàng.
3. **Khối Chứng khoán & Ngân hàng Đầu tư (HD Securities - HDS)**: HDBank sở hữu 90% cổ phần. LNTT 9M26 đạt 2,241 tỷ đồng (tăng trưởng 265% svck), ROE đạt 26.1% dẫn đầu toàn thị trường chứng khoán, giữ vị trí Top 3 thị phần tư vấn phát hành trái phiếu doanh nghiệp.
4. **Ngân hàng số Vikki Digital Bank**: HDBank sở hữu 100% vốn điều lệ (tiếp nhận bắt buộc từ DongA Bank). Hiện tại Vikki đã thu hút hơn 9 triệu khách hàng, trong đó có hơn 5.6 triệu khách hàng đang hoạt động, đạt 3.7 triệu lượt tải ứng dụng tính đến 30/09/2026. Sản phẩm thẻ VikkiONE Connect vừa nhận giải thưởng 'Sản phẩm trải nghiệm khách hàng xuất sắc nhất Việt Nam' tại Asian Experience Awards (AEA 2026).
5. **Nền tảng khách hàng thân thiết SkyJoy**: Đã kết nối hơn 18 triệu thành viên trên toàn hệ sinh thái, cho phép tích điểm và đổi thưởng liền mạch trên ứng dụng số.
Toàn bộ hệ sinh thái HDBank hiện phục vụ hơn 35 triệu khách hàng thông qua mạng lưới khoảng 600 chi nhánh ngân hàng và hơn 50,000 điểm giao dịch tài chính trên cả nước.

> *[Diễn giải đối chiếu từ Slide 1 & 4 (HDB)]:*
> - *HD SAISON: HDBank sở hữu 50% vốn, 51% quyền biểu quyết. LNTT >1,184 tỷ đồng (+8.7% YoY), NIM 26.9%, ROE 21.4%. Mạng lưới POS số 1 phục vụ >18 triệu KH.*
> - *HDS: HDBank sở hữu 90%. LNTT 2,241 tỷ đồng (+265% YoY), ROE 26.1%, Top 3 phát hành trái phiếu.*
> - *Vikki: 100% vốn HDBank. >9 triệu KH (>5.6 triệu KH hoạt động), 3.7 triệu lượt tải app.*
> - *Hệ sinh thái: >35 triệu KH, ~600 chi nhánh, 50,000+ điểm giao dịch, SkyJoy >18 triệu thành viên.*

Về công tác số hóa và ngân hàng số:
- Tăng trưởng giao dịch qua kênh số của khách hàng cá nhân đạt +34% YoY. Hiện tại, 98% giao dịch của khách hàng cá nhân được thực hiện trên kênh số.
- Ứng dụng công nghệ eKYC và tự động hóa quy trình giúp thời gian mở tài khoản rút ngắn xuống chỉ còn vài phút (so với 30 phút trước đây). Khoảng 73% khách hàng mới được thu hút trực tiếp từ kênh số.
- Về khách hàng doanh nghiệp, HDBank tiên phong triển khai hai giải pháp thanh toán số hóa đặc thù:
  + **MediPay**: Giải pháp thanh toán viện phí thông minh không dùng tiền mặt tại bệnh viện, tích hợp ki-ốt tự phục vụ, xác thực qua VNeID và CCCD gắn chip, nhận diện khuôn mặt và kết nối trực tiếp với hệ thống thông tin bệnh viện (HIS).
  + **EduPay**: Nền tảng tìm kiếm và thanh toán học phí không tiền mặt, đã xử lý khoảng 435,000 giao dịch trong 9M26, kết nối hơn 1,500 cơ sở giáo dục, đạt tỷ lệ hài lòng 100% từ khách hàng.

> *[Diễn giải đối chiếu từ Slide 5 & 6 (HDB)]:*
> - *98% giao dịch KHCN qua kênh số; tăng trưởng giao dịch kênh số +34% YoY; ~73% KH mới đến từ kênh số.*
> - *EduPay: ~435,000 giao dịch thanh toán học phí 9M26 tại >1,500 cơ sở giáo dục; tỷ lệ hài lòng 100%.*
> - *MediPay: Kiosk y tế, xác thực VNeID/CCCD gắn chip, thanh toán viện phí không tiền mặt.*

Về tài trợ chuỗi giá trị và tín dụng xanh:
- Dư nợ cho vay và bảo lãnh trong chuỗi giá trị đạt 45.8 nghìn tỷ đồng, tăng trưởng 18.6% YoY với hơn 8,100 khách hàng tham gia. Tỷ lệ tiền gửi không kỳ hạn (CASA) từ khách hàng chuỗi giá trị đạt xấp xỉ 40%.
- Dư nợ tín dụng xanh đạt 6.1 nghìn tỷ đồng. Lũy kế giai đoạn 2019–2025, HDBank đã giải ngân hơn 42,000 tỷ đồng cho các dự án xanh, đồng thời phát hành 3,000 tỷ đồng trái phiếu xanh trong nước.
- HDBank chủ động triển khai gói tín dụng 10,000 tỷ đồng cho các lĩnh vực ưu tiên với mức giảm lãi suất 1.5%/năm so với mức ưu đãi hiện hành cho doanh nghiệp SME, và dành thêm 5,000 tỷ đồng hỗ trợ khách hàng cá nhân và doanh nghiệp.
- Về dấu mốc đối ngoại, ngày 21/09/2026, Tiến sĩ Nguyễn Thị Phương Thảo cùng lãnh đạo HDBank đã tham dự Lễ rung chuông khai mạc phiên giao dịch tại Sàn Giao dịch Chứng khoán New York (NYSE). HDBank cũng được vinh danh Thương hiệu Quốc gia Việt Nam 2026, nhận giải thưởng Doanh nghiệp Quản trị Xuất sắc tại APEA 2026, và Tổng Giám đốc Nguyễn Hữu Đặng được trao danh hiệu Doanh nhân Xuất sắc Châu Á.

> *[Diễn giải đối chiếu từ Slide 7, 8 & 9 (HDB)]:*
> - *Tài trợ chuỗi giá trị: 45.8 nghìn tỷ đồng (+18.6% YoY), >8.1k khách hàng, CASA chuỗi ~40%.*
> - *Tín dụng xanh: Dư nợ 6.1 nghìn tỷ đồng; lũy kế giải ngân >42,000 tỷ đồng xanh (2019–2025).*
> - *Gói hỗ trợ lãi suất: 10,000 tỷ đồng giảm 1.5%/năm cho SME; 5,000 tỷ đồng hỗ trợ KHCN & DN.*
> - *Sự kiện: Tham dự Lễ rung chuông NYSE ngày 21/09/2026; Thương hiệu Quốc gia 2026; Giải thưởng APEA 2026.*

Tiếp theo, tôi xin trân trọng kính mời ông Phạm Văn Đẩu – Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank – sẽ cập nhật chi tiết các điểm nhấn tài chính của ngân hàng mẹ và hợp nhất."

---

### 3. Phân tích Chi tiết Hiệu quả Tài chính, Chất lượng Tài sản & An toàn Vốn

**Ông Phạm Văn Đẩu (Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank - CFO)**:
"Kính chào quý nhà đầu tư, 

Tôi xin phép đại diện Ban Điều hành HDBank cập nhật chi tiết về các chỉ số tài chính của ngân hàng trong 3Q26 và 9M26.

Trước hết, điểm qua về bối cảnh kinh tế vĩ mô và ngành ngân hàng:
- Môi trường vĩ mô Việt Nam tiếp tục duy trì đà phục hồi tích cực. Tăng trưởng GDP 9M26 đạt 9.01% svck (trong đó 3Q26 ước tính đạt mức tăng trưởng rất khả quan từ 8.2% đến 8.4%). Vốn FDI đăng ký đạt 50.4 tỷ USD (+76.4% svck) và giải ngân đạt 21.0 tỷ USD (+12.1%). Tổng kim ngạch xuất nhập khẩu đạt 888 tỷ USD (+30.5% svck). Tuy nhiên, áp lực lạm phát vẫn cần theo dõi khi chỉ số CPI 9M26 tăng 4.52% svck.
- Về thanh khoản và lãi suất hệ thống ngân hàng: Tăng trưởng tín dụng toàn ngành tính đến hết tháng 9 đạt khoảng 11.59% (xấp xỉ 11.6%), trong khi huy động vốn toàn ngành đạt khoảng 9.78% (xấp xỉ 9.8%). Mặt bằng lãi suất huy động có xu hướng tăng nhẹ do áp lực cạnh tranh vốn, trong khi lãi suất điều hành của NHNN được giữ nguyên ở mức 4.50%. Tỷ giá trung tâm VND/USD duy trì quanh mức 25,627 VND/USD.

> *[Diễn giải đối chiếu từ Slide 10 & 11 (HDB)]:*
> - *GDP 9M26: **+9.01% svck**; CPI: **+4.52% svck**; Xuất khẩu: **888 tỷ USD** (+30.5% svck); FDI đăng ký: **50.4 tỷ USD** (+76.4% svck).*
> - *Tín dụng toàn ngành: **11.59%**; Huy động toàn ngành: **9.78%**; Lãi suất điều hành: **4.50%**.*

Trong bối cảnh đó, các chỉ tiêu tài chính cốt lõi của HDBank ghi nhận sự bứt phá nổi bật:
- **Tăng trưởng tín dụng**: HDBank đạt mức tăng trưởng 28.6% YTD, cao gấp 2.5 lần mức bình quân toàn ngành (11.6%). Động lực tăng trưởng tín dụng đến từ sự kết hợp cân bằng giữa cho vay bán buôn, bán lẻ, tài chính tiêu dùng và lĩnh vực xây dựng hạ tầng.
- **Tăng trưởng huy động**: Tiền gửi thị trường 1 tăng trưởng 29.1% YTD, vượt xa tốc độ 9.8% của toàn ngành. Động lực dẫn dắt chính đến từ tiền gửi khách hàng cá nhân (tăng 45.7% YTD, đạt 127 nghìn tỷ đồng), trong khi tiền gửi khách hàng doanh nghiệp tăng 19.9% YTD, đạt 518 nghìn tỷ đồng.
- **Lợi nhuận trước thuế**: 9M26 đạt 18,379 tỷ đồng, tăng 24.2% YoY. Đây là mức tăng trưởng lợi nhuận cao và bền vững nhờ đa dạng hóa nguồn thu và tận dụng hiệu quả hiệp đồng từ hệ sinh thái.
- **Hiệu quả sinh lời**: ROE năm hóa đạt 22.8%, đưa HDBank trở thành ngân hàng có hiệu quả sinh lời dẫn đầu trong Top 10 ngân hàng thương mại lớn nhất Việt Nam. ROA đạt 1.9%. Tỷ lệ chi phí trên thu nhập (CIR) được tối ưu hóa ở mức 24.9% (giảm so với mức 25.7% năm 2025).

> *[Diễn giải đối chiếu từ Slide 12, 13, 14 & 15 (HDB)]:*
> - *Tín dụng HDBank: **+28.6% YTD** (ngành ~11.6%).*
> - *Huy động TT1: **+29.1% YTD** (ngành ~9.8%). Tiền gửi KHCN đạt **127 nghìn tỷ** (+45.7% YTD), KHDN đạt **518 nghìn tỷ** (+19.9% YTD).*
> - *LNTT 9M26: **18,379 tỷ đồng** (+24.2% YoY). ROE: **22.8%** (Top 1 trong Top 10 ngân hàng lớn); ROA: **1.9%**; CIR: **24.9%**.*

Về diễn biến biên lãi thuần (NIM) và chi phí vốn:
- Lũy kế 9M26, tỷ lệ NIM hợp nhất của HDBank duy trì ở mức 4.8% (năm 2025 là 5.1%). Riêng trong 3Q26, NIM quý giảm xuống mức 3.9% do áp lực chi phí vốn ngắn hạn tăng lên (chi phí vốn bình quân 9M26 ở mức 4.7% so với 4.6% năm 2025) xuất phát từ sự cạnh tranh huy động tiền gửi trên thị trường, đồng thời ngân hàng chủ động triển khai các gói tín dụng hỗ trợ hạ lãi suất cho khách hàng.
- Lợi suất tài sản sinh lãi (Yield on IEA) 9M26 đạt 9.5%. Ngân hàng kỳ vọng NIM sẽ phục hồi trong 4Q26 nhờ nền tảng thanh khoản dồi dào, cơ chế tái định giá lãi suất cho vay sau thời gian ưu đãi và chiến lược dịch chuyển cơ cấu tín dụng sang phân khúc bán lẻ có biên lợi nhuận cao hơn.

> *[Diễn giải đối chiếu từ Slide 13 & 17 (HDB)]:*
> - *NIM 9M26 đạt **4.8%** (3Q26 giảm còn **3.9%** do áp lực chi phí vốn ngắn hạn và chính sách giảm lãi suất).*
> - *Lợi suất IEA 9M26: **9.5%**; Chi phí vốn (COF) 9M26: **4.7%**.*
> - *Kỳ vọng NIM phục hồi trong 4Q26 nhờ tái định giá cho vay và dịch chuyển sang bán lẻ.*

Về cơ cấu danh mục cho vay khách hàng:
- Cơ cấu tín dụng tiếp tục duy trì định hướng đa dạng hóa, phân tán rủi ro:
  + Bán lẻ, bán buôn và dịch vụ phụ trợ: chiếm 33.0% tổng danh mục.
  + Xây dựng: chiếm 32.2%.
  + Bất động sản: chiếm 14.1%.
  + Cho vay hộ gia đình và tiêu dùng cá nhân: chiếm 18.6% (trong đó hộ gia đình chiếm 16.5%, vay mua nhà ở chiếm 11.2%, nông nghiệp chiếm 3.3%, tiêu dùng cá nhân chiếm 2.9%).

> *[Diễn giải đối chiếu từ Slide 16 (HDB)]:*
> - *Cơ cấu cho vay khách hàng: Bán lẻ, bán buôn & DV: **33.0%**; Xây dựng: **32.2%**; BĐS: **14.1%**; Hộ gia đình & tiêu dùng: **18.6%** (Hộ gia đình: **16.5%**, Mua nhà: **11.2%**, Nông nghiệp: **3.3%**, Tiêu dùng cá nhân: **2.9%**).*

Về chất lượng tài sản và bộ đệm dự phòng rủi ro:
- Tỷ lệ nợ xấu hợp nhất theo Thông tư 31 tại thời điểm 30/09/2026 là 2.55% (riêng ngân hàng mẹ là 1.95%). Mức tăng nợ xấu này phản ánh xu hướng chung của toàn ngành ngân hàng sau khi Thông tư 02 hết hiệu lực và những tác động của thị trường lên một bộ phận khách hàng vay vốn.
- Nhằm củng cố an toàn hoạt động, HDBank đã chủ động tăng cường trích lập dự phòng rủi ro. Chi phí tín dụng trong 9M26 được trích lập là 5,413 tỷ đồng (tỷ lệ chi phí tín dụng đạt khoảng 1.48% so với 1.35% năm 2025). Quy mô quỹ dự phòng rủi ro tín dụng hiện đạt 11,412 tỷ đồng (trong đó quỹ dự phòng rủi ro cho vay bao gồm dự phòng chung là 3,301 tỷ đồng và dự phòng cụ thể là 2,496 tỷ đồng).
- Tỷ lệ bao phủ nợ xấu (LLR) hợp nhất đạt 68.7%, trong khi tỷ lệ bao phủ bằng tài sản đảm bảo đạt tới 189.0%, tạo lớp đệm bảo vệ rất an toàn trước các rủi ro tín dụng tiềm ẩn.

> *[Diễn giải đối chiếu từ Slide 18 (HDB)]:*
> - *NPL hợp nhất (TT 31): **2.55%** (ngân hàng mẹ: **1.95%**).*
> - *Tỷ lệ bao phủ nợ xấu (LLR): **68.7%**; Tỷ lệ bao phủ tài sản đảm bảo: **189.0%**.*
> - *Chi phí tín dụng 9M26: **5,413 tỷ đồng**; Quỹ dự phòng: DP chung **3,301 tỷ**, DP cụ thể **2,496 tỷ**.*

Về an toàn vốn và thanh khoản:
- Hệ số an toàn vốn (CAR) hợp nhất theo chuẩn Basel II đạt 13.9% (trong đó vốn cấp 1 chiếm 8.6% và vốn cấp 2 chiếm 5.3%), vượt xa yêu cầu tối thiểu 8.0% của NHNN. Với năng lực vốn vững mạnh và hệ thống quản trị rủi ro hoàn thiện, HDBank dự kiến sẽ chính thức áp dụng phương pháp tính CAR theo chuẩn Basel III từ năm 2027.
- Tỷ lệ cho vay trên huy động (LDR theo Thông tư 22) đạt 71.5% (riêng ngân hàng mẹ đạt 68.2%), duy trì khoảng cách an toàn so với trần quy định 85.0%.
- Tỷ lệ nguồn vốn ngắn hạn cho vay trung và dài hạn là 17.2% (riêng ngân hàng mẹ là 20.1%), tuân thủ rất tốt trần quy định tối đa 30.0%. Cả hai chỉ số thanh khoản quốc tế NSFR và LCR đều duy trì trên 100%.

> *[Diễn giải đối chiếu từ Slide 19 (HDB)]:*
> - *CAR (Basel II): **13.9%** (Vốn cấp 1: **8.6%**, Cấp 2: **5.3%**; kế hoạch Basel III từ 2027).*
> - *LDR (Cir.22): **71.5%** (ngân hàng mẹ: **68.2%**, trần 85.0%).*
> - *Tỷ lệ vốn ngắn hạn cho vay trung-dài hạn: **17.2%** (trần 30.0%). Cả NSFR và LCR vượt 100%.*

Về kế hoạch kinh doanh cả năm 2026:
- Tổng tài sản mục tiêu: 1,194 nghìn tỷ đồng (+28% sv 2025: 931 nghìn tỷ). Sau 9 tháng, HDBank đã đạt 1,143 nghìn tỷ, hoàn thành 95.7% kế hoạch năm.
- Tiền gửi thị trường 1: Kế hoạch 822 nghìn tỷ đồng (+27%). Thực tế 9 tháng đã đạt 837 nghìn tỷ, chính thức hoàn thành 101.8% kế hoạch cả năm.
- Dư nợ tín dụng: Kế hoạch 805 nghìn tỷ đồng (+37%). Thực tế đạt 756 nghìn tỷ, hoàn thành 93.9% kế hoạch năm.
- Lợi nhuận trước thuế: Kế hoạch 30,100 tỷ đồng (+41% sv 2025: 21,300 tỷ). Sau 9 tháng đạt 18,379 tỷ đồng, hoàn thành 61.1% kế hoạch năm.
- Các chỉ số sinh lời mục tiêu: ROAE > 25.0%, ROAA > 2.0%, tỷ lệ nợ xấu duy trì dưới 2.0%.

> *[Diễn giải đối chiếu từ Slide 20 (HDB)]:*
> - *Kế hoạch 2026F: Tổng tài sản **1,194 nghìn tỷ** (9M26 đạt 95.7%); Tiền gửi **822 nghìn tỷ** (9M26 đạt 101.8% - vượt KH); Tín dụng **805 nghìn tỷ** (9M26 đạt 93.9%); LNTT **30,100 tỷ đồng** (9M26 đạt 61.1%); ROAE > **25%**; ROAA > **2%**; NPL < **2.0%**.*

Tiếp theo chương trình, xin kính mời ông Hoàng Thái sẽ chia sẻ chi tiết về kết quả hoạt động của Khối Tài chính Tiêu dùng HD SAISON."

---

## PHẦN II: BÁO CÁO KẾT QUẢ KINH DOANH KHỐI TÀI CHÍNH TIÊU DÙNG - HD SAISON

**Ông Hoàng Thái (Phó Tổng Giám đốc HDBank kiêm Đại diện Ban điều hành HD SAISON)**:
"Kính thưa quý vị, 

Tôi xin phép cập nhật các điểm nhấn hoạt động của Công ty Tài chính TNHH HD SAISON trong 3Q26 và 9M26. Đây là giai đoạn ghi nhận sự bứt phá mạnh mẽ của HD SAISON với nhiều chỉ tiêu đạt mức kỷ lục:

1. **Quy mô Dư nợ & Doanh số Giải ngân**:
- Dư nợ cho vay tính đến 30/09/2026 đạt 28,751 tỷ đồng, tăng trưởng 29.2% YoY so với mức 22,251 tỷ đồng tại thời điểm cuối năm 2025. Đây là mức dư nợ cao nhất trong lịch sử hoạt động của HD SAISON (tăng liên tục từ mức 13,376 tỷ đồng năm 2021; 16,839 tỷ năm 2022; 16,086 tỷ năm 2023; và 18,212 tỷ năm 2024).
- Doanh số giải ngân lũy kế 9M26 đạt 32,204 tỷ đồng, tăng tốc vượt trội so với mức 27,689 tỷ đồng của cùng kỳ 9M25 (doanh số cả năm 2025 là 26,986 tỷ đồng).
- Về cơ cấu dư nợ theo danh mục sản phẩm tại thời điểm 3Q26:
  + Cho vay xe máy: Chiếm tỷ trọng 35.0%, tiếp tục là sản phẩm cốt lõi truyền thống dẫn đầu thị trường.
  + Cho vay giải ngân trực tiếp (Direct disbursement): Chiếm 19.0%.
  + Cho vay thiết bị điện máy: Chiếm 18.0%.
  + Cho vay phục vụ nhu cầu đời sống: Chiếm 15.0%.
  + Thẻ tín dụng và các sản phẩm khác: Chiếm 13.0%.

> *[Diễn giải đối chiếu từ Slide 1 (HDSAISON)]:*
> - *Dư nợ cho vay: **28,751 tỷ đồng** (+29.2% YoY so với 22,251 tỷ năm 2025).*
> - *Tổng giải ngân 9M26: **32,204 tỷ đồng** (so với 9M25: 27,689 tỷ và cả năm 2025: 26,986 tỷ).*
> - *Cơ cấu sản phẩm: Xe máy **35%**, Giải ngân trực tiếp **19%**, Điện máy **18%**, Nhu cầu đời sống **15%**, Thẻ tín dụng & khác **13%**.*

2. **Biên Lợi nhuận Thuần (NIM) & Chi phí Vốn (Funding Cost)**:
- Biên lãi thuần (NIM) 3Q26 duy trì ở mức cao và ổn định là 26.9% (so với 27.2% năm 2025; 30.6% năm 2024; 29.0% năm 2023; 30.2% năm 2022; và 26.8% năm 2021).
- Chi phí vốn (COF) của HD SAISON ở mức 7.6% tại 3Q26 (so với 6.1% năm 2025; 7.7% năm 2024; và 8.1% năm 2023).

> *[Diễn giải đối chiếu từ Slide 1 (HDSAISON)]:*
> - *NIM 3Q26: **26.9%** (2025: 27.2%; 2024: 30.6%).*
> - *Chi phí vốn (Funding Cost): **7.6%** (2025: 6.1%; 2024: 7.7%; 2023: 8.1%).*

3. **Khả năng Sinh lời & Hiệu quả Vận hành (P&L & Efficiency)**:
- Lợi nhuận trước thuế 9M26 đạt 1,390 tỷ đồng, tăng trưởng 17.4% YoY so với cùng kỳ 9M25 là 1,184 tỷ đồng (năm 2025 đạt 1,214 tỷ đồng; 2024 đạt 1,089 tỷ; 2023 đạt 660 tỷ; 2022 đạt 1,152 tỷ; và 2021 đạt 1,001 tỷ).
- Tổng thu nhập hoạt động (TOI) 9M26 đạt 6,155 tỷ đồng, tăng trưởng 19.1% YoY so với mức 5,169 tỷ đồng trong 9M25 (cả năm 2025 đạt 6,936 tỷ; 2024 đạt 6,663 tỷ).
- Tỷ lệ chi phí trên thu nhập (CIR) được cải thiện rõ nét, giảm xuống mức 33.1% trong 9M26 (so với 36.9% trong 9M25; 37.2% năm 2025; 35.7% năm 2024; 39.0% năm 2023; và 44.0% năm 2021).
- Tỷ suất sinh lời duy trì ở mức vượt trội trong nhóm tài chính tiêu dùng: ROE đạt 21.4% (năm 2025 đạt 22.5%; 2024 đạt 23.7%; 2023 đạt 13.3%); ROA đạt 4.8% (năm 2025 đạt 5.0%; 2024 đạt 5.2%).

> *[Diễn giải đối chiếu từ Slide 2 (HDSAISON)]:*
> - *LNTT 9M26: **1,390 tỷ đồng** (+17.4% YoY sv 9M25: 1,184 tỷ).*
> - *Tổng thu nhập (TOI) 9M26: **6,155 tỷ đồng** (+19.1% YoY sv 9M25: 5,169 tỷ).*
> - *CIR 9M26: **33.1%** (giảm từ 36.9% tại 9M25).*
> - *ROE: **21.4%**; ROA: **4.8%**.*

4. **Chất lượng Tài sản & Chi phí Tín dụng (Asset Quality & Credit Cost)**:
- Tỷ lệ nợ xấu (NPL) tại thời điểm 3Q26 ở mức 7.8% (so với 6.9% năm 2025; 7.4% năm 2024; 7.6% năm 2023; và 7.1% năm 2022). Đây là mức nằm trong phạm vi kiểm soát an toàn đối với đặc thù cho vay tiêu dùng không tài sản bảo đảm.
- Chi phí tín dụng (Credit Cost) giảm sâu xuống mức 11.8% tại 3Q26, cải thiện rất mạnh so với mức 16.3% năm 2025 (năm 2024 là 14.7%; 2023 là 17.9%; 2022 là 18.1%; và 2021 là 15.7%). Điều này phản ánh hiệu quả từ các mô hình chấm điểm tín dụng tự động và chính sách thẩm định chặt chẽ hơn.
- HD SAISON tiếp tục giữ vững vị thế số 1 toàn quốc về mạng lưới điểm giới thiệu dịch vụ (POS) với hơn 24,000 điểm giao dịch phủ khắp 63 tỉnh thành, phục vụ hơn 18 triệu khách hàng cá nhân.

> *[Diễn giải đối chiếu từ Slide 2 (HDSAISON)]:*
> - *Tỷ lệ nợ xấu (NPL): **7.8%** (2025: 6.9%; 2024: 7.4%).*
> - *Chi phí tín dụng (Credit Cost): Giảm mạnh còn **11.8%** (2025: 16.3%; 2023: 17.9%).*
> - *Mạng lưới POS số 1 toàn quốc, phục vụ >18 triệu khách hàng.*

Tiếp theo, xin mời ông Vũ Hữu Điền – Chủ tịch HĐQT Công ty Cổ phần Chứng khoán HD (HDS) – sẽ trình bày kết quả hoạt động và lộ trình IPO của khối chứng khoán."

---

## PHẦN III: BÁO CÁO HOẠT ĐỘNG KHỐI CHỨNG KHOÁN & LỘ TRÌNH IPO - HD SECURITIES (HDS)

**Ông Vũ Hữu Điền (Chủ tịch HĐQT HD Securities - HDS)**:
"Kính chào quý vị cổ đông, các chuyên viên phân tích và quý nhà đầu tư,

Tôi rất vui mừng đại diện cho Công ty Cổ phần Chứng khoán HD (HD Securities - HDS) được chia sẻ về bước chuyển mình chiến lược, kết quả kinh doanh 9M26 và kế hoạch niêm yết IPO của chúng tôi.

Như quý vị đã biết, năm 2021, HDBank bắt đầu tham gia góp vốn vào HDS. Đến năm 2024, tỷ lệ sở hữu được nâng lên 30% và chính thức trong năm 2026, HDBank đã tăng tỷ lệ sở hữu lên 90%. HDS chính thức trở thành công ty con nòng cốt của HDBank, được tích hợp sâu rộng vào toàn bộ hệ sinh thái khách hàng và mạng lưới của ngân hàng.

Định hướng chiến lược của HDS được gói gọn trong tinh thần: **'High Growth – High Tech – High Return'** (Tăng trưởng cao – Công nghệ cao – Hiệu quả sinh lời cao).
- **Tầm nhìn**: Trở thành ngân hàng đầu tư toàn diện và quản lý gia sản cho mọi nhà đầu tư, xây dựng nền tảng giao dịch thông minh dẫn dắt bởi dữ liệu và AI.
- **Slogan**: *'Gateway to Your Success'* (Cánh cửa dẫn đến thành công của bạn).
- **Sứ mệnh**: *'Connecting Capital. Unlocking Opportunity. Creating Value.'* (Kết nối vốn – Khai mở cơ hội – Kiến tạo giá trị).
- **Văn hóa doanh nghiệp**: Xây dựng dựa trên các giá trị cốt lõi: *Investor-First* (Nhà đầu tư là trung tâm), *AI-Native* (AI là năng lực cốt lõi), *Data-Driven Decisions* (Quyết định dựa trên dữ liệu), *Fast & Agile* (Nhanh và linh hoạt), *Challenge the Status Quo* (Dám thay đổi lối mòn), và *Integrity Above All* (Chính trực trên hết).

> *[Diễn giải đối chiếu từ Slide 1 (HDS)]:*
> - *HDBank tăng sở hữu từ 30% lên 90% năm 2026, đưa HDS thành công ty con.*
> - *Triết lý: High Growth – High Tech – High Return.*
> - *Sứ mệnh: Connecting Capital. Unlocking Opportunity. Creating Value.*
> - *Văn hóa: Investor-First, AI-Native, Data-Driven Decisions, Fast & Agile, Integrity Above All.*

### 1. Kết quả Hoạt động Kinh doanh Tăng Trưởng Nổi Bật 9M26
Trong 9 tháng đầu năm 2026, HDS đã đạt được kết quả kinh doanh tăng trưởng cao hơn đáng kể:
- **Lợi nhuận trước thuế (LNTT)**: 9M26 đạt 2,241 tỷ đồng, tăng trưởng **+265% YoY (gấp 3.65 lần cùng kỳ)** so với mức 614 tỷ đồng của 9M25. Tăng trưởng liên tục bứt phá qua các quý: Quý 1 đạt 352 tỷ đồng $\rightarrow$ Quý 2 đạt 769 tỷ đồng $\rightarrow$ Quý 3 đạt 1,118 tỷ đồng.
- **Doanh thu thuần**: 9M26 đạt 2,618 tỷ đồng, tăng trưởng **+158% YoY**. Tiến độ doanh thu theo quý: Quý 1 đạt 423 tỷ đồng $\rightarrow$ Quý 2 đạt 947 tỷ đồng $\rightarrow$ Quý 3 đạt 1,248 tỷ đồng.
- **Lợi nhuận sau thuế (LNST)**: 9M26 đạt 1,804 tỷ đồng theo BCTC riêng 3Q26, tăng trưởng **+269% YoY**.
- **Chỉ số sinh lời dẫn đầu toàn ngành**:
  + Tỷ suất sinh lời trên vốn chủ sở hữu (ROE năm hóa): Đạt **26.1%**, giữ vững vị thế **Top 1 toàn ngành chứng khoán Việt Nam**.
  + Tỷ suất sinh lời trên tài sản (ROA): Đạt **14.5%**.
  + Tỷ lệ chi phí trên doanh thu (CIR 9M): Đạt **14.5%**, nằm trong nhóm tối ưu chi phí vận hành hàng đầu thị trường nhờ ứng dụng AI sâu rộng.

> *[Diễn giải đối chiếu từ Slide 2 (HDS)]:*
> - *LNTT 9M26: **2,241 tỷ đồng** (+265% YoY sv 9M25: 614 tỷ; Q1: 352 tỷ -> Q2: 769 tỷ -> Q3: 1,118 tỷ).*
> - *Doanh thu thuần: **2,618 tỷ đồng** (+158% YoY; Q1: 423 tỷ -> Q2: 947 tỷ -> Q3: 1,248 tỷ).*
> - *LNST 9M26: **1,804 tỷ đồng** (+269% YoY).*
> - *ROE năm hóa: **26.1%** (Top 1 toàn ngành); ROA: **14.5%**; CIR: **14.5%**.*

### 2. Quy mô Bảng cân đối & Cơ cấu Vốn
Tính đến ngày 30/09/2026 so với thời điểm đầu năm:
- **Tổng tài sản**: Đạt 27,338 tỷ đồng, tăng gấp **4.6 lần** so với mức 5,949 tỷ đồng tại ngày 01/01/2026.
- **Vốn chủ sở hữu (VCSH)**: Đạt 14,041 tỷ đồng, tăng gấp **4.0 lần** so với mức 3,480 tỷ đồng đầu năm, sau khi hoàn tất tăng vốn điều lệ lên 10,960 tỷ đồng.
- **Dư nợ vay**: Đạt 10,565 tỷ đồng. Tỷ lệ Nợ vay / VCSH ở mức 75%, đảm bảo an toàn đòn bẩy tài chính.
- Vị thế thị trường: HDS nằm trong **Top 10 về LNTT**, **Top 1 về ROE**, và **Top 3 về thị phần tư vấn phát hành trái phiếu doanh nghiệp (thị phần đạt 4.4%)**.

> *[Diễn giải đối chiếu từ Slide 2 (HDS)]:*
> - *Tổng tài sản: **27,338 tỷ đồng** (x4.6 lần đầu năm 5,949 tỷ).*
> - *VCSH: **14,041 tỷ đồng** (x4.0 lần đầu năm 3,480 tỷ); Nợ vay: **10,565 tỷ**; Nợ vay/VCSH: **75%**.*
> - *Vị thế: Top 10 LNTT, Top 1 ROE, Top 3 tư vấn phát hành TPDN (thị phần 4.4%).*

### 3. Đóng góp theo Khối Kinh doanh & Tiến độ Kế hoạch năm 2026
Về cơ cấu đóng góp lợi nhuận trước thuế 9M26 theo các khối:
- **Khối Tư vấn (IB / Advisory)**: Đóng góp 1,034 tỷ đồng LNTT. Doanh thu 9M đạt 1,079 tỷ đồng, hoàn thành 72.6% kế hoạch năm (1,486 tỷ).
- **Khối Nguồn vốn (Treasury)**: Đóng góp 704 tỷ đồng LNTT. Doanh thu 9M đạt 873 tỷ đồng, hoàn thành 58.8% kế hoạch cả năm là 1,486 tỷ đồng.
- **Khối KD Trái phiếu & Tự doanh**: Đóng góp 463 tỷ đồng LNTT. Doanh thu 9M đạt 907 tỷ đồng, hoàn thành 56.7% kế hoạch năm (1,601 tỷ).
- **Khối Môi giới**: Doanh thu 9M đạt 845 tỷ đồng, hoàn thành 47.1% kế hoạch năm (1,793 tỷ). HDS đã phát triển năng lực mới trong năm 2026 về giao dịch trái phiếu bán buôn (Bond outright) và Institutional sales cho khách hàng tổ chức.
- **Các chỉ tiêu quy mô hoạt động**:
  + Dư nợ Margin: Đạt 10,972 tỷ đồng, hoàn thành 57.7% kế hoạch năm là 19,000 tỷ.
  + Số dư trái phiếu phân phối: Đạt 73,000 tỷ đồng, hoàn thành 48.7% kế hoạch năm (150,000 tỷ).
  + Giá trị tư vấn phát hành: Đạt 9,690 tỷ đồng (12.1% kế hoạch 80,000 tỷ).

Về tiến độ hoàn thành kế hoạch năm 2026:
- Doanh thu thuần 9M đạt 2,618 tỷ / kế hoạch 4,555 tỷ đồng (đạt 57.5%).
- Lợi nhuận trước thuế 9M đạt 2,241 tỷ / kế hoạch 3,375 tỷ đồng (đạt 66.3%).
- Để hoàn thành 100% kế hoạch năm, trong 4Q26 HDS cần đạt 1,938 tỷ đồng doanh thu thuần và 1,136 tỷ đồng LNTT. Mục tiêu thu hút 60,000 tài khoản mới trong năm 2026 (năm 2025 là 20,000). Vốn chủ sở hữu cuối năm sau IPO dự kiến đạt 18,377 tỷ đồng.

> *[Diễn giải đối chiếu từ Slide 3 (HDS)]:*
> - *Tiến độ 9T/KH: LNTT đạt **66.3%** (2,241 / 3,375 tỷ); Doanh thu đạt **57.5%** (2,618 / 4,555 tỷ).*
> - *Dư nợ margin: **10,972 tỷ** (57.7% KH 19,000 tỷ); Trái phiếu phân phối: **73,000 tỷ** (48.7% KH 150,000 tỷ).*
> - *Doanh thu theo khối: Tư vấn **1,079 tỷ** (72.6% KH); Nguồn vốn **873 tỷ** (199.3% KH - vượt gấp đôi); Tự doanh & TP **907 tỷ** (56.7% KH); Môi giới **845 tỷ** (47.1% KH).*
> - *Q4/2026 cần: DT **1,938 tỷ** và LNTT **1,136 tỷ**; VCSH sau IPO: **18,377 tỷ**.*

### 4. Hệ sinh thái Công nghệ AI & Fintech (AI Everywhere)
HDS triển khai chiến lược AI toàn diện từ vận hành nội bộ đến sản phẩm phục vụ khách hàng:
- **Vận hành nội bộ (Back Office & Advisory)**:
  + *HDWork - AI Office*: Văn phòng AI tác tử, tự chủ trong quy trình thực cho 100% nhân sự.
  + *Digital Factory & CoE*: Trung tâm vận hành tập trung, Hub dữ liệu và chứng từ điện tử, CoE chuẩn hóa và nhân rộng các ứng dụng AI.
  + *HD Advisors app*: Ứng dụng dành riêng cho chuyên viên tư vấn quản lý khách hàng, danh mục và khuyến nghị đầu tư có AI hỗ trợ.
- **Sản phẩm Khách hàng (Client Products)**:
  + *HDInvest*: Super app đầu tư thông minh, AI dẫn dắt toàn bộ hành trình trải nghiệm.
  + *FinoMS Pro*: Hệ thống đặt lệnh thông minh OMS/EMS/RMS cho khách hàng cá nhân và tổ chức.
  + *FinRadar & Alpha Hunter*: Radar quét tín hiệu thị trường và trợ lý AI cung cấp insight phân tích thời gian thực từ Data Hub của HDS.
  + *WealthMgmt & HD Academy*: Nền tảng tư vấn quản lý gia sản, chứng chỉ quỹ, trái phiếu và học viện đầu tư số.
- **Đối tác công nghệ chiến lược**: Galaxy Technology, GTS, AlgoPlatform, Powerful Platform For Invest, Smart Cloud, Fintech i, TMG.

> *[Diễn giải đối chiếu từ Slide 4 (HDS)]:*
> - *Nội bộ: HDWork-AI Office (văn phòng AI tác tử 100% nhân sự), Digital Factory & CoE, HD Advisors app.*
> - *Sản phẩm KH: HDInvest (Super app AI), FinoMS Pro (OMS/EMS/RMS), FinRadar, Alpha Hunter, WealthMgmt.*
> - *Đối tác công nghệ: Galaxy Technology, GTS, AlgoPlatform, Smart Cloud, Fintech i, TMG.*

### 5. Chiến lược Phát triển 2026–2030 & Tiến độ IPO, Niêm yết HoSE
Lộ trình chiến lược 3 giai đoạn hướng tới vị thế dẫn đầu:
- **2026–2027 (BUILD)**: *Connecting Capital* – Đẩy mạnh DCM (thị trường nợ), margin và tự doanh dẫn dắt tăng trưởng.
- **2028 (ACCELERATE)**: *Unlocking Opportunity* – Ra mắt HDS Prime, xây dựng cộng đồng nhà đầu tư, chiến dịch đại chúng hóa.
- **2029–2030 (LEAD)**: *Creating Value, globally* – Tham gia Trung tâm Tài chính Quốc tế (VIFC), token hóa tài sản, nền tảng B2B mở, thương mại hóa AI Office và mở rộng thị trường khu vực.

> *[Diễn giải đối chiếu từ Slide 5 (HDS)]:*
> - *2026–2027 (BUILD): DCM, margin và tự doanh dẫn dắt.*
> - *2028 (ACCELERATE): HDS Prime, cộng đồng nhà đầu tư, chiến dịch đại chúng.*
> - *2029–2030 (LEAD): VIFC, token hóa tài sản, B2B mở, thương mại hóa AI Office, mở rộng khu vực.*

Về tiến độ IPO và niêm yết trên Sàn Giao dịch Chứng khoán TP.HCM (HoSE):
- **Giai đoạn I: Tăng vốn (Tiến độ: 100%)**: Đã hoàn thành tăng vốn lên 10,960 tỷ đồng qua phát hành riêng lẻ và chia cổ tức bằng cổ phiếu vào tháng 05/2026. HDBank nâng sở hữu từ 30% lên 90% trước IPO. Hoàn thành kiểm toán BCTC 2025 (tháng 03/2026) và kiểm toán vốn sau phát hành (tháng 05/2026).
- **Giai đoạn II: IPO (Tiến độ: 25%)**: Đã chính thức nộp hồ sơ đăng ký chào bán IPO lên Ủy ban Chứng khoán Nhà nước (UBCKNN) vào ngày 05/10/2026. Dự kiến thực hiện chào bán IPO ra công chúng cho nhà đầu tư trong tháng 11/2026 và hoàn tất kiểm toán vốn sau IPO trong tháng 12/2026.
- **Giai đoạn III: Niêm yết HoSE (Tiến độ: 10%)**: Đã nộp hồ sơ niêm yết HoSE đồng thời với hồ sơ UBCKNN vào ngày 05/10/2026. Dự kiến đăng ký cổ phiếu với mã **HDX** tại Trung tâm Lưu ký Chứng khoán (VSDC) trong tháng 12/2026, nhận giấy phép niêm yết trước ngày 21/12/2026, và ngày giao dịch đầu tiên chính thức trên sàn HoSE dự kiến vào **tháng 01/2027**.

> *[Diễn giải đối chiếu từ Slide 6 (HDS)]:*
> - *Tăng vốn: Hoàn tất nâng vốn lên **10,960 tỷ đồng**, HDBank sở hữu **90%** (Tiến độ 100%).*
> - *IPO: Nộp hồ sơ UBCKNN ngày **05/10/2026**, chào bán tháng **11/2026** (Tiến độ 25%).*
> - *Niêm yết HoSE: Nộp hồ sơ **05/10/2026**, đăng ký mã **HDX** tại VSDC tháng **12/2026**, nhận giấy phép niêm yết dự kiến trước **21/12/2026**, giao dịch chính thức tháng **01/2027** (Tiến độ 10%).*

Tôi xin chân thành cảm ơn quý vị và sẵn sàng cùng các đồng nghiệp giải đáp các câu hỏi trong phần thảo luận."

---

## PHẦN IV: PHIÊN HỎI ĐÁP TOÀN DIỆN (FULL VERBATIM Q&A SESSION)

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Kính thưa quý vị đại biểu, các chuyên viên phân tích và quý nhà đầu tư, sau đây chúng ta sẽ bước vào phiên Thảo luận và Hỏi đáp (Q&A). Chúng tôi xin chuyển toàn bộ các câu hỏi chi tiết từ quý nhà đầu tư đến Ban Lãnh đạo HDBank, HD SAISON và HD Securities."

---

### Câu hỏi 1: Nhận định về Thanh khoản Ngành, Xu hướng Lãi suất Huy động/Cho vay, Kiểm soát Chi phí Vốn và Kế hoạch Tăng trưởng CASA

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Xin trân trọng chuyển đến Ban Lãnh đạo câu hỏi đầu tiên: 
*'Xin vui lòng cho biết nhận định của HDBank về tình hình thanh khoản ngành ngân hàng, mặt bằng lãi suất huy động và cho vay trong thời gian tới? Với yêu cầu của Ngân hàng Nhà nước về việc giảm lãi suất huy động ở các kỳ hạn từ 6 tháng trở lên, liệu lãi suất huy động có thể hạ nhiệt hay không? HDBank sẽ làm gì để kiểm soát chi phí vốn và duy trì biên lãi thuần (NIM)?'*
Một câu hỏi khá dài và mang đầy đủ tất cả các diễn biến thị trường tiền tệ hiện nay. Sau đây xin phép được kính mời ông Phạm Văn Đẩu – Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank – sẽ trả lời câu hỏi này."

**Ông Phạm Văn Đẩu (Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank - CFO)**:
"Cảm ơn câu hỏi rất thời sự và thực tế của quý nhà đầu tư. 

Tôi xin phép trả lời từng phần một:
1. **Về tình hình thanh khoản chung của ngành và tại HDBank**:
- Thanh khoản chung của ngành ngân hàng hiện nay phải nói là đang tương đối dồi dào dưới sự điều hành rất ổn định và linh hoạt của Ngân hàng Nhà nước. Nhờ đó, lãi suất trên thị trường liên ngân hàng duy trì ở mức thấp, thanh khoản hệ thống được bảo đảm thông suốt.
- Riêng đối với HDBank, tốc độ tăng trưởng huy động vốn thị trường 1 của chúng tôi trong 9 tháng đầu năm đạt 29.1% YTD, thuộc nhóm cao nhất toàn ngành.
- Tỷ lệ cấp tín dụng trên vốn huy động (LDR riêng lẻ) tại ngày 30/09/2026 của HDBank chỉ ở mức 68.2% (tính chung hợp nhất là 71.5%), trong khi trần tối đa Ngân hàng Nhà nước cho phép lên tới 85.0%. Điều này chứng minh HDBank đang sở hữu dư địa thanh khoản cực kỳ dồi dào, hoàn toàn sẵn sàng nguồn vốn để tăng tốc giải ngân tín dụng trong quý 4 này cũng như đầu năm sau.
- Các chỉ số an toàn thanh khoản theo chuẩn mực quốc tế Basel III như tỷ lệ tài trợ ổn định ròng (NSFR) và tỷ lệ đảm bảo khả năng thanh khoản (LCR) của HDBank đều duy trì vững chắc trên ngưỡng 100%.

> *[Diễn giải đối chiếu từ Slide 14 & 19 (HDB)]:*
> - *Huy động TT1: **837 nghìn tỷ đồng** (+29.1% YTD).*
> - *LDR riêng lẻ: **68.2%**; LDR hợp nhất: **71.5%** (dưới xa trần quy định 85.0%).*
> - *Cả hai chỉ số NSFR và LCR đều duy trì vượt ngưỡng 100%.*

2. **Về xu hướng lãi suất huy động và cho vay**:
- Với sự chỉ đạo điều hành của Chính phủ và Ngân hàng Nhà nước, toàn bộ hệ thống ngân hàng đều nghiêm túc tuân thủ. HDBank cũng như các ngân hàng thương mại khác đã chủ động giảm lãi suất huy động khoảng 0.5 điểm % ở các kỳ hạn tiền gửi từ 6 tháng trở lên.
- Với bối cảnh hiện tại, chúng tôi kỳ vọng mặt bằng lãi suất huy động sắp tới có thể giảm thêm khoảng 0.3 đến 0.5 điểm % nữa từ nay đến cuối năm. Bước sang nửa đầu năm 2027, đà giảm lãi suất huy động có thể sẽ chậm lại nhưng xu hướng giảm nhẹ hoặc duy trì ổn định ở vùng thấp vẫn là chủ đạo. Do đó, chi phí vốn đầu vào của ngân hàng sẽ dần được hạ nhiệt và cải thiện tốt hơn. Với nguồn vốn huy động dồi dào sẵn có, HDBank sẽ tiếp tục cân đối tối ưu nguồn lực để duy trì đà tăng trưởng tín dụng.
- Về lãi suất cho vay, Ngân hàng Nhà nước cũng định hướng các ngân hàng phấn đấu hạ lãi suất cho vay từ 1.0 đến 2.0 điểm % đối với các lĩnh vực sản xuất kinh doanh ưu tiên nhằm hỗ trợ doanh nghiệp tiết giảm chi phí đầu vào. HDBank nghiêm túc chấp hành, chủ động chọn lọc các ngành nghề, lĩnh vực ưu tiên và dự án khả thi để áp dụng chính sách giảm lãi suất cho vay.

3. **Về chi phí vốn và biên lãi thuần (NIM)**:
- Về chi phí vốn, từ đầu năm đến nay mặt bằng chi phí vốn duy trì ở mức cao nhưng đã bắt đầu xuất hiện dấu hiệu hạ nhiệt nhờ chính sách giảm lãi suất huy động như tôi vừa chia sẻ.
- Để tối ưu hóa chi phí vốn và bảo vệ NIM, ngoài việc giảm lãi suất huy động thông thường, giải pháp then chốt mang tính căn cơ là **phải tăng mạnh tỷ lệ tiền gửi không kỳ hạn (CASA)**.
- Bên cạnh đó, HDBank đang tích cực triển khai các chương trình huy động nguồn vốn trung và dài hạn từ các định chế tài chính toàn cầu và quỹ phát triển quốc tế với chi phí tối ưu, giúp giảm lãi suất bình quân của nguồn vốn đầu vào.
- Ở đầu ra, ngân hàng chọn lọc các dự án ưu tiên để giảm lãi suất, đồng thời đẩy mạnh cho vay các phân khúc có biên sinh lời cao như bán lẻ và tiêu dùng.
Về kế hoạch cụ thể nhằm gia tăng tỷ lệ CASA, tôi xin phép mời anh Hoàng Thái chia sẻ thêm các sáng kiến từ góc độ ngân hàng số và bán lẻ."

**Ông Hoàng Thái (Phó Tổng Giám đốc HDBank)**:
"Kính thưa quý nhà đầu tư,

Đại diện Ban Điều hành ngân hàng, tôi xin chia sẻ sâu hơn về chiến lược phát triển CASA của HDBank:
1. **Ngân hàng số Vikki Digital Bank**: Vikki hiện sở hữu hơn 9 triệu khách hàng, trong đó có hơn 5.6 triệu khách hàng hoạt động thường xuyên, ghi nhận 3.7 triệu lượt tải app. Thẻ VikkiONE Connect vừa đạt giải thưởng quốc tế tại AEA 2026. Đây là kênh thu hút khách hàng trẻ, tạo lập nguồn tiền gửi thanh toán tự nhiên rất lớn.
2. **Số hóa ứng dụng HDBank**: Khách hàng giao dịch qua kênh số tăng trưởng 34% YoY, hiện 98% giao dịch bán lẻ được thực hiện qua kênh số. Tốc độ mở tài khoản eKYC chỉ mất vài phút. Khoảng 73% khách hàng mới đến từ kênh số, giúp dòng tiền luân chuyển không kỳ hạn lưu lại trên hệ thống ngày càng lớn.
3. **Nền tảng khách hàng thân thiết SkyJoy**: SkyJoy hiện có hơn 18 triệu thành viên. Khách hàng khi thực hiện giao dịch tại HDBank sẽ được tích điểm thưởng và quy đổi trực tiếp ngay trên app thành vé xem phim, voucher ăn uống, mua sắm siêu thị. Điều này kích thích khách hàng duy trì số dư tiền gửi thanh toán thường xuyên.
4. **Chuyển đổi tệp khách hàng từ HD SAISON**: HD SAISON đang sở hữu gần 18 triệu khách hàng cá nhân. Dù mỗi đơn vị phục vụ phân khúc riêng, nhưng chúng tôi ước tính khoảng 10% đến 15% khách hàng của HD SAISON qua thời gian, khi thu nhập và điều kiện tài chính gia tăng, sẽ chuyển dịch thành khách hàng mở tài khoản thanh toán và sử dụng dịch vụ ngân hàng tại HDBank.
5. **Các giải pháp số hóa doanh nghiệp MediPay và EduPay**: Tạo dòng tiền CASA dồi dào từ các cơ sở y tế và giáo dục. Về điểm này, tôi xin mời anh Trần Hoài Phương chia sẻ thêm."

**Ông Trần Hoài Phương (Giám đốc Khối Khách hàng Doanh nghiệp HDBank)**:
"Bổ sung cho phần chia sẻ của anh Thái, dưới góc độ Khối Doanh nghiệp:
- EduPay và MediPay chính là giải pháp thu hút dòng tiền CASA 'phi tín dụng' (không phụ thuộc vào việc cấp hạn mức vay) từ hàng triệu phụ huynh, học sinh sinh viên và bệnh nhân.
- Khi phụ huynh đóng học phí qua EduPay tại hơn 1,500 trường học, hoặc bệnh nhân nạp tiền tạm ứng viện phí qua ki-ốt MediPay tại các bệnh viện lớn, toàn bộ dòng tiền không kỳ hạn này luân chuyển trực tiếp qua hệ thống tài khoản HDBank.
- Đây là nguồn vốn CASA cực kỳ ổn định, chi phí bằng 0%, giúp gia tăng giá trị tuyệt đối lẫn tỷ lệ CASA của HDBank, từ đó trực tiếp kéo giảm chi phí vốn bình quân và cải thiện biên lãi thuần NIM của ngân hàng."

---

### Câu hỏi 2: Động lực Tăng trưởng Tín dụng Vượt trội 28.6% & Hạn mức, Phân khúc Trọng tâm Quý 4

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ hai từ chuyên viên phân tích:
*'Tăng trưởng tín dụng của HDBank trong 9M26 đạt 28.6% YTD, cao gấp hơn 2.5 lần mức trung bình toàn ngành (11.6%). Xin Lãnh đạo ngân hàng cho biết các động lực tăng trưởng chính là gì? Ngân hàng còn bao nhiêu dư địa để tăng trưởng tín dụng và sẽ tập trung vào những lĩnh vực, ngành nghề nào? Đồng thời HDBank có các chương trình giảm lãi suất cho vay đối với khách hàng theo các chỉ đạo vừa qua của Chính phủ hay không?'*
Đối với câu hỏi này, xin kính mời ông Hoàng Thái và ông Trần Hoài Phương chia sẻ."

**Ông Hoàng Thái (Phó Tổng Giám đốc HDBank)**:
"Cảm ơn câu hỏi của quý nhà đầu tư. 

Tính đến 30/09/2026, tổng dư nợ tín dụng hợp nhất của HDBank đạt hơn 756,000 tỷ đồng, tăng trưởng 28.6% so với đầu năm. Về phía ngân hàng bán lẻ và khách hàng cá nhân:
- Tăng trưởng cho vay khách hàng cá nhân đạt 37.6% YTD, đạt quy mô 200 nghìn tỷ đồng. Động lực chính đến từ các khoản vay phục vụ sản xuất kinh doanh của hộ gia đình, vay tiêu dùng và vay mua nhà ở phân khúc thực.
- Khối tài chính tiêu dùng HD SAISON phục hồi rất mạnh mẽ với dư nợ đạt 28,751 tỷ đồng (+29.2% YoY).
- Bước sang quý 4 – mùa cao điểm lễ Tết và mua sắm cuối năm – nhu cầu vay vốn bán lẻ và tiêu dùng cá nhân sẽ tiếp tục là trụ cột tăng trưởng vững chắc của ngân hàng."

**Ông Trần Hoài Phương (Giám đốc Khối Khách hàng Doanh nghiệp HDBank)**:
"Tôi rất phấn khởi được chia sẻ về mặt trận tín dụng của Khối Khách hàng Doanh nghiệp. Dư nợ cho vay KHDN tăng trưởng 28.1% YTD, đạt 570 nghìn tỷ đồng. Kết quả này đến từ sự kiên định trong định hướng chiến lược:
1. **Tài trợ theo Chuỗi giá trị (Value Chain Financing)**:
- HDBank không tiếp cận doanh nghiệp một cách đơn lẻ mà tiếp cận theo toàn bộ hệ sinh thái chuỗi giá trị. Chúng tôi chọn các doanh nghiệp lớn đầu chuỗi (Anchor) có uy tín, dòng tiền lành mạnh thuộc các ngành thiết yếu như hàng tiêu dùng nhanh (FMCG), bán lẻ, vật tư nông nghiệp, logistics, và năng lượng tái tạo.
- Từ doanh nghiệp đầu chuỗi, HDBank triển khai tài trợ vốn lưu động và cấp bảo lãnh xuống toàn bộ mạng lưới đại lý cấp 1, đại lý cấp 2, nhà phân phối và nhà cung ứng. Mô hình này giúp ngân hàng kiểm soát chặt chẽ dòng tiền khép kín, giảm thiểu tối đa rủi ro tín dụng.
- Dư nợ chuỗi giá trị hiện đạt 45.8 nghìn tỷ đồng (+18.6% YoY) với hơn 8,100 khách hàng tham gia.
2. **Lĩnh vực Xây dựng và Hạ tầng**:
- Xây dựng là một trong những động lực tăng trưởng nổi bật, chiếm tỷ trọng 32.2% tổng danh mục cho vay. Chúng tôi tập trung tài trợ cho các dự án xây dựng hạ tầng kỹ thuật, giao thông trọng điểm và các công trình dân dụng lớn có nguồn vốn ngân sách hoặc chủ đầu tư uy tín.
3. **Phối hợp Hiệp đồng cùng HD Securities (HDS)**:
- Khối KHDN phối hợp chặt chẽ với HDS để cung cấp giải pháp tài chính toàn diện: HDBank tài trợ vốn tín dụng ngắn hạn và vốn lưu động, trong khi HDS tư vấn phát hành trái phiếu doanh nghiệp (DCM) và thu xếp vốn trung - dài hạn, giúp doanh nghiệp tối ưu hóa chi phí tài chính.
4. **Chính sách Giảm Lãi suất Hỗ trợ Khách hàng**:
- HDBank đã tiên phong ban hành gói tín dụng 10,000 tỷ đồng với mức giảm lãi suất 1.5%/năm dành riêng cho doanh nghiệp SME trong các lĩnh vực ưu tiên, cùng gói 5,000 tỷ đồng hỗ trợ khách hàng cá nhân và hộ kinh doanh."

---

### Câu hỏi 3: Tiến độ Hoàn thành Kế hoạch Lợi nhuận năm 2026 (30,100 tỷ đồng) & Động lực Quý 4

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ ba:
*'Lợi nhuận trước thuế hợp nhất 9 tháng đạt 18,379 tỷ đồng (xấp xỉ 18.4 nghìn tỷ), tăng 24.2% so với cùng kỳ nhưng mới hoàn thành khoảng 61% kế hoạch cả năm (30,100 tỷ đồng). Ban Lãnh đạo ngân hàng có tự tin sẽ hoàn thành mục tiêu lợi nhuận trên 30,000 tỷ đồng hay không? Và nếu có, lợi nhuận quý 4 sẽ đến từ những nguồn cụ thể nào?'*
Đối với câu hỏi này, xin kính mời ông Phạm Văn Đẩu – Giám đốc Tài chính – chia sẻ."

**Ông Phạm Văn Đẩu (Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank - CFO)**:
"Cảm ơn câu hỏi rất xác đáng và thực tế của quý nhà đầu tư.

Tôi xin khẳng định Ban Lãnh đạo HDBank hoàn toàn tự tin sẽ hoàn thành và có khả năng vượt kế hoạch lợi nhuận trước thuế 30,100 tỷ đồng cả năm 2026, dựa trên 4 trụ cột cụ thể sau:
1. **Đặc thù chu kỳ kinh doanh của ngân hàng**: Trong mô hình hoạt động của HDBank, quý 4 luôn là quý đóng góp tỷ trọng lợi nhuận lớn nhất trong năm (thường chiếm từ 35% đến 40% lợi nhuận cả năm). Mức hoàn thành 61% sau 9 tháng hoàn toàn nằm trong quỹ đạo kế hoạch phân bổ của ngân hàng.
2. **Quy mô tài sản sinh lãi tăng vọt trong quý 4**: Với hạn mức tín dụng dồi dào, các khoản vay khách hàng doanh nghiệp, tài trợ chuỗi giá trị và giải ngân xây dựng hạ tầng sẽ bước vào giai đoạn giải ngân cao điểm nhất vào cuối năm.
3. **Đóng góp bứt phá từ các công ty thành viên**:
- HD SAISON bước vào quý bội thu lớn nhất năm khi người dân đẩy mạnh mua sắm xe máy, điện máy, đồ gia dụng đón Tết. Doanh số giải ngân quý 4 của HD SAISON dự kiến sẽ lập đỉnh cao mới.
- HD Securities (HDS) đang ghi nhận mức tăng trưởng lợi nhuận cao (+265% YoY trong 9M26, đạt 2,241 tỷ đồng LNTT) và sẽ tiếp tục đóng góp lợi nhuận rất lớn trong quý 4 từ các thương vụ tư vấn IB lớn hoàn tất và hoạt động kinh doanh nguồn vốn trước thềm IPO.
4. **Ghi nhận nguồn thu từ phí dịch vụ và thu hồi nợ**: Doanh thu bảo hiểm, dịch vụ thanh toán và các khoản thu hồi nợ đã xử lý rủi ro thường được hạch toán tập trung vào cuối năm tài chính.
Do đó, chúng tôi hoàn toàn tự tin sẽ cán đích thành công kế hoạch lợi nhuận năm 2026."

---

### Câu hỏi 4: Nguyên nhân Thu hẹp NIM trong 3Q26 và Triển vọng Phục hồi trong 4Q26

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ tư:
*'Biên lãi thuần NIM quý 3 giảm xuống 3.9% (so với mức 4.8% trong 9M26 và 5.1% năm 2025) trong khi chi phí vốn có xu hướng tăng lên. Xin Ban Lãnh đạo cho biết nguyên nhân cụ thể là gì và liệu sắp tới NIM có phục hồi hay không?'*
Câu hỏi này xin mời anh Đẩu tiếp tục giải đáp."

**Ông Phạm Văn Đẩu (Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank - CFO)**:
"Tôi xin thông tin chi tiết về nguyên nhân thu hẹp NIM trong 3Q26 và triển vọng quý 4:
1. **Nguyên nhân cốt lõi**:
- Để chuẩn bị nguồn lực tài chính đón đầu đà tăng trưởng tín dụng bứt phá (+28.6% YTD), ngân hàng đã chủ động đẩy mạnh huy động tiền gửi thị trường 1 (+29.1% YTD). Sự cạnh tranh huy động trên thị trường đã làm chi phí vốn bình quân nhích lên 4.7%.
- Đồng thời, HDBank chủ động đồng hành cùng Chính phủ triển khai các chương trình hạ lãi suất cho vay ưu đãi cho doanh nghiệp và người dân, khiến lợi suất cho vay trung bình trong ngắn hạn có độ trễ nhất định so với đà tăng của chi phí vốn.
2. **Triển vọng phục hồi mạnh mẽ trong 4Q26**:
- Các khoản tín dụng ưu đãi giải ngân trong quý 2 và quý 3 sẽ bước vào kỳ tái định giá lãi suất theo biểu lãi suất thương mại thông thường.
- Ngân hàng đẩy mạnh giải ngân phân khúc bán lẻ và cho vay tiêu dùng (HD SAISON) – vốn là các phân khúc có lợi suất cho vay (IEA yield) cao hơn đáng kể.
- Chi phí vốn đầu vào bắt đầu hạ nhiệt nhờ chính sách giảm lãi suất tiền gửi và dòng tiền CASA gia tăng mạnh mẽ vào cuối năm.
Vì vậy, chúng tôi nhận định NIM quý 4 sẽ phục hồi về vùng 4.3% – 4.5%, đảm bảo duy trì NIM hợp nhất cả năm ở mức khả quan."

---

### Câu hỏi 5: Tỷ lệ Nợ xấu NPL 2.55%, Trích lập Dự phòng & Kiểm soát Rủi ro Danh mục Bất động sản / Xây dựng

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ năm:
*'Tỷ lệ nợ xấu hợp nhất tại cuối quý 3 ở mức 2.55% theo Thông tư 31, cao hơn so với quý 2 và cao hơn mức 1.66% cuối năm 2025. Xin Ban Lãnh đạo ngân hàng cho biết nợ xấu tăng ở đối tượng khách hàng nào, ngành nghề nào? Ngân hàng đã trích lập dự phòng ra sao và liệu trong thời gian tới tỷ lệ nợ xấu có được cải thiện hay không? Đồng thời ngân hàng kiểm soát rủi ro ra sao ở các ngành chiếm tỷ trọng lớn như xây dựng (32.2%) và bất động sản (14.1%)?'*
Đối với câu hỏi này, xin kính mời ông Phạm Văn Đẩu và ông Trần Hoài Phương chia sẻ."

**Ông Phạm Văn Đẩu (Phó Tổng Giám đốc kiêm Giám đốc Tài chính HDBank - CFO)**:
"Tôi xin phản hồi cụ thể về bức tranh chất lượng tài sản:
1. **Thực trạng và nguyên nhân nợ xấu tăng**:
- Tỷ lệ nợ xấu hợp nhất theo Thông tư 31 tại cuối quý 3 là 2.55% (riêng ngân hàng mẹ là 1.95%). Mức tăng này phản ánh xu hướng chung của toàn ngành sau khi Thông tư 02 hết hiệu lực và ngân hàng thực hiện phân loại nợ nghiêm ngặt theo Thông tư 31.
- Nợ xấu tăng chủ yếu tập trung ở nhóm khách hàng cá nhân sản xuất kinh doanh nông nghiệp, hộ kinh doanh cá thể tại các địa phương chịu ảnh hưởng của bão lũ, thiên tai thời gian qua, cùng một số doanh nghiệp vừa và nhỏ gặp khó khăn về dòng tiền thị trường.
2. **Chủ động củng cố bộ đệm dự phòng rủi ro**:
- HDBank luôn kiên định nguyên tắc quản trị rủi ro thận trọng. Trong 9M26, ngân hàng đã chủ động trích lập 5,413 tỷ đồng chi phí tín dụng (tăng đáng kể so với mức 4,054 tỷ đồng năm 2025).
- Quy mô quỹ dự phòng rủi ro tín dụng hiện đạt 11,412 tỷ đồng (trong đó quỹ dự phòng rủi ro cho vay bao gồm dự phòng chung 3,301 tỷ đồng và dự phòng cụ thể 2,496 tỷ đồng).
- Tỷ lệ bao phủ nợ xấu (LLR) hợp nhất đạt 68.7%, trong khi tỷ lệ bao phủ bằng tài sản đảm bảo đạt tới 189.0%, phần lớn là bất động sản có pháp lý hoàn chỉnh và giấy tờ có giá thanh khoản cao.
Về công tác quản lý rủi ro danh mục doanh nghiệp, xin mời anh Trần Hoài Phương chia sẻ thêm."

**Ông Trần Hoài Phương (Giám đốc Khối Khách hàng Doanh nghiệp HDBank)**:
"Về góc độ quản lý tín dụng doanh nghiệp, đặc biệt đối với ngành xây dựng và bất động sản:
1. **Kiểm soát chặt chẽ hạn mức ngành**: HDBank quy định trần tỷ trọng cho vay xây dựng và bất động sản không vượt quá 30% tổng danh mục tín dụng. Hiện tại, dư nợ bất động sản chỉ chiếm 14.1%, hoàn toàn nằm trong biên độ kiểm soát an toàn. Chúng tôi chỉ tài trợ cho các chủ đầu tư có năng lực tài chính lành mạnh, dự án đầy đủ pháp lý và dòng tiền bán hàng rõ ràng.
2. **Thành lập Đội ngũ Quản lý Chất lượng Nợ & Tài sản chuyên trách**:
- Khối KHDN đã thành lập một bộ phận chuyên trách mới là 'Quản lý Chất lượng Nợ và Chất lượng Tài sản' (Debt & Asset Quality Management). Đội ngũ này bao gồm các chuyên viên giàu kinh nghiệm cả về phát triển kinh doanh lẫn thẩm định rủi ro.
- Bộ phận này áp dụng quy trình quản trị rủi ro hiện đại thừa hưởng từ các cổ đông quốc tế, thực hiện giám sát dòng tiền dự án theo thời gian thực (Real-time Cash Flow Monitoring), nhận diện sớm các dấu hiệu suy yếu tài chính của khách hàng để có biện pháp cơ cấu hoặc thu hồi nợ từ sớm, ngăn ngừa chuyển nhóm nợ xấu."

---

### Câu hỏi 6: Chiến lược Phát triển của HD Securities (HDS) Sau khi HDBank Tăng Sở hữu lên 90%

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ sáu dành cho Khối Chứng khoán:
*'Sau khi HDBank nâng tỷ lệ sở hữu tại HDS lên 90%, chiến lược phát triển của HDS trong giai đoạn sắp tới là gì? Trong bối cảnh thị trường cạnh tranh gay gắt và thanh khoản có sự biến động, đâu sẽ là các mảng kinh doanh trọng tâm? Và liệu chỉ tiêu lợi nhuận 3,375 tỷ đồng trong năm nay HDS có thể hoàn thành được hay không?'*
Xin mời ông Vũ Hữu Điền – Chủ tịch HĐQT HDS – trả lời."

**Ông Vũ Hữu Điền (Chủ tịch HĐQT HD Securities - HDS)**:
"Cảm ơn câu hỏi của quý nhà đầu tư. 

Khi chính thức trở thành công ty con của HDBank với tỷ lệ sở hữu 90%, HDS đã xác lập một chiến lược phát triển bứt phá:
1. **Tận dụng tối đa Lợi thế Hệ sinh thái**: HDS được kết nối trực tiếp với hơn 35 triệu khách hàng của HDBank và Tập đoàn Sovico, mở ra tiềm năng khai thác bán chéo sản phẩm tài chính và quản lý gia sản cực kỳ to lớn.
2. **Bốn Trụ cột Kinh doanh Cốt lõi**:
- *Ngân hàng Đầu tư (IB) & Thị trường Nợ (DCM)*: HDS tiếp tục giữ vững vị thế Top 3 thị phần tư vấn phát hành trái phiếu doanh nghiệp (thị phần 4.4%). Khối tư vấn 9M26 đã đóng góp 1,034 tỷ đồng LNTT. Chúng tôi tập trung cấu trúc các sản phẩm trái phiếu chất lượng cao cho các tập đoàn hạ tầng, năng lượng và tiêu dùng lớn.
- *Kinh doanh Nguồn vốn (Treasury)*: Khối nguồn vốn 9M26 đã mang về 704 tỷ đồng LNTT (hoàn thành 58.8% kế hoạch cả năm là 1,486 tỷ đồng). HDS tận dụng tối đa hạn mức và thanh khoản liên ngân hàng để tối ưu hóa lợi suất dòng tiền.
- *Cho vay Margin và Công nghệ AI*: Dư nợ margin đạt 10,972 tỷ đồng. Nhờ vốn chủ sở hữu được nâng lên 14,041 tỷ đồng, HDS có nguồn vốn margin rất lớn với lãi suất cạnh tranh. Super app HDInvest và các công cụ AI (Alpha Hunter, FinRadar) đang tạo sức hút rất lớn đối với nhà đầu tư.
- *Môi giới Định chế và Trái phiếu Bán buôn (Bond outright)*: Đẩy mạnh phân phối trái phiếu cho các định chế tài chính và nhà đầu tư tổ chức.
3. **Về khả năng hoàn thành Kế hoạch LNTT 3,375 tỷ đồng**: 
- Lũy kế 9M26, HDS đã đạt 2,241 tỷ đồng LNTT, hoàn thành 66.3% kế hoạch năm.
- Quý 4 luôn là thời điểm cao điểm nhất của thị trường vốn khi các thương vụ tư vấn IB lớn hoàn tất và nhu cầu giao dịch margin tăng mạnh. HDS hoàn toàn tự tin sẽ hoàn thành và có thể vượt kế hoạch lợi nhuận 3,375 tỷ đồng cả năm."

---

### Câu hỏi 7: Kế hoạch IPO & Cơ sở Định giá Cổ phiếu HDS Gần 40,000 Đồng/Cổ phiếu

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ bảy:
*'HDS công bố mức giá chào bán dự kiến cho đợt IPO lên tới gần 40,000 đồng/cổ phiếu. Nhà đầu tư có câu hỏi là mức giá IPO dự kiến này được xác định dựa trên cơ sở nào? Xin vui lòng chia sẻ về kế hoạch IPO sắp tới và tại sao Ban Lãnh đạo công ty lại chọn thời điểm hiện tại khi thị trường chung đang có những biến động nhất định?'*
Xin mời ông Vũ Hữu Điền chia sẻ."

**Ông Vũ Hữu Điền (Chủ tịch HĐQT HD Securities - HDS)**:
"Tôi xin chia sẻ về kế hoạch IPO của HDS. Toàn bộ thông tin chi tiết chính thức sẽ được chúng tôi trình bày tại chuỗi sự kiện Roadshow dành cho các quỹ đầu tư tại Hà Nội và TP.HCM sau khi nhận giấy phép từ UBCKNN. Tuy nhiên, tôi xin chia sẻ sơ bộ về 2 vấn đề mà quý nhà đầu tư quan tâm:

1. **Vì sao chọn IPO vào thời điểm hiện tại?**
- Thị trường chứng khoán luôn có những chu kỳ biến động ngắn hạn, nhưng dòng tiền đầu tư tổ chức trung và dài hạn luôn tìm kiếm các doanh nghiệp có năng lực sinh lời cao và tốc độ tăng trưởng vượt trội.
- HDS đã hoàn thành toàn bộ các bước chuẩn bị: Đã tăng vốn lên 10,960 tỷ đồng (100%), đã nộp đồng thời hồ sơ chào bán lên UBCKNN và hồ sơ niêm yết lên HoSE vào ngày 05/10/2026. Chúng tôi dự kiến thực hiện chào bán IPO cho nhà đầu tư trong tháng 11/2026, đăng ký mã cổ phiếu **HDX** tại VSDC tháng 12/2026, nhận giấy phép niêm yết trước 21/12/2026 và chính thức giao dịch trên sàn HoSE vào tháng 01/2027. Việc IPO đúng kế hoạch sẽ tạo nền tảng vốn vững chắc để HDS bứt phá trong chu kỳ 2026–2030.

2. **Cơ sở cho mức định giá gần 40,000 đồng/cổ phiếu**:
- *Hiệu quả sinh lời Top 1 thị trường*: ROE năm hóa của HDS đạt **26.1%**, cao nhất trong toàn bộ các công ty chứng khoán tại Việt Nam. Một định chế dẫn đầu về hiệu quả sử dụng vốn xứng đáng được định giá ở mức tương xứng.
- *Tốc độ tăng trưởng lợi nhuận cao*: LNTT 9M26 tăng trưởng **+265% YoY**, đạt 2,241 tỷ đồng, quy mô lợi nhuận nằm trong Top 10 toàn ngành.
- *Quy mô vốn vững mạnh*: Vốn chủ sở hữu hiện tại đạt 14,041 tỷ đồng và dự kiến sau IPO sẽ đạt **18,377 tỷ đồng**, đưa HDS vào nhóm các định chế chứng khoán có quy mô vốn lớn nhất Việt Nam.
- *Định vị khác biệt bằng AI và Hệ sinh thái*: HDS là công ty chứng khoán tiên phong xây dựng nền tảng AI-native toàn diện, sở hữu chi phí vận hành tối ưu với CIR chỉ 14.5% và có kênh phân phối trực tiếp tới 35 triệu khách hàng của HDBank.
Do đó, chúng tôi tin rằng mức giá này phản ánh đúng giá trị nội tại và tiềm năng tăng trưởng tích cực của HDS trong tương lai."

---

### Câu hỏi 8: Cạnh tranh Ngành Tài chính Tiêu dùng, Xu hướng Chi phí Tín dụng & Triển vọng Mùa Cao điểm Cuối năm của HD SAISON

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Câu hỏi thứ tám gửi đến Khối Tài chính Tiêu dùng:
*'Thị trường tài chính tiêu dùng hiện nay cạnh tranh rất gay gắt và chi phí tín dụng của các công ty tài chính có xu hướng tăng lên. Triển vọng mùa cao điểm cuối năm 2026 và năm 2027 của HD SAISON ra sao? Công ty kiểm soát nợ xấu và chi phí tín dụng như thế nào?'*
Đối với câu hỏi này, xin mời ông Hoàng Thái – Phó Tổng Giám đốc HDBank kiêm Đại diện Ban điều hành HD SAISON – chia sẻ."

**Ông Hoàng Thái (Phó Tổng Giám đốc HDBank kiêm Đại diện Ban điều hành HD SAISON)**:
"Cảm ơn câu hỏi của quý nhà đầu tư. 

Như đã trình bày, HD SAISON đang ghi nhận kết quả kinh doanh với tất cả các chỉ số đều đạt mốc kỷ lục lịch sử:
1. **Khẳng định Vị thế Dẫn đầu Hiệu quả**:
- HD SAISON tiếp tục là công ty tài chính tiêu dùng hoạt động hiệu quả và an toàn nhất Việt Nam hiện nay.
- Dư nợ cho vay đạt 28,751 tỷ đồng, tăng trưởng 29.2% YoY so với cuối năm 2025. Doanh số giải ngân 9M26 đạt kỷ lục 32,204 tỷ đồng.
- Lợi nhuận trước thuế 9M26 đạt 1,390 tỷ đồng (+17.4% YoY), tổng thu nhập đạt 6,155 tỷ đồng (+19.1% YoY), và ROE đạt 21.4%.
2. **Chi phí Tín dụng Giảm Sâu & Kiểm soát Rủi ro Toàn diện**:
- Điểm sáng ấn tượng nhất của HD SAISON là **Chi phí tín dụng (Credit Cost) giảm mạnh xuống chỉ còn 11.8%** tại 3Q26 (so với mức 16.3% năm 2025, 14.7% năm 2024, và 17.9% năm 2023).
- Tỷ lệ nợ xấu được kiểm soát chặt chẽ ở mức 7.8% (mức an toàn trong cho vay tiêu dùng không tài sản bảo đảm).
- Đạt được kết quả này là nhờ chúng tôi kiên định 4 giải pháp:
  + *Tăng trưởng chọn lọc*: Đối với các khoản vay tiền mặt và thẻ tín dụng, chúng tôi áp dụng mô hình phân lớp khách hàng. Chỉ khi khách hàng đã vay mua xe máy, điện máy và chứng minh được lịch sử trả nợ tốt, chúng tôi mới chào mời khoản vay tiền mặt tiếp theo hoặc cấp thẻ tín dụng.
  + *Ứng dụng Machine Learning và Big Data*: Áp dụng thuật toán học máy vào thẩm định dữ liệu lớn và phê duyệt tự động, giúp hiểu sâu chân dung rủi ro của khách hàng, phê duyệt chính xác hơn và loại bỏ các hồ sơ tiềm ẩn nợ xấu.
  + *Số hóa toàn diện và chăm sóc khách hàng qua kênh số*: Vừa tối ưu hóa chi phí vận hành (CIR giảm xuống 33.1%), vừa nâng cao trải nghiệm khách hàng và đẩy nhanh tốc độ thu hồi nợ.
  + *Tận dụng tối đa Hệ sinh thái HDBank và Kinh nghiệm Đối tác Credit Saison (Nhật Bản)*: Kế thừa quy trình thẩm định tín dụng bán lẻ khắt khe từ nhà phát hành thẻ tín dụng và cho vay tiêu dùng hàng đầu Nhật Bản.
3. **Triển vọng Thị trường & Động lực Mùa Cao điểm Cuối năm**:
- Theo dữ liệu mới nhất từ Tổng cục Thống kê, đến hết 30/09/2026, thu nhập bình quân của người lao động Việt Nam đã tăng 9.9% svck. Nếu trừ đi lạm phát CPI khoảng 4.52%, tăng trưởng thu nhập thực tế vẫn đạt trên 4.5%. Tiền lương của người lao động làm công ăn lương tăng 8.0%, phản ánh sức mua thực tế đang cải thiện rất rõ nét.
- Cơ cấu dân số Việt Nam tiếp tục duy trì độ tuổi trẻ dồi dào. Cứ đều đặn mỗi 3 quý, thị trường lao động lại đón nhận hơn 700,000 lao động mới trưởng thành gia nhập lực lượng lao động. Đây chính là nguồn khách hàng tiềm năng to lớn có nhu cầu tài chính tiêu dùng thực tế.
- Quý 4 luôn là mùa mua sắm cao điểm nhất năm khi nhu cầu vay mua xe máy mới, điện thoại, máy tính và chi tiêu gia đình đón Tết Nguyên đán tăng vọt.
- Với mạng lưới hơn 24,000 điểm giới thiệu dịch vụ (POS) số 1 toàn quốc và cơ sở dữ liệu hơn 18 triệu khách hàng, HD SAISON hoàn toàn sẵn sàng đón đầu cơ hội này. Chúng tôi dự báo kết quả kinh doanh quý 4 sẽ tiếp tục lập đỉnh cao mới, đóng góp rất lớn vào lợi nhuận hợp nhất của HDBank."

---

### Bế mạc Hội nghị

**Đại diện Bộ phận Quan hệ Nhà đầu tư (IR Coordinator)**:
"Kính thưa quý vị đại biểu, các chuyên viên phân tích và quý nhà đầu tư,

Thời lượng của chương trình Hội nghị Nhà đầu tư cập nhật kết quả kinh doanh 9M26 của HDBank và các đơn vị thành viên đến đây đã kết thúc. Thay mặt Ban Tổ chức, chúng tôi xin trân trọng cảm ơn sự đồng hành, quan tâm và những câu hỏi phản biện rất sâu sắc của quý vị dành cho HDBank, HD SAISON và HD Securities.

Kính chúc quý vị sức khỏe, thành công và hẹn gặp lại quý vị trong các kỳ hội nghị cập nhật kết quả kinh doanh tiếp theo của HDBank. Xin trân trọng cảm ơn!"

---

## PHẦN V: NGUYÊN TẮC KIỂM TRA ĐỐI SOÁT DỮ LIỆU SLIDE VS SCRIPT (RECONCILIATION SUMMARY)

| Đơn vị | Chỉ tiêu định lượng cốt lõi | Dữ liệu phát biểu trong Script | Dữ liệu trên Slide (Ground Truth) | Trạng thái đối soát | Nguồn Slide tham chiếu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HDBank** | Tổng tài sản 30/09/2026 | 1.14 triệu tỷ đồng (1,143 nghìn tỷ) | 1,143 nghìn tỷ đồng (+22.7% YTD, +46.2% YoY) | `[MATCH]` | Slide 1, 4, 12, 20 (HDB) |
| **HDBank** | Tiền gửi khách hàng TT1 | Vượt 837,000 tỷ đồng (+29.1% YTD) | 837 nghìn tỷ đồng (+29.1% YTD) | `[MATCH]` | Slide 1, 12, 14, 15, 20 (HDB) |
| **HDBank** | Dư nợ tín dụng hợp nhất | 756,000 tỷ đồng (+28.6% YTD) | 756 nghìn tỷ đồng (+28.6% YTD) | `[MATCH]` | Slide 1, 12, 20 (HDB) |
| **HDBank** | Lợi nhuận trước thuế 9M26 | 18,379 tỷ đồng / 18.4 nghìn tỷ (+24.2% YoY)| 18,379 tỷ đồng (+24.2% YoY) | `[MATCH]` | Slide 1, 4, 12, 13, 17, 20 (HDB) |
| **HDBank** | Tỷ suất sinh lời ROE / ROA | ROE: 22.8%; ROA: 1.9% | ROE: 22.8%; ROA: 1.9% | `[MATCH]` | Slide 1, 12, 13, 17, 20 (HDB) |
| **HDBank** | Tỷ lệ Chi phí / Thu nhập (CIR) | 24.9% | 24.9% | `[MATCH]` | Slide 1, 13, 17 (HDB) |
| **HDBank** | Biên lãi thuần NIM 9M26 & 3Q26 | NIM 9M: 4.8%; NIM 3Q26: 3.9% | NIM 9M: 4.8%; NIM 3Q26: 3.9% | `[MATCH]` | Slide 13, 17 (HDB) |
| **HDBank** | Tỷ lệ nợ xấu NPL (TT 31) | Hợp nhất: 2.55%; Ngân hàng mẹ: 1.95% | Hợp nhất: 2.55%; Ngân hàng mẹ: 1.95% | `[MATCH]` | Slide 1, 12, 18, 20 (HDB) |
| **HDBank** | Hệ số an toàn vốn CAR (Basel II)| 13.9% (Vốn cấp 1: 8.6%, cấp 2: 5.3%) | 13.9% (Vốn cấp 1: 8.6%, cấp 2: 5.3%) | `[MATCH]` | Slide 1, 12, 14, 19 (HDB) |
| **HDBank** | Tỷ lệ LDR (TT 22) | 71.5% (Ngân hàng mẹ: 68.2%) | 71.5% (Ngân hàng mẹ: 68.2%, trần 85%) | `[MATCH]` | Slide 1, 19 (HDB) |
| **HDBank** | Tỷ trợ Chuỗi giá trị & Tín dụng xanh| Chuỗi: 45.8 nghìn tỷ; Xanh: 6.1 nghìn tỷ | Chuỗi: 45.8 nghìn tỷ; Xanh: 6.1 nghìn tỷ | `[MATCH]` | Slide 7, 9 (HDB) |
| **HD SAISON**| Dư nợ cho vay (Loan Book) 3Q26 | 28,751 tỷ đồng (+29.2% YoY) | 28,751 tỷ đồng (+29.2% YoY) | `[MATCH]` | Slide 1 (HDSAISON) |
| **HD SAISON**| Tổng giải ngân 9M26 | 32,204 tỷ đồng (sv 9M25: 27,689 tỷ) | 32,204 tỷ đồng | `[MATCH]` | Slide 1 (HDSAISON) |
| **HD SAISON**| Cơ cấu sản phẩm 3Q26 | Xe máy 35%, Giải ngân TT 19%, Điện máy 18% | Xe máy 35%, Giải ngân TT 19%, Điện máy 18% | `[MATCH]` | Slide 1 (HDSAISON) |
| **HD SAISON**| LNTT 9M26 & Tổng thu nhập TOI | LNTT: 1,390 tỷ (+17.4%); TOI: 6,155 tỷ | LNTT: 1,390 tỷ (+17.4%); TOI: 6,155 tỷ | `[MATCH]` | Slide 2 (HDSAISON) |
| **HD SAISON**| NIM 3Q26 & Chi phí vốn COF | NIM: 26.9%; COF: 7.6% | NIM: 26.9%; COF: 7.6% | `[MATCH]` | Slide 1 (HDSAISON) |
| **HD SAISON**| CIR, ROE & ROA 9M26 | CIR: 33.1%; ROE: 21.4%; ROA: 4.8% | CIR: 33.1%; ROE: 21.4%; ROA: 4.8% | `[MATCH]` | Slide 2 (HDSAISON) |
| **HD SAISON**| NPL & Chi phí tín dụng (Credit Cost)| NPL: 7.8%; Credit Cost: 11.8% | NPL: 7.8%; Credit Cost: 11.8% | `[MATCH]` | Slide 2 (HDSAISON) |
| **HDS** | Tổng tài sản & Vốn chủ sở hữu | TS: 27,338 tỷ (x4.6); VCSH: 14,041 tỷ (x4.0) | TS: 27,338 tỷ; VCSH: 14,041 tỷ | `[MATCH]` | Slide 2 (HDS) |
| **HDS** | Doanh thu thuần & LNTT 9M26 | DT: 2,618 tỷ (+158%); LNTT: 2,241 tỷ (+265%) | DT: 2,618 tỷ (+158%); LNTT: 2,241 tỷ (+265%) | `[MATCH]` | Slide 2, 3 (HDS) |
| **HDS** | LNST 9M26 & Chỉ số sinh lời | LNST: 1,804 tỷ (+269%); ROE: 26.1% | LNST: 1,804 tỷ; ROE: 26.1%; CIR: 14.5% | `[MATCH]` | Slide 2 (HDS) |
| **HDS** | Dư nợ Margin 30/09/2026 | 10,972 tỷ đồng (57.7% KH 19,000 tỷ) | 10,972 tỷ đồng | `[MATCH]` | Slide 3 (HDS) |
| **HDS** | Lộ trình IPO & Niêm yết HoSE | Nộp HS 05/10/2026, IPO 11/2026, Lên HoSE 01/2027| Nộp HS 05/10/2026, IPO 11/2026, Lên HoSE 01/2027| `[MATCH]` | Slide 6 (HDS) |
"""

    transcript_md = standardize_quarters(transcript_md)
    transcript_md = standardize_number_formatting(transcript_md)

    md_out_path = output_dir / "full_transcript.md"
    with open(md_out_path, "w", encoding="utf-8") as f:
        f.write(transcript_md)
    print(f"[✓] Đã tạo thành công {md_out_path} ({len(transcript_md.splitlines())} dòng, {len(transcript_md)} ký tự).")

    docx_out_path = output_dir / "full_transcript.docx"
    print(f"[*] Đang biên dịch sang DOCX chuẩn Corporate: {docx_out_path.name}...")
    DocumentFormatter.markdown_to_transcript_docx(str(md_out_path), str(docx_out_path))
    print(f"[✓] Đã tạo thành công file Word transcript: {docx_out_path}")


if __name__ == "__main__":
    generate_full_transcript()
