# Full Plan for a 1,0 — Grambank Side-Harmony Robustness

Role of this document: research + data-science operating plan.  
Framing decision (locked): **A1 — robustness of side-harmony**, not naive “does harmony exist?” and not Greenberg Universal 20.

---

## 0. Executive verdict

| Item | Decision |
|------|----------|
| Question | How **stable** is Num/Dem **side-harmony** (GB024 × GB025) in Grambank under coding rules and areal structure? |
| Design | Confirmatory replication + sensitivity analysis |
| Data | `grambank.csv` only (already in course materials) |
| Success for 1,0 | Clear RQ/H, proposal adhered to, correct stats, honest limitations, full reproducibility |
| Non-goals | Novelty for its own sake; phylogenetics; scraping; surveys; deep learning |

Session 12 grades **result quality + fidelity to the proposal**. Scope control beats ambition.

---

## 1. Scientific framing (get this right)

### 1.1 What we claim

**Side-harmony:** languages tend to place numeral and adnominal demonstrative on the **same side** of the noun:

| Harmonious | Disharmonious |
|------------|---------------|
| Num-N + Dem-N | Num-N + N-Dem |
| N-Num + N-Dem | N-Num + Dem-N |

Pilot on course file (strict orders, N≈1700): ~**76%** harmonious; by macroarea **65–89%**.

### 1.2 What we do **not** claim

- **Not** Greenberg Universal 20 (relative Dem–Num–Adj order on one side of N).  
  GB024/GB025 do not encode that sequence.
- **Not** a Cinque-style movement analysis.
- **Not** “we discovered a new universal.”

### 1.3 Hypotheses (proposal language)

- **H1:** Harmonious cells are more frequent than expected under independence of GB024 and GB025.
- **H2:** Association strength varies across macroareas.
- **H3 (secondary, optional if listed in proposal):** Macroarea accounts for a non-trivial share of the apparent association (logit / stratified comparison).

Null / “failed” outcome is still a valid grade path if argued cleanly.

---

## 2. What the instructor grades (Session 12)

| Criterion | How to hit 1,0 |
|-----------|----------------|
| Research question clarity | One sentence RQ; variables named (GB024, GB025, Macroarea) |
| Testable hypotheses | H1–H2 mandatory; H3 only if pre-registered in proposal |
| Proposal adherence | Do exactly what the proposal promises; log justified deviations |
| Methods from the course | Pandas wrangling, contingency / association, optional logistic regression, bootstrap (Session 11) |
| Interpretation | Link results to RQ; cite Dryer/WALS-style typology, not overclaim |
| Reproducibility | Raw archive, documented transforms, seeds, README, `requirements.txt` with versions |
| Scope honesty | Explicit in/out; limitations section that anticipates Galton / areal confounding |
| Deliverable | Jupyter notebook with Markdown narrative (+ GitHub invite) |

Workload fiction: 90h/person on paper. Quality density matters more than padding.

---

## 3. Critique of weaker designs (why we rejected them)

| Design | Failure mode |
|--------|----------------|
| A0: “Is there harmony?” | Trivial yes; looks like homework extension |
| “Replicate U20 with GB024×GB025” | Conceptually false → credibility hit |
| Full phylogenetic correction | Correct science, wrong scope for this course deadline |
| Add many extra GB features | Multiple testing + proposal drift |
| New online survey | Explicitly out; not needed for 1,0 |

---

## 4. End-to-end work plan

### Phase P — Proposal (now → **31 Aug 2026**) — critical path

| Step | Deliverable | Done when |
|------|-------------|-----------|
| P1 | Lock title, contributors, track | Written in `proposal/PROPOSAL_DRAFT.md` |
| P2 | Write all 8 Session-12 proposal sections | Self-check against rubric |
| P3 | Freeze scope table (in/out) | No “if time” items that aren’t labeled secondary |
| P4 | Week-by-week plan through Dec | Realistic; AI-assisted coding assumed |
| P5 | Submit to Dellert; wait one feedback round | File `proposal/FEEDBACK.md` with responses |
| P6 | If major revision required | Re-approve before expanding analysis |

**Rule:** After approval, treat proposal as contract.

### Phase D — Data contract

