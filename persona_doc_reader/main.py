from extractor.persona_extractor import extract_sections_from_pdf
import os
import json
import re
from datetime import datetime


# Job-specific keywords
KEYWORDS = [
    "trip", "plan", "itinerary", "activities", "things to do",
    "beach", "group", "college", "friends", "day", "day 1", "day 2",
    "restaurant", "hotel", "nightlife", "budget", "tips", "adventure",
    "cultural", "relaxation", "travel", "transport", "packing", "fun"
]


def clean_text(text):
    return re.sub(r"\s+", " ", text).strip()


def weighted_rank_sections(sections):
    ranked = []

    for sec in sections:
        title = sec["section_title"].lower()
        content = " ".join(sec["content"]).lower()
        score = 0

        # Boost keywords in title
        score += sum(3 for kw in KEYWORDS if kw in title)

        # Regular keyword match in content
        score += sum(1 for kw in KEYWORDS if kw in content)

        if score >= 4:  # Only include relevant ones
            ranked.append({
                "document": sec["document"],
                "section_title": sec["section_title"],
                "importance_rank": score,
                "page_number": sec["page"]
            })

    ranked.sort(key=lambda x: -x["importance_rank"])
    return ranked


def extract_focused_subsections(ranked_sections, all_sections):
    refined = []

    for ranked in ranked_sections:
        doc = ranked["document"]
        page = ranked["page_number"]

        for sec in all_sections:
            if (
                sec["document"] == doc
                and sec["page"] == page
                and sec["section_title"] == ranked["section_title"]
            ):
                content = " ".join(sec["content"])
                sentences = re.split(r'(?<=[.!?]) +', content)
                filtered = [
                    s for s in sentences if any(kw in s.lower() for kw in KEYWORDS)
                ]
                snippet = " ".join(filtered[:4]) if filtered else content[:400]
                refined.append({
                    "document": doc,
                    "page": page,
                    "refined_text": clean_text(snippet)
                })
                break

    return refined


def main():
    print(" Starting enhanced persona-based extractor...")

    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    input_data = {
        "documents": [
            {"filename": f} for f in os.listdir(input_dir) if f.endswith(".pdf")
        ],
        "persona": {"role": "Travel Planner"},
        "job_to_be_done": {
            "task": "Plan a trip of 4 days for a group of 10 college friends."
        }
    }

    all_sections = []
    for doc in input_data["documents"]:
        filepath = os.path.join(input_dir, doc["filename"])
        sections = extract_sections_from_pdf(filepath)
        all_sections.extend(sections)
        print(f" Parsed {len(sections)} sections from {doc['filename']}")

    ranked_sections = weighted_rank_sections(all_sections)
    refined_texts = extract_focused_subsections(ranked_sections, all_sections)

    top_ranked = ranked_sections[:3]
    top_refined = refined_texts[:2]

    output = {
        "metadata": {
            "documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": input_data["persona"]["role"],
            "job_to_be_done": input_data["job_to_be_done"]["task"],
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": [
            {
                "document": sec["document"],
                "page": sec["page_number"],
                "section_title": sec["section_title"],
                "importance_rank": sec["importance_rank"]
            }
            for sec in top_ranked
        ],
        "subsection_analysis": top_refined
    }

    out_path = os.path.join(output_dir, "persona_output.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f" Output saved to {out_path}")


if __name__ == "__main__":
    main()
