# Project Proposal (Draft)

**Title:** How robust is numeral–demonstrative side-harmony in Grambank?  
**Course:** Data Science for Linguists, Summer 2026  
**Instructor:** Johannes Dellert  
**Contributors:** [YOUR NAME]  
**Registration track:** Variation, Evolution & Change / unrestricted [pick one]  
**Deadline (proposal):** 31 August 2026  
**Deadline (project):** 31 December 2026 (default)

---

## 1. Introduction and research question

Word-order typology has long observed that nominal modifiers often prefer to appear on the **same side** of the noun (side-harmony), a pattern related to—but distinct from—Greenberg’s Universal 20, which concerns the **relative** order of demonstrative, numeral, and adjective when they co-occur.

**Research question:**  
In the Grambank database, how robust is the association between numeral–noun order (GB024) and demonstrative–noun order (GB025) when we (a) apply transparent coding filters and (b) account for macro-areal structure?

We treat this as a **replication-plus-sensitivity** study on an existing typological dataset, not as a claim of a newly discovered universal.

---

## 2. Objective

1. Quantify side-harmony between GB024 and GB025 on a clearly defined sample.  
2. Test whether the association holds under independence baselines (H1).  
3. Assess heterogeneity across Grambank macroareas (H2).  
4. *(Secondary, if time)* Estimate how much macroarea structure reduces the apparent predictive link from numeral order to demonstrative order (H3).

---

## 3. Preliminary literature and resources

**Concepts / typology**

- Dryer, M. S. — Greenbergian word-order correlations; WALS “Order of numeral and noun” / demonstrative–noun order.  
- Greenberg (1963) Universal 20; Cinque (2005); Dryer (2018) — consulted to **avoid** mis-identifying our design with U20.

**Dataset / methods**

- Grambank (Skirgård et al.): feature definitions GB024, GB025 on grambank.clld.org.  
- Course stack: pandas, seaborn/matplotlib, scipy/statsmodels association tests, bootstrap (Session 11), optional logistic regression (Session 07).

**Fallback if stuck:** WALS chapters on numeral/demonstrative order; Grambank feature wiki pages for coding procedures.

---

## 4. Scope

### In scope

- Features: **GB024**, **GB025**, **Macroarea**, language name/ID.  
- Side-harmony coding and contingency analysis.  
- Strict sample (unique unmarked orders) + documentation of excluded `both.` / missing.  
- Stratified tests by macroarea; bootstrap uncertainty.  
- Optional secondary logit only if Phase A finishes early.

### Out of scope

- New data collection or elicitation.  
- Phylogenetic comparative models / cognacy.  
- Full Universal-20 order inventories (Dem–Num–Adj sequences).  
- Large feature sets / unsupervised ML / classification of macroarea (already covered in coursework).  
- Scraping beyond citing official Grambank documentation.

**Reasons:** data already available; time budget; proposal adherence; conceptual clarity.

---

## 5. Hypotheses

- **H1:** Harmonious same-side combinations are more frequent than expected if GB024 and GB025 were independent.  
- **H2:** The strength of association differs across macroareas.  
- **H3 (secondary):** Adding macroarea as a covariate substantially attenuates the coefficient linking numeral order to demonstrative order.

---

## 6. Methodology

### Data

- Source file: course material `grambank.csv` (archived under `data/raw/` with provenance).  
- No redistribution claims beyond Grambank’s own terms; cite Grambank in the notebook.

### Preprocessing

- Map codes to labels (Num-N / N-Num / both.; Dem-N / N-Dem / both.).  
- Primary analysis sample: languages with a single unmarked order for both features.  
- Report exclusion counts before inference.

### Analysis

1. Descriptive contingency tables and visualisation.  
2. Test of independence + odds ratio with confidence interval.  
3. Per-macroarea repetition; summarise heterogeneity.  
4. Bootstrap CIs for key summary statistics.  
5. Optional: logistic regression with/without macroarea (H3).

### Interpretation standard

Emphasise effect sizes and robustness; treat p-values as secondary. Discuss Galton’s problem and coding limitations explicitly.

---

## 7. Preliminary week plan (solo)

| Period | Work |
|--------|------|
| W1–W2 (Aug) | Finalise & submit proposal; archive raw data |
| W3–W4 (Sep) | Data prep notebook; descriptive plots |
| W5–W6 (Sep) | Inference + stratified tests + bootstrap |
| W7–W8 (Oct) | Optional H3; figure polish; draft narrative |
| W9–W10 (Nov) | Limitations, README, pin requirements, GitHub |
| W11–W12 (Dec) | Buffer, supervisor feedback, freeze |

Deviation rule: any method not listed here requires a short written amendment before it enters the graded notebook.

---

## 8. Expected outcomes

- Confirmation or partial confirmation of side-harmony (H1) with quantified uncertainty.  
- A clear map of where the pattern is stronger/weaker (H2).  
- If H3 is run: an estimate of how much “global harmony” is entangled with areal structure.  

**If results are weak or mixed:** we conclude that Grambank side-harmony is less universal than textbook summaries suggest once areal structure and coding filters are taken seriously—and document that as a substantive finding, not a project failure.

---

## Sign-off

Contributor: _________________ Date: _________  
Submitted to supervisor: _________ Feedback received: _________
