# -*- coding: utf-8 -*-
"""
Script: build_vpl_transcripts.py
Mục đích: Tự động tạo 2 file Word chuyên nghiệp (.docx) cho Vinpearl (VPL) bao gồm đầy đủ cả phần Trình bày và 12 câu hỏi Q&A:
1. VPL_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx (Bản tiếng Việt biên tập chuẩn định chế)
2. VPL_Earnings_Call_3Q2026_Script_EN.docx (Bản tiếng Anh chuẩn hóa, sửa lỗi chính tả/thuật ngữ từ audio gốc)
Sử dụng template chuẩn: workspace/F88_Earnings_Call_Q3_2026_Transcript_Bien_Tap.docx
"""

import os
import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
import docx
from docx.shared import Pt, RGBColor

TEMPLATE_PATH = "workspace/F88_Earnings_Call_Q3_2026_Transcript_Bien_Tap.docx"
OUT_DIR = "workspace/VPL/output"
OUT_ROOT = "workspace/VPL"

def setup_document():
    doc = docx.Document(TEMPLATE_PATH)
    for p in list(doc.paragraphs):
        p._p.getparent().remove(p._p)
    return doc

def add_header(doc, title_text, subtitle_text, speakers_text):
    p_title = doc.add_paragraph(title_text, style="Title F88")
    
    p_sub = doc.add_paragraph(style="Normal")
    r_sub = p_sub.add_run(subtitle_text)
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True
    r_sub.font.color.rgb = RGBColor(0x3C, 0x5C, 0x7A)
    
    p_spk = doc.add_paragraph(style="Normal")
    r_label = p_spk.add_run("Speakers: ")
    r_label.font.bold = True
    r_names = p_spk.add_run(speakers_text)

def add_section(doc, sec_num, sec_title):
    doc.add_paragraph(f"{sec_num:02d}  |  {sec_title}", style="Section F88")

def add_speaker_para(doc, speaker_name, text):
    p = doc.add_paragraph(style="Speaker F88")
    if speaker_name:
        r_spk = p.add_run(f"[{speaker_name}]: ")
        r_spk.font.bold = True
        r_spk.font.color.rgb = RGBColor(0x13, 0x3F, 0x69)
    p.add_run(text)
    return p

def add_editorial_note(doc, note_text):
    if not (note_text.startswith("Editorial Note:") or note_text.startswith("Ghi chú biên tập:")):
        note_text = f"Editorial Note: {note_text}"
    doc.add_paragraph(note_text, style="Note F88")

