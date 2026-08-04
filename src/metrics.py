"""Agreement metrics vs SpaCy reference labels."""

from __future__ import annotations

import numpy as np
import pandas as pd

from .config import UPOS_TAGS


def normalize_upos(label: str) -> str:
    lab = (label or "").strip().upper()
    if lab in UPOS_TAGS:
        return lab
    return "OTHER"


def normalize_lemma(lemma: str) -> str:
    return (lemma or "").strip().lower()


def upos_accuracy(ref: pd.Series, hyp: pd.Series) -> float:
    ref_n = ref.map(normalize_upos)
    hyp_n = hyp.map(normalize_upos)
    return float((ref_n == hyp_n).mean())


def lemma_accuracy(ref: pd.Series, hyp: pd.Series) -> float:
    return float((ref.map(normalize_lemma) == hyp.map(normalize_lemma)).mean())


def bootstrap_agreement(
    sent_ids: pd.Series,
    correct: pd.Series,
    n_boot: int = 1000,
    seed: int = 42,
) -> tuple[float, float, float]:
    """Bootstrap mean token accuracy by resampling sentence ids."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"sent_id": sent_ids, "correct": correct.astype(bool)})
    unique = df["sent_id"].unique()
    stats = []
    for _ in range(n_boot):
        chosen = rng.choice(unique, size=len(unique), replace=True)
        part = df[df["sent_id"].isin(chosen)]
        stats.append(part["correct"].mean())
    arr = np.asarray(stats, dtype=float)
    return float(arr.mean()), float(np.quantile(arr, 0.025)), float(np.quantile(arr, 0.975))
