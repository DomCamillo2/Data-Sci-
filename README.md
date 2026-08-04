# Project: SpaCy vs LLM Annotation Agreement on Kafka

**Working title:** How strongly do SpaCy and an LLM agree on POS and lemmas in Kafka’s *Trial* (German vs English)?  
**Course:** Data Science for Linguists (SoSe 2026) · Johannes Dellert  
**Track:** Language Use / Language & Cognition / unrestricted (pick at registration)  
**Grade target:** 1,0  
**Topic code:** L1  

## Quick links

| Doc | Purpose |
|-----|---------|
| [`PLAN.md`](PLAN.md) | Full 1,0 plan, critique, timeline |
| [`proposal/PROPOSAL_DRAFT.md`](proposal/PROPOSAL_DRAFT.md) | Proposal (due **31 Aug 2026**) |
| [`reports/L1_DEEP_DIVE.md`](reports/L1_DEEP_DIVE.md) | Thematic stress test |
| [`reports/GRADE_RUBRIC.md`](reports/GRADE_RUBRIC.md) | Grading checklist |
| [`reports/MISTAKES.md`](reports/MISTAKES.md) | Common mistakes |

## Layout

```
project/
├── PLAN.md
├── README.md
├── requirements.txt
├── proposal/
├── data/raw/            # Kafka DE + EN (immutable)
├── data/processed/      # sampled sentences, annotation tables
├── notebooks/           # 01–04 analysis narrative
├── src/                 # load, sample, align, metrics
├── figures/
├── reports/
└── literature/
```

## GitHub

- **Private repo:** https://github.com/DomCamillo2/grambank-side-harmony  
  (name is legacy; content is L1 — rename on GitHub if desired)  
- Branch: `main`

## Reproduce (after analysis exists)

```bash
cd project
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m spacy download de_core_news_md
python -m spacy download en_core_web_md
jupyter lab
```

Random seed: **42** (`src/config.py`).
