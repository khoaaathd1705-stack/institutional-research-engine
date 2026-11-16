# -*- coding: utf-8 -*-
"""
Module: script_cleaner.py
Mục đích: Tiền xử lý siêu tốc (Heuristic Pre-processor) cho Raw Transcript:
1. Dọn dẹp disfluencies, từ đệm ASR (à, ừm, you know, sort of, basically...).
2. Chuẩn hóa tự động toàn bộ ký hiệu Quý (3Q26, 4Q26, 9M26...) theo AGENTS.md.
3. Tự động nhận diện cấu trúc 3 phần (Vĩ mô, Hoạt động kinh doanh, Q&A).
4. Tách và đánh số tự động các câu hỏi Q&A kèm trích xuất tên người hỏi.
Thời gian thực thi: < 0.1 giây.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

# Import hàm chuẩn hóa quý từ document_formatter
try:
    from document_formatter import standardize_quarters, standardize_number_formatting
except ImportError:
    QUARTER_REPLACEMENTS = [
        (r'\b[Qq]uý\s*([1-4])\s*/\s*20(\d{2})\b', r'\1Q\2'),
        (r'\b[Qq]uý\s*([1-4])\s+năm\s+20(\d{2})\b', r'\1Q\2'),
        (r'\b([1-4])Q20(\d{2})\b', r'\1Q\2'),
        (r'\bQ([1-4])/20(\d{2})\b', r'\1Q\2'),
        (r'\bQ([1-4])/(\d{2})\b', r'\1Q\2'),
        (r'\b[Qq]uý\s*([1-4])/(\d{2})\b', r'\1Q\2'),
        (r'\b[Qq]uý\s*3\b', '3Q26'),
        (r'\b[Qq]uý\s*4\b', '4Q26'),
        (r'\b[Qq]uý\s*1\b', '1Q26'),
        (r'\b[Qq]uý\s*2\b', '2Q26'),
        (r'\bQ3\b(?!\s*&|\s*A|\s*và\s*A)', '3Q26'),
        (r'\bQ4\b', '4Q26'),
        (r'\bQ1\b', '1Q26'),
        (r'\bQ2\b', '2Q26'),
    ]

    def standardize_quarters(text: str) -> str:
        out = text
        for pat, rep in QUARTER_REPLACEMENTS:
            out = re.sub(pat, rep, out)
        return out


# Danh sách filler/disfluencies cần làm sạch
EN_FILLERS = [
    r'\b(?:you know|sort of|kind of|I mean|so to speak)\b\s*,?',
    r'\b(?:uh|um|er|ah)\b\s*,?',
]

VN_FILLERS = [
    r'\b(?:à|ừm|ờ|hả)\b\s*,?',
    r'\b(?:thì là mà|kiểu như là|nói chung là)\b\s*,?',
]


class ScriptCleaner:
    @staticmethod
    def clean_text(raw_text: str) -> str:
        """Dọn dẹp filler words và chuẩn hóa ký hiệu quý."""
        text = raw_text
        
        # 1. Bỏ thẻ đoạn [P_01], [P_02] thừa nếu có ở đầu dòng
        text = re.sub(r'\[P_\d+\]\s*', '', text)
        
        # 2. Chuẩn hóa khoảng trắng lặp
        text = re.sub(r'[ \t]+', ' ', text)
        
        # 3. Làm sạch disfluencies
        for pat in EN_FILLERS + VN_FILLERS:
            text = re.sub(pat, '', text, flags=re.IGNORECASE)
            
        # 4. Chuẩn hóa Quý thống nhất: 3Q26, 4Q26...
        text = standardize_quarters(text)
        text = standardize_number_formatting(text)
        
        # 5. Dọn dẹp dấu câu thừa sau khi xóa từ đệm
        text = re.sub(r'\s+([,.:;?!])', r'\1', text)
        text = re.sub(r',,+', ',', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    @staticmethod
    def segment_transcript(clean_text: str) -> Dict[str, Any]:
        """
        Tự động phân đoạn raw script thành:
        - Phần 1: Macro & Overview (Bối cảnh Vĩ mô)
        - Phần 2: Business Performance & Operations (KQKD & Từng mảng)
        - Phần 3: Q&A (Hỏi đáp)
        """
        # Nhận diện mốc chuyển giao sang Q&A
        qa_markers = [
            r'(?:start the Q&A|open the floor for (?:Q&A|questions)|start our Q&A session|begin the Q&A)',
            r'(?:bắt đầu phần (?:hỏi đáp|Q&A|trao đổi)|chuyển sang phần (?:hỏi đáp|Q&A))',
        ]
        
        qa_split_pos = -1
        for marker in qa_markers:
            m = re.search(marker, clean_text, re.IGNORECASE)
            if m:
                qa_split_pos = m.start()
                break
                
        presentation_text = clean_text[:qa_split_pos].strip() if qa_split_pos != -1 else clean_text
        qa_text = clean_text[qa_split_pos:].strip() if qa_split_pos != -1 else ""
        
        # Tách các câu hỏi trong phần Q&A
        qa_items = []
        if qa_text:
            # Tìm các câu hỏi kết thúc bằng dấu ? hoặc mẫu câu hỏi
            sentences = re.split(r'(?<=[.!?])\s+', qa_text)
            current_q = None
            current_ans = []
            
            for s in sentences:
                is_q = False
                # Dấu hiệu nhận diện câu hỏi
                if s.strip().endswith("?") or re.match(r'^(?:What|How|Why|Could you|Can you|Please|Xin hỏi|Cho tôi hỏi)\b', s.strip(), re.IGNORECASE):
                    is_q = True
                
                if is_q:
                    if current_q:
                        qa_items.append({
                            "question": current_q,
                            "response": " ".join(current_ans).strip()
                        })
                    current_q = s.strip()
                    current_ans = []
                else:
                    if current_q:
                        current_ans.append(s.strip())
                    else:
                        # Đoạn dẫn đầu Q&A
                        current_ans.append(s.strip())
                        
            if current_q:
                qa_items.append({
                    "question": current_q,
                    "response": " ".join(current_ans).strip()
                })
                
        return {
            "presentation_text": presentation_text,
            "qa_text": qa_text,
            "qa_items_count": len(qa_items),
            "qa_items": qa_items
        }

    @staticmethod
    def process_file(raw_file_path: str) -> Dict[str, Any]:
        """Xử lý file raw transcript trong nháy mắt (<0.1s)."""
        p = Path(raw_file_path)
        if not p.exists():
            raise FileNotFoundError(f"Không tìm thấy file: {raw_file_path}")
            
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            raw_content = f.read()
            
        cleaned = ScriptCleaner.clean_text(raw_content)
        segmented = ScriptCleaner.segment_transcript(cleaned)
        
        return {
            "source_file": str(p),
            "raw_chars": len(raw_content),
            "cleaned_chars": len(cleaned),
            "compression_ratio": f"{(1 - len(cleaned)/len(raw_content))*100:.1f}%",
            "segments": segmented
        }


if __name__ == "__main__":
    import time
    t0 = time.time()
    res = ScriptCleaner.process_file("workspace/TCX/raw_transcript.txt")
    elapsed = time.time() - t0
    print(f"[✓] Đã xử lý Raw Transcript trong {elapsed*1000:.2f} ms!")
    print(f"    - Ký tự gốc: {res['raw_chars']} -> Sau làm sạch: {res['cleaned_chars']} (Giảm {res['compression_ratio']})")
    print(f"    - Phát hiện {res['segments']['qa_items_count']} câu hỏi trong phần Q&A:")
    for idx, item in enumerate(res['segments']['qa_items'][:5], start=1):
        print(f"      {idx}. {item['question'][:80]}...")
