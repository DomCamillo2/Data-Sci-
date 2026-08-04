#!/usr/bin/env python3
"""Rebuild llm_corpus lecture markdown from Vorlesungenslides PDFs.

Produces:
  llm_corpus/raw/*.txt          — full page dumps
  llm_corpus/lectures/*.md      — LLM-oriented markdown (every page kept)
  llm_corpus/manifest.json
  llm_corpus/TOPIC_INDEX.md
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

from pypdf import PdfReader

SCRIPT_DIR = Path(__file__).resolve().parent
# scripts/ may live at workspace root or under project/
CANDIDATE_ROOTS = [SCRIPT_DIR.parent, SCRIPT_DIR.parent.parent]
ROOT = next(
    (p for p in CANDIDATE_ROOTS if (p / "Vorlesungenslides").is_dir() or (p / "llm_corpus").is_dir()),
    SCRIPT_DIR.parent,
)
PDF_DIR = next(
    (p / "Vorlesungenslides" for p in CANDIDATE_ROOTS if (p / "Vorlesungenslides").is_dir()),
    ROOT / "Vorlesungenslides",
)
# Always write corpus next to the course llm_corpus if present, else under ROOT
CORPUS_ROOT = next(
    (p for p in CANDIDATE_ROOTS if (p / "llm_corpus" / "lectures").is_dir()),
    ROOT,
)
OUT_RAW = CORPUS_ROOT / "llm_corpus" / "raw"
OUT_LECT = CORPUS_ROOT / "llm_corpus" / "lectures"

# (id, title, pdf_name, out_stem, date_hint)
LECTURES = [
    ("01", "Introduction, IPython and Jupyter", "datsci-01-ipython-jupyter.pdf", "01_ipython_jupyter", "2026-04-23"),
    ("02", "NumPy and Seaborn", "datsci-02-numpy-seaborn.pdf", "02_numpy_seaborn", None),
    ("03", "Pandas and Data Handling", "datsci-03-pandas-data-handling.pdf", "03_pandas_data_handling", None),
    ("04", "Linguistic Preprocessing", "datsci-04-linguistic-preprocessing.pdf", "04_linguistic_preprocessing", "2026-05-21"),
    ("05", "Data Wrangling", "datsci-05-data-wrangling.pdf", "05_data_wrangling", None),
    ("06", "Data Aggregation and Grouping", "datsci-06-data-aggregation-and-grouping.pdf", "06_data_aggregation_and_grouping", None),
    ("07", "Modeling and Prediction", "datsci-07-modeling-and-prediction.pdf", "07_modeling_and_prediction", "2026-06-25"),
    ("08", "Classification", "datsci-08-classification.pdf", "08_classification", "2026-07-02"),
    ("09", "Clustering", "datsci-09-clustering.pdf", "09_clustering", "2026-07-09"),
    ("10", "Pattern Extraction and Density Estimation", "datsci-10-pattern-extraction.pdf", "10_pattern_extraction", "2026-07-16"),
    ("11", "Statistical Inference", "datsci-11-statistical-inference.pdf", "11_statistical_inference", "2026-07-23"),
    ("12", "Data Science Projects", "DataScience_Lingo.pdf", "12_data_science_projects", "2026-07-30"),
]

HEADER_NOISE = re.compile(
    r"^(Philosophische Fakultät|Seminar für Sprachwissenschaft|"
    r"Data Science for Linguists|Summer 2026)\s*$",
    re.M,
)
FOOTER_NOISE = re.compile(
    r"^\d+\s*\|\s*Johannes Dellert.*$",
    re.M,
)
BULLET = re.compile(r"^[•▷▪◦]\s*", re.M)


def extract_pages(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for page in reader.pages:
        text = page.extract_text() or ""
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        # Normalize common PDF quirks
        text = re.sub(r" +\n", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r" +([,.;:!?])", r"\1", text)
        text = text.strip() + "\n"
        pages.append(text)
    return pages


def clean_page_body(text: str) -> str:
    text = HEADER_NOISE.sub("", text)
    text = FOOTER_NOISE.sub("", text)
    text = BULLET.sub("- ", text)
    # Collapse excess blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def guess_heading(page_text: str, page_no: int) -> str | None:
    """Use first substantial non-bullet line as a section heading when short."""
    lines = [ln.strip() for ln in page_text.splitlines() if ln.strip()]
    if not lines:
        return None
    # Skip pure "Table of Contents" pages for heading? Still keep content.
    first = lines[0]
    if first.startswith("- "):
        return None
    if len(first) > 90:
        return None
    # Avoid repeating session title on every page
    if first.lower().startswith("session ") and page_no > 2:
        if len(lines) > 1 and not lines[1].startswith("- "):
            first = lines[1]
        else:
            return None
    if first in {"Questions", "Course Plan", "Table of Contents"}:
        return first
    # Prefer Title Case / short topic lines
    if first.endswith(":") or (len(first.split()) <= 12 and not first.endswith(".")):
        return first.rstrip(":")
    return None


def write_raw(pdf_name: str, pages: list[str]) -> Path:
    OUT_RAW.mkdir(parents=True, exist_ok=True)
    stem = Path(pdf_name).stem
    out = OUT_RAW / f"{stem}.txt"
    chunks = []
    for i, p in enumerate(pages, 1):
        chunks.append(f"===== PAGE {i}/{len(pages)} =====\n\n{p.rstrip()}\n")
    out.write_text("\n".join(chunks) + "\n", encoding="utf-8")
    return out


def write_lecture_md(
    lecture_id: str,
    title: str,
    pdf_name: str,
    out_stem: str,
    date_hint: str | None,
    pages: list[str],
) -> Path:
    OUT_LECT.mkdir(parents=True, exist_ok=True)
    out = OUT_LECT / f"{out_stem}.md"
    session_title = f"Session {int(lecture_id)}: {title}"
    fm = [
        "---",
        f'id: "{lecture_id}"',
        f'title: "{title}"',
        'kind: "lecture"',
        'course: "Data Science for Linguists"',
        'term: "Summer 2026"',
        'instructor: "Johannes Dellert"',
        f'source_pdf: "Vorlesungenslides/{pdf_name}"',
        f"pages: {len(pages)}",
    ]
    if date_hint:
        fm.append(f'date: "{date_hint}"')
    fm.append("---")

    body: list[str] = [
        "\n".join(fm),
        "",
        f"# {session_title}",
        "",
        f"> Full slide text extracted from `{pdf_name}` for LLM use. "
        "Every PDF page is included; page markers are HTML comments.",
        "",
    ]

    seen_headings: set[str] = set()
    for i, raw in enumerate(pages, 1):
        cleaned = clean_page_body(raw)
        body.append(f"<!-- page:{i} source:{pdf_name} -->")
        body.append("")
        if not cleaned:
            body.append("*(empty / figure-only page)*")
            body.append("")
            continue
        heading = guess_heading(cleaned, i)
        content = cleaned
        if heading and heading not in seen_headings:
            seen_headings.add(heading)
            # Drop the heading line from body if it duplicates
            lines = cleaned.splitlines()
            if lines and lines[0].strip().rstrip(":") == heading:
                content = "\n".join(lines[1:]).strip()
            body.append(f"## {heading}")
            body.append("")
        if content:
            body.append(content)
            body.append("")
        body.append("---")
        body.append("")

    out.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
    return out


def rebuild_topic_index(manifest: list[dict]) -> None:
    lines = [
        "# Topic Index",
        "",
        "Auto-generated from `##` headings in `lectures/`. Use for retrieval routing.",
        "",
    ]
    for entry in manifest:
        path = CORPUS_ROOT / entry["path"]
        text = path.read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, re.M)
        lines.append(f"## Session {entry['id']}: {entry['title']}")
        lines.append("")
        lines.append(f"File: `{entry['path']}`")
        lines.append("")
        for h in headings:
            # Skip ultra-generic repeated footers
            if h in {"Questions", "Course Plan"} and headings.count(h) > 1:
                continue
            lines.append(f"- {h}")
        lines.append("")
    (CORPUS_ROOT / "llm_corpus" / "TOPIC_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    manifest: list[dict] = []
    for lecture_id, title, pdf_name, out_stem, date_hint in LECTURES:
        pdf_path = PDF_DIR / pdf_name
        if not pdf_path.exists():
            raise SystemExit(f"Missing PDF: {pdf_path}")
        pages = extract_pages(pdf_path)
        write_raw(pdf_name, pages)
        md_path = write_lecture_md(lecture_id, title, pdf_name, out_stem, date_hint, pages)
        rel = f"llm_corpus/lectures/{md_path.name}"
        manifest.append(
            {
                "id": lecture_id,
                "title": title,
                "filename": md_path.name,
                "kind": "lecture",
                "source": pdf_name,
                "date": date_hint,
                "path": rel,
                "chars": md_path.stat().st_size,
                "pages": len(pages),
                "extracted": date.today().isoformat(),
            }
        )
        print(f"[OK] {lecture_id} {pdf_name}: {len(pages)} pages → {rel}")

    manifest_path = CORPUS_ROOT / "llm_corpus" / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    rebuild_topic_index(manifest)
    print(f"PDF dir: {PDF_DIR}")
    print(f"Corpus:  {CORPUS_ROOT / 'llm_corpus'}")
    print(f"Wrote {manifest_path} and TOPIC_INDEX.md ({len(manifest)} lectures)")


if __name__ == "__main__":
    main()
