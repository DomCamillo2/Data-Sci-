# Agent guide — Kafka annotation-loci project

## Framing (locked)

- **RQ:** Which UPOS categories show strongest SpaCy↔LLM disagreement, and does the profile differ DE vs EN?
- Track: **Language Use** (corpus linguistics). Models are instruments.
- Out of scope: bake-off claims, human gold, deps/NER, fine-tuning, multi-LLM cook-offs.

## Doc map

| File | Use |
|------|-----|
| `PLAN.md` | Hypotheses + locks |
| `IMPLEMENTATION_PLAN.md` | Execution steps |
| `proposal/PROPOSAL_DRAFT.md` | Submit ≤ 31 Aug 2026 |
| `reports/PREP_STATUS.md` | Checklist |
| `reports/MISTAKES.md` | Anti-patterns |
| `reports/LLM_CHOICE.md` | Frozen Ollama model |
| `src/prompt_template.md` | Annotation prompt |

## Pipeline rules

1. SpaCy tokenizes first; LLM returns one UPOS (+ lemma) per `tok_id`.
2. Seed **42**; model **`llama3.2:3b`**; temperature 0.
3. Prefer `scripts/run_llm_annotate.py` (resumable cache) over ad-hoc notebook loops for full runs.
4. Analysis (notebook 03) leads with **per-UPOS loci** and DE vs EN profiles — not overall accuracy as the headline.

## Course context

Parent workspace `../llm_corpus/` holds lecture/assignment extracts for LLM use.
