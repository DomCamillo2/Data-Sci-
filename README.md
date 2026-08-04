# Linguistic loci of annotation disagreement (Kafka DE/EN)

**Team:** Dominik Soballa, Luca Bouché  
**Course:** Data Science for Linguists (SoSe 2026)  
**Track (recommended):** Language Use  

## What this project is

A **corpus-linguistics** study: where automatic POS/lemma annotation becomes unreliable in **literary** German and English (Kafka), and whether those **loci** differ across languages.

SpaCy and a local LLM are two automatic annotators — **instruments**, not the research question.

## What it is not

A leaderboard / “SpaCy vs ChatGPT who wins” bake-off.

## Quick links

| Doc | Purpose |
|-----|---------|
| [`PLAN.md`](PLAN.md) | Topic lock + hypotheses |
| [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md) | Step-by-step execution |
| [`proposal/PROPOSAL_DRAFT.md`](proposal/PROPOSAL_DRAFT.md) | Submit by **31 Aug 2026** |
| [`reports/LLM_CHOICE.md`](reports/LLM_CHOICE.md) | Ollama `llama3.2:3b` |

## Status

- [x] Raw Kafka texts  
- [x] SpaCy samples (300 sents/language) in `data/processed/`  
- [x] Ollama + smoke annotation  
- [ ] Full LLM annotation (notebook 02)  
- [ ] Loci analysis DE/EN (notebook 03)  
- [ ] Report (notebook 04)  

## Setup

```bash
cd project
source .venv/bin/activate   # Python 3.11 via uv
# Ollama.app running; model: llama3.2:3b
python scripts/run_data_prep.py   # regenerate samples if needed
```

## GitHub

https://github.com/DomCamillo2/grambank-side-harmony *(rename recommended)*
