# Implementation Plan — Linguistic loci (Kafka DE/EN)

**Team:** Dominik Soballa, Luca Bouché (joint)  
**Scientific focus:** category-wise disagreement + DE vs EN profile  
**Tools:** SpaCy + Ollama `llama3.2:3b` (instruments only)

Hard deadlines: Proposal **31 Aug 2026** · Project **31 Dec 2026**

---

## North star

Notebook 04 answers:

1. **Which UPOS categories** disagree most? (H1)  
2. **Do DE and EN profiles differ?** (H2)  
3. Is overall disagreement structured (not random)? (H3)  

Overall accuracy is a **summary statistic**, not the headline.

---

## Phase 0 — Proposal (→ 31 Aug)

| # | Task | Done when |
|---|------|-----------|
| 0.1 | Confirm track (default: Language Use) | written in proposal |
| 0.2 | Submit proposal PDF/MD to Dellert | logged in `FEEDBACK.md` |
| 0.3 | Optional rename GitHub repo | README URL updated |

**Timebox:** 4–8 h

---

## Phase 1 — Environment

| # | Task | Status |
|---|------|--------|
| 1.1 | `.venv` Python 3.11 + SpaCy models | done |
| 1.2 | Ollama + `llama3.2:3b` | done |
| 1.3 | Keep `reports/ENV.txt` / `LLM_CHOICE.md` current | done |

---

## Phase 2 — SpaCy sample *(done)*

| Output | Path |
|--------|------|
| DE tokens | `data/processed/tokens_de_sample.csv` |
| EN tokens | `data/processed/tokens_en_sample.csv` |
| Notebook | `notebooks/01_data_prep.ipynb` |
| Script | `scripts/run_data_prep.py` |

Exit: seed 42 reproducible sent_ids.

---

## Phase 3 — LLM annotation

| # | Task | Output |
|---|------|--------|
| 3.1 | Batch annotate all sample sentences via `src/ollama_client.py` | caches |
| 3.2 | Merge → `annotations_{de,en}.csv` | processed |
| 3.3 | Coverage: parse_ok ≥ 95% | report cell |

Keep Ollama.app open. Overnight OK on M4 Pro.

---

## Phase 4 — Linguistic loci analysis (headline)

| # | Task | Hypothesis |
|---|------|------------|
| 4.1 | Per-UPOS disagreement rate (DE, EN) | H1 |
| 4.2 | Top confusion pairs + examples with linguistic notes | H1 |
| 4.3 | Compare DE vs EN category profiles (table/plot) | H2 |
| 4.4 | Overall acc/κ + bootstrap CI (summary only) | H3 |
| 4.5 | Lemma disagreement as secondary | — |

**Writing rule:** Results section leads with loci/plots, not “LLM scored X%.”

---

## Phase 5 — Report notebook

Order: RQ (linguistic) → data → method (two annotators) → **loci results** → DE/EN → limitations → corpus takeaway.

---

## Phase 6 — Package & submit

Pin requirements; README test by other teammate; invite Dellert; tag release.

---

## Calendar

| When | Focus |
|------|-------|
| → 31 Aug | Proposal submit |
| Sep | Phase 3 annotation |
| Oct | Phase 4 loci analysis |
| Nov | Report + packaging |
| Dec | Buffer |

---

## Immediate next actions

1. Submit reframed proposal  
2. Run full Ollama annotation (Phase 3)  
3. Build loci figures before overall-score tables  
