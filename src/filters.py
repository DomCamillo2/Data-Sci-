"""Filtering and harmony helpers for GB024 × GB025."""

from __future__ import annotations

import pandas as pd

from .config import (
    COL_DEM,
    COL_LANGUAGE,
    COL_MACROAREA,
    COL_NUM,
    HARMONIOUS,
    STRICT_DEM,
    STRICT_NUM,
)


def load_raw(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def select_columns(df: pd.DataFrame) -> pd.DataFrame:
    cols = [COL_LANGUAGE, COL_NUM, COL_DEM, COL_MACROAREA]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"Missing columns: {missing}")
    out = df[cols].copy()
    for c in cols:
        out[c] = out[c].astype("string").str.strip()
    return out


def strict_mask(df: pd.DataFrame) -> pd.Series:
    return df[COL_NUM].isin(STRICT_NUM) & df[COL_DEM].isin(STRICT_DEM)


def add_harmony(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["harmony"] = [
        (n, d) in HARMONIOUS for n, d in zip(out[COL_NUM], out[COL_DEM], strict=True)
    ]
    return out


def exclusion_report(df: pd.DataFrame) -> pd.DataFrame:
    """Counts for proposal/notebook transparency."""
    n = len(df)
    m_num = df[COL_NUM].isna() | (df[COL_NUM] == "") | (df[COL_NUM] == "<NA>")
    m_dem = df[COL_DEM].isna() | (df[COL_DEM] == "") | (df[COL_DEM] == "<NA>")
    both = df[COL_NUM].eq("both.") | df[COL_DEM].eq("both.")
    strict = strict_mask(df)
    rows = [
        ("all_rows", n),
        ("missing_GB024_or_GB025", int((m_num | m_dem).sum())),
        ("any_both_order", int(both.sum())),
        ("strict_sample", int(strict.sum())),
    ]
    return pd.DataFrame(rows, columns=["subset", "n"])
