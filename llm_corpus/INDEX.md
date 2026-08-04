# Data Science for Linguists — LLM Corpus Index

**Course:** Data Science for Linguists (Summer 2026)  
**Instructor:** Johannes Dellert · Seminar für Sprachwissenschaft, Universität Tübingen  
**Purpose:** Machine-readable full-text extracts of every lecture slide and assignment sheet so an LLM can answer questions without parsing PDFs.

## How an LLM should use this corpus

1. Start here, or `COURSE_MAP.md` / `TOPIC_INDEX.md`, for orientation.
2. Open **only** the relevant `lectures/NN_*.md` or `assignments/exNN.md` file(s).
3. Use `solutions/` only when the user asks for worked solutions.
4. Raw page dumps are generated locally by rebuild scripts (not in git). Prefer these cleaned markdown files.
5. Cite YAML `source_pdf` and `<!-- page:N -->` markers when grounding answers.
6. Assignment data lives in `assignment_NN/` (see `ASSIGNMENTS.md (workspace) / course assignment folders`).

## Directory layout

```
llm_corpus/
  INDEX.md              ← this file
  COURSE_MAP.md         ← syllabus, goals, project rules
  TOPIC_INDEX.md        ← heading index over lectures
  manifest.json         ← machine index of lecture extracts
  lectures/             ← sessions 01–12 (full slide text)
  assignments/          ← ex01–ex08 sheets
  solutions/            ← ex01, ex07, ex08 solutions
```

Rebuild from PDFs: `.venv/bin/python scripts/rebuild_llm_corpus.py`  
and `.venv/bin/python scripts/rebuild_assignments_md.py`.

## Lecture map (full page coverage)

| ID | File | Topic | Pages |
|----|------|-------|------:|
| 01 | [lectures/01_ipython_jupyter.md](lectures/01_ipython_jupyter.md) | Intro, IPython, Jupyter | 34 |
| 02 | [lectures/02_numpy_seaborn.md](lectures/02_numpy_seaborn.md) | NumPy & Seaborn | 27 |
| 03 | [lectures/03_pandas_data_handling.md](lectures/03_pandas_data_handling.md) | Pandas | 40 |
| 04 | [lectures/04_linguistic_preprocessing.md](lectures/04_linguistic_preprocessing.md) | SpaCy / NLTK | 20 |
| 05 | [lectures/05_data_wrangling.md](lectures/05_data_wrangling.md) | Join / reshape | 30 |
| 06 | [lectures/06_data_aggregation_and_grouping.md](lectures/06_data_aggregation_and_grouping.md) | GroupBy | 29 |
| 07 | [lectures/07_modeling_and_prediction.md](lectures/07_modeling_and_prediction.md) | Regression / prediction | 28 |
| 08 | [lectures/08_classification.md](lectures/08_classification.md) | Classification | 41 |
| 09 | [lectures/09_clustering.md](lectures/09_clustering.md) | Clustering | 34 |
| 10 | [lectures/10_pattern_extraction.md](lectures/10_pattern_extraction.md) | PCA / density | 31 |
| 11 | [lectures/11_statistical_inference.md](lectures/11_statistical_inference.md) | Inference | 19 |
| 12 | [lectures/12_data_science_projects.md](lectures/12_data_science_projects.md) | Research projects | 25 |

Source PDFs: `Vorlesungenslides/ (local PDFs; optional)` (optional; markdown is authoritative for LLM work).

## Assignments

| ID | Sheet | Folder | Solution MD |
|----|-------|--------|-------------|
| ex01 | [assignments/ex01.md](assignments/ex01.md) | `assignment_01/` | [ex01_solution.md](solutions/ex01_solution.md) |
| ex02 | [assignments/ex02.md](assignments/ex02.md) | `assignment_02/` | — |
| ex03 | [assignments/ex03.md](assignments/ex03.md) | `assignment_03/` | — |
| ex04 | [assignments/ex04.md](assignments/ex04.md) | `assignment_04/` | — |
| ex05 | [assignments/ex05.md](assignments/ex05.md) | `assignment_05/` | — |
| ex06 | [assignments/ex06.md](assignments/ex06.md) | `assignment_06/` | — |
| ex07 | [assignments/ex07.md](assignments/ex07.md) | `assignment_07/` | [ex07_solution.md](solutions/ex07_solution.md) |
| ex08 | [assignments/ex08.md](assignments/ex08.md) | `assignment_08/` | [ex08_solution.md](solutions/ex08_solution.md) |

## Quick topic → file routing

| User asks about… | Open |
|------------------|------|
| Jupyter / IPython | `01` |
| NumPy / Seaborn | `02` |
| Pandas / missing data | `03` |
| SpaCy / NLTK / lemmas | `04` |
| merge / pivot / MultiIndex | `05` |
| groupby / crosstab | `06` |
| regression / Patsy / CV | `07` |
| NB / SVM / RF / kNN | `08` |
| k-means / GMM / DBSCAN | `09` |
| PCA / MDS / KDE | `10` |
| bootstrap / Bayes / tests | `11` |
| project proposal / tracks | `12` |

## Format convention

```yaml
---
id: "03"
title: "Pandas and Data Handling"
kind: "lecture"
source_pdf: "Vorlesungenslides/...."
pages: N
---
```

```html
<!-- page:12 source:datsci-03-pandas-data-handling.pdf -->
```

## Caveats

- PDF text extraction: spacing quirks, missing figures/plots, incomplete equations.
- `solutions/ex08_solution.md` is large — retrieve subsections, do not dump whole file.
- Consult the PDF only when visuals matter.
