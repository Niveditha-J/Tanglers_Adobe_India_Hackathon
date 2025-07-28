import os
import fitz  # PyMuPDF
import re


def is_heading(text):
    return re.match(r"^\d+\.", text) or text.istitle()


def get_level(text):
    if re.match(r"^\d+\.\d+\.\d+", text): return "H3"
    elif re.match(r"^\d+\.\d+", text): return "H2"
    elif re.match(r"^\d+\.", text): return "H1"
    return "H1" if text.istitle() else None


def extract_sections_from_pdf(file_path):
    doc = fitz.open(file_path)
    sections = []
    current_section = None

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if not text or len(text) < 3:
                continue

            if is_heading(text):
                level = get_level(text)
                current_section = {
                    "document": os.path.basename(file_path),
                    "page": page_num,
                    "section_title": text,
                    "level": level,
                    "content": []
                }
                sections.append(current_section)
            elif current_section:
                current_section["content"].append(text)

    return sections
