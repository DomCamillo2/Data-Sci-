# Trial run results

> Part of the lab log — full history of runs/changes: [`CHANGELOG_RUNS.md`](CHANGELOG_RUNS.md)

**Setup:** 15 sentences / language · `llama3.2:3b` · temperature 0 · 2026-08-04  
**Verdict: pipeline is implementable end-to-end.**

## DE
- sentences: 15 (parse_ok 14 = 93%), tokens: 496
- UPOS agreement: **64.3%**, lemma: 51.4%
- bootstrap: 64.3% CI95=[61.7%, 66.5%]
- top loci:
  - `CCONJ`: 100.0%
  - `PART`: 100.0%
  - `SCONJ`: 100.0%
  - `AUX`: 88.0%
  - `ADV`: 71.4%

## EN
- sentences: 15 (parse_ok 15 = 100%), tokens: 315
- UPOS agreement: **68.9%**, lemma: 82.2%
- bootstrap: 68.7% CI95=[64.7%, 72.3%]
- top loci:
  - `PART`: 100.0%
  - `SCONJ`: 100.0%
  - `AUX`: 87.0%
  - `CCONJ`: 71.4%
  - `ADV`: 63.2%

## Notes

- DE: 1/15 sentence failed JSON parse (`sent_65`) — resumable cache handles retries.
- Small trial; full 300+300 will stabilize loci.
- Next: `python scripts/run_llm_annotate.py`
