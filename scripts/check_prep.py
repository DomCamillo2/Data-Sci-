#!/usr/bin/env python3
"""Verify all preparations are in place before full annotation / analysis."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
ok = True


def check(cond: bool, msg: str) -> None:
    global ok
    status = "OK " if cond else "FAIL"
    print(f"[{status}] {msg}")
    if not cond:
        ok = False


def main() -> None:
    check((ROOT / "data/raw/kafka_1925_der-prozess.txt").exists(), "raw DE text")
    check((ROOT / "data/raw/kafka_1925_the-trial.txt").exists(), "raw EN text")
    check((ROOT / "data/processed/tokens_de_sample.csv").exists(), "DE SpaCy sample")
    check((ROOT / "data/processed/tokens_en_sample.csv").exists(), "EN SpaCy sample")
    check((ROOT / "proposal/PROPOSAL_DRAFT.md").exists(), "proposal draft")
    check((ROOT / "src/ollama_client.py").exists(), "ollama client")
    check((ROOT / "src/spacy_pipeline.py").exists(), "spacy pipeline")
    check((ROOT / "src/metrics.py").exists(), "metrics helpers")
    check((ROOT / ".venv").exists(), "project venv")

    try:
        import spacy

        spacy.load("de_core_news_md")
        spacy.load("en_core_web_md")
        check(True, f"spaCy models loadable (spacy {spacy.__version__})")
    except Exception as e:  # noqa: BLE001
        check(False, f"spaCy models: {e}")

    try:
        r = requests.get("http://127.0.0.1:11434/api/tags", timeout=5)
        models = [m["name"] for m in r.json().get("models", [])]
        check(r.ok and "llama3.2:3b" in models, f"Ollama API + llama3.2:3b ({models})")
    except Exception as e:  # noqa: BLE001
        check(False, f"Ollama API: {e}")

    print("---")
    if ok:
        print("All preparations OK. Next: python scripts/run_llm_annotate.py")
        sys.exit(0)
    print("Fix FAIL items before full annotation.")
    sys.exit(1)


if __name__ == "__main__":
    main()
