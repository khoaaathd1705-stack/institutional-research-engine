# -*- coding: utf-8 -*-
"""
Script to build HDB_AM.docx and HDS_AM.docx matching the exact format of VPB_AM.docx and VPX_AM.docx.
"""

import os
from pathlib import Path
import docx

def md_to_docx(md_path: Path, docx_path: Path):
    doc = docx.Document()
    
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for line in lines:
        text = line.strip()
        if not text:
            continue
        doc.add_paragraph(text)
        
    doc.save(docx_path)
    print(f"Successfully generated {docx_path}")

if __name__ == "__main__":
    base_dir = Path(r"d:\AM\workspace")
    hdb_md = base_dir / "HDB" / "HDB_AM_Template.md"
    hdb_docx = base_dir / "HDB" / "HDB_AM.docx"
    
    hds_md = base_dir / "HDS" / "HDS_AM_Template.md"
    hds_docx = base_dir / "HDS" / "HDS_AM.docx"
    
    md_to_docx(hdb_md, hdb_docx)
    md_to_docx(hds_md, hds_docx)
