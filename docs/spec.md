# Tài Liệu Đặc Tả Kỹ Thuật (System Specification)
# Dự Án: Hệ Thống Tự Động Hóa Phân Tích Cuộc Họp (Meeting Analyst Pipeline)

* **Phiên bản**: 1.0.0
* **Ngày cập nhật**: 16/10/2026
* **Trạng thái**: Đã phê duyệt (Approved)
* **Quy trình áp dụng**: Hybrid Human-in-the-loop (Kết hợp Xử lý Tự động & NotebookLM)

---

## 1. Tổng Quan & Mục Tiêu Dự Án (Project Overview & Objectives)

### 1.1. Bối cảnh bài toán
Người dùng có các file video ghi âm cuộc họp (qua Windows + G hoặc phần mềm họp trực tuyến) có dung lượng lớn (2 – 3 GB / file). Việc đưa trực tiếp video dung lượng lớn này vào các mô hình AI hoặc công cụ Speech-to-Text trực tuyến thường gặp các vấn đề:
- Vượt quá dung lượng tải lên tối đa.
- Tốn băng thông và thời gian xử lý do 90–95% dung lượng là luồng hình ảnh không cần thiết.
- Khó kiểm soát và kiểm chứng tính xác thực của thông tin sau khi tóm tắt.

### 1.2. Mục tiêu hệ thống
Xây dựng một đường ống xử lý bán tự động (Semi-automated Pipeline) giúp:
1. **Tiền xử lý siêu nhẹ (Lightweight Preprocessing)**: Giảm dung lượng file từ hàng GB xuống chỉ còn vài chục MB (giảm 97%+), tự động cắt thành các block audio 25 phút.
2. **Khai thác NotebookLM hiệu quả**: Người dùng sử dụng các chunk MP3 siêu nhẹ để tạo bản script/transcript gốc chất lượng cao bằng NotebookLM.
3. **Chuẩn hóa & Chống suy diễn (Anti-Hallucination & Provenance)**: Đối chiếu transcript gốc với tài liệu họp đính kèm (Slide PDF, kế hoạch) để tạo ra bản Full Transcript chuẩn xác.
4. **Báo cáo Analyst chuyên sâu**: Tự động sinh báo cáo theo chuẩn chuyên viên phân tích tài chính/doanh nghiệp, phân định rành mạch giữa **phát biểu thực tế**, **diễn giải ngữ cảnh** và **nhận định của AI**.

---

## 2. Nguyên Tắc Cốt Lõi (Cardinal Principles)

> [!IMPORTANT]
> **Nguyên tắc bất di bất dịch về tính trung thực dữ liệu**:
> 1. **100% Dữ Kiện Thực Tế, Nghiêm Cấm Nhận Định Của AI (Pure Facts Only - Zero AI Opinions)**:
>    - Toàn bộ nội dung Báo cáo Analyst Meeting và Full Transcript **CHỈ ĐƯỢC** xây dựng từ 2 nguồn: Lời phát biểu của Ban lãnh đạo trong audio/script và Số liệu cứng trên slide tài liệu.
>    - **Tuyệt đối cấm đưa nhận định, suy đoán, dự báo chủ quan của AI vào.** Cái người dùng cần là FACTS, không phải OPINIONS.
> 2. **Không có thì bỏ, tuyệt đối không được bịa ra (Omission over Fabrication)**:
>    - Nếu một mục/chỉ tiêu trong khung mẫu không được đề cập trong cuộc họp hay slide tài liệu, **BẮT BUỘC PHẢI BỎ MỤC ĐÓ**, tuyệt đối không tự ý suy đoán hay lấy kiến thức ngoài lề để điền vào.
> 3. **Tính truy vết (Traceability & Grounding)**: Mọi số liệu trong báo cáo phân tích đều phải dẫn chiếu nguồn (Ví dụ: `(Nguồn: Phút 12:45 trong cuộc họp)` hoặc `(Nguồn: Slide trang 8)`).

---

## 3. Quy Trình Vận Hành Chi Tiết (Operational Workflow)

```
[ GIAI ĐOẠN 1: TIỀN XỬ LÝ MEDIA ] (Antigravity AI)
   Input: Video 2-3GB (MP4, MKV...) hoặc Audio MP3
   │
   ▼
   Trích xuất Audio Stream -> Nén Speech-optimized MP3 -> Cắt đoạn 10 phút
   │
   ▼
   Output: Thư mục chunks/ chứa part_001.mp3, part_002.mp3...
   ═══════════════════════════════════════════════════════════════════
[ GIAI ĐOẠN 2: CHUYỂN GIỌNG NÓI THÀNH VĂN BẢN ] (Người Dùng)
   Input: Các file part_xxx.mp3
   │
   ▼
   Người dùng kéo thả vào NotebookLM -> Tạo Transcript
   │
   ▼
   Output: Lưu file raw_transcript.txt và gửi lại cho AI
   ═══════════════════════════════════════════════════════════════════
[ GIAI ĐOẠN 3: CHUẨN HÓA TRANSCRIPT & ĐỐI CHIẾU ] (Antigravity AI)
   Input: raw_transcript.txt + Tài liệu họp (Slide PDF / File Word)
   │
   ▼
   - Sửa lỗi ngữ cảnh chuyên môn (EBITDA, P/E, Margin, Doanh thu, v.v.)
   - Giữ nguyên verbatim, bổ sung chú thích ngữ cảnh trong ngoặc vuông
   │
   ▼
   Output: full_transcript_standardized.md
   ═══════════════════════════════════════════════════════════════════
[ GIAI ĐOẠN 4: TỔNG HỢP BÁO CÁO ANALYST MEETING ] (Antigravity AI)
   Input: full_transcript_standardized.md + Tài liệu đối chiếu
   │
   ▼
   Phân tích cấu trúc: Executive Summary, Số liệu, Luận điểm, Outlook, Rủi ro, Action Items
   │
   ▼
   Output: analyst_meeting_report.md
```

