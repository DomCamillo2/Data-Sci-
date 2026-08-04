#!/usr/bin/env python3
"""Batch-annotate SpaCy sample tokens with Ollama (resumable)."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.ollama_client import DEFAULT_MODEL, annotate_tokens  # noqa: E402


def annotate_language(lang: str, limit: int | None, model: str) -> Path:
    sample_path = ROOT / "data" / "processed" / f"tokens_{lang}_sample.csv"
    cache_dir = ROOT / "data" / "processed" / "llm_cache" / lang
    cache_dir.mkdir(parents=True, exist_ok=True)
    out_path = ROOT / "data" / "processed" / f"annotations_{lang}.csv"

    df = pd.read_csv(sample_path)
    sent_ids = sorted(df["sent_id"].unique())
    if limit is not None:
        sent_ids = sent_ids[:limit]

    rows: list[dict] = []
    n_ok = 0
    n_fail = 0
    t0 = time.time()

    for i, sid in enumerate(sent_ids, 1):
        cache_file = cache_dir / f"sent_{sid}.json"
        sent = df[df["sent_id"] == sid].sort_values("tok_id")
        tokens = sent["token"].astype(str).tolist()
        spacy_upos = sent["upos"].astype(str).tolist()
        spacy_lemma = sent["lemma"].astype(str).tolist()

        parse_ok = True
        err = ""
        labels: list[dict] = []

        if cache_file.exists():
            payload = json.loads(cache_file.read_text(encoding="utf-8"))
            labels = payload.get("labels", [])
            parse_ok = bool(payload.get("parse_ok", True))
            err = payload.get("error", "")
        else:
            try:
                labels = annotate_tokens(tokens, model=model, temperature=0.0)
                cache_file.write_text(
                    json.dumps(
                        {"sent_id": int(sid), "parse_ok": True, "labels": labels, "error": ""},
                        ensure_ascii=False,
                        indent=2,
                    ),
                    encoding="utf-8",
                )
            except Exception as e:  # noqa: BLE001 — resume-friendly batch
                parse_ok = False
                err = str(e)
                labels = [
                    {
                        "tok_id": j,
                        "upos": "X",
                        "lemma": tokens[j],
                        "upos_norm": "OTHER",
                        "upos_valid": False,
                    }
                    for j in range(len(tokens))
                ]
                cache_file.write_text(
                    json.dumps(
                        {"sent_id": int(sid), "parse_ok": False, "labels": labels, "error": err},
                        ensure_ascii=False,
                        indent=2,
                    ),
                    encoding="utf-8",
                )

        if parse_ok:
            n_ok += 1
        else:
            n_fail += 1

        for j, tok in enumerate(tokens):
            lab = labels[j] if j < len(labels) else {}
            rows.append(
                {
                    "language": lang,
                    "sent_id": int(sid),
                    "tok_id": j,
                    "token": tok,
                    "upos_spacy": spacy_upos[j],
                    "lemma_spacy": spacy_lemma[j],
                    "upos_llm": lab.get("upos", "X"),
                    "lemma_llm": lab.get("lemma", tok),
                    "upos_llm_norm": lab.get("upos_norm", "OTHER"),
                    "parse_ok": parse_ok,
                    "error": err,
                }
            )

        if i % 10 == 0 or i == len(sent_ids):
            elapsed = time.time() - t0
            print(
                f"[{lang}] {i}/{len(sent_ids)} sents | ok={n_ok} fail={n_fail} | {elapsed:.0f}s",
                flush=True,
            )

    out = pd.DataFrame(rows)
    out.to_csv(out_path, index=False)
    rate = n_ok / max(len(sent_ids), 1)
    print(f"[{lang}] wrote {out_path} rows={len(out)} parse_ok_rate={rate:.1%}")
    return out_path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--lang", choices=["de", "en", "both"], default="both")
    p.add_argument("--limit", type=int, default=None, help="Max sentences per language (pilot)")
    p.add_argument("--model", default=DEFAULT_MODEL)
    args = p.parse_args()

    langs = ["de", "en"] if args.lang == "both" else [args.lang]
    for lang in langs:
        annotate_language(lang, args.limit, args.model)


if __name__ == "__main__":
    main()
