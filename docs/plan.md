# Kế Hoạch Vận Hành Hệ Thống (Master Execution Plan & Runbook)
# Dự Án: Meeting Analyst Automation Pipeline

> **Dành cho Agent tiếp quản (Agent Instruction)**:  
> File này chứa toàn bộ quy trình vận hành từng bước (SOP) để bất kỳ AI Agent nào khi đọc vào cũng biết chính xác trạng thái hiện tại, nhiệm vụ cần làm, lệnh cần chạy, cấu trúc dữ liệu và tiêu chuẩn đầu ra mà không cần hỏi lại các quyết định kiến trúc đã thống nhất.

---

## 1. Bản Đồ Tổng Thể Quy Trình (Workflow Map)

Dự án vận hành theo mô hình **Hybrid Human-in-the-loop (5 Giai đoạn)**:

```
[ Giai đoạn 1: AGENT ]    --> Nhận video 2-3GB -> Chạy audio_splitter.py -> Xuất MP3 gối đầu
[ Giai đoạn 1.5: AGENT ]  --> Số hóa toàn bộ Slide trong input_docs/ -> Tạo ground_truth.md (chạy song song lúc User làm GĐ 2)
[ Giai đoạn 2: USER ]     --> Kéo thả MP3 vào NotebookLM -> Lưu raw_transcript.txt
[ Giai đoạn 3: AGENT ]    --> Khử trùng overlap + Chuẩn hóa chuyên môn + Tra cứu nhanh qua ground_truth.md -> full_transcript.md
[ Giai đoạn 4: AGENT ]    --> Xuất Báo cáo Analyst Meeting 3 phần (Chống bịa đặt) -> analyst_report.md
```

---

## 2. Nguyên Tắc Cốt Lõi Bắt Buộc Tuân Thủ (Non-Negotiable Rules)

1. **100% Dữ Kiện Thực Tế, Nghiêm Cấm Nhận Định Của AI (Pure Facts Only - Zero AI Opinions)**:
   - Xuyên suốt Báo cáo Analyst Meeting và Full Transcript, **CHỈ ĐƯỢC** ghi nhận sự thật khách quan từ 2 nguồn: Lời phát biểu của Ban lãnh đạo trong audio và Số liệu cứng trên slide tài liệu.
   - **Tuyệt đối không đưa bất kỳ nhận định, suy luận, dự báo, bình luận hay ý kiến chủ quan nào của AI vào.**
2. **Không có thì bỏ, tuyệt đối không bịa ra (Omission over Fabrication)**:
   - Nếu một mục/chỉ tiêu trong khung mẫu không được đề cập trong cuộc họp hay slide tài liệu, **BẮT BUỘC PHẢI BỎ MỤC ĐÓ**, tuyệt đối không tự ý suy đoán hay lấy kiến thức ngoài lề để điền vào.
3. **Bộ lọc thời sự (The Recency Rule)**:
   - Chỉ lấy dữ liệu kỳ mới nhất (Tháng 9 / 9T khi họp vào tháng 10), loại bỏ số liệu 6T cũ đã qua 4 tháng trước.
4. **Quy chuẩn file âm thanh cho NotebookLM**:
   - `Mono (-ac 1)`, tần số `16000Hz`, bitrate `64kbps CBR`.
   - Chunk `1500 giây` (25 phút), gối đầu `20 giây` (overlap), bước nhảy `1480 giây`.
   - Đặt tên file: `part_01_00m00s_25m00s.mp3`, `part_02_24m40s_49m40s.mp3`, `part_03_49m20s_74m20s.mp3`...
5. **Nguồn tham chiếu duy nhất (Single Benchmark Rule)**:
   - **CHỈ THAM KHẢO DUY NHẤT 1 CASE LÀ TCX (`workspace/tcx/`)**: Khi cần đối soát cấu trúc file, định dạng, hay mẫu Word/Markdown, Agent chỉ mở đúng thư mục `workspace/tcx/`. Tuyệt đối không đọc lại các bên khác (SHB, IMP, F88...) để rút ngắn tối đa thời gian xử lý.

---

## 3. Cấu Trúc Thư Mục Chuẩn (Workspace Conventions)

Khi xử lý một cuộc họp mới, Agent luôn tạo hoặc sử dụng đúng cấu trúc thư mục sau:

