import fitz 
import os
import json
import re


def is_junk(text):
    if not text.strip():
        return True
    junk_patterns = [
        r"^[\s\.,\-–—]*$",
        r"^\d{1,2}$",
        r"^[A-Z]{1,2}\d{0,2}$",
        r"^(Page \d+ of \d+)$",
        r"^(Yes|No|N/A|Rs\.?)$",
        r"^(Name|Age|Date|S\.?No|Amount|Remarks)$",
        r"^\d+\.?$",
        r"^\d+\.\d+$",
        r"^\d+\.\d+\s*$",
        r"^\d+\.\s*$"
    ]
    return any(re.match(pattern, text.strip(), re.IGNORECASE) for pattern in junk_patterns)


def get_level_from_text(text):
    if re.match(r"^\d+\.\d+\.\d+", text): return "H3"
    elif re.match(r"^\d+\.\d+", text): return "H2"
    elif re.match(r"^\d+\.", text): return "H1"
    return None


def extract_outline(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    all_lines, headings, title_lines = [], [], []
    toc_detected = False
    toc_page = -1

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                text = ""
                max_size = 0
                bold = False
                font = ""

                for span in line["spans"]:
                    if is_junk(span["text"]): continue
                    text += span["text"].strip() + " "
                    if span["size"] > max_size:
                        max_size = span["size"]
                        font = span["font"]
                    if "Bold" in span["font"] or span.get("flags", 0) & 2:
                        bold = True

                full_text = text.strip()
                if not full_text or is_junk(full_text): continue

                # Detect if this is TOC page
                if "table of contents" in full_text.lower():
                    toc_detected = True
                    toc_page = page_num

                # Skip TOC lines (but not the entire page)
                if toc_detected and page_num == toc_page and re.match(r"^\d+(\.\d+)*(\s+.+)?$", full_text):
                    continue

                all_lines.append({
                    "text": full_text,
                    "size": max_size,
                    "font": font,
                    "bold": bold,
                    "page": page_num
                })

    sizes = [line["size"] for line in all_lines]
    avg_size = sum(sizes) / len(sizes) if sizes else 12
    top_sizes = sorted(set(sizes), reverse=True)

    
    for line in all_lines:
        if line["page"] == 1 and line["size"] == top_sizes[0]:
            title_lines.append(line["text"])
    title = " ".join(title_lines).strip()

    seen = set()
    for line in all_lines:
        text = line["text"]
        if text in seen or is_junk(text):
            continue
        seen.add(text)

        level = get_level_from_text(text)

        # Skip numbered-only TOC-style lines
        if level == "H3" or re.match(r"^\d+(\.\d+)*$", text.strip()):
            continue

        # Ignore paragraph-like content
        if len(text.split()) > 15:
            continue

        score = 0
        if line["size"] >= avg_size: score += 1
        if line["bold"]: score += 1
        if len(text.split()) <= 12: score += 1
        if re.match(r"^[A-Z0-9]", text): score += 1
        if not text.endswith("."): score += 1
        if text.isupper(): score += 1

        if score >= 3 or level in {"H1", "H2"}:
            if not level:
                if line["size"] == top_sizes[0]:
                    level = "H1"
                elif len(top_sizes) > 1 and line["size"] == top_sizes[1]:
                    level = "H2"
                else:
                    continue
            headings.append({
                "level": level,
                "text": text,
                "page": line["page"]
            })

    # Fallback for flyer-style docs (like file05)
    if not headings and all_lines:
        top_line = max(all_lines, key=lambda l: (l["size"], l["bold"]))
        headings.append({
            "level": "H1",
            "text": top_line["text"],
            "page": top_line["page"]
        })

    output = {
        "title": title,
        "outline": headings
    }

    os.makedirs(output_path, exist_ok=True)
    out_file = os.path.join(output_path, os.path.splitext(os.path.basename(pdf_path))[0] + ".json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Outline saved to: {out_file}")
