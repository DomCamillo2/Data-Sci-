#!/usr/bin/env python3
"""Phase 2: SpaCy parse + sample export for DE/EN Kafka."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.config import (  # noqa: E402
    N_SENTENCES_PER_LANGUAGE,
    RANDOM_SEED,
    RAW_DE,
    RAW_EN,
)
from src.spacy_pipeline import (  # noqa: E402
    load_spacy,
    load_text,
    sample_sentence_ids,
    sentences_to_frame,
)


def prepare_language(lang: str, raw_rel: str) -> None:
    raw_path = ROOT / raw_rel
    print(f"[{lang}] loading {raw_path.name} ...")
    text = load_text(raw_path)
    print(f"[{lang}] chars={len(text):,}; loading spaCy ...")
    nlp = load_spacy(lang)
    # Speed: we only need sentencizer+tagger+morphologizer+lemmatizer+attribute_ruler
    # Keep full pipeline for Assignment-03 parity.
    print(f"[{lang}] parsing (this can take a few minutes) ...")
    df = sentences_to_frame(nlp, text, language=lang)
    non_space = df.loc[~df["is_space"]]
    print(f"[{lang}] tokens={len(df):,} non_space={len(non_space):,} sents={df['sent_id'].nunique():,}")

    # usable sentences: >= 3 non-space tokens
    sizes = non_space.groupby("sent_id").size()
    usable_ids = sizes.loc[sizes >= 3].index
    usable_df = df[df["sent_id"].isin(usable_ids)].copy()
    print(f"[{lang}] usable sents (>={3} tokens)={usable_df['sent_id'].nunique():,}")

    sent_ids = sample_sentence_ids(usable_df, n=N_SENTENCES_PER_LANGUAGE, seed=RANDOM_SEED)
    sample = usable_df[usable_df["sent_id"].isin(sent_ids)].copy()
    # drop pure space tokens from export
    sample = sample.loc[~sample["is_space"], ["language", "sent_id", "tok_id", "token", "upos", "lemma"]]

    out = ROOT / "data" / "processed" / f"tokens_{lang}_sample.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    sample.to_csv(out, index=False)
    print(f"[{lang}] wrote {out} rows={len(sample):,} sents={sample['sent_id'].nunique()}")


def main() -> None:
    prepare_language("de", RAW_DE)
    prepare_language("en", RAW_EN)
    print("DONE")


if __name__ == "__main__":
    main()
