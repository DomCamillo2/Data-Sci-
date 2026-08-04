# Preparations checklist

Last verified: 2026-08-04

Full run/change history: [`CHANGELOG_RUNS.md`](CHANGELOG_RUNS.md) · latest trial: [`TRIAL_RUN.md`](TRIAL_RUN.md)

- [x] Topic framed as linguistic loci (Language Use)
- [x] Proposal draft complete (`proposal/PROPOSAL_DRAFT.md`)
- [x] Raw Kafka texts archived
- [x] Python 3.11 venv + SpaCy DE/EN models
- [x] Ollama + `llama3.2:3b`
- [x] SpaCy samples 300/lang (`tokens_*_sample.csv`)
- [x] Batch annotator script (`scripts/run_llm_annotate.py`)
- [x] Prep check script (`scripts/check_prep.py`) — all OK
- [x] Pilot annotation (5 sents/lang)
- [x] Trial annotation (15 sents/lang) — pipeline OK; see `TRIAL_RUN.md`
- [x] `normalize_lemma` NaN-safe (`src/metrics.py`)
- [x] Notebooks 01–04 scaffolds
- [x] `reports/ENV.txt` + pinned `requirements.txt`
- [x] Course slide markdown corpus in repo (`llm_corpus/`)
- [ ] Full annotation 300+300 (`python scripts/run_llm_annotate.py`)
- [ ] Loci analysis + report
- [ ] Submit proposal to Dellert (≤ 31 Aug)

## Commands

```bash
cd project
source .venv/bin/activate
export PATH="$HOME/.local/bin:$PATH"
open -a Ollama   # if needed
python scripts/check_prep.py
python scripts/run_llm_annotate.py          # full run (resumable)
python scripts/run_llm_annotate.py --limit 5  # pilot
```
