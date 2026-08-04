# Common Mistakes — Linguistic loci project

## Framing

- [ ] Do **not** pitch the project as “which model is better.”
- [ ] Do **not** lead the report with a single accuracy score as the main finding.
- [ ] Do **lead** with category-wise loci and DE vs EN profile differences.

## Conceptual

- [ ] Do **not** treat SpaCy as gold truth.
- [ ] Do **not** interpret Kafka’s plot instead of annotation loci.

## Alignment

- [ ] Do **not** let the LLM re-tokenize.
- [ ] Do **not** mix non-UPOS label schemes without mapping.

## Scope

- [ ] Do **not** add NER/deps without proposal amendment.
- [ ] Do **not** run many LLMs “to compare models” (forking paths + bake-off framing).

## Stats

- [ ] Do **not** pool DE+EN without separate profiles.
- [ ] Do **not** skip per-category tables/confusion.
- [ ] Do report bootstrap uncertainty for key rates.

## Repro

- [ ] Pin Ollama model id; T=0; seed 42; never edit `data/raw/`.