---

## 4. Đặc Tả Chi Tiết Từng Bước Kỹ Thuật

### 4.1. Giai đoạn 1: Media Processor (`audio_splitter.py`)
- **Đầu vào hỗ trợ**:
  - Video formats: `.mp4`, `.mkv`, `.mov`, `.avi`, `.webm` (kích thước lớn 2 – 5GB).
  - Audio formats: `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`.
- **Thông số kỹ thuật nén âm thanh**:
  - Bỏ toàn bộ hình ảnh (`-vn`).
  - Kênh âm thanh (Channels): `Mono` (`-ac 1`) — Giảm tối đa dung lượng, tập trung vào giọng nói.
  - Tần số lấy mẫu (Sample Rate): `16,000 Hz` (`-ar 16000`) — Chuẩn tần số tối ưu cho mô hình Speech-to-Text & NotebookLM.
  - Tốc độ truyền tải (Bitrate): `64 kbps CBR` (`-b:a 64k`).
- **Cơ chế Cắt Gối Đầu (Sliding Window với Overlap)**:
  - Độ dài tối đa mỗi đoạn (`chunk_duration`): 1500 giây (25 phút).
  - Thời gian gối đầu (`overlap_duration`): 20 giây (mỗi đoạn sau lùi lại 20 giây so với điểm kết thúc đoạn trước để không làm đứt câu thoại).
  - Bước nhảy (`step_size`): 1480 giây (Đoạn thứ $i$ bắt đầu tại $i \times 1480$ giây).
- **Quy tắc đặt tên file (Giữ nguyên thứ tự và mốc thời gian)**:
  - `part_01_00m00s_25m00s.mp3`
  - `part_02_24m40s_49m40s.mp3`
  - `part_03_49m20s_74m20s.mp3`
  - ...
  - `part_{idx:02d}_{start_m:02d}m{start_s:02d}s_{end_m:02d}m{end_s:02d}s.mp3`

### 4.2. Giai đoạn 1.5: Slide Ground Truth Extractor (`extract_ground_truth.py`)
- **Mục tiêu**: Tự động hóa trích xuất số liệu chuẩn từ Slide thuyết trình để làm căn cứ đối soát (Single Source of Truth).
- **Đầu vào hỗ trợ**:
  - File Slide thuyết trình: `.pdf`, `.pptx`.
  - Thư mục chứa các ảnh slide: `.png`, `.jpg`, `.jpeg`.
- **Cơ chế kỹ thuật**:
  - **Trích xuất hình ảnh**: Tự động render từng trang slide sang ảnh chất lượng cao 150 DPI lưu vào `slides/slide_XX.png`.
  - **Động cơ OCR cục bộ**: Sử dụng `RapidOCR` trên nền tảng `onnxruntime` cục bộ (chạy offline 100%, tốc độ ~1.5 - 2s/slide, bảo mật dữ liệu tuyệt đối).
  - **Tái cấu trúc bảng & dòng**: Nhóm các khối chữ theo tọa độ hình học $(x, y)$ thành các dòng bảng phân tích.
- **Đầu ra**:
  - `ground_truth.md`: Báo cáo số liệu chuẩn hóa chi tiết theo từng trang slide.
  - `ground_truth_raw.json`: Toàn bộ dữ liệu thô phục vụ tra cứu tự động.

### 4.3. Giai đoạn 2: NotebookLM Ingestion & Raw Transcript
- Người dùng nhận danh sách các file `part_xxx.mp3` trong thư mục output.
- Kéo thả các file này vào NotebookLM theo từng cụm hoặc toàn bộ.
- NotebookLM tự động phân tích và tạo transcript/ghi chú.
- Người dùng sao chép nội dung transcript và lưu thành `raw_transcript.txt`.

### 4.4. Giai đoạn 3: Chuẩn Hóa Full Transcript (`Bước 4`)
- **Tài liệu nạp vào**:
  1. `raw_transcript.txt`: Bản ghi âm thô từ NotebookLM.
  2. `meeting_docs/`: Các file đính kèm như Slide thuyết trình (`.pdf`), biên bản cuộc họp, kế hoạch kinh doanh.
