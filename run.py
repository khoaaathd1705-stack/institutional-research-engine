# -*- coding: utf-8 -*-
"""
Entry point thực thi Master Pipeline cho Analyst Meeting (AM).
Cách dùng:
    python run.py workspace/TCX
    python run.py workspace/VPL --period 9M2026
"""
import sys
from pathlib import Path

# Thêm thư mục scripts vào sys.path
scripts_dir = Path(__file__).resolve().parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from am_pipeline import main

if __name__ == "__main__":
    main()
