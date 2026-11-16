# Bản Đặc Tả Yêu Cầu & Kế Hoạch Dự Án (Intent & Implementation Plan)
## Hệ Thống Automation: Meeting Analyst Pipeline (Video/MP3 to Analyst Report)

---

## 1. Kết Quả Xác Nhận Ý Định (Clarified Intent)

| Tiêu chí | Lựa chọn từ phỏng vấn | Ghi chú kỹ thuật |
| :--- | :--- | :--- |
| **Dữ liệu đầu vào** | Hỗ trợ cả 2: Video 2-3GB (MP4/MKV/MOV) hoặc file MP3 có sẵn | Dùng `FFmpeg` tách luồng âm thanh, nén chuẩn giọng nói (Speech-optimized MP3) |
| **Chia nhỏ audio (Chunking)** | Cắt thành các đoạn 10-15 phút có đánh số thứ tự | Đáp ứng giới hạn của NotebookLM / Web STT, giữ nguyên timeline |
| **Ngôn ngữ cuộc họp** | Tiếng Việt có pha trộn thuật ngữ Tài chính / Chứng khoán / Tech | Cần prompt & từ điển chuyên ngành để sửa lỗi chính tả theo ngữ cảnh |
| **Cơ chế Speech-to-Text** | Bán tự động (NotebookLM / STT Tool) + Hỗ trợ CLI Ingest | Xuất chunk audio gọn nhẹ -> Người dùng thả vào NotebookLM -> Lưu raw transcript -> Đưa vào CLI xử lý tiếp |
| **Tài liệu đối chiếu** | Có hỗ trợ tải kèm Slide (PDF), File kế hoạch/tài liệu họp | Đưa vào prompt Bước 4 & Bước 5 để AI đối chiếu chéo số liệu thực tế |
| **Giao diện & Vận hành** | Python CLI / Script đơn giản, nhanh, gọn nhẹ | Cấu trúc module rõ ràng, logging đẹp bằng `rich`, lệnh dòng lệnh trực quan |
| **Nguyên tắc cốt lõi** | **Tuyệt đối không bịa đặt** | Phân tách rành mạch 3 tầng dữ liệu: **[Transcript gốc]** vs **[Diễn giải]** vs **[Nhận định AI]** |

---

## 2. Kiến Trúc Chi Tiết Của Hệ Thống (Detailed Architecture)

```
[ Video 2-3GB / File MP3 ]  +  [ Tài liệu họp (PDF / TXT / DOCX) ]
           │
           ▼ (Bước 1 & 2: Preprocessing CLI)
┌────────────────────────────────────────────────────────┐
│ 1. Audio Extractor & Optimizer (FFmpeg)                │
│    - Strip video track -> Nén MP3 64-96kbps Mono       │
│ 2. Audio Chunker                                       │
│    - Chia file thành các block 10 phút (part_01, 02...)│
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Bước 3: STT Ingestion)
┌────────────────────────────────────────────────────────┐
│ 3. NotebookLM / STT Tool                               │
│    - Tải các file audio chunk lên NotebookLM / Whisper │
│    - Xuất và lưu `raw_transcript.txt`                  │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Bước 4: Normalization CLI)
┌────────────────────────────────────────────────────────┐
│ 4. Transcript Normalizer & Fact Checker (LLM Engine)   │
│    - Đối chiếu raw_transcript với Tài liệu họp đính kèm│
│    - Sửa lỗi chính tả từ ngữ chuyên ngành (Finance/Tech│
│    - Giữ nguyên verbatim, bổ sung chú thích trong ngoặc│
│    - Xuất file: `full_transcript_standardized.md`      │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (Bước 5: Analyst Report CLI)
┌────────────────────────────────────────────────────────┐
│ 5. Meeting Analyst Generator (LLM Engine)              │
│    - Tổng hợp: Executive Summary, Số liệu then chốt,   │
│      Luận điểm, Outlook, Rủi ro, Action Items          │
│    - Gắn nhãn nguồn tin: [Phát biểu] vs [AI suy luận]  │
│    - Xuất file: `analyst_meeting_report.md`            │
└────────────────────────────────────────────────────────┘
```