def build_vietnamese_docx():
    print("[*] Đang khởi tạo bản tiếng Việt: VPL_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx...")
    doc = setup_document()
    
    add_header(
        doc,
        title_text="VINPEARL | Earnings Call Transcript",
        subtitle_text="3Q2026 and 9M2026 Financial Results & Strategic Update",
        speakers_text="[Điều phối viên / Ban IR] (Quan hệ Nhà đầu tư, Vinpearl); [Bà Hương] (Tổng Giám đốc / CEO, Vinpearl); [Ông Trần Duy] (Giám đốc Tài chính / CFO, Vinpearl); [Bà Nguyễn Hạnh] (Kế toán trưởng / Chief Accountant, Vinpearl); [Bà Mai Hương] (Giám đốc Đầu tư / Director of Investment, Vinpearl)."
    )
    
    # Section 01
    add_section(doc, 1, "Bối cảnh Kinh tế Vĩ mô & Thị trường Du lịch Việt Nam 9T2026")
    add_speaker_para(
        doc,
        "Điều phối viên / Ban IR",
        "Kính chào quý nhà đầu tư, các chuyên gia phân tích và quý vị đại biểu đã tham dự buổi công bố Kết quả Kinh doanh Quý 3 và 9 tháng đầu năm 2026 của Công ty Cổ phần Vinpearl. Sau đây, chúng tôi xin trân trọng kính mời Bà Hương, Tổng Giám đốc Vinpearl, bắt đầu phần trình bày cập nhật kinh doanh và định hướng chiến lược."
    )
    add_speaker_para(
        doc,
        "Bà Hương – Tổng Giám đốc / CEO, Vinpearl",
        "Kính thưa quý vị, kinh tế Việt Nam ghi nhận mức tăng trưởng GDP trên 9% trong 9 tháng đầu năm 2026 (+9,01% YoY), xác lập tốc độ tăng trưởng 9 tháng nhanh nhất trong vòng 15 năm qua, trong khi lạm phát được kiểm soát ở mức 4,52%, sát mục tiêu 4,5% của Quốc hội. Song hành cùng bối cảnh vĩ mô tích cực, ngành du lịch Việt Nam duy trì đà phục hồi vững chắc với lượng khách quốc tế đạt gần 18 triệu lượt (+14,5% YoY) và doanh thu du lịch toàn quốc đạt 874 nghìn tỷ đồng (+10,2% YoY), hoàn thành xấp xỉ 78% kế hoạch năm."
    )
    add_speaker_para(
        doc,
        None,
        "Trước bối cảnh thuận lợi đó, Vinpearl đạt kết quả kinh doanh 9 tháng rất tích cực: Doanh thu thuần hợp nhất đạt gần 10,7 nghìn tỷ đồng (+18,6% YoY); Lợi nhuận sau thuế đạt hơn 2,8 nghìn tỷ đồng, gấp khoảng 6,6 lần so với cùng kỳ năm 2025. Ở cấp độ vận hành, cả hai mảng khách sạn và công viên giải trí đều ghi nhận tốc độ tăng trưởng EBITDA vượt trội so với doanh thu, chứng minh hiệu ứng đòn bẩy hoạt động (operating leverage) đang chuyển hóa mạnh mẽ thành lợi nhuận ròng. Tỷ lệ lấp đầy phòng khách sạn đạt 64% (+9 điểm phần trăm YoY), trong khi VinWonders đón 8,9 triệu lượt khách (+6% YoY). Động lực tăng trưởng của chúng tôi không chỉ đến từ lượng khách mà chủ yếu từ thời gian lưu trú kéo dài hơn (+10% YoY) và mức chi tiêu bình quân cao hơn trên toàn bộ danh mục."
    )
    add_speaker_para(
        doc,
        None,
        "Xét về các yếu tố vĩ mô tác động trực tiếp: Khách nội địa hiện chiếm khoảng 40% lượng khách khách sạn của Vinpearl và là tệp khách hàng cốt lõi của VinWonders. Tiêu dùng nội địa phục hồi mạnh mẽ với tổng mức bán lẻ hàng hóa và dịch vụ tiêu dùng tăng 13,4% YoY lên 5.926 nghìn tỷ đồng. Giải ngân đầu tư công đạt 643 nghìn tỷ đồng (+46% YoY), tập trung mở rộng sân bay, cao tốc và đường sắt kết nối trực tiếp đến các điểm đến của Vinpearl. Vốn FDI thực hiện tăng 12% YoY lên mức cao nhất 9 tháng trong 5 năm, tạo lực đẩy mạnh mẽ cho nhu cầu du lịch công vụ và MICE. Về thể chế, Nghị quyết 168/NQ-CP đặt mục tiêu tăng trưởng 11,9% trong nửa cuối năm; Ngân hàng Nhà nước ban hành Công văn số 8509/NHNN-TD loại trừ tín dụng dự án du lịch khỏi hạn ngạch bất động sản; và Nghị quyết 26-NQ/TW của Bộ Chính trị xác định du lịch là ngành kinh tế mũi nhọn với mục tiêu đến 2030 đóng góp 10-12% GDP và đón 45-50 triệu lượt khách quốc tế."
    )
    add_speaker_para(
        doc,
        None,
        "Về thị trường quốc tế, cơ cấu nguồn khách đang đa dạng hóa rõ nét: Châu Âu là khu vực tăng trưởng nhanh nhất (+55% YoY), dẫn đầu bởi lượng khách Nga tăng mạnh +160% YoY; các thị trường truyền thống như Trung Quốc và Hàn Quốc tiếp tục đóng góp ổn định, chiếm ~40% tổng lượt khách quốc tế. Tại Vinpearl, khách từ Trung Đông tăng khoảng 40% YoY, Nga & CIS tăng khoảng 20% và Ấn Độ tăng khoảng 14%. Việc đa dạng hóa này giúp gia tăng giá bán phòng bình quân (ADR) và giảm thiểu rủi ro phụ thuộc vào bất kỳ thị trường đơn lẻ nào."
    )
    add_editorial_note(
        doc,
        "Reference Slide 4, Slide 6 & Slide 7: Tăng trưởng GDP 9M2026 đạt 9,01% YoY (cao nhất 15 năm); CPI 9M2026 tăng 4,52% YoY; Bán lẻ hàng hóa & dịch vụ đạt 5.926 nghìn tỷ đồng (+13,4% YoY); Giải ngân đầu tư công đạt 643 nghìn tỷ đồng (+46,0% YoY, hoàn thành 62,9% kế hoạch năm). Khách quốc tế đến Việt Nam đạt 17,7 triệu lượt (+14,5% YoY, hoàn thành 70,8% mục tiêu năm); Doanh thu du lịch toàn quốc đạt 874 nghìn tỷ đồng (+10,2% YoY, hoàn thành 77,6% kế hoạch năm). Châu Á chiếm 74,5% khách quốc tế; Châu Âu tăng trưởng mạnh nhất (+55,0% YoY), Nga tăng +160,6% YoY. Vinpearl 9M2026: Doanh thu thuần đạt 10.686 tỷ đồng (+18,6% YoY); Lợi nhuận sau thuế đạt 2.829 tỷ đồng (gấp c. 6,6 lần 9M2025: 428 tỷ đồng); Tỷ lệ lấp đầy phòng khách sạn đạt 64% (+9%pt YoY vs 55% trong 9M25); Khách tham quan VinWonders đạt 8,9 triệu lượt (+6% YoY)."
    )
    
    # Section 02
    add_section(doc, 2, "Chiến lược Mở rộng 2 Siêu Quần thể Nghỉ dưỡng Tích hợp: Tuyên Quang & Cần Giờ")
    add_speaker_para(
        doc,
        "Bà Hương – Tổng Giám đốc / CEO, Vinpearl",
        "Để tối đa hóa giá trị cộng hưởng trong hệ sinh thái và đón đầu các cơ hội tăng trưởng dài hạn, Vinpearl đang phát triển 2 siêu quần thể nghỉ dưỡng tích hợp (super-clusters) mới: Quần thể Tuyên Quang tại miền Bắc (khai trương Quý 4/2026) và Siêu quần thể Cần Giờ tại miền Nam (khai trương theo từng phân kỳ từ Quý 3/2027). Mô hình siêu quần thể được thiết kế chuyên biệt nhằm giải quyết bài toán căn bản của du lịch Việt Nam: chuyển hóa lượng khách đông đảo thành thời gian lưu trú dài hơn và mức chi tiêu bình quân cao hơn. Tại TP.HCM, thành phố đón 54 triệu lượt khách năm 2025 nhưng thời gian lưu trú bình quân vẫn dưới 2 đêm. Việc tích hợp toàn diện Khách sạn & Nghỉ dưỡng + Vui chơi Giải trí + Sân Golf + MICE & Chăm sóc sức khỏe trong một điểm đến khép kín giúp kéo dài ngày lưu trú, tối đa hóa chi tiêu bình quân qua bán chéo (cross-selling) và tối ưu chi phí vận hành trên hạ tầng dùng chung."
    )
    add_speaker_para(
        doc,
        None,
        "Tại miền Bắc, Quần thể Tuyên Quang tọa lạc tại Vinhomes Mỹ Lâm (455 ha), kết nối nhanh chóng với Hà Nội qua cao tốc Nội Bài – Lào Cai và cao tốc Tuyên Quang – Phú Thọ (rút ngắn thời gian di chuyển xuống còn 2 giờ). Dự án gồm: Vinpearl Seiko Onsen (4,2 ha, 56 bể khoáng nóng onsen tự nhiên, lớn nhất miền Bắc); Vinpearl Onsen Resort 5 sao (235 phòng khách); Công viên giải trí chủ đề Nhật Bản VinWonders Tuyên Quang (5,4 ha, 20+ trò chơi và đường đua địa hình ATV off-road); Vinpearl Golf Mỹ Lâm 18 hố tiêu chuẩn quốc tế (75,8 ha, thiết kế bởi Golfplan); và Vin New Horizon (2,5 ha, 240 căn hộ) - mô hình dưỡng lão và chăm sóc sức khỏe liên tục (CCRC) đầu tiên tại Việt Nam kết nối trực tiếp với hệ sinh thái y tế Vinmec. Về mặt chiến lược, suối khoáng nóng đạt đỉnh nhu cầu vào mùa thu - đông, bổ trợ hoàn hảo cho danh mục du lịch biển và tạo ra nguồn doanh thu nghịch mùa (counter-seasonal revenue) ổn định quanh năm."
    )
    add_speaker_para(
        doc,
        None,
        "Tại miền Nam, Siêu quần thể Cần Giờ tọa lạc tại trái tim Đại đô thị lấn biển Vinhomes Green Paradise Cần Giờ (2.870 ha), hưởng lợi từ các đại dự án hạ tầng: Cao tốc Bến Lức – Long Thành, Cầu Cần Giờ (thay thế phà Bình Khánh, rút ngắn thời gian về trung tâm TP.HCM xuống 45 phút), Tuyến đường sắt tốc độ cao TP.HCM – Cần Giờ VinSpeed (20 phút) và Cầu vượt biển Cần Giờ – Vũng Tàu (10 phút). Dự án quy tụ: Đại công viên VinWonders Cần Giờ quy mô 122 ha (3 đại công viên chủ đề, 300 trò chơi, 30 show diễn/ngày); Vinpearl Golf Cần Giờ 36 hố đẳng cấp (155 ha, đồng thiết kế bởi Robert Trent Jones II và Tiger Woods); Khách sạn 5 sao Vinpearl Dream Palace (836 phòng, chủ đề du hành thời gian); Bộ sưu tập Khách sạn Boutique (4+ thương hiệu quốc tế: Best Western, iBis, iBis Styles, JO&JOE); 137 căn biệt thự ven biển Bespoke Villas; cùng Tổ hợp Hội nghị & Nhà hát Blue Wave 7 ha (nhà hát 5.000 chỗ ngồi và hội trường 10.000 khách). Dự án mở cửa theo phân kỳ: Ngày 01/07/2027 khai trương công viên, sân golf, khách sạn và villa; Ngày 01/11/2027 khai trương trung tâm hội nghị và nhà hát Blue Wave; giai đoạn tiếp theo phát triển phân khu dưỡng lão cao cấp."
    )
    add_editorial_note(
        doc,
        "Reference Slide 9, Slide 10 & Slide 11: Mô hình Siêu quần thể (Super-Cluster Model): Tích hợp Khách sạn + Giải trí + Golf + MICE/Wellness. Quy mô bổ sung: +2 Siêu quần thể tại 2 miền, +2 công viên VinWonders, +54 hố golf tiêu chuẩn quốc tế. Tuyên Quang (455 ha, khai trương 4Q2026): Vinpearl Seiko Onsen (4,2 ha, 56 bể onsen); Vinpearl Onsen Resort (235 phòng); VinWonders Tuyên Quang (5,4 ha); Vinpearl Golf Mỹ Lâm (75,8 ha, 18 hố); Vin New Horizon (2,5 ha, 240 căn hộ CCRC + Vinmec). Cần Giờ (2.870 ha, khai trương từ 3Q2027): VinWonders Cần Giờ (122 ha, 3 mega parks, 300 trò chơi, 30 show/ngày); Vinpearl Golf Cần Giờ (155 ha, 36 hố, đồng thiết kế bởi Robert Trent Jones II và Tiger Woods); Khách sạn Dream Palace (836 phòng); Boutique Hotels (Best Western, iBis, JO&JOE...); Bespoke Beachfront Villas (137 căn); Trung tâm hội nghị 10.000 khách & Nhà hát Blue Wave 5.000 chỗ (7 ha)."
    )
    
    # Section 03
    add_section(doc, 3, "Kết quả Vận hành Mảng Khách sạn - Nghỉ dưỡng & Khu Vui chơi Giải trí 9T2026")
    add_speaker_para(
        doc,
        "Bà Hương – Tổng Giám đốc / CEO, Vinpearl",
        "Đi sâu vào mảng Khách sạn & Nghỉ dưỡng: Doanh thu hoạt động toàn hệ thống trong 9 tháng đầu năm 2026 đạt 10.304 tỷ đồng (+32% YoY), tương đương 99% doanh thu cả năm 2025. Tăng trưởng đạt được toàn diện cả về giá và sản lượng: Lượng đêm phòng bán đạt 2,24 triệu đêm phòng (+20% YoY); Giá bán phòng bình quân (ADR) đạt 2,95 triệu đồng/đêm (+12% YoY); Nhờ đó doanh thu trên mỗi phòng khả dụng (RevPAR) tăng mạnh 29% YoY lên 1,876 triệu đồng. Tỷ lệ lấp đầy phòng bình quân đạt 64% (+9 điểm phần trăm YoY so với 55% của 9M25 và cao hơn nhiều mức 41% năm 2019). Thời gian lưu trú bình quân kéo dài thêm 10%, giúp tiết giảm chi phí quay vòng phòng và thúc đẩy chi tiêu dịch vụ bổ trợ F&B, spa. Doanh thu tăng trưởng đồng đều trên mọi đơn vị vận hành: Vinpearl tự quản lý (+33% YoY), Marriott (+32% YoY), Meliá (+32% YoY). Trong đó, Nha Trang tiếp tục là điểm đến lớn nhất, đóng góp ~40% tổng doanh thu và gần một nửa mức tăng trưởng của toàn mảng."
    )
    add_speaker_para(
        doc,
        None,
        "Đối với Mảng Khu Vui chơi Giải trí (VinWonders): Doanh thu hoạt động 9 tháng đạt 5.260 tỷ đồng (+28% YoY), biên EBITDA mở rộng thêm 2,5 điểm phần trăm lên mức 63%. Động lực tăng trưởng chủ yếu đến từ việc gia tăng chi tiêu bình quân trên mỗi lượt khách (Revenue per Visit), đạt 589 nghìn đồng (+20% YoY); đặc biệt trong Quý 3 đạt kỷ lục lịch sử 631 nghìn đồng/lượt (+19% YoY), giúp doanh thu Quý 3 tăng 18% YoY dù lượng khách tham quan Quý 3 biến động nhẹ (-2% YoY đạt 2,82 triệu lượt; lũy kế 9 tháng đạt 8,93 triệu lượt, +6% YoY). Du khách tích cực sử dụng các dịch vụ giá trị gia tăng như ẩm thực F&B, vé ưu tiên Fast Pass, VIP tour, quà lưu niệm và các gói combo tích hợp, kết hợp điều chỉnh giá vé hợp lý. Ba quần thể nòng cốt Nha Trang, Phú Quốc và Nam Hội An tăng trưởng doanh thu 34% YoY, chiếm xấp xỉ 94% tổng mức tăng trưởng doanh thu toàn mảng; trong đó Vinpearl Safari Phú Quốc dẫn đầu với doanh thu 9 tháng tăng trưởng khoảng +51% YoY. Nhờ cơ cấu chi phí cố định lớn, phần doanh thu gia tăng từ dịch vụ biên cao đã chuyển hóa trực tiếp vào lợi nhuận thuần, tạo đòn bẩy biên EBITDA mạnh mẽ."
    )
    add_editorial_note(
        doc,
        "Reference Slide 13 & Slide 14: Vận hành Khách sạn & Nghỉ dưỡng 9M2026: Đêm phòng bán đạt 2.244 nghìn (+20% YoY vs 1.872 nghìn 9M25); RevPAR đạt 1.876 nghìn đồng (+29% YoY vs 1.455 nghìn đồng); ADR đạt 2,95 triệu đồng (+12% YoY vs 2,64 triệu đồng); Doanh thu hoạt động hệ thống đạt 10.304 tỷ đồng (+32% YoY vs 7.778 tỷ đồng); Doanh thu cơ sở thuộc sở hữu Vinpearl đạt 4.654 tỷ đồng (+22% YoY vs 3.823 tỷ đồng); Tỷ lệ lấp đầy phòng đạt 64% (+9%pt YoY vs 55% 9M25, 41% năm 2019). Vận hành Công viên Giải trí VinWonders 9M2026: Lượt khách tham quan đạt 8.930 nghìn (+6% YoY vs 8.417 nghìn); Doanh thu bình quân trên khách đạt 589 nghìn đồng (+20% YoY vs 489 nghìn đồng); Quý 3 đạt kỷ lục 631 nghìn đồng (+19% YoY); Doanh thu hoạt động mảng công viên đạt 5.260 tỷ đồng (+28% YoY vs 4.119 tỷ đồng); Doanh thu cơ sở thuộc sở hữu đạt 4.590 tỷ đồng (+29% YoY vs 3.570 tỷ đồng); Biên EBITDA mở rộng lên 63% (+2,5%pt YoY vs 60% trong 9M25). Quần thể lõi (Nha Trang, Phú Quốc, Nam Hội An) tăng trưởng +33,8% YoY, chiếm ~94% tăng trưởng; Vinpearl Safari Phú Quốc tăng ~51% YoY."
    )
    
    # Section 04
    add_section(doc, 4, "Kết quả Tài chính Hợp nhất 9T2026 & Sức mạnh Bảng Cân đối Kế toán")
    add_speaker_para(
        doc,
        "Bà Hương – Tổng Giám đốc / CEO, Vinpearl",
        "Về kết quả tài chính hợp nhất theo chuẩn mực kế toán Việt Nam (VAS): Lũy kế 9 tháng đầu năm 2026, Doanh thu thuần hợp nhất đạt 10.686 tỷ đồng (+18,6% YoY so với 9.014 tỷ đồng). Doanh thu mảng cốt lõi (Khách sạn & Vui chơi giải trí) tăng trưởng 27% YoY đạt 10.439 tỷ đồng (so với 8.250 tỷ đồng). Lợi nhuận gộp đạt 3.242 tỷ đồng (+33,0% YoY so với 2.438 tỷ đồng); Biên lợi nhuận gộp mảng cốt lõi mở rộng mạnh mẽ từ 23% lên 32%. Thu nhập tài chính thuần ghi nhận 468 tỷ đồng (so với 47 tỷ đồng trong 9M25); Lợi nhuận thuần từ hoạt động kinh doanh đạt 1.578 tỷ đồng (+172,6% YoY so với 579 tỷ đồng); Thu nhập khác đạt 1.706 tỷ đồng. Lợi nhuận trước thuế (PBT) đạt 3.285 tỷ đồng (+524,6% YoY so với 526 tỷ đồng). Lợi nhuận sau thuế (PAT) đạt 2.829 tỷ đồng, tăng gấp ~6,6 lần (+560,7% YoY so với 428 tỷ đồng trong 9M25). EBITDA hợp nhất đạt 3.950 tỷ đồng (+18% YoY so với 3.323 tỷ đồng); Biên EBITDA mảng cốt lõi mở rộng từ 34% lên 37%. Sau 9 tháng, công ty đã hoàn thành 67% kế hoạch doanh thu và 94% kế hoạch lợi nhuận sau thuế cả năm 2026."
    )
    add_speaker_para(
        doc,
        None,
        "Về sức mạnh Bảng cân đối kế toán: Tổng vốn chủ sở hữu tại ngày 30/09/2026 đạt 46.010 tỷ đồng (+28% YoY so với 35.924 tỷ đồng tại Sep-25). Tổng tài sản mở rộng 46% YoY lên 129.009 tỷ đồng (so với 88.620 tỷ đồng tại Sep-25) nhằm tài trợ cho đường ống phát triển các siêu quần thể mới. Tỷ lệ Nợ vay thuần trên Vốn chủ sở hữu (Net Debt / Equity) ghi nhận ở mức 46,3%, duy trì an toàn trong biên độ đòn bẩy thận trọng và giảm rất sâu so với mức 785,9% năm 2019 và 89,3% năm 2023. Tỷ lệ Tổng nợ vay trên Tổng tài sản duy trì ở mức thấp 17,1%. Cấu trúc vốn vững chắc cùng việc Ngân hàng Nhà nước miễn trừ tín dụng du lịch khỏi hạn ngạch bất động sản tạo nền tảng vững vàng để công ty triển khai các siêu dự án mới."
    )
    add_editorial_note(
        doc,
        "Reference Slide 15, Slide 16 & Slide 17: Báo cáo Tài chính Hợp nhất (VAS): Doanh thu thuần 3Q26 đạt 3.892 tỷ đồng (+25,5% YoY); 9M26 đạt 10.686 tỷ đồng (+18,6% YoY vs 9.014 tỷ). Lợi nhuận gộp 3Q26 đạt 917 tỷ đồng (+11,9% YoY); 9M26 đạt 3.242 tỷ đồng (+33,0% YoY vs 2.438 tỷ). Biên lợi nhuận gộp mảng cốt lõi đạt 32% (vs 23% 9M25). Lợi nhuận trước thuế 3Q26 đạt 766 tỷ đồng (+427,5% YoY); 9M26 đạt 3.285 tỷ đồng (+524,6% YoY vs 526 tỷ). Lợi nhuận sau thuế 3Q26 đạt 649 tỷ đồng (+283,0% YoY); 9M26 đạt 2.829 tỷ đồng (+560,7% YoY vs 428 tỷ), hoàn thành ~94% kế hoạch năm. EBITDA hợp nhất 9M26 đạt 3.950 tỷ đồng (+18% YoY vs 3.323 tỷ). Bảng cân đối kế toán tại 30/09/2026: Tổng tài sản đạt 129.009 tỷ đồng (+46% YoY); Vốn chủ sở hữu đạt 46.010 tỷ đồng (+28% YoY); Tỷ lệ Net Debt / Equity ở mức 46,3%; Tỷ lệ Total Debt / Total Assets ở mức 17,1%."
    )
    
    # Section 05
    add_section(doc, 5, "Kế hoạch Kinh doanh & Triển vọng Cho Giai đoạn Còn Lại của Năm 2026")
    add_speaker_para(
        doc,
        "Bà Hương – Tổng Giám đốc / CEO, Vinpearl",
        "Hướng tới giai đoạn còn lại của năm tài chính 2026, Vinpearl duy trì quỹ đạo tăng trưởng vững chắc và tự tin hoàn thành toàn diện kế hoạch cả năm: Doanh thu thuần hợp nhất mục tiêu 16.000 tỷ đồng (+3% so với thực hiện 2025) và Lợi nhuận sau thuế mục tiêu 3.000 tỷ đồng (+172% so với thực hiện 2025). Sau 9 tháng, công ty đã hoàn thành tương ứng 67% kế hoạch doanh thu và 94% kế hoạch lợi nhuận. Chúng tôi bước vào Quý 4 – mùa cao điểm truyền thống của du khách quốc tế – với động lực vận hành rất mạnh mẽ: Phú Quốc chuyển sang mùa cao điểm du lịch đẹp nhất trong năm (tháng 11 đến tháng 3); mùa bay charter đón khách Nga & CIS khởi động sớm hơn năm trước; giá phòng bình quân và chi tiêu bình quân duy trì đà tăng; và việc ra mắt Quần thể Tuyên Quang trong Quý 4 sẽ tạo động cơ tăng trưởng nghịch mùa mới. Về vĩ mô, kịch bản tăng trưởng 2H2026 của Chính phủ đạt 11,9% cùng các giải pháp chiến lược thúc đẩy toàn ngành du lịch tiếp tục tạo môi trường thuận lợi. Tóm lại, Vinpearl hiện tại đạt mức sinh lời cao hơn, sở hữu cơ cấu khách hàng đa dạng hơn và đường ống các siêu quần thể mang lại tầm nhìn tăng trưởng rõ ràng cho năm 2027 và tương lai."
    )
    add_editorial_note(
        doc,
        "Reference Slide 19: Kế hoạch Kinh doanh FY2026: Doanh thu thuần mục tiêu 16.000 tỷ đồng (+3% vs thực hiện 2025, 9M hoàn thành 67%); Lợi nhuận sau thuế mục tiêu 3.000 tỷ đồng (+172% vs thực hiện 2025, 9M hoàn thành 94%). Động lực cốt lõi: Mùa cao điểm quốc tế Quý 4; Phú Quốc vào mùa đẹp nhất; Mùa charter Nga & CIS khởi động sớm; Khai trương Quần thể Nghỉ dưỡng Tuyên Quang; Kịch bản tăng trưởng vĩ mô 2H2026 đạt 11,9%."
    )
    
    # Section 06: Q&A
    add_section(doc, 6, "Phiên Đối đáp và Trả lời Câu hỏi với Nhà Đầu tư (Live Q&A Session)")
    add_speaker_para(
        doc,
        "Điều phối viên / Ban IR",
        "Phần trình bày của Ban Điều hành đến đây là kết thúc. Sau đây, chúng tôi xin chuyển quyền điều phối phiên Hỏi – Đáp cho Bà Mai Hương, Giám đốc Đầu tư của Vinpearl."
    )
    
    qa_list = [
        ("Chuyên viên Phân tích: Nguyên nhân suy giảm biên lợi nhuận gộp trong Quý 3/2026?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Sự suy giảm nhẹ của biên lợi nhuận gộp trong Quý 3 phản ánh 2 yếu tố: (1) Ghi nhận trọn vẹn chi phí 1 quý của công viên VinWonders Vũ Yên đang trong giai đoạn đầu vận hành (ramping-up); (2) Vinpearl Hạ Long chuyển đổi sang mô hình nhận quyền quản lý (chỉ ghi nhận phí quản lý thay vì toàn bộ doanh thu/chi phí). Nếu loại trừ 2 yếu tố này, biên lợi nhuận gộp cốt lõi nền tảng vẫn duy trì ổn định và có xu hướng cải thiện nhờ ADR và chi tiêu trên mỗi lượt khách tăng."),
        
        ("Bà Trang Nguyễn: Động lực tăng trưởng doanh thu tài chính trong Quý 3/2026 trong môi trường lãi suất cao?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Doanh thu tài chính Q3 tăng mạnh YoY chủ yếu nhờ vị thế tiền mặt dồi dào từ các hợp đồng hợp tác kinh doanh (BCC) và tiền trả trước của khách hàng tại các dự án mở bán trong năm (như Vinpearl Làng Vân); đồng thời công ty tối ưu hóa tiền gửi ngắn hạn và cho vay các bên liên quan nội bộ theo lãi suất thị trường."),
         
        ("Bà Trang Nguyễn: Tại sao biên gộp mảng BĐS Quý 3 chỉ đạt ~10% và Cập nhật nguồn vốn 55 triệu USD cổ phiếu ưu đãi chuyển đổi?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Doanh thu BĐS ghi nhận theo tiến độ bàn giao từng dự án. Doanh thu Q3 chủ yếu từ việc bàn giao tại dự án Vũ Yên và điều chỉnh chi phí hỗ trợ lãi suất từ các dự án đã bàn giao trước đây, làm giảm biên gộp BĐS tạm thời. Công ty đã hoàn tất huy động 55 triệu USD qua cổ phiếu ưu đãi cổ tức chuyển đổi để củng cố vốn chủ sở hữu tài trợ đầu tư trong 12 tháng tới."),
         
        ("Tâm Nguyễn: Cập nhật mức lãi suất cho vay đang áp dụng đối với các bên liên quan nội bộ?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Các khoản vay cung cấp cho các bên liên quan đều được xác định theo nguyên tắc thị trường, hiện tại áp dụng ở mức 12%/năm."),
         
        ("Trúc: Tỷ trọng đóng góp của Quần thể Phú Quốc vào doanh thu và EBITDA 9T2026 & Triển vọng APEC 2027?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Quần thể Phú Quốc tạo ra khoảng 2.500 tỷ đồng doanh thu trong 9T2026, chiếm xấp xỉ 24% tổng doanh thu toàn công ty, tăng trưởng 35% YoY và đóng góp rất tích cực vào EBITDA. Triển vọng 2027 duy trì khả quan khi nguồn cung mới được hấp thụ tốt nhờ mở rộng công suất sân bay và hạ tầng giao thông. Sự kiện APEC 2027 và các dự án giao thông sẽ hỗ trợ tăng trưởng dài hạn cho Phú Quốc sang các năm sau 2027. Lượng đặt phòng sớm (pre-booking) cho mùa cao điểm tại Phú Quốc đang ghi nhận tỷ lệ rất tích cực."),
         
        ("Bà Trang Nguyễn: Tại sao lượt khách VinWonders Q3 giảm 2% và Kế hoạch đạt mục tiêu 15 triệu lượt cả năm? Kế hoạch CapEx?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Lượt khách Q3 giảm nhẹ do mưa bão nhiều hơn cùng kỳ tại miền Bắc và miền Trung, tập trung ở các điểm vui chơi riêng lẻ. Tại các đại quần thể cốt lõi, lượng khách vẫn tăng ~10% YoY và chi tiêu/khách tăng ~20% (Q3 đạt kỷ lục 631 nghìn đồng/lượt), giúp doanh thu công viên Q3 vẫn tăng 18% YoY. Mục tiêu 15 triệu lượt khách cả năm là thách thức lớn, kỳ vọng mùa cao điểm quốc tế tại Phú Quốc sẽ hỗ trợ. Tuy nhiên, ưu tiên chiến lược của Vinpearl là bảo đảm doanh thu và hiệu quả lợi nhuận thay vì chạy theo số lượng khách làm tổn hại tỷ suất sinh lời. CapEx được giải ngân linh hoạt theo tiến độ và dòng tiền hoạt động, tập trung vào tài sản vận hành như Tuyên Quang và Làng Vân."),
         
        ("Nhật Phạm: Kỳ vọng của Ban Điều hành về tốc độ tăng trưởng giá bán phòng bình quân (ADR) trong các năm tới?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Chúng tôi kỳ vọng mức tăng trưởng ADR bình quân hàng năm đạt khoảng 15% trong các năm tới, với định hướng trọng tâm là tối đa hóa giá bán phòng trong mùa du lịch cao điểm. Tại một số điểm đến trọng điểm có sức hút lớn, tăng trưởng ADR có thể đạt mức cao hơn."),
         
        ("Tâm Nguyễn: Nợ phải trả mảng phát triển và chuyển nhượng BĐS chiếm 60% tổng nợ, kế hoạch xử lý ra sao?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Phần lớn nợ phải trả mảng BĐS là tiền khách hàng trả trước, vốn góp theo hợp đồng hợp tác kinh doanh (BCC) và nợ vay tài trợ dự án; các khoản này sẽ được tất toán và chuyển hóa thành doanh thu khi bàn giao sản phẩm nhà ở/BĐS cho khách hàng."),
         
        ("Trúc: Kỳ vọng RevPAR/ADR Dự án Tuyên Quang và Biến động Dư nợ vay Quý 3?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Dự án Tuyên Quang mở cửa trong Quý 4/2026, kỳ vọng các chỉ số RevPAR và ADR ban đầu sẽ tương đồng với giai đoạn đầu vận hành của các dự án tại miền Bắc. Về nợ vay: Trong Quý 3/2026, dư nợ vay chỉ tăng 1,2 nghìn tỷ đồng lên 22 nghìn tỷ đồng vào cuối quý, chủ yếu từ khoản vay dài hạn bổ sung để tài trợ cho hoạt động kinh doanh."),
         
        ("Trúc: Số lượng khách sạn, số phòng và biệt thự tại Cần Giờ? Kỳ vọng RevPAR/ADR năm 2027 và Doanh thu BĐS?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Cần Giờ gồm Khách sạn Vinpearl Dream Palace (836 phòng) mở cửa tháng 7/2027, các khách sạn boutique quốc tế (Best Western, iBis, JO&JOE) và 137 căn biệt thự ven biển Bespoke. Dự án Phú Quốc tiếp tục ghi nhận doanh thu BĐS trong năm 2027; dự án Làng Vân (Đà Nẵng) đã mở bán năm nay và dự kiến bắt đầu ghi nhận doanh thu từ năm 2027 tùy thuộc tiến độ bàn giao."),
         
        ("Phương Hoàng: Biên lợi nhuận gộp Q3 loại trừ Khấu hao VinWonders và Chuyển đổi mô hình Vinpearl Hạ Long?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Biên lợi nhuận gộp của VinWonders đạt khoảng 70% nếu loại trừ chi phí khấu hao; tác động từ việc chuyển đổi Vinpearl Hạ Long sang mô hình nhận quyền quản lý làm giảm biên gộp hợp nhất toàn công ty khoảng 2,5 điểm phần trăm."),
         
        ("Trúc: Quyền lợi Kinh tế tại Quần thể Tuyên Quang và Cần Giờ? Có hợp nhất 100% doanh thu/lợi nhuận không?",
         "Bà Mai Hương – Giám đốc Đầu tư, Vinpearl",
         "Tại Tuyên Quang, Vinpearl hưởng lợi và hợp nhất toàn bộ kết quả kinh doanh từ mảng Khách sạn và VinWonders; hợp phần dưỡng lão Vin New Horizon không thuộc phạm vi hợp nhất. Tại Cần Giờ, quyền lợi kinh tế phân bổ giữa tài sản tự sở hữu và nhận quyền quản lý vận hành, thông tin chi tiết sẽ công bố sau.")
    ]
    
    for q_title, a_spk, a_text in qa_list:
        add_speaker_para(doc, None, q_title)
        add_speaker_para(doc, a_spk, a_text)
        
    add_speaker_para(
        doc,
        "Điều phối viên / Ban IR",
        "Thời lượng phiên Q&A hôm nay đã kết thúc. Xin lưu ý Tập đoàn Vingroup sẽ tổ chức Earnings Call Quý 3/2026 vào ngày 30 tháng 10 năm 2026. Xin chân thành cảm ơn quý vị!"
    )
    
    doc.save(os.path.join(OUT_DIR, "VPL_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx"))
    doc.save(os.path.join(OUT_ROOT, "VPL_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx"))
    print("[✓] Đã tạo thành công VPL_Earnings_Call_3Q2026_Transcript_Bien_Tap.docx (đầy đủ Q&A)")