- **Quy tắc chuẩn hóa ngôn ngữ**:
  - Nhận diện và sửa các từ ngữ chuyên môn Tiếng Việt bị nhận diện sai âm (Ví dụ: *"doanh thu thuần"*, *"lợi nhuận sau thuế"*, *"dự phóng"*, *"chiết khấu"*, *"pha loãng cổ phiếu"*...).
  - Sửa các từ viết tắt chuyên ngành tài chính/công nghệ quốc tế: `EBITDA`, `P/E`, `P/B`, `ROE`, `ROA`, `WACC`, `API`, `SaaS`, `KPI`, `OKR`.
- **Định dạng đầu ra**:
  - Mỗi đoạn hội thoại có mốc thời gian (nếu có) và tên người phát biểu (Speaker A, Speaker B hoặc tên thật nếu xác định được).
  - Phần diễn giải giải thích ngữ cảnh được đặt tách biệt:
    ```markdown
    **Ông Nguyễn Văn A (Giám đốc Tài chính)** [00:14:20]:
    "Quý này biên lợi nhuận gộp của mảng bán lẻ đạt 18.5%, tăng 200 điểm cơ bản so với cùng kỳ."
    > *[Diễn giải từ Slide 12: Mức tăng 200 bps tương đương +2.0%, chủ yếu nhờ tối ưu chi phí logistics và giảm tỷ lệ hàng hủy]*
    ```

### 4.5. Giai đoạn 4: Báo Cáo Analyst Meeting (`Bước 5`)
Báo cáo phân tích hoàn chỉnh được cấu trúc theo 6 phần tiêu chuẩn của các báo cáo phân tích đầu tư và doanh nghiệp:

| Mục báo cáo | Nội dung chi tiết | Quy tắc dẫn chứng |
| :--- | :--- | :--- |
| **1. Executive Summary** | Tóm lược điều hành: 3 – 5 điểm cốt lõi nhất của cuộc họp | Tóm lược khách quan, không đưa quan điểm cá nhân |
| **2. Key Metrics & Financials** | Bảng tổng hợp số liệu: Doanh thu, tăng trưởng, kế hoạch, tỷ suất | Ghi rõ nguồn: [Phát biểu] hay [Slide đối chiếu] |
| **3. Core Arguments** | Các luận điểm chính được ban lãnh đạo và các bên đưa ra thảo luận | Trích dẫn rõ ai phát biểu và lập luận như thế nào |
| **4. Outlook & Guidance** | Kế hoạch tương lai, mục tiêu quý/năm tiếp theo | Dựa trên cam kết và phát biểu của ban điều hành |
| **5. Risk Analysis** | Phân tích rủi ro: Cạnh tranh, thị trường, pháp lý, chi phí phát sinh | Phân định: Rủi ro được họp nêu vs Rủi ro AI nhận định |
| **6. Action Items** | Bảng phân công công việc: Nội dung, Người phụ trách, Hạn chót | Lập bảng rõ ràng, có trạng thái theo dõi |

---

## 5. Cấu Trúc Thư Mục Dữ Liệu Dự Án

```text
./
├── intent.md                          # Ý định dự án & kết quả phỏng vấn
├── spec.md                            # Bản đặc tả kỹ thuật chi tiết (Tài liệu này)
├── audio_splitter.py                  # Script xử lý tách video 2-3GB -> MP3 chunks
├── workspace/                         # Không gian làm việc cho từng cuộc họp
│   └── meeting_01/
│       ├── input_media/               # Chứa video 2-3GB (video.mp4) hoặc audio gốc
│       ├── input_docs/                # Chứa Slide PDF, tài liệu họp đính kèm
│       ├── audio_chunks/              # Chứa part_001.mp3, part_002.mp3... (10 phút/file)
│       ├── raw_transcript.txt         # File script do người dùng lấy từ NotebookLM
│       └── output/
│           ├── full_transcript.md     # Bản Full Transcript chuẩn hóa có diễn giải
│           └── analyst_report.md      # Báo cáo Analyst hoàn chỉnh
```

---

## 6. Tiêu Chuẩn Nghiệm Thu (Acceptance Criteria)

1. **Hiệu suất xử lý Media**:
   - File video 2.3GB được chuyển đổi thành công trong thời gian < 3 phút.
   - Dung lượng toàn bộ các file MP3 con không vượt quá 60MB.
   - Các file MP3 nghe rõ lời thoại, không bị rè, vấp âm thanh, không lệch nhịp thời gian.
2. **Tính dễ dùng với NotebookLM**:
   - Mỗi file nhỏ hơn 10 phút, kích thước dưới 5MB/file, tương thích 100% khi upload vào NotebookLM.
3. **Chất lượng báo cáo Analyst**:
   - Không chứa bất kỳ thông tin nào bịa đặt.
   - Mọi số liệu quan trọng đều có nguồn gốc đối chiếu rõ ràng.
   - Định dạng Markdown chuẩn, sẵn sàng để xuất sang PDF hoặc Word.
