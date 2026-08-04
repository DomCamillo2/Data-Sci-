# Project: Numeral–Demonstrative Side-Harmony in Grambank

**Working title:** How robust is numeral–demonstrative side-harmony in Grambank?  
**Course:** Data Science for Linguists (SoSe 2026) · Johannes Dellert  
**Track:** Variation, Evolution & Change (or unrestricted graded Schein)  
**Grade target:** 1,0  
**Data policy:** no new data collection — public Grambank only  

## Quick links

| Doc | Purpose |
|-----|---------|
| [`PLAN.md`](PLAN.md) | Full 1,0 research plan, critique, mistakes, timeline |
| [`proposal/PROPOSAL_DRAFT.md`](proposal/PROPOSAL_DRAFT.md) | Proposal text (due **31 Aug 2026**) |
| [`reports/GRADE_RUBRIC.md`](reports/GRADE_RUBRIC.md) | What the instructor actually grades |
| [`reports/MISTAKES.md`](reports/MISTAKES.md) | Common mistakes checklist |

## Layout

```
project/
├── README.md
├── PLAN.md
├── requirements.txt
├── .gitignore
├── proposal/           # graded planning artifact
├── data/
│   ├── raw/            # immutable originals (+ provenance)
│   ├── processed/      # analysis-ready tables (generated)
│   └── external/       # optional codebooks / citations only
├── notebooks/          # narrative + figures (main deliverable)
├── src/                # reusable functions (imported by notebooks)
├── figures/            # exported plots for proposal/report
├── reports/            # rubric, mistakes, final writeup notes
└── literature/         # bib / reading notes
```

## Reproduce (after analysis exists)

```bash
cd project
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
# open notebooks/01_data_prep.ipynb … 04_report.ipynb
```

Random seed: **42** (fixed in `src/config.py`).

## GitHub

- **Private repo:** https://github.com/DomCamillo2/grambank-side-harmony  
- Branch: `main` (tracking `origin/main`)  
- Later: invite Dellert under Settings → Collaborators (or `gh repo invite …`)