| Step | Action |
|------|--------|
| D1 | Copy/symlink immutable raw CSV → `data/raw/` |
| D2 | Write `data/raw/PROVENANCE.md` (source, date, license/citation) |
| D3 | Document feature definitions (GB024, GB025) from grambank.clld.org |
| D4 | Define inclusion rules in `src/filters.py` (strict vs `both.`) |
| D5 | Never edit raw files; only write `data/processed/` |

### Phase A — Analysis (notebooks)

| Notebook | Purpose |
|----------|---------|
| `01_data_prep.ipynb` | Load, tidy, filter counts, codebook |
| `02_descriptive.ipynb` | Contingency, stacked bars, macroarea rates |
| `03_inference.ipynb` | χ²/Fisher, odds ratios, stratified tests, bootstrap CIs; optional logit |
| `04_report.ipynb` | Narrative tying H1–H3 to results + limitations |

Shared code lives in `src/` (no copy-paste of filter logic across notebooks).

### Phase R — Reproducibility & submission

| Step | Artifact |
|------|----------|
| R1 | `requirements.txt` pinned versions |
| R2 | `README.md` run instructions |
| R3 | Seed = 42 everywhere stochastic |
| R4 | Export key figures → `figures/` |
| R5 | GitHub repo; invite supervisor |
| R6 | Final pass: proposal checklist vs notebook TOC |

---

## 5. Methods specification (implement exactly this)

### 5.1 Sample definitions

1. **Strict:** GB024 ∈ {Num-N, N-Num} and GB025 ∈ {Dem-N, N-Dem}.  
2. **Sensitivity:** report how many languages are dropped for `both.` / missing; optional third analysis treating `both.` separately (descriptive only unless pre-registered).

### 5.2 Primary tests

- 2×2 or 2×2 harmony coding + full 2×2 of orders.
- Odds ratio for same-side vs opposite-side.
- χ² test of independence (report expected counts; if sparse cells → Fisher).
- Effect size (OR + CI), not p-value alone.

### 5.3 Robustness (this is the grade differentiator)

- Repeat association **within each macroarea**.
- Bootstrap CI for global harmony rate and/or OR (Session 11).
- Optional: logistic regression `harmony ~ 1` vs models with macroarea; or predict Dem side from Num side ± macroarea (only if H3 in proposal).

### 5.4 What we acknowledge in Limitations

- Languages are phylogenetically non-independent (Galton).
- Macroarea is a coarse areal proxy, not a family tree.
- Grammar coding uncertainty / missingness in Grambank.
- Side-harmony ≠ Universal 20.

---

## 6. Timeline (solo, AI-assisted)

| Window | Focus | Hours (est.) |
|--------|-------|--------------|
| Now – 10 Aug | Proposal draft + folder freeze | 6–8 |
| 11–31 Aug | Polish proposal, submit | 4–6 |
| Sep (early) | Data prep + descriptive notebooks | 8–12 |
| Sep (late) | Inference + bootstrap + stratif. | 10–14 |
| Oct | Optional logit; figures; narrative | 8–10 |
| Nov | Limitations, README, pin deps, GitHub | 6–8 |
| Dec buffer | Supervisor questions / small fixes | 4+ |

Total ~45–60h of real work if AI writes boilerplate — enough if every section is sharp.

---

## 7. Deliverables checklist (submission)

- [ ] Approved proposal (PDF/MD) matching final notebook
- [ ] `data/raw/` + provenance
- [ ] Notebooks 01–04 executable top-to-bottom
- [ ] `src/` imported, not duplicated
- [ ] `figures/` for main plots
- [ ] `requirements.txt` with versions
- [ ] README with run steps
- [ ] Fixed seeds
- [ ] Explicit limitations section
- [ ] GitHub access for Dellert

---

## 8. Quality bar for 1,0 (self-exam)

Before submit, answer yes to all:

1. Could a typologist skim the intro and see we did **not** confuse U20 with side-harmony?  
2. Does every analysis appear in the proposal (or a logged amendment)?  
3. Are inclusion/exclusion counts reported before any p-value?  
4. Do we report effect sizes + uncertainty, not only significance?  
5. Do we show areal heterogeneity instead of hiding it?  
6. Can a stranger re-run from README in &lt;30 minutes?

If any “no” → fix before calling it done.
