"""Ollama HTTP client for token-aligned UPOS/lemma annotation."""

from __future__ import annotations

import json
import re
from typing import Any

import requests

from .config import UPOS_TAGS
from .metrics import normalize_upos

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
DEFAULT_MODEL = "llama3.2:3b"

PROMPT_TEMPLATE = """You are a linguistic annotator.
You receive a JSON list of tokens in order.
Return ONLY a JSON list of the same length (no markdown, no commentary).
Each item must be an object:
  {{"tok_id": <int>, "upos": <UD UPOS tag>, "lemma": <string>}}
Use only these UPOS tags:
ADJ ADP ADV AUX CCONJ DET INTJ NOUN NUM PART PRON PROPN PUNCT SCONJ SYM VERB X
Do not add, remove, or split tokens.

Tokens:
{tokens_json}
"""


def _extract_json_list(text: str) -> list[Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    start = text.find("[")
    end = text.rfind("]")
    if start < 0 or end < 0:
        raise ValueError("No JSON list found in model output")
    return json.loads(text[start : end + 1])


def annotate_tokens(
    tokens: list[str],
    model: str = DEFAULT_MODEL,
    temperature: float = 0.0,
    timeout: int = 120,
) -> list[dict[str, Any]]:
    """Return list of {tok_id, upos, lemma, upos_norm} aligned to input tokens."""
    payload_tokens = [{"tok_id": i, "token": t} for i, t in enumerate(tokens)]
    prompt = PROMPT_TEMPLATE.format(tokens_json=json.dumps(payload_tokens, ensure_ascii=False))
    resp = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": temperature},
        },
        timeout=timeout,
    )
    resp.raise_for_status()
    raw = resp.json().get("response", "")
    items = _extract_json_list(raw)
    if len(items) != len(tokens):
        raise ValueError(f"Length mismatch: got {len(items)} labels for {len(tokens)} tokens")

    out: list[dict[str, Any]] = []
    for i, item in enumerate(items):
        upos = str(item.get("upos", "X"))
        lemma = str(item.get("lemma", tokens[i]))
        out.append(
            {
                "tok_id": i,
                "upos": upos,
                "lemma": lemma,
                "upos_norm": normalize_upos(upos),
                "upos_valid": normalize_upos(upos) in UPOS_TAGS or normalize_upos(upos) == "OTHER",
            }
        )
    return out
