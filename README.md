# Linguistic loci of annotation disagreement in Kafka DE/EN

A corpus-linguistics project on where automatic POS/lemma annotation becomes unreliable in literary German and English, and whether the disagreement profile differs across languages.

## Project summary

This project uses Kafka’s German and English prose as a test case for annotation instability in real literary language. The focus is not on deciding which system is “better,” but on identifying the grammatical categories where annotation disagreement becomes systematic.

We compare two automatic annotators on the same tokenized sentences:
- SpaCy as the token-alignment baseline
- a local Ollama LLM as the second annotation system

The research question is:

Which UPOS categories show the strongest disagreement between automatic annotators in Kafka’s literary German and English, and does the disagreement profile differ between the two languages?

## Core hypotheses

- H1: disagreement is uneven across UPOS categories
- H2: DE and EN disagreement profiles differ
- H3: overall agreement is above chance but below ceiling

## What this project is not

- not a model leaderboard
- not a “SpaCy vs ChatGPT” comparison
- not a dependency or NER benchmark
- not a fine-tuning project

## Repository guide

| Purpose | Location |
|---|---|
| Full project brief for future LLMs | [AGENTS.md](AGENTS.md) |
| Short routing pointer | [llms.txt](llms.txt) |
| Topic lock and RQ | [PLAN.md](PLAN.md) |
| Execution roadmap | [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) |
| Proposal draft | [proposal/PROPOSAL_DRAFT.md](proposal/PROPOSAL_DRAFT.md) |
| Prep checklist | [reports/PREP_STATUS.md](reports/PREP_STATUS.md) |
| Change log | [reports/CHANGELOG_RUNS.md](reports/CHANGELOG_RUNS.md) |
| Course corpus / lecture archive | [llm_corpus/INDEX.md](llm_corpus/INDEX.md) |
| Analysis notebooks | [notebooks](notebooks) |
| Annotation scripts | [scripts](scripts) |
| Source code | [src](src) |

## Current status

- [x] Kafka DE/EN raw texts archived
- [x] Fixed token samples for DE and EN
- [x] Prep validation passes
- [x] Ollama + llama3.2:3b setup
- [x] Annotation pipeline and trial checks
- [ ] Full 300+300 annotation run
- [ ] Loci analysis and report
- [ ] Final proposal hand-in

## Quick start

```bash
cd project
source .venv/bin/activate
python scripts/check_prep.py
python scripts/run_llm_annotate.py
```

Make sure Ollama is running and the model `llama3.2:3b` is available.

## Project structure

```text
project/
├── AGENTS.md
├── PLAN.md
├── IMPLEMENTATION_PLAN.md
├── README.md
├── data/
├── figures/
├── llm_corpus/
├── notebooks/
├── proposal/
├── reports/
├── scripts/
├── src/
└── requirements.txt
```

## GitHub

https://github.com/DomCamillo2/Data-Sci-

## Team

- Dominik Soballa
- Luca Bouché

Course: Data Science for Linguists (SoSe 2026)