def build_english_docx():
    print("[*] Đang khởi tạo bản tiếng Anh: VPL_Earnings_Call_3Q2026_Script_EN.docx...")
    doc = setup_document()
    
    add_header(
        doc,
        title_text="VINPEARL | Earnings Call Transcript",
        subtitle_text="3Q2026 and 9M2026 Financial Results & Strategic Update",
        speakers_text="[Moderator / IR Team] (Investor Relations, Vinpearl); [Ms. Huong] (Chief Executive Officer, Vinpearl); [Mr. Duy Tran] (Chief Financial Officer, Vinpearl); [Ms. Hanh Nguyen] (Chief Accountant, Vinpearl); [Ms. Mai Huong] (Director of Investment, Vinpearl)."
    )
    
    # Section 01
    add_section(doc, 1, "Macro Landscape & Vietnam Tourism Sector Dynamics 9M2026")
    add_speaker_para(
        doc,
        "Moderator – IR Team, Vinpearl",
        "Good afternoon, esteemed investors, financial analysts, and conference participants. Welcome to Vinpearl Joint Stock Company's 3Q and 9M2026 Earnings Call. Before we begin, please note that all participants will be muted for the presentation, followed by a live Q&A session. This call is conducted in English and recorded. Earnings materials are available online on our website at vinpearl.com. Joining us today from executive management are Ms. Huong, CEO; Mr. Duy Tran, CFO; Ms. Hanh Nguyen, Chief Accountant; and Ms. Mai Huong, Director of Investment. I will now turn the floor over to Ms. Huong, CEO of Vinpearl, for the management presentation."
    )
    add_speaker_para(
        doc,
        "Ms. Huong – CEO, Vinpearl",
        "Thank you, and good afternoon, everyone. Vietnam's economy grew over 9% in the first nine months of 2026 (+9.01% YoY), representing the fastest 9-month GDP growth in 15 years, while CPI inflation was closely monitored at 4.52%, marginally above the National Assembly's 4.5% target. Concurrently, Vietnam's tourism sector maintained strong upward momentum: international tourist arrivals reached nearly 18 million (+14.5% YoY, fulfilling 70.8% of the full-year target), while nationwide tourism revenue reached VND 874 trillion (+10.2% YoY, achieving 77.6% of the annual plan)."
    )
    add_speaker_para(
        doc,
        None,
        "Against this supportive macro backdrop, Vinpearl delivered solid operating and financial performance in 9M2026: Consolidated net revenue reached VND 10,686 billion (+18.6% YoY), and Profit After Tax reached VND 2,829 billion, expanding approximately 6.6-fold compared to 9M2025 (VND 428 billion). At the operating level, both our hotels and amusement parks demonstrated faster EBITDA growth than revenue, evidencing that our business model's operating leverage is translating powerfully into bottom-line earnings. In terms of operations, hotel occupancy reached 64% in 9M2026 (+9 percentage points YoY vs. 55% in 9M25 and well above 41% pre-Covid), while VinWonders recorded 8.93 million visits (+6% YoY). Importantly, growth is increasingly driven not just by visitor numbers, but by longer guest stays (+10% YoY) and higher spending per guest across our facilities, demonstrating clear quality improvement in our growth profile."
    )
    add_speaker_para(
        doc,
        None,
        "Looking into domestic macro drivers: Domestic travelers account for approximately 40% of our hotel guests and form the core visitor base for VinWonders. Domestic retail sales of goods and consumer services rose 13.4% YoY to VND 5,926 trillion, supported by an expanding middle class. Public investment disbursement accelerated to VND 643 trillion (+46% YoY, reaching 62.9% of the annual budget), with substantial allocation to airports, expressways, and railways that directly enhance connectivity to our destinations. Disbursed FDI rose 12.1% YoY to a 5-year 9-month peak, stimulating business travel and MICE demand. On the policy front, Resolution 168 outlines an 11.9% GDP growth scenario for 2H2026; SBV Dispatch No. 8509 explicitly exempts hospitality loans from real estate credit quotas; and Resolution No. 26-NQ/TW firmly establishes tourism as a spearhead national economic sector, targeting 10-12% direct GDP contribution and 45-50 million international arrivals by 2030."
    )
    add_speaker_para(
        doc,
        None,
        "Regarding international inbound markets, source market diversification is accelerating: Europe emerged as the fastest-growing source region (+55% YoY), led by Russia (+160.6% YoY), while traditional markets China and South Korea remain resilient, together representing ~40% of total inbound arrivals. At Vinpearl, hotel guests from the Middle East surged ~40% YoY, Russia & CIS (our second largest international source market) grew ~20%, and India increased ~14%. Guests from these emerging markets stay longer and spend more, driving higher ADR across our portfolio while mitigating single-market concentration risk."
    )
    add_editorial_note(
        doc,
        "Reference Slide 4, Slide 6 & Slide 7: 9M2026 Macro & Tourism Highlights: Vietnam GDP growth reached 9.01% YoY (15-year high); CPI increased 4.52% YoY; Retail sales reached VND 5,926 trillion (+13.4% YoY); Public investment disbursement totaled VND 643 trillion (+46.0% YoY, 62.9% of budget); Inbound international arrivals reached 17.7 million (+14.5% YoY, 70.8% of FY target); Tourism revenue totaled VND 874 trillion (+10.2% YoY, 77.6% of FY plan). Asia accounts for 74.5% of arrivals (+7.6% YoY); Europe grew fastest (+55.0% YoY), led by Russia (+160.6% YoY). Vinpearl 9M2026 Highlights: Net revenue VND 10,686 bn (+18.6% YoY); Profit After Tax VND 2,829 bn (c. 6.6x vs. VND 428 bn in 9M25); Occupancy rate 64% (+9%pt YoY vs 55% in 9M25); VinWonders visits reached 8.93 million (+6% YoY)."
    )
    
    # Section 02
    add_section(doc, 2, "Strategic Expansion: Two New Integrated Super-Clusters (Tuyen Quang & Can Gio)")
    add_speaker_para(
        doc,
        "Ms. Huong – CEO, Vinpearl",
        "To maximize ecosystem synergy and capture structural tourism demand, we are developing two new landmark integrated super-clusters: Tuyen Quang in Northern Vietnam (opening 4Q2026) and Can Gio in Southern Vietnam (phased opening starting 3Q2027). The super-cluster model specifically addresses a fundamental structural bottleneck in Vietnam's tourism industry: converting high visitor volume into extended lengths of stay and higher spend per guest. In Ho Chi Minh City, for instance, the city welcomed 54 million visitors in 2025 (including 8.5 million international arrivals), yet the average length of stay remained under two nights. By seamlessly integrating Hotels & Resorts + Entertainment + Golf Courses + MICE/Wellness within a self-contained destination, we extend stay duration, capture greater guest wallet share via cross-selling and upselling, and drive operational cost efficiencies through shared infrastructure."
    )
    add_speaker_para(
        doc,
        None,
        "In the North, Tuyen Quang Cluster is located within Vinhomes My Lam (455 ha), approximately 2 hours from Hanoi via the Noi Bai – Lao Cai and Tuyen Quang – Phu Tho expressways. The cluster features: Vinpearl Seiko Onsen (4.2 ha, 56 natural onsen baths, the largest Japanese-style hot spring retreat in Northern Vietnam); Vinpearl Onsen Resort (235 5-star guest rooms); VinWonders Tuyen Quang (5.4 ha, Northern Vietnam's first Japan-themed amusement park with 20+ family attractions and off-road ATV courses); Vinpearl Golf My Lam (75.8 ha, 18-hole championship course designed by Golfplan); and Vin New Horizon (2.5 ha, 240 units) – Vietnam's inaugural Continuing Care Retirement Community (CCRC) model integrated with Vinmec healthcare facilities. Strategically, onsen wellness demand peaks during the cooler autumn-winter months when beach holiday demand softens, generating highly accretive counter-seasonal revenue that stabilizes our annual earnings profile."
    )
    add_speaker_para(
        doc,
        None,
        "In the South, Can Gio Super-Cluster is situated at the center of the 2,870-ha Vinhomes Green Paradise coastal township in Ho Chi Minh City. Connectivity is enhanced by the Ben Luc – Long Thanh Expressway, Can Gio Bridge (replacing Binh Khanh ferry, 45 mins to central HCMC), the VinSpeed high-speed railway (20 mins), and the Can Gio – Vung Tau sea-crossing bridge (10 mins). Key components include: VinWonders Can Gio (122 ha, 3 mega theme parks, 300 rides, 30 daily shows, 365-day festival experience); Vinpearl Golf Can Gio (155 ha, 36-hole masterpiece co-designed by Robert Trent Jones II and Tiger Woods); Vinpearl Dream Palace Hotel (836 5-star rooms, Vietnam's first time-travel themed luxury hotel); Boutique Hotel Collection (4+ international brands: Best Western, iBis, iBis Styles, JO&JOE); 137 Bespoke Beachfront Villas; and a 7-ha Convention Center & Blue Wave Theatre complex (5,000-seat theater and 10,000-guest convention hall). Phased openings are slated for July 1, 2027 (parks, golf, hotels & villas), November 1, 2027 (convention center and theater), followed post-2027 by senior living communities."
    )
    add_editorial_note(
        doc,
        "Reference Slide 9, Slide 10 & Slide 11: Super-Cluster Model: Integration of Hotels + Entertainment + Golf + MICE/Wellness. Scale additions: +2 Super-clusters in North & South, +2 VinWonders theme parks, +54 golf holes. Tuyen Quang Cluster (455 ha, opening 4Q2026): Vinpearl Seiko Onsen (4.2 ha, 56 onsen baths); Vinpearl Onsen Resort (235 rooms); VinWonders Tuyen Quang (5.4 ha); Vinpearl Golf My Lam (75.8 ha, 18 holes, Golfplan); Vin New Horizon (2.5 ha, 240 CCRC units + Vinmec). Can Gio Super-Cluster (2,870 ha, opening 3Q2027): VinWonders Can Gio (122 ha, 3 mega parks, 300 rides, 30 shows/day); Vinpearl Golf Can Gio (155 ha, 36 holes, RTJ II & Tiger Woods); Dream Palace Hotel (836 rooms); Boutique Hotels (Best Western, iBis, JO&JOE); Bespoke Villas (137 units); Convention Center (10,000 guests) & Blue Wave Theatre (5,000 seats)."
    )
    
    # Section 03
    add_section(doc, 3, "Operational Performance: Hotels, Resorts and VinWonders Amusement Parks")
    add_speaker_para(
        doc,
        "Ms. Huong – CEO, Vinpearl",
        "Examining our hospitality operations: Total system-wide hotel operating revenue in 9M2026 reached VND 10,304 billion (+32% YoY vs. VND 7,778 bn in 9M25), already matching ~99% of full-year 2025 revenue within 9 months. Growth was broad-based across volume and rates: Room nights sold rose 20% YoY to 2.24 million in 9M2026 (3Q: 744k, +9% YoY); ADR advanced 12% YoY to VND 2.95 million (3Q: VND 2.94m, +10% YoY); driving RevPAR up 29% YoY to VND 1.876 million (3Q: VND 1.835m, +17% YoY). System occupancy reached 64% (+9%pt YoY vs. 55% in 9M25 and 41% in 2019). Average length of stay extended 10% YoY, dampening room turnover costs while lifting ancillary spending on F&B and wellness. Revenue expanded consistently across operating partners: Vinpearl-managed (+33% YoY), Marriott-managed (+32% YoY), and Meliá-managed (+32% YoY). Nha Trang remained our largest destination anchor, contributing ~40% of hotel revenue and nearly half of total hospitality growth."
    )
    add_speaker_para(
        doc,
        None,
        "In our Amusement Parks business (VinWonders): 9M2026 operating revenue reached VND 5,260 billion (+28% YoY vs. VND 4,119 bn), with EBITDA margin expanding by 2.5 percentage points YoY to 63%. Performance was primarily driven by higher spending per visitor rather than volume: 9M visits grew 6% YoY to 8.93 million, while revenue per visit rose 20% YoY to VND 589k. Notably in 3Q2026, revenue per visit reached a record quarterly high of VND 631k (+19% YoY), elevating quarterly revenue by 18% YoY despite stable visitor volumes (2.82 million visits, -2% YoY). Spending uplift was underpinned by strong guest adoption of premium value-added offerings (F&B packages, Fast Passes, VIP tours, merchandise) and modest ticket adjustments. Core parks in Nha Trang, Phu Quoc, and Nam Hoi An grew combined revenue by 33.8% YoY, delivering ~94% of segment revenue growth, led by Vinpearl Safari Phu Quoc (+51% YoY in 9M). Because incremental revenue flows from high-margin services over a fixed cost infrastructure, significant gains flowed directly to operating profits."
    )
    add_editorial_note(
        doc,
        "Reference Slide 13 & Slide 14: Hospitality Key Metrics 9M2026: Room Nights Sold reached 2,244k (+20% YoY); RevPAR reached VND 1,876k (+29% YoY); ADR reached VND 2.95m (+12% YoY); Total operating revenue VND 10,304 bn (+32% YoY vs. VND 7,778 bn); Owned-properties revenue VND 4,654 bn (+22% YoY vs. VND 3,823 bn); Occupancy rate 64% (+9%pt YoY vs. 55% 9M25, 41% 2019). Amusement Parks Key Metrics 9M2026: Total visits reached 8,930k (+6% YoY); Rev per visit VND 589k (+20% YoY); 3Q26 Rev per visit reached record VND 631k (+19% YoY); Operating revenue VND 5,260 bn (+28% YoY vs. VND 4,119 bn); Owned-properties revenue VND 4,590 bn (+29% YoY vs. VND 3,570 bn); EBITDA margin expanded to 63% (+2.5%pt YoY vs. 60% 9M25). Core parks (Nha Trang, Phu Quoc, Nam Hoi An) up +33.8% YoY, generating ~94% of total revenue growth; Safari Phu Quoc up ~51% YoY."
    )
    
    # Section 04
    add_section(doc, 4, "Consolidated Financial Performance & Resilient Balance Sheet")
    add_speaker_para(
        doc,
        "Ms. Huong – CEO, Vinpearl",
        "Turning to consolidated VAS financial highlights: In 9M2026, consolidated net revenue reached VND 10,686 billion (+18.6% YoY vs. VND 9,014 bn). Core hospitality and entertainment revenue grew even faster at +26.5% YoY to VND 10,439 billion (vs. VND 8,250 bn). Gross profit expanded 33.0% YoY to VND 3,242 billion (vs. VND 2,438 bn), with core gross profit margin widening meaningfully from 23% to 32%. Net financial income reached VND 468 billion (vs. VND 47 bn in 9M25); Operating profit rose 172.6% YoY to VND 1,578 billion (vs. VND 579 bn); and Net other income stood at VND 1,706 billion. Profit Before Tax surged 524.6% YoY to VND 3,285 billion (vs. VND 526 bn). Profit After Tax reached VND 2,829 billion, a 6.6-fold increase (+560.7% YoY vs. VND 428 bn). Consolidated EBITDA reached VND 3,950 billion (+18% YoY vs. VND 3,323 bn), with core EBITDA margin widening from 34% to 37%. In the first 9 months, Vinpearl has achieved ~67% of its full-year revenue target and ~94% of its full-year profit target."
    )
    add_speaker_para(
        doc,
        None,
        "On capital structure: Total equity expanded 28% YoY to VND 46,010 billion as of September 30, 2026 (vs. VND 35,924 bn as of Sep-25). Total assets expanded 46% YoY to VND 129,009 billion (vs. VND 88,620 bn as of Sep-25), reflecting capital mobilized to fund our landmark super-cluster pipeline. The Net Debt to Equity ratio stood prudently at 46.3% (vs. 20.4% at Sep-25 and 27.0% at FY2025, dramatically reduced from 785.9% in 2019 and 89.3% in 2023). Total Debt to Total Assets remained conservative at 17.1%. This resilient balance sheet and supportive SBV lending guidelines ensure sufficient financial bandwidth to execute our pipeline within prudent risk limits."
    )
    add_editorial_note(
        doc,
        "Reference Slide 15, Slide 16 & Slide 17: Consolidated VAS Financials: 3Q26 Net Revenue VND 3,892 bn (+25.5% YoY); 9M26 Net Revenue VND 10,686 bn (+18.6% YoY vs. VND 9,014 bn). 9M26 Core Revenue VND 10,439 bn (+26.5% YoY). 9M26 Gross Profit VND 3,242 bn (+33.0% YoY); Core gross margin expanded to 32% (vs 23% 9M25). 9M26 PBT VND 3,285 bn (+524.6% YoY vs. VND 526 bn). 9M26 PAT VND 2,829 bn (+560.7% YoY vs. VND 428 bn), achieving ~94% of FY2026 budget. 9M26 Consolidated EBITDA VND 3,950 bn (+18% YoY vs. VND 3,323 bn). Balance Sheet at Sep 30, 2026: Total Assets VND 129,009 bn (+46% YoY); Total Equity VND 46,010 bn (+28% YoY); Net Debt / Equity 46.3%; Total Debt / Total Assets 17.1%."
    )
    
    # Section 05
    add_section(doc, 5, "Business Plan Execution & FY2026 Full-Year Outlook")
    add_speaker_para(
        doc,
        "Ms. Huong – CEO, Vinpearl",
        "Looking ahead to the remainder of 2026, Vinpearl remains on a solid growth trajectory, firmly positioned to deliver our full-year targets: Targeted Consolidated Revenue of VND 16,000 billion (+3% vs. 2025 actuals) and Targeted Profit After Tax of VND 3,000 billion (+172% vs. 2025 actuals). Having completed 67% and 94% of these respective targets in 9M2026, we enter the fourth-quarter peak international inbound season with strong momentum: Phu Quoc is transitioning from the rainy season into its prime travel period (November to March); Russian and CIS charter flight operations commenced earlier than last year; average room rates and visitor spending continue to expand; and the Q4 launch of Tuyen Quang Cluster will unlock a new counter-seasonal growth engine. With supportive macro GDP targets of 11.9% in 2H2026 and national tourism policy tailwinds, Vinpearl is more profitable and diversified than ever, with clear growth visibility extending into 2027 and beyond."
    )
    add_editorial_note(
        doc,
        "Reference Slide 19: FY2026 Guidance & Outlook: Target Consolidated Revenue VND 16,000 bn (+3% vs. 2025 actuals, 67% completed in 9M); Target Profit After Tax VND 3,000 bn (+172% vs. 2025 actuals, 94% completed in 9M). Core drivers: Q4 international peak season; Phu Quoc peak weather window; Early Russia & CIS charter season; Launch of Tuyen Quang wellness cluster; Macro 2H2026 GDP growth target of 11.9%."
    )
    
    # Section 06: Q&A
    add_section(doc, 6, "Questions & Answers Session (Live Q&A)")
    add_speaker_para(
        doc,
        "Moderator – IR Team, Vinpearl",
        "This concludes management's prepared presentation. I will now hand over moderation to Ms. Mai Huong, Director of Investment at Vinpearl, to address your questions."
    )
    
    qa_list_en = [
        ("Financial Analyst: Drivers behind the gross margin contraction in 3Q2026?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "The slight decline in 3Q gross margin reflects two specific factors: (1) A full quarter of operational costs recognized from VinWonders Vu Yen (Hai Phong), which is still in its early ramping-up phase and temporarily weighs on overall margins; (2) A modest impact from Vinpearl Ha Long's transition from an owned property model to a managed hotel model, where we now recognize management fees rather than full hotel revenue and cost. Excluding these two items, underlying core gross margins remain stable to improving, underpinned by higher ADR and spending per guest."),
         
        ("Ms. Trang Nguyen: How did Vinpearl achieve significant growth in financial income during 3Q2026 despite the rising interest rate environment?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "In 3Q2026, financial income rose substantially year-over-year, primarily driven by Vinpearl's strong cash position accumulated from business cooperation contracts (BCCs) and customer down payments from newly launched property projects this year, such as Vinpearl Lang Van (Da Nang); alongside optimizing short-term deposit balances and extending short-term loans to internal related parties at prevailing market rates."),
         
        ("Ms. Trang Nguyen: Why was property transfer gross margin in 3Q only around 10% versus historical levels above 50%? Update on the USD 55 million preferred shares?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Real estate revenue is recognized strictly based on project handover progress. 3Q property revenue mainly reflects deliveries at the Vu Yen complex project (Vinhomes Royal Island) alongside cost adjustments associated with interest rate support programs from previously handed-over projects, temporarily dampening gross margins. On capital raising: Vinpearl successfully secured USD 55 million via convertible dividend preference shares, bolstering our equity capital base to support investment and project development over the next 12 months in tandem with operating cash flows."),
         
        ("Tam Nguyen: Could you update us on the lending rates applied to related party loans?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Lending rates for related party loans are strictly market-based on an arm's-length basis, currently standing at 12.0% per annum."),
         
        ("Truc: Revenue and EBITDA contribution of Phu Quoc Cluster in 9M2026 and FY2026? Long-term outlook and APEC 2027 impact?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Phu Quoc generated approximately VND 2,500 billion in revenue in 9M2026, accounting for ~24% of consolidated revenue, expanding 35% YoY and contributing very positively to EBITDA. For 2027 and beyond, new supply is expected to be well absorbed alongside robust market growth, aided by airport capacity expansion and connectivity infrastructure. Global milestones such as APEC 2027 will support Phu Quoc's long-term multi-year development. Pre-bookings for our Phu Quoc properties for the upcoming high season are demonstrating very positive uptake."),
         
        ("Ms. Trang Nguyen: Why did VinWonders visits decline 2% YoY in 3Q? How will you achieve the 15 million visit full-year target when 9M stands at 8.9 million? What is your CapEx guidance?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "The 2% YoY dip in 3Q visitation was predominantly caused by heavier rainfall compared to last year, particularly in Northern and Central Vietnam, curbing outdoor activities. The decline was concentrated in standalone attractions; conversely, our core integrated destination clusters continued to expand, with visits up ~10% YoY and revenue per visit up ~20% (3Q hit a record VND 631k), driving quarterly amusement revenue up 18% YoY. We acknowledge that achieving 15 million visits is challenging, supported by Q4 international peak season and festive events; however, Vinpearl's core priority is sustaining top-line revenue and profitability rather than chasing visitor volume at the expense of margins. CapEx is deployed flexibly according to project milestones and cash flow, focusing on operational and near-operational assets like Tuyen Quang and Lang Van."),
         
        ("Nhat Pham: What is management's forward expectation for Average Daily Rate (ADR) growth?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "We anticipate average ADR growth of approximately 15% per annum over the coming years, focused on optimizing yield during peak holiday seasons. In select marquee destinations, ADR growth could reach even higher levels driven by concentrated demand surges."),
         
        ("Tam Nguyen: Real estate liabilities account for ~60% of total liabilities. How does management plan to address them?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Most liabilities in the real estate segment comprise customer down payments, capital contributions under BCC agreements, and construction financing borrowings. These obligations are non-debt in nature and will be progressively settled and recognized into revenue and profit upon unit handovers to buyers."),
         
        ("Truc: RevPAR and ADR expectations for Tuyen Quang in 4Q26 and 2027? Drivers of the 3Q debt increase?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Tuyen Quang opens in 4Q2026, and we expect its operational trajectory to mirror other ramping-up Northern clusters during initial phases. Regarding debt: Total borrowings increased by only VND 1.2 trillion in 3Q2026 to ~VND 22 trillion at quarter-end, primarily reflecting an additional long-term facility to support operational capital."),
         
        ("Truc: Hospitality room count at Can Gio? 2027 RevPAR/ADR expectations and property revenue recognition pipeline?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Can Gio features the 836-room 5-star Vinpearl Dream Palace Hotel (opening July 2027), international boutique hotels (Best Western, iBis, JO&JOE), and 137 bespoke beachfront villas, mostly opening in July 2027 with select hotels opening through 2027–2028. Specific ADR/RevPAR targets are not yet disclosed. On real estate: Phu Quoc handovers will continue into 2027, and Lang Van (Da Nang) commenced sales this year, with handover revenue recognition expected to begin in 2027."),
         
        ("Phuong Hoang: What was 3Q gross margin excluding VinWonders depreciation and Vinpearl Ha Long's model shift?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "Excluding depreciation and amortization, VinWonders gross margin reached approximately 70%. The operational model transition at Vinpearl Ha Long impacted consolidated gross margin by approximately 2.5 percentage points."),
         
        ("Truc: What is Vinpearl's economic interest in Tuyen Quang and Can Gio? Will Vinpearl consolidate 100% of financials?",
         "Ms. Mai Huong – Director of Investment, Vinpearl",
         "For Tuyen Quang, Vinpearl fully consolidates the hotel and VinWonders amusement park components, while the Vin New Horizon senior living community is not consolidated under Vinpearl. For Can Gio, economic interest will reflect a blended mix between owned and managed assets, which will be disclosed in detail closer to commercial operations.")
    ]
    
    for q_title, a_spk, a_text in qa_list_en:
        add_speaker_para(doc, None, q_title)
        add_speaker_para(doc, a_spk, a_text)
        
    add_speaker_para(
        doc,
        "Moderator – IR Team, Vinpearl",
        "This concludes today's Q&A session. As a reminder, Vingroup will host its 3Q2026 Earnings Call on October 30, 2026. Thank you for participating today!"
    )
    
    doc.save(os.path.join(OUT_DIR, "VPL_Earnings_Call_3Q2026_Script_EN.docx"))
    doc.save(os.path.join(OUT_ROOT, "VPL_Earnings_Call_3Q2026_Script_EN.docx"))
    print("[✓] Đã tạo thành công VPL_Earnings_Call_3Q2026_Script_EN.docx (đầy đủ Q&A)")

if __name__ == "__main__":
    build_vietnamese_docx()
    build_english_docx()
