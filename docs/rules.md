# BỘ QUY TẮC CHUẨN HÓA BÁO CÁO ANALYST MEETING (ANALYST MEETING REPORT RULES)

* **Mã quy tắc**: `RULE-AM-RES-01`
* **Phiên bản**: 3.0.0 (Cập nhật ngày 16/10/2026)
* **Tài liệu tham chiếu ví dụ thực tế**: Xem toàn bộ các ví dụ mẫu và case study cụ thể tại **[examples.md](./examples.md)**.
* **Mục tiêu**: Định hình quy chuẩn bắt buộc để AI Agent trích xuất, đối chiếu dữ liệu và xuất báo cáo Analyst Meeting (Step 5) chính xác, khách quan, súc tích và tuân thủ định dạng chuẩn.

---

## 1. NGUYÊN TẮC CỐT LÕI BẮT BUỘC (CARDINAL PRINCIPLES)

> [!IMPORTANT]
> ### NGUYÊN TẮC 1: 100% SỰ THẬT KHÁCH QUAN, NGHIÊM CẤM Ý KIẾN AI (PURE FACTS ONLY - ZERO AI OPINIONS)
> - **Chỉ đưa dữ kiện thực tế (Facts)**: Toàn bộ nội dung trong Báo cáo Analyst Meeting và Full Transcript **CHỈ ĐƯỢC** hình thành từ hai nguồn duy nhất:
>   1. Lời phát biểu thực tế của Ban lãnh đạo trong audio/script.
>   2. Số liệu cứng in trên slide và tài liệu cuộc họp chính thức.
> - **Tuyệt đối cấm nhận định của AI**: Xuyên suốt toàn bộ văn bản, **NGHIÊM CẤM** đưa bất kỳ nhận định, suy luận, bình luận cá nhân, dự đoán chủ quan hoặc quan điểm riêng của AI vào.
> - **Tham chiếu ví dụ**: Xem minh họa lỗi vi phạm và cách viết đúng tại **[examples.md#ví-dụ-3-minh-họa-quy-tắc-pure-facts-only--omission-over-fabrication](./examples.md#ví-dụ-3-minh-họa-quy-tắc-pure-facts-only--omission-over-fabrication)**.

> [!IMPORTANT]
> ### NGUYÊN TẮC 2: KHÔNG CÓ THÌ BỎ, TUYỆT ĐỐI KHÔNG BỊA RA (OMISSION OVER FABRICATION)
> - Nếu một đề mục, một chỉ tiêu tài chính, một kế hoạch hoặc một câu hỏi nào trong khung mẫu **KHÔNG ĐƯỢC ĐỀ CẬP** trong audio cuộc họp (hoặc slide tài liệu), **BẮT BUỘC PHẢI BỎ MỤC ĐÓ RA KHỎI BÁO CÁO**.
> - Tuyệt đối không được tự ý suy đoán, không dùng kiến thức ngoài lề để "lấp đầy chỗ trống".

> [!IMPORTANT]
> ### NGUYÊN TẮC 3: BỘ LỌC THỜI SỰ & LOẠI BỎ CHUỖI SỐ LIỆU ĐA NĂM (RECENCY & DROP MULTI-YEAR LISTINGS)
> - Xác định mốc thời gian cuộc họp (Ví dụ: Tháng T).
> - **CHỈ ĐƯỢC** tập trung vào dữ liệu tài chính của kỳ mới nhất (Quý gần nhất và Lũy kế gần nhất), đi kèm với Kế hoạch cả năm và các thông điệp định hướng quý tiếp theo.
> - **LOẠI BỎ TOÀN BỘ chuỗi số liệu đa năm (Drop multi-year chronological listings)**: Bỏ hoàn toàn việc liệt kê dữ liệu thô nhiều năm liên tiếp (như chuỗi 2021-2024 raw data); **CHỈ GIỮ LẠI** kỳ hiện tại so với kỳ so sánh cơ sở (YoY / YTD / 2025). Không đưa các bảng số liệu chi tiết của các kỳ cũ đã qua nhiều năm vào phần phân tích chính.

> [!IMPORTANT]
> ### NGUYÊN TẮC 4: QUY CHUẨN ĐỒNG NHẤT KÝ HIỆU QUÝ (UNIFIED QUARTER NOTATION: 3Q26)
> - Tất cả mọi đề cập đến kỳ quý trong toàn bộ hệ thống tài liệu (Full Transcript, Analyst Report, Keynotes, Tiêu đề, Đề mục, Lời thoại, Q&A) **BẮT BUỘC** phải viết thống nhất theo định dạng chuẩn:
>   - **`[Số Quý]Q[2 số cuối của Năm]`** (Ví dụ: `3Q26`, `4Q26`, `1Q26`, `2Q26`, `3Q25`, `3Q27`...).
> - **TUYỆT ĐỐI CẤM** dùng các biến thể không đồng nhất sau:
>   - *Cấm:* `Quý 3/ 2026`, `Quý 3/2026`, `Quý 3 năm 2026`, `3Q2026`, `Q3/2026`, `Q3/26`, `Quý 3`, `Q3`...
>   - *Bắt buộc thay bằng:* `3Q26` (hoặc `4Q26`, `3Q25` tương ứng theo bối cảnh).

> [!IMPORTANT]
> ### NGUYÊN TẮC 5: QUY CHUẨN XỬ LÝ CHỈ SỐ TÀI CHÍNH TRUNG GIAN (INTERMEDIATE METRICS FILTERING)
> - **Chỉ số Cốt lõi (Bắt buộc trong văn bản)**: Doanh thu thuần (Top-line), Lợi nhuận gộp & Biên lợi nhuận gộp (Gross Margin), Lợi nhuận sau thuế (LNST / NPAT - Bottom-line), và Tiến độ hoàn thành Kế hoạch năm.
> - **Chỉ số Trung gian (Mặc định CẮT)**: Lợi nhuận hoạt động (Operating Profit), Lợi nhuận trước thuế (LNTT / PBT), EBITDA & Biên EBITDA. Các số liệu này được lưu trữ đầy đủ trong Báo cáo Đối chiếu Dữ liệu (`data_reconciliation.md`), do đó **MẶC ĐỊNH BỎ KHỎI VĂN BẢN** để tránh loãng thông tin và biến báo cáo thành bản "đọc lại BCTC".
> - **Ngoại lệ (Biến động bất thường cần giải thích riêng)**: Chỉ giữ lại chỉ số trung gian khi có phân kỳ tăng trưởng (growth divergence), biến động lớn về chi phí lãi vay/tài chính, OPEX/SG&A shock, các khoản thu nhập/chi phí một lần (one-off non-operating items) hoặc thuế suất thực tế méo mó tác động trực tiếp đến kết quả kinh doanh. Khi giữ lại, bắt buộc phải gắn liền với câu giải thích nguyên nhân gốc rễ (Root Cause).

> [!IMPORTANT]
> ### NGUYÊN TẮC 6: QUY CHUẨN ĐỊNH DẠNG SỐ LIỆU TÀI CHÍNH (DOT FOR DECIMAL, COMMA FOR THOUSANDS)
> - **Dấu chấm (`.`) BẮT BUỘC dùng cho phần thập phân (Decimal point)**: Ví dụ: `21.03%`, `4,057.6 tỷ`, `13.90%`, `1.5%`, `18.1%`.
> - **Dấu phẩy (`,`) BẮT BUỘC dùng cho phân cách hàng ngàn (Thousands separator)**: Ví dụ: `1,000 tỷ`, `4,057.6 tỷ`, `11,438.2 tỷ`, `18,000 tỷ`, `2,533.6 tỷ`.
> - **TUYỆT ĐỐI CẤM** dùng ngược lại theo kiểu cũ (dùng dấu chấm cho hàng ngàn và dấu phẩy cho thập phân như `4.057,6` hay `21,03%`). Áp dụng nhất quán trên toàn bộ Báo cáo Phân tích, Transcript và Đối chiếu Dữ liệu.



> [!IMPORTANT]

> ### NGUYÊN TẮC 7: CÚ PHÁP ĐẦU RA CHUẨN HÓA CHO CHỈ SỐ (STANDARDIZED METRIC OUTPUT FORMAT)

> - Mọi dòng chỉ tiêu tài chính và hoạt động kinh doanh trong các bullet point **BẮT BUỘC** áp dụng cú pháp:

>   `[Metric Name]: [Value] ([Δ QoQ / YoY / YTD], [% Target reached]), [Direct Driver/Catalyst].`

> - Ví dụ: `Doanh thu thuần: 2,618.0 tỷ VND (+158.0% YoY, đạt 57.5% KH), động lực từ khối Tư vấn và khối Kinh doanh Trái phiếu.`

> [!IMPORTANT]
> ### NGUYÊN TẮC 7: CÚ PHÁP ĐẦU RA CHUẨN HÓA CHO CHỈ SỐ (STANDARDIZED METRIC OUTPUT FORMAT)
> - Mọi dòng chỉ tiêu tài chính và hoạt động kinh doanh trong các bullet point **BẮT BUỘC** áp dụng cú pháp:
>   `[Metric Name]: [Value] ([Δ QoQ / YoY / YTD], [% Target reached]), [Direct Driver/Catalyst].`
> - Ví dụ: `Doanh thu thuần: 2,618.0 tỷ VND (+158.0% YoY, đạt 57.5% KH), động lực từ khối Tư vấn và khối Kinh doanh Trái phiếu.`

---

## 2. KHUNG ĐỊNH DẠNG CHUẨN 3 PHẦN (EXACT TEMPLATE SPECIFICATION)

> Xem báo cáo mẫu hoàn chỉnh tại: **[examples.md#ví-dụ-1-báo-cáo-mẫu-analyst-meeting-chuẩn-benchmark-report](./examples.md#ví-dụ-1-báo-cáo-mẫu-analyst-meeting-chuẩn-benchmark-report)**.

Cấu trúc tiêu đề báo cáo:  
`[Tên Đơn vị Research] – Cập nhật Analyst Meeting [MÃ CK] ([Kỳ báo cáo]): [Tiêu đề cuộc họp]`

---

### PHẦN 1: KẾT QUẢ HOẠT ĐỘNG KINH DOANH ƯỚC TÍNH [QUÝ MỚI NHẤT] VÀ [LŨY KẾ MỚI NHẤT]

Chia thành đúng 4 nhóm đề mục con (chỉ đưa các mục có dữ liệu thực tế):

1. **Quy mô tổng tài sản & Tín dụng:**
   - **Tổng tài sản**: [Con số mới nhất] ([% tăng so với đầu năm hoặc YoY]) tại thời điểm [Ngày/Tháng/Năm mới nhất], [tiến độ tiệm cận cột mốc].
   - **Dư nợ tín dụng**: [Con số mới nhất] ([% tăng]) tại [Ngày/Tháng/Năm]. Cơ cấu dịch chuyển thực chất sang các phân khúc khách hàng.
2. **Huy động vốn & Nguồn vốn quốc tế:**
   - **Huy động vốn**: [Con số mới nhất] ([% tăng]), cơ cấu tiền gửi và tỷ lệ tái tục tiền gửi.
   - **Thị trường quốc tế**: Các thương vụ phát hành trái phiếu quốc tế và các khoản vay hợp vốn nước ngoài; số dư huy động ngoại tệ quốc tế.
3. **Hiệu quả kinh doanh & Chỉ số sinh lời:**
   - **Lợi nhuận trước thuế (LNTT)**: Ước tính [Quý mới nhất] đạt [Con số] ([% svck]), [Lũy kế mới nhất] đạt [Con số] ([% svck]), hoàn thành xấp xỉ [%] kế hoạch cả năm ([Con số kế hoạch]).
4. **Chất lượng tài sản & Bộ đệm an toàn:**
   - **Nợ xấu (NPL)**: Tỷ lệ nợ xấu kiểm soát ở mức [Con số %] tại thời điểm [Ngày/Tháng/Năm].
   - **Dự phòng rủi ro & Thanh khoản**: Tỷ lệ dự trữ thanh khoản (LRR), tỷ lệ LDR (so với trần quy định), hệ số CAR hợp nhất, quy mô Vốn tự có hợp nhất ([% YoY]), và tỷ lệ vốn ngắn hạn cho vay trung dài hạn.

---

### PHẦN 2: ĐỊNH HƯỚNG CHIẾN LƯỢC SẮP TỚI CỦA [DOANH NGHIỆP]

> [!IMPORTANT]
> **TRIỆT TIÊU ĐỊNH HƯỚNG CHUNG CHUNG (DROP GENERIC CORPORATE ASPIRATIONS)**:
> - Loại bỏ toàn bộ các tuyên bố nguyện vọng chung chung, sáo rỗng hoặc khẩu hiệu PR của doanh nghiệp (corporate aspirations).
> - **CHỈ GIỮ LẠI** các yếu tố thúc đẩy cụ thể (concrete catalysts), mốc thời hạn rõ ràng (deadlines) và các ngưỡng số liệu/chỉ tiêu định lượng (numerical thresholds).

Trình bày theo các gạch đầu dòng chiến lược súc tích:

1. **Mục tiêu hoàn thành kế hoạch [Năm hiện tại]:** Tuyên bố của Ban lãnh đạo về khả năng hoàn thành kế hoạch ĐHĐCĐ giao (Mốc Tổng tài sản, Dư nợ tín dụng mục tiêu, LNTT cả năm, NPL mục tiêu và Tỷ lệ chi trả cổ tức dự kiến).
2. **Kế hoạch chi trả cổ tức [Năm trước / Năm nay]:**
   - **Cổ tức tiền mặt X%**: Thời gian dự kiến chi trả, điều kiện phê duyệt pháp lý, thủ tục chốt danh sách cổ đông.
   - **Cổ tức bằng cổ phiếu Y%**: Tiến độ hoàn tất, quyền lợi của lượng cổ phiếu phát hành thêm.
3. **Định vị chiến lược "[Tên khẩu hiệu/Tầm nhìn]":** Triển khai dựa trên các trụ cột cốt lõi do Ban lãnh đạo công bố.
4. **Tái cơ cấu danh mục & Mảng kinh doanh trọng điểm:** Xu hướng dịch chuyển phân khúc khách hàng; cơ cấu chi tiết danh mục rủi ro/đặc thù; định hướng dòng vốn theo xu thế vĩ mô và tiêu chuẩn ESG.
5. **Nâng chuẩn quản trị & Tìm kiếm cổ đông chiến lược:** Cập nhật chuẩn mực quản trị quốc tế; tiến độ tiếp xúc, thẩm định và đàm phán với đối tác chiến lược nước ngoài (các thị trường trọng điểm).

---

### PHẦN 3: ĐỐI ĐÁP VÀ TRẢ LỜI CÂU HỎI VỚI NHÀ ĐẦU TƯ (Q&A)

> [!IMPORTANT]
> **QUY CHUẨN BIÊN SOẠN Q&A: TỐI ĐA KHÔNG QUÁ 8 CÂU HỎI (HARD CAP)**
> - **Kiểm soát trực tiếp từ User**: User là người trực tiếp kiểm duyệt và quyết định các câu hỏi Q&A nào là trọng yếu đưa vào báo cáo (tối đa không quá 8 câu).
> - **Giới hạn số lượng**: Khung chuẩn mực từ 5 – 7 câu hỏi, tối đa tuyệt đối không quá 8 câu. Cấm để danh sách câu hỏi phình to 10 – 15 câu làm loãng thông tin.
> - **Gom cụm chủ đề chiến lược (Thematic Consolidation)**: Cấm phân mảnh theo từng lượt thoại thô; gom các câu hỏi con cùng bản chất vào một tiêu đề lớn.
> - **Ghi nhận danh tính người hỏi (Analyst Attribution)**: Luôn trích xuất tên chuyên viên / quỹ đặt câu hỏi (Ví dụ: *Question from Ms. Trang Nguyen*).

Định dạng chuẩn từng câu hỏi (Cấu trúc 3 luận điểm cốt lõi):
```text
STT. [Tiêu đề chủ đề gom cụm] – Question from [Tên chuyên viên / Quỹ nếu có]:
Management Response (hoặc Phản hồi từ Ban Lãnh đạo):
- (1) Core root cause: [Nguyên nhân gốc rễ cốt lõi / Động lực trực tiếp đằng sau vấn đề]
- (2) Mitigating factor/buffer: [Yếu tố giảm thiểu rủi ro, dự phòng hoặc vùng đệm an toàn]
- (3) Forward guidance: [Kế hoạch hành động cụ thể, mốc thời hạn (deadlines) và các ngưỡng định lượng (numerical thresholds)]
```

---

## 3. QUY TRÌNH 4 BƯỚC ĐỐI CHIẾU SCRIPT VỚI SLIDES ĐỂ LẤY SỐ LIỆU CHÍNH XÁC (SCRIPT-TO-SLIDES AUDIT PROTOCOL)

> Xem chi tiết bảng so sánh các trường hợp sai lệch âm thanh thực tế tại: **[examples.md#ví-dụ-2-đối-chiếu--hiệu-chỉnh-sai-lệch-giữa-script-và-slides](./examples.md#ví-dụ-2-đối-chiếu--hiệu-chỉnh-sai-lệch-giữa-script-và-slides)**.

1. **Bước 1 - Trích xuất số liệu gốc từ Slides (Ground Truth Extraction)**: Quét toàn bộ hình ảnh slide trong `input_docs/` để lập ma trận số liệu cứng chính thức (Đơn vị tính, Bảng cân đối, P&L, tỷ lệ an toàn, chỉ số KPI) và lưu thành file `input_docs/ground_truth.md` (Single Source of Truth). Số liệu trên slide luôn là Chân Lý Chuẩn.
2. **Bước 2 - Khớp nối theo dòng thời gian & chủ đề (Timeline & Topic Alignment)**: Ghép từng khối thoại trong script với slide tương ứng đang hiển thị trên màn hình.
3. **Bước 3 - Hiệu chỉnh sai lệch âm thanh & chuẩn hóa số liệu (Discrepancy Reconciliation)**:
   - Sửa lỗi diễn giả nói làm tròn số bằng con số chính xác trên slide.
   - Sửa lỗi STT nhận diện nhầm âm thanh (phát âm số, tên viết tắt của quỹ, tên sàn giao dịch quốc tế, tên nghiệp vụ tài chính).
   - Quy tắc giải quyết xung đột: Bắt buộc lấy số liệu trên slide làm số liệu chính thức.
4. **Bước 4 - Gắn thẻ truy vết minh bạch (Traceability Tagging)**: Mọi số liệu trong báo cáo đều có nguồn dẫn chứng rõ ràng.

---

## 4. CHECKLIST KIỂM TRA BẮT BUỘC TRƯỚC KHI XUẤT FILE (AGENT PRE-FLIGHT CHECKLIST)

- [ ] **100% Dữ kiện thực tế (Pure Facts Only)**: Toàn bộ nội dung đều là phát biểu của Ban lãnh đạo hoặc số liệu slide? Đã loại bỏ hoàn toàn mọi nhận định, suy đoán, dự báo, bình luận của AI chưa? *(Tham chiếu: [examples.md#ví-dụ-3](./examples.md#ví-dụ-3-minh-họa-quy-tắc-pure-facts-only--omission-over-fabrication))*.
- [ ] **Không có thì bỏ (Omission over Fabrication)**: Nếu một mục trong mẫu không có thông tin trong audio/slide, đã bỏ mục đó chưa (tuyệt đối không bịa ra)?
- [ ] **Bộ lọc thời sự (The Recency Rule)**: Số liệu tài chính là số liệu mới nhất (3Q và 9T), không đưa số liệu 6T cũ đã qua nhiều tháng?
- [ ] **Đã tạo file ground_truth.md và thực hiện đủ 4 bước đối chiếu Script với Slides chưa?** *(Tham chiếu: [examples.md#ví-dụ-2](./examples.md#ví-dụ-2-đối-chiếu--hiệu-chỉnh-sai-lệch-giữa-script-và-slides))*.
- [ ] Đúng 3 Phần lớn (`Phần 1`, `Phần 2`, `Phần 3`) như file mẫu **[examples.md](./examples.md)**.
- [ ] Phần 1 có đủ 4 tiểu mục con in đậm: `Quy mô tổng tài sản & Tín dụng`, `Huy động vốn & Nguồn vốn quốc tế`, `Hiệu quả kinh doanh & Chỉ số sinh lời`, `Chất lượng tài sản & Bộ đệm an toàn` (với các mục có dữ liệu thực tế).
- [ ] Phần 2 có đủ các ý được Ban lãnh đạo chia sẻ: Mục tiêu kế hoạch năm, Kế hoạch cổ tức tiền mặt & cổ phiếu, Định vị chiến lược, Tái cơ cấu danh mục, Cổ đông chiến lược.
- [ ] Phần 3 các câu Q&A đánh số 1., 2., 3... kèm dòng thụt `Phản hồi từ [Ban lãnh đạo/Chức vụ]:`.
