# Topic note — Linguistic loci (reframed L1)

**Status:** Locked framing (2026-08-04): corpus/linguistic question first; models as instruments.

**Title:** Linguistic loci of automatic annotation disagreement in literary German and English (Kafka’s *Trial*)

**Verdict:** GO — addresses teammate concern that a pure model comparison would not match Session 12 example projects.

## What changed vs earlier “SpaCy vs LLM” pitch

| Before | Now |
|--------|-----|
| Main object: systems | Main object: **grammar/categories in literary text** |
| Headline metric: overall agreement | Headline: **where** disagreement happens |
| DE/EN as secondary | DE/EN **profile contrast** as core H2 |

## Pipeline (unchanged)

Kafka → SpaCy tokens → Ollama labels → loci analysis.

See `proposal/PROPOSAL_DRAFT.md` and `IMPLEMENTATION_PLAN.md`.
