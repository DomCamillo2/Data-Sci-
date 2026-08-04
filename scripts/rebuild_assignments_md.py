#!/usr/bin/env python3
"""Rebuild assignment + solution markdown for llm_corpus from PDFs."""

from __future__ import annotations

import json
import re
from pathlib import Path

from pypdf import PdfReader

SCRIPT_DIR = Path(__file__).resolve().parent
CANDIDATE_ROOTS = [SCRIPT_DIR.parent, SCRIPT_DIR.parent.parent]
ROOT = next(
    (p for p in CANDIDATE_ROOTS if (p / "assignment_01").is_dir() or (p / "llm_corpus").is_dir()),
    SCRIPT_DIR.parent,
)
CORPUS_ROOT = next(
    (p for p in CANDIDATE_ROOTS if (p / "llm_corpus").is_dir()),
    ROOT,
)
OUT_ASS = CORPUS_ROOT / "llm_corpus" / "assignments"
OUT_SOL = CORPUS_ROOT / "llm_corpus" / "solutions"
OUT_RAW = CORPUS_ROOT / "llm_corpus" / "raw_assignments"

ASSIGNMENTS = [
    (1, "Token Frequencies in a First Jupyter Notebook", "assignment_01/datsci-ex01.pdf", "ex01"),
    (2, "Exploring Vocabulary Acquisition Data with NumPy and Seaborn", "assignment_02/datsci-ex02.pdf", "ex02"),
    (3, "Linguistic Preprocessing of a Kafka Novel", "assignment_03/datsci-ex03.pdf", "ex03"),
    (4, "Exploring Typological Feature Dependencies", "assignment_04/datsci-ex04.pdf", "ex04"),
    (5, "Emotion Ratings and Word Frequencies", "assignment_05/datsci-ex05.pdf", "ex05"),
    (6, "Aggregating Lexical Data Across Languages", "assignment_06/datsci-ex06.pdf", "ex06"),
    (7, "Predicting Morphological Complexity", "assignment_07/datsci-ex07.pdf", "ex07"),
    (8, "Dialect Classification and Clustering", "assignment_08/datsci-ex08.pdf", "ex08"),
]

SOLUTIONS = [
    (1, "assignment_01/datsci-ex01-solution.pdf", "ex01_solution"),
    (7, "assignment_07/datsci-ex07-solution.pdf", "ex07_solution"),
    (8, "assignment_08/datsci-ex08-solution.pdf", "ex08_solution"),
]

HEADER_NOISE = re.compile(
    r"^(Philosophische Fakultät|Seminar für Sprachwissenschaft|"
    r"Data Science for Linguists|Summer 2026|Universität Tübingen)\s*$",
    re.M,
)
BULLET = re.compile(r"^[•▷▪◦]\s*", re.M)


def extract_pages(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        text = (page.extract_text() or "").replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r" +\n", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        text = re.sub(r" +([,.;:!?])", r"\1", text)
        pages.append(text.strip() + "\n")
    return pages


def clean(text: str) -> str:
    text = HEADER_NOISE.sub("", text)
    text = BULLET.sub("- ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def write_doc(kind: str, num: int, title: str, rel_pdf: str, out_path: Path, pages: list[str]) -> None:
    pdf_name = Path(rel_pdf).name
    fm = "\n".join(
        [
            "---",
            f'id: "{num:02d}"' if kind != "solution" else f'id: "ex{num:02d}-solution"',
            f'title: "{title}"',
            f'kind: "{kind}"',
            'course: "Data Science for Linguists"',
            'term: "Summer 2026"',
            'instructor: "Johannes Dellert"',
            f'source_pdf: "{rel_pdf}"',
            f"pages: {len(pages)}",
            "---",
        ]
    )
    parts = [
        fm,
        "",
        f"# {title}",
        "",
        f"> Extracted from `{pdf_name}` for LLM use. All pages included.",
        "",
    ]
    for i, raw in enumerate(pages, 1):
        body = clean(raw)
        parts.append(f"<!-- page:{i} source:{pdf_name} -->")
        parts.append("")
        parts.append(body if body else "*(empty / figure-only page)*")
        parts.append("")
        parts.append("---")
        parts.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def write_raw(rel_pdf: str, pages: list[str]) -> None:
    OUT_RAW.mkdir(parents=True, exist_ok=True)
    stem = Path(rel_pdf).stem
    chunks = [f"===== PAGE {i}/{len(pages)} =====\n\n{p.rstrip()}\n" for i, p in enumerate(pages, 1)]
    (OUT_RAW / f"{stem}.txt").write_text("\n".join(chunks) + "\n", encoding="utf-8")


def main() -> None:
    manifest = []
    for num, title, rel, stem in ASSIGNMENTS:
        pdf = ROOT / rel
        if not pdf.exists():
            raise SystemExit(f"Missing {pdf}")
        pages = extract_pages(pdf)
        write_raw(rel, pages)
        out = OUT_ASS / f"{stem}.md"
        write_doc("assignment", num, title, rel, out, pages)
        manifest.append(
            {
                "assignment": num,
                "title": title,
                "llm_md": f"llm_corpus/assignments/{stem}.md",
                "source_pdf": rel,
                "pages": len(pages),
                "folder": f"assignment_{num:02d}",
            }
        )
        print(f"[OK] assignment {num}: {len(pages)} pages → {out.name}")

    for num, rel, stem in SOLUTIONS:
        pdf = ROOT / rel
        pages = extract_pages(pdf)
        write_raw(rel, pages)
        title = f"Assignment {num} Solution"
        out = OUT_SOL / f"{stem}.md"
        write_doc("solution", num, title, rel, out, pages)
        print(f"[OK] solution {num}: {len(pages)} pages → {out.name}")

    (OUT_ASS / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("Wrote assignments/manifest.json")


if __name__ == "__main__":
    main()
