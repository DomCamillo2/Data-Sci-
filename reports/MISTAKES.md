# Common Mistakes to Avoid — L1 Kafka SpaCy vs LLM

## Conceptual

- [ ] Do **not** claim SpaCy is gold truth / the LLM is “wrong” when they differ.
- [ ] Do **not** frame the project as proving LLMs replace NLP pipelines.
- [ ] Do **not** interpret Kafka’s plot instead of measuring agreement.

## Alignment / annotation

- [ ] Do **not** let the LLM re-tokenize (breaks comparison).
- [ ] Do **not** mix STTS / coarse tags / English glosses into UPOS without mapping.
- [ ] Do **not** silently drop tokens that fail to parse as JSON.

## Scope

- [ ] Do **not** add dependencies, NER, coreference without proposal amendment.
- [ ] Do **not** annotate the full novel via API unless explicitly amended + funded.
- [ ] Do **not** run five different LLMs “for fun” (forking paths).

## Stats / reporting

- [ ] Do **not** pool DE+EN into one accuracy without also reporting separate scores.
- [ ] Do **not** report only accuracy — include κ and error structure.
- [ ] Do **not** skip uncertainty (bootstrap over sentences).

## Reproducibility

- [ ] Do **not** leave model name as “ChatGPT” without version/ID.
- [ ] Do **not** use temperature &gt; 0 for the main run.
- [ ] Do **not** edit `data/raw/` texts.