---

## 3. Lộ Trình Triển Khai (Step-by-step Implementation Plan)

### Giai đoạn 1: Thiết lập môi trường & Bộ xử lý Media (Audio Engine)
- Cài đặt & cấu hình môi trường Python 3.10+, thư viện `pydub`, `rich`, `google-genai` (hoặc LLM client), kiểm tra `ffmpeg`.
- Viết module `media_processor.py`:
  - Nhận file đầu vào (Video hoặc Audio).
  - Tự động phát hiện định dạng: nếu là video -> bóc tách audio stream.
  - Nén về định dạng speech tiêu chuẩn (MP3, 64kbps, 16kHz/22.05kHz, Mono) để giảm từ 2-3GB xuống còn ~30-50MB cho cả buổi họp 2 tiếng.
  - Tự động cắt thành các file 10 phút: `output/audio_chunks/chunk_01.mp3`, `chunk_02.mp3`...

### Giai đoạn 2: Trình đọc tài liệu đối chiếu (Document Ingestor)
- Viết module `doc_loader.py` để đọc text từ các file tài liệu cuộc họp đính kèm: Slide thuyết trình (PDF), biên bản, số liệu kinh doanh.
- Trích xuất text sạch để làm ngữ cảnh chuẩn (Context Grounding) cho AI đối chiếu.

### Giai đoạn 3: Module Chuẩn hóa Transcript (Bước 4)
- Viết prompt chuyên biệt cho Tiếng Việt chuyên ngành Tài chính / Doanh nghiệp / Công nghệ.
- Đọc `raw_transcript.txt` từ NotebookLM và tài liệu đính kèm.
- **Ràng buộc Prompt**:
  - Không xóa bỏ hoặc sửa đổi ý người nói.
  - Sửa lỗi nghe nhầm (ví dụ: *EBITDA* bị nhận diện nhầm thành *ê bít đa*, *P/E* thành *pi i*, *dự phóng* thành *dự phòng*...).
  - Đánh dấu rõ ràng diễn giải trong ngoặc vuông `[Diễn giải: ...]`.

### Giai đoạn 4: Module Phân tích Cuộc họp Analyst Meeting (Bước 5)
- Viết prompt tổng hợp báo cáo theo chuẩn Analyst:
  1. **Executive Summary**: Tóm tắt 3-5 ý cốt lõi.
  2. **Key Financial & Operating Metrics**: Bảng số liệu, chỉ số, doanh thu, lợi nhuận, kế hoạch được công bố.
  3. **Core Arguments & Insights**: Luận điểm của ban lãnh đạo / các bên tham gia.
  4. **Future Outlook & Guidance**: Triển vọng thị trường, định hướng thời gian tới.
  5. **Risk Analysis**: Rủi ro cạnh tranh, chính sách, tài chính, vận hành.
  6. **Action Items**: Nhiệm vụ, người chịu trách nhiệm, thời hạn bàn giao.
- **Tuân thủ quy tắc chống bịa đặt**: Mọi thông tin đều gắn citation hoặc phân định rõ:
  - `(Nguồn: Phát biểu của [Tên/Vai trò] tại phút XX)`
  - `(Ghi chú AI: Phân tích bổ sung dựa trên tài liệu đính kèm)`

### Giai đoạn 5: Tích hợp CLI hoàn chỉnh & Hướng dẫn sử dụng
- Xây dựng CLI `main.py` với các lệnh:
  - `python main.py prepare --input meeting.mp4` (Tách video 2.3GB -> nén -> chia chunk 10 phút)
  - `python main.py normalize --transcript raw.txt --docs doc1.pdf` (Chuẩn hóa transcript)
  - `python main.py analyze --transcript normalized.md --docs doc1.pdf` (Xuất báo cáo Analyst)
  - Hoặc 1 lệnh liên kết mượt mà.
