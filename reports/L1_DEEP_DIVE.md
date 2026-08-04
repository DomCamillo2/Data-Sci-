# L1 Thematic Deep Dive — LLM vs SpaCy on Kafka

**Status:** Topic **locked** (L1). Project docs/repo retargeted 2026-08-04.  
**Verdict:** **GO**, if framed as *reference agreement* (not truth) and scope stays narrow.

---

## 1. Plain-language core

You have the same novel in German and English.  
**SpaCy** (course tool) and an **LLM** both assign labels to words (mainly: part of speech + dictionary form).

We ask: *How often do they agree? Does that differ for German vs English? Which word classes disagree most?*

We do **not** ask: *Which one is correct?* (unless you later add tiny human spot-checks — out of scope by default).

---

## 2. Why this is a real linguistics + data-science topic

| Angle | Why it matters |
|-------|----------------|
| Annotation | Central to corpus linguistics; LLMs are increasingly used as annotators |
| Domain | Literary Kafka ≠ news text many tools saw in training |
| Cross-lingual | DE vs EN with course models `de_core_news_md` / `en_core_web_md` |
| Continuity | Extends Assignment 03 / Session 04 from exploration → systematic evaluation |
| DS methods | Agreement, κ, confusion matrices, stratification, bootstrap CIs |

---

## 3. Stress test (idea check)

### Passes

- Clear variables and units (token, label, language)
- Existing public-domain data (`assignment_03/`)
- Fits graded Session-12 norms (repro, hypotheses, limitations)
- Exciting enough to stay motivated; not a trivial χ² on a known universal
- AI can implement the pipeline; no participant recruitment

### Fails if mishandled

| Failure mode | Effect | Mandatory fix |
|--------------|--------|----------------|
| Treat SpaCy as gold truth | Overclaim; weak science | Call it **reference**; discuss dual error |
| Free LLM tokenization | Fake disagreements | SpaCy tokens fixed → LLM labels that list |
| Too many tasks (POS+Deps+NER…) | Scope explosion | **UPOS + Lemma only** |
| Whole novel via paid API | Cost + non-repro | Sample ~300 sentences/language, seed 42 |
| Unpinned ChatGPT | Irreproducible | Pin model ID or use local/HF model |
| Chat screenshots as “results” | Not a DS project | Tables + metrics in notebook |

### Critical design rule

**1:1 alignment:** SpaCy tokenizes → LLM returns one UPOS (and lemma) per token in JSON → compare.  
If the LLM tokenizes freely, the project is methodologically broken.

---

## 4. Locked research design (recommended)

**Title:** Agreement between SpaCy and an LLM on POS and lemmas in Kafka’s *Trial* (German vs English)

**RQ:** How strongly do SpaCy and a frozen LLM agree on UPOS (and lemmas) in DE/EN Kafka, and where do they diverge?

**H1:** UPOS agreement ≫ chance, but &lt; ceiling on literary text.  
**H2:** Agreement differs between DE and EN.  
**H3:** Disagreement concentrates in specific UPOS tags (e.g. PROPN, AUX/VERB).

**In scope:** UPOS, lemma; sampled sentences; DE+EN; confusion + bootstrap.  
**Out of scope:** human gold, dependencies, NER, fine-tuning, full-book API runs.

**Primary metrics:** token UPOS accuracy vs SpaCy; Cohen’s κ; per-tag confusion; DE vs EN contrast.

---

## 5. Expected findings (even if “boring”)

Typical pattern in annotator comparisons:

- High agreement on closed class / punctuation
- Lower on PROPN / ambiguous VERB–AUX / literary oddities
- Possible DE–EN gap from model quality or morphology (compounds)

That profile **is** the result. You do not need a flashy “LLM wins.”

---

## 6. Final verdict

| Criterion | Score |
|-----------|-------|
| Thematic interest | High |
| Course fit | High |
| 1,0 feasibility | High **if** constraints above held |
| Main scientific risk | Mis-framing SpaCy as truth |
| Compared to Grambank harmony | Stronger motivation, similar grade path |

**Decision:** Proceed with L1. Rewrite proposal before 31 Aug; retarget `project/` repo away from Grambank.