```text
./
├── intent.md                          # Mục tiêu & yêu cầu đã phỏng vấn
├── spec.md                            # Đặc tả kỹ thuật chi tiết
├── plan.md                            # Hướng dẫn vận hành này
├── rules.md                           # Bộ quy tắc chuẩn hóa báo cáo
├── examples.md                        # Tài liệu ví dụ tham chiếu
├── audio_splitter.py                  # Tool cắt video/audio gối đầu
└── workspace/
    └── <meeting_id>/                  # Ví dụ: meeting_01 hoặc meeting_2026_10_16
        ├── input_media/               # Chứa video 2-3GB (video.mp4) hoặc audio gốc
        ├── input_docs/                # Chứa tài liệu cuộc họp (Slide PDF, kế hoạch)
        │   └── ground_truth.md        # [SSOT] Số liệu chuẩn trích xuất từ slide (Single Source of Truth)
        ├── audio_chunks/              # Chứa các file part_xx_...mp3 (do Agent tạo ra)
        ├── raw_transcript.txt         # Transcript thô từ NotebookLM (do User cung cấp)
        └── output/
            ├── full_transcript.md     # Bản Full Transcript đã chuẩn hóa & diễn giải
            └── analyst_report.md      # Báo cáo Analyst chuyên sâu hoàn chỉnh
```

---

## 4. Hướng Dẫn Thao Tác Chi Tiết Từng Giai Đoạn

### Giai Đoạn 1: Tiền Xử Lý Media (Agent Thực Hiện)
* **Kích hoạt khi**: User cung cấp file video (hoặc copy vào `input_media/` hoặc gửi đường dẫn).
* **Nhiệm vụ của Agent**:
  1. Xác định đường dẫn file video và thư mục `audio_chunks` đích:
     ```bash
     python audio_splitter.py "<đường_dẫn_video>" --out "./workspace/<meeting_id>/audio_chunks"
     ```
  2. Kiểm tra xem các file `part_xx_...mp3` đã được tạo đầy đủ chưa.
  3. Gửi thông báo cho User danh sách file, tổng dung lượng và đường dẫn thư mục `audio_chunks/`.
  4. Hướng dẫn User chuyển sang Giai đoạn 2.

---

### Giai Đoạn 1.5: Tự Động Hóa Trích Xuất Dữ Liệu Slide - Tạo Ground Truth (`extract_ground_truth.py`)
* **Kích hoạt khi**: Có file Slide thuyết trình (`.pdf`, `.pptx`) hoặc thư mục ảnh slide trong `workspace/<meeting_id>/input_docs/`.
* **Mục tiêu**: Tự động hóa 100% việc số hóa toàn bộ dữ liệu cứng từ slide bằng công cụ local ONNX OCR + PyMuPDF, tạo nguồn dữ liệu Chân Lý Duy Nhất (Single Source of Truth - SSOT) trong vòng dưới 30 giây, chống nhầm lẫn hoặc rò rỉ dữ liệu ngoài.
* **Lệnh thực thi chuẩn**:
  ```bash
  python extract_ground_truth.py \
    --input "workspace/<meeting_id>/input_docs/presentation.pdf" \
    --out-dir "workspace/<meeting_id>/input_docs" \
    --ticker "<TICKER>" \
    --period "<PERIOD>" \
    --meeting "<MEETING_NAME>"
  ```
* **Kết quả đầu ra tự động**:
  1. `input_docs/slides/`: Thư mục chứa toàn bộ ảnh slide chất lượng cao (150 DPI) phục vụ đối chiếu trực quan.
  2. `input_docs/ground_truth_raw.json`: Dữ liệu thô gồm vị trí hộp văn bản, điểm tin cậy và cấu trúc dòng bảng.
  3. `input_docs/ground_truth.md`: Báo cáo số liệu chuẩn hóa chi tiết từng trang slide để Agent dùng đối soát tức thì ở Giai đoạn 3 & 4.

---

