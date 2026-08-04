# 01 — Data prep (SpaCy)

**Status:** stub → convert to `01_data_prep.ipynb`

## Goals

1. Load `data/raw/kafka_1925_*.txt` via `src.spacy_pipeline.load_text`
2. Run DE/EN SpaCy models; build token dataframes
3. Sample `N_SENTENCES_PER_LANGUAGE` sentence ids (seed 42)
4. Export to `data/processed/tokens_{de,en}_sample.csv`

See `PLAN.md` Phase A.
