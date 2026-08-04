"""Load Kafka texts and run SpaCy sentence/token pipelines."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import spacy
from spacy.language import Language

from .config import SPACY_MODEL_DE, SPACY_MODEL_EN


def load_text(path: str | Path) -> str:
    """Load file and replace newlines with spaces (Assignment 03 convention)."""
    text = Path(path).read_text(encoding="utf-8")
    return text.replace("\n", " ")


def load_spacy(lang: str) -> Language:
    if lang == "de":
        return spacy.load(SPACY_MODEL_DE)
    if lang == "en":
        return spacy.load(SPACY_MODEL_EN)
    raise ValueError(f"Unsupported lang: {lang}")


def sentences_to_frame(nlp: Language, text: str, language: str) -> pd.DataFrame:
    """Return one row per token with sentence id, token id, text, upos, lemma."""
    doc = nlp(text)
    rows: list[dict] = []
    for sent_i, sent in enumerate(doc.sents):
        for tok_i, tok in enumerate(sent):
            rows.append(
                {
                    "language": language,
                    "sent_id": sent_i,
                    "tok_id": tok_i,
                    "token": tok.text,
                    "upos": tok.pos_,
                    "lemma": tok.lemma_,
                    "is_space": tok.is_space,
                }
            )
    return pd.DataFrame(rows)


def sample_sentence_ids(
    token_df: pd.DataFrame, n: int, seed: int
) -> list[int]:
    """Sample unique sentence ids (exclude empty / whitespace-only sentences)."""
    usable = (
        token_df.loc[~token_df["is_space"]]
        .groupby("sent_id")
        .size()
        .loc[lambda s: s > 0]
        .index.to_series()
    )
    n_take = min(n, len(usable))
    return (
        usable.sample(n=n_take, random_state=seed).sort_values().astype(int).tolist()
    )