### Giai Đoạn 2: NotebookLM Ingestion (User Thực Hiện)
* **Nhiệm vụ của User**:
  1. Mở [NotebookLM](https://notebooklm.google.com/).
  2. Tải các file `part_01_...mp3`, `part_02_...mp3`... trong thư mục `audio_chunks` lên.
  3. Xuất toàn bộ nội dung script/transcript mà NotebookLM nhận diện được.
  4. Lưu vào file `workspace/<meeting_id>/raw_transcript.txt` và báo cho Agent.

---

### Giai Đoạn 3: Chuẩn Hóa Transcript & Khử Overlap (Agent Thực Hiện)
* **Kích hoạt khi**: Đã có `raw_transcript.txt` và `ground_truth.md`.
* **Nhiệm vụ của Agent**:
  1. **Khử trùng lặp ở vùng gối đầu 20 giây (Overlap Deduplication)**:
     - Do mỗi file mp3 gối đầu 20s với file liền trước, transcript thô sẽ có các câu nói bị lặp lại ở điểm giao nhau giữa 2 chunk.
     - Agent đối chiếu mốc giờ ở tên file (ví dụ `24m40s -> 25m00s`) và loại bỏ phần trùng lặp để nội dung liền mạch 100%.
  2. **Chuẩn hóa thuật ngữ & chính tả tiếng Việt**:
     - Ngành Tài chính/Chứng khoán: *EBITDA, P/E, P/B, ROE, CAGR, Margin, doanh thu thuần, lợi nhuận sau thuế, dự phóng, trích lập dự phòng, pha loãng, thoái vốn...*
     - Ngành Công nghệ/SaaS: *API, Backend, Frontend, Cloud, CI/CD, Deployment, SLA, KPI, OKR, Roadmap...*
  3. **Quy trình 4 Bước Đối chiếu Script với Ground Truth (Script-to-Slides Grounding Protocol)**:
     - **Bước 1 - Nạp Ground Truth**: Đọc trực tiếp file `input_docs/ground_truth.md` (đã số hóa ở Giai đoạn 1.5), không cần load lại các file ảnh rời rạc.
     - **Bước 2 - Khớp nối theo chủ đề**: Ghép đoạn thoại của diễn giả với chỉ tiêu tương ứng trong bảng Ground Truth.
     - **Bước 3 - Hiệu chỉnh sai lệch âm thanh**:
       + Sửa số làm tròn/nói ước lượng bằng số chính xác (Ví dụ: ~963.000 tỷ $\rightarrow$ 962.960 tỷ; 9.149 tỷ $\rightarrow$ 9.143 tỷ).
       + Sửa lỗi nhận diện nhầm âm thanh: 290 triệu SGD $\rightarrow$ 229 triệu SGD; "quỹ JCF của Asb" $\rightarrow$ CGIF (ADB); "Syiket Lô" $\rightarrow$ Syndicated Loan.
       + Quy tắc ưu tiên: Khi có mâu thuẫn giữa lời nói và slide, **bắt buộc dùng số liệu trên slide**.
     - **Bước 4 - Gắn thẻ truy vết**: Chú thích rõ nguồn đối chiếu: `> *[Diễn giải từ Slide X, Trang Y: ...]*`.
  4. **Xuất file**:
     - Lưu kết quả vào `workspace/<meeting_id>/output/full_transcript.md`.

---

### Giai Đoạn 4: Tổng Hợp Báo Cáo Analyst Meeting (Agent Thực Hiện)
* **Kích hoạt khi**: Đã có `full_transcript.md`.
* **Tiêu chuẩn bắt buộc**: Agent **bắt buộc tuân thủ 100% cấu trúc mẫu tại [examples.md](./examples.md) và bộ quy tắc tại [rules.md](./rules.md)**:
  - **100% Sự thật khách quan (Pure Facts Only)**: Không đưa bất kỳ nhận định/quan điểm nào của AI vào.
  - **Không có thì bỏ (Omission over Fabrication)**: Không có dữ liệu trong audio/slide thì bỏ mục đó, không được bịa ra.
  - **Quy tắc tính thời sự (Recency Rule)**: Chỉ đưa dữ liệu mới nhất (tháng 9 / 9T khi họp vào tháng 10), loại bỏ số liệu 6T cũ thừa thãi.
  - **Lọc bỏ Chỉ số Trung gian (Intermediate Metrics Protocol)**:
    - Mặc định **CẮT KHỎI PHẦN VĂN BẢN** các chỉ số trung gian: LN hoạt động, LNTT (PBT), EBITDA (đã được lưu tại `data_reconciliation.md`).
    - Chỉ giữ lại khi có **biến động bất thường cần giải thích riêng** (one-off, tăng đột biến chi phí lãi vay/thuế/SG&A, phân kỳ tăng trưởng) và bắt buộc đi liền câu phân tích nguyên nhân tác động đến LNST.
  - **Cấu trúc 3 Phần chuẩn Institutional Research**:
    - **Phần 1: Kết quả hoạt động kinh doanh ước tính [Quý mới nhất] và [9T mới nhất]**: Gồm 4 nhóm: *Quy mô tổng tài sản & Tín dụng*, *Huy động vốn & Nguồn vốn quốc tế*, *Hiệu quả kinh doanh & Chỉ số sinh lời*, *Chất lượng tài sản & Bộ đệm an toàn*.
    - **Phần 2: Định hướng chiến lược sắp tới**: Gồm: *Mục tiêu hoàn thành kế hoạch năm*, *Kế hoạch chi trả cổ tức*, *Định vị chiến lược*, *Tái cơ cấu danh mục & Tín dụng xanh*, *Nâng chuẩn quản trị & Cổ đông chiến lược*.
    - **Phần 3: Đối đáp và trả lời câu hỏi với nhà đầu tư (Q&A)**: Đánh số 1, 2, 3... kèm thụt dòng `Phản hồi từ [Ban lãnh đạo/Tổng Giám đốc]:`.
* **Xuất file**:
  - Lưu kết quả vào `workspace/<meeting_id>/output/analyst_report.md`.

---

### Giai Đoạn 4.5: Đóng Gói Định Dạng Tự Động (Format Packager & Master Pipeline)
* **Kích hoạt khi**: Đã có `full_transcript.md` và `analyst_report.md`.
* **Mục tiêu**: Tự động chuyển đổi trực tiếp toàn bộ Markdown sang các file Word (.docx) chuẩn định chế trong vòng dưới 1 giây, tuyệt đối không format thủ công.
* **Quy chuẩn định dạng (Tham chiếu duy nhất case TCX `workspace/tcx/`)**:
  - **Full Transcript DOCX**:
    + Tiêu đề: `Title F88` (Calibri 20pt Bold, màu `#133F69`).
    + Subtitle: `Normal` (Calibri 12pt Bold, màu `#3C5C7A`).
    + Danh sách Speakers: `Normal` (Calibri 10pt, nhãn bold).
    + Đề mục Section: `Section F88` (Calibri 13pt Bold, màu `#133F69`, format: `01  |  Tên Section`).
    + Tên Diễn Giả: `Speaker F88` (Gắn nhãn `[Tên Diễn Giả]: ` in đậm màu `#133F69` ở đầu lượt thoại, line-spacing 1.15, text 10pt).
    + Chú thích Slide (Note): `Note F88` (Calibri 9.5pt Italic màu `#595959`, thụt lề 0.25 inch, format: `Editorial Note: Reference Slide X...`).
  - **Analyst Report DOCX**:
    + Tiêu đề: Calibri 15.5pt Bold màu `#133F69`.
    + Heading 1 (Phần 1, Phần 2, Phần 3): Calibri 13pt Bold màu `#1E4E79`, before 14pt, after 6pt.
    + Heading 2 (Nhóm chỉ tiêu): Calibri 11pt Bold màu `#2E75B6`, before 8pt, after 3pt.
    + Bullets: Style `List Bullet`, lead-in in đậm, nội dung định lượng trung tính.
    + Q&A: Câu hỏi Calibri 10.5pt Bold màu `#1F497D`, câu trả lời thụt lề 0.2 inch với nhãn `Phản hồi từ [Diễn giả]: ` in đậm màu `#333333`.
* **Lệnh thực thi 1 chạm (Format Packager CLI)**:
  ```bash
  python document_formatter.py --workspace "workspace/<meeting_id>" --ticker "<TICKER>" --period "<PERIOD>"
  ```
* **Lệnh thực thi toàn diện Master Pipeline (One-Stop CLI Runner)**:
  ```bash
  python am_pipeline.py "workspace/<meeting_id>" --ticker "<TICKER>" --period "<PERIOD>"
  ```
* **Kiểm định tuân thủ ngôn từ định chế (Fact-based Linter)**:
  - Tự động quét và cảnh báo toàn bộ các từ PR, quảng cáo bị cấm (*bùng nổ, đột phá, ngoạn mục, xuất sắc, thần tốc, áp đảo...*) theo quy chuẩn tại `AGENTS.md`.

---

## 5. Danh Sách Kiểm Tra Nhanh Khi Tiếp Quản (Agent Checklist)

Mỗi khi người dùng đưa ra yêu cầu mới, Agent tự kiểm tra:

- [ ] File video đầu vào đã được nén về `Mono, 16000Hz, 64kbps` chưa?
- [ ] Các đoạn audio con có tuân thủ overlap `20s` (25 phút/chunk) và tên file mốc giờ `part_xx_...mp3` không?
- [ ] Đã nhận được file `raw_transcript.txt` từ User chưa?
- [ ] Đã quét toàn bộ slide trong `input_docs/` và xuất file `ground_truth.md` chuẩn chưa?
- [ ] Đã khử trùng các câu lặp ở vùng gối đầu 20 giây chưa?
- [ ] **100% là Facts (lời phát biểu của Ban lãnh đạo + số liệu slide)? Đã loại bỏ hoàn toàn mọi nhận định của AI chưa?**
- [ ] **Không có thì bỏ? Đã bỏ các mục không có dữ liệu thay vì tự bịa chưa?**
- [ ] **Đã áp dụng đúng quy tắc thời sự trong `rules.md` (chỉ dùng data mới nhất, không đưa data 6T cũ khi đã có 9T) chưa?**
- [ ] Báo cáo Analyst có đúng cấu trúc mẫu chuẩn tại **[examples.md](./examples.md)** chưa?
