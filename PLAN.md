# Full Plan for a 1,0 — L1 SpaCy vs LLM on Kafka

Locked topic after thematic deep dive (`reports/L1_DEEP_DIVE.md`).  
Former Grambank side-harmony plan is **abandoned**.

---

## 0. Executive verdict

| Item | Decision |
|------|----------|
| Question | How strongly do SpaCy and a frozen LLM agree on **UPOS** (and **lemmas**) in Kafka DE/EN, and where do they diverge? |
| Design | Reference-agreement study (SpaCy ≠ truth) |
| Data | `kafka_1925_der-prozess.txt`, `kafka_1925_the-trial.txt` |
| Success for 1,0 | Clear RQ/H, fixed tokenization, pinned models, metrics + limitations, proposal fidelity |
| Non-goals | Human gold, deps/NER, fine-tuning, “LLM is better”, full-book API runs |

---

## 1. Scientific framing

### Claim

Measure **system agreement** between:

1. SpaCy pipelines (`de_core_news_md`, `en_core_web_md`)  
2. One frozen LLM prompted to label **pre-tokenized** tokens

on literary text in two languages.

### Non-claim

- Not Universal 20 / typology  
- Not proof that either system is correct  
- Not a chatbot or generation demo  

### Hypotheses

- **H1:** UPOS agreement ≫ chance / majority baseline, but below ceiling on literary text.  
- **H2:** Agreement differs between German and English.  
- **H3:** Disagreement concentrates in specific UPOS tags (e.g. PROPN, AUX/VERB).

---

## 2. What Dellert grades (Session 12)

| Criterion | How L1 hits it |
|-----------|----------------|
| Clear RQ | Agreement + DE/EN contrast named |
| Testable H | H1–H3 pre-registered |
| Proposal fidelity | Only UPOS+lemma (+ listed secondary) |
| Course methods | SpaCy (S04), tables/plots, κ/confusion, bootstrap (S11) |
| Reproducibility | Raw texts archived; model IDs; T=0; seed 42; requirements |
| Limitations | Reference≠gold; literary domain; tokenization rule |

---

## 3. Critical design rules (non-negotiable)

1. **SpaCy tokenizes; LLM only labels** that token list (JSON 1:1).  
2. **UPOS only** as primary tagset (map LLM output; invalid → `OTHER`).  
3. **Sample** sentences (e.g. 300/language), not the whole novel by default.  
4. **One LLM**, one prompt version, temperature 0.  
5. Report **DE and EN separately**.

Violating (1) breaks the evaluation.

---

## 4. Work plan

### Phase P — Proposal (→ 31 Aug 2026)

| Step | Deliverable |
|------|-------------|
| P1 | Fill contributors + track in proposal |
| P2 | Submit `proposal/PROPOSAL_DRAFT.md` (export PDF if required) |
| P3 | Log supervisor feedback in `proposal/FEEDBACK.md` |

### Phase D — Data

| Step | Action |
|------|--------|
| D1 | Keep raw Kafka texts immutable under `data/raw/` |
| D2 | SpaCy sentence split + token tables → `data/processed/` |
| D3 | Draw stratified sample (seed 42) → `sample_sentences_{de,en}.csv` |

### Phase A — Analysis notebooks

| Notebook | Content |
|----------|---------|
| `01_data_prep` | Load texts, SpaCy parse, sample, export token tables |
| `02_llm_annotate` | Call LLM on token lists; cache outputs |
| `03_agreement` | Accuracy, κ, confusion, DE vs EN, bootstrap CIs |
| `04_report` | Narrative answering H1–H3 + limitations |

### Phase R — Submit

README, pinned `requirements.txt`, figure exports, GitHub invite to supervisor.

---

## 5. Methods spec

### SpaCy

- DE: `de_core_news_md` · EN: `en_core_web_md` (same as Assignment 03)  
- Replace newlines with spaces before parsing (Assignment 03 rule)  
- Record package + model versions in notebook

### LLM

- Prefer pinned open model (local/HF) **or** documented API model ID + date  
- Prompt: given ordered tokens, return UPOS (+ lemma) per index  
- Temperature 0; refuse free tokenization  

### Metrics

- Token UPOS accuracy vs SpaCy  
- Cohen’s κ  
- Per-UPOS confusion / error rates  
- Lemma match rate (normalized: lowercased lemma string)  
- Bootstrap CI over sentences for agreement  

### Sample (default proposal numbers — adjust only via amendment)

- ~300 sentences per language  
- Stratify by chapter if chapter markers exist; else uniform with seed 42  

---

## 6. Timeline (pair, AI-assisted)

| Window | Focus |
|--------|-------|
| Now–10 Aug | Proposal finalize + team roles |
| → 31 Aug | Submit proposal |
| Sep | Data prep + SpaCy baselines + sample |
| Oct | LLM annotation + agreement analyses |
| Nov | Report notebook, limitations, pin deps |
| Dec | Buffer / supervisor fixes |

Suggested split: Partner A = SpaCy/data/metrics; Partner B = LLM prompting/caching; both = interpretation.

---

## 7. Deliverables checklist

- [ ] Approved proposal matching notebook  
- [ ] Raw Kafka + provenance  
- [ ] Processed sample + annotation caches  
- [ ] Notebooks 01–04 runnable  
- [ ] `src/` shared (no duplicated filter logic)  
- [ ] requirements + model download notes  
- [ ] Seeds / T=0 / model IDs documented  
- [ ] Limitations section  
- [ ] GitHub access for Dellert  

---

## 8. Pre-submit self-exam

1. Does the intro say SpaCy is a **reference**, not gold?  
2. Is tokenization fixed to SpaCy?  
3. Are H1–H3 answered with numbers + figures?  
4. Are DE and EN not pooled into one misleading accuracy?  
5. Can a stranger re-run from README?
