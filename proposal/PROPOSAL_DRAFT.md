# Project Proposal (Draft) — L1

**Title:** Agreement between SpaCy and an LLM on POS tags and lemmas in Kafka’s *The Trial* (German vs English)  
**Course:** Data Science for Linguists, Summer 2026  
**Instructor:** Johannes Dellert  
**Contributors:** [NAME 1], [NAME 2]  
**Registration track:** [Language Use / Language & Cognition / unrestricted]  
**Deadline (proposal):** 31 August 2026  
**Deadline (project):** 31 December 2026 (default)

---

## 1. Introduction and research question

Automatic linguistic annotation is a prerequisite for corpus-based work. Classical NLP pipelines such as **SpaCy** and, more recently, **large language models (LLMs)** can both assign part-of-speech tags and lemmas. These systems may diverge—especially on **literary** text, which differs from the news-like data many tools are associated with—and divergence may differ across languages.

We study Franz Kafka’s *Der Prozess* / *The Trial* (public-domain texts already used in this course). We treat SpaCy as a **reference annotator**, not as ground truth: both systems can err. The scientific contribution is a quantified **agreement profile**, not a claim that one system is “correct.”

**Research question:**  
How strongly do SpaCy and a frozen LLM agree on Universal POS (UPOS) tags and lemmas in German and English Kafka, and does agreement differ by language and by POS category?

---

## 2. Objective

1. Build aligned token-level annotations from SpaCy and one LLM on a sampled sentence set (DE + EN).  
2. Estimate overall UPOS agreement and Cohen’s κ (H1).  
3. Compare agreement between German and English (H2).  
4. Localise disagreement via confusion / per-tag error rates (H3).  
5. Quantify uncertainty with bootstrap confidence intervals over sentences.

---

## 3. Preliminary literature and resources

**Course / tools**

- Session 04 (linguistic preprocessing), Assignment 03 (Kafka + SpaCy models `de_core_news_md`, `en_core_web_md`)  
- Session 08/11 ideas: evaluation metrics, resampling for uncertainty  
- Session 12: reproducibility, proposal fidelity  

**Background themes**

- Domain shift and literary NLP (pipelines evaluated on narrative German; e.g. literary processing work such as LLpro / related evaluations)  
- POS evaluation caveats: annotation scheme mismatch and cross-resource divergence (UD-related discussions)  
- Emerging practice of LLMs as annotators — we position our study as a **controlled agreement** study with fixed tokenization  

**Data**

- `kafka_1925_der-prozess.txt`, `kafka_1925_the-trial.txt` (Project Gutenberg / course materials)

---

## 4. Scope

### In scope

- Languages: German + English Kafka texts above  
- SpaCy models as in Assignment 03 (versions pinned in the notebook)  
- One LLM (pinned model ID; temperature 0)  
- Tasks: **UPOS** (primary), **lemma** (secondary)  
- Sampled sentences (~300 per language, random seed 42; stratification by chapter if feasible)  
- Metrics: accuracy vs SpaCy, Cohen’s κ, confusion / per-tag rates, DE vs EN contrast, bootstrap CIs  

### Out of scope

- Human gold annotation  
- Dependency parsing, NER, coreference, sentiment  
- Fine-tuning or training new models  
- Claims that the LLM (or SpaCy) is factually correct  
- Annotating the entire novel via paid API by default  

**Reasons:** time budget; methodological validity (alignment); proposal adherence.

---

## 5. Hypotheses

- **H1:** Token-level UPOS agreement with SpaCy is substantially above chance/majority baseline, but below near-perfect ceiling on this literary sample.  
- **H2:** Agreement rates differ between the German and English samples.  
- **H3:** Disagreements are uneven across UPOS tags (concentrated in categories such as proper nouns or auxiliary/verb distinctions).

---

## 6. Methodology

### Data preparation

- Load raw texts; replace newlines with spaces (Assignment 03).  
- Run SpaCy sentence segmentation and tokenization.  
- Draw the sentence sample; store SpaCy `token` / `upos` / `lemma` tables.

### LLM annotation (critical design choice)

- **SpaCy tokenization is fixed.** The LLM receives an ordered list of tokens and must return one UPOS (and lemma) per index (structured JSON).  
- Free re-tokenization by the LLM is disallowed to avoid spurious disagreement.  
- Invalid / non-UPOS labels mapped to `OTHER` and reported.

### Analysis

- Overall and per-language UPOS agreement + κ  
- Confusion matrices / top disagreement pairs  
- Lemma match rate (normalized strings)  
- Bootstrap CIs for agreement (resample sentences)  

### Work split (two contributors)

- Contributor A: SpaCy pipeline, sampling, metric code  
- Contributor B: LLM prompting, caching, error qualitative examples  
- Joint: interpretation, limitations, final notebook narrative  

---

## 7. Preliminary week plan

| Period | Work |
|--------|------|
| Aug (→ 31) | Finalize & submit proposal; pin tool versions |
| Sep | Data prep, SpaCy annotations, sample export |
| Oct | LLM annotation + agreement analyses + figures |
| Nov | Report notebook, README, requirements, GitHub cleanup |
| Dec | Buffer / supervisor feedback |

Any method not listed here needs a written amendment before entering the graded deliverable.

---

## 8. Expected outcomes

- Numeric agreement profile (DE vs EN) with uncertainty.  
- A map of high- vs low-agreement UPOS categories.  
- Practical takeaway for linguists: when SpaCy and LLM labels are interchangeable for coarse corpus counts—and when they are not.

**If agreement is unexpectedly high or low:** we still report the estimate with CIs and discuss domain, model, and reference limitations—that remains a successful project outcome.

---

## Sign-off

Contributors: _________________ / _________________ Date: _________  
Submitted to supervisor: _________ Feedback received: _________
