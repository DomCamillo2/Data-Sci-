# 02 — LLM annotate

**Status:** stub → convert to `02_llm_annotate.ipynb`

## Goals

1. Load sampled SpaCy token tables
2. For each sentence, prompt LLM with **ordered tokens only**
3. Parse JSON labels (UPOS + lemma) aligned by `tok_id`
4. Cache raw responses under `data/processed/llm_cache/`
5. Write `data/processed/annotations_{de,en}.csv`

**Rule:** LLM must not re-tokenize.
