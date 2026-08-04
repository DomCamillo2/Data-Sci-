# Linguistic loci of annotation disagreement (Kafka DE/EN)

**Team:** Dominik Soballa, Luca Bouché  
**Course:** Data Science for Linguists (SoSe 2026)  
**Track (recommended):** Language Use  

## What this project is

A **corpus-linguistics** study: where automatic POS/lemma annotation becomes unreliable in **literary** German and English (Kafka), and whether those **loci** differ across languages.

SpaCy and a local LLM are two automatic annotators — **instruments**, not the research question.

## What it is not

A leaderboard / “SpaCy vs ChatGPT who wins” bake-off.

## LLM / agent entrypoints

| What | Where |
|------|--------|
| **Full instructions for future LLMs** | [`AGENTS.md`](AGENTS.md) |
| Short pointer | [`llms.txt`](llms.txt) |
| Run & change log | [`reports/CHANGELOG_RUNS.md`](reports/CHANGELOG_RUNS.md) |
| All lecture slides (markdown) | [`llm_corpus/INDEX.md`](llm_corpus/INDEX.md) |
| Topic lock | [`PLAN.md`](PLAN.md) |
| Proposal draft | [`proposal/PROPOSAL_DRAFT.md`](proposal/PROPOSAL_DRAFT.md) |
| Prep checklist | [`reports/PREP_STATUS.md`](reports/PREP_STATUS.md) |
| LLM choice | [`reports/LLM_CHOICE.md`](reports/LLM_CHOICE.md) |

## Status

- [x] Raw Kafka texts  
- [x] SpaCy samples (300 sents/language)  
- [x] Ollama + smoke/pilot annotation  
- [x] Prep scripts + notebooks 01–04  
- [ ] Full LLM annotation 300+300  
- [ ] Loci analysis DE/EN  
- [ ] Report + proposal submit  

See `reports/PREP_STATUS.md`.

## Setup

```bash
cd project
source .venv/bin/activate   # Python 3.11 via uv
# Ollama.app running; model: llama3.2:3b
python scripts/run_data_prep.py   # regenerate samples if needed
```

## GitHub

https://github.com/DomCamillo2/Data-Sci-
