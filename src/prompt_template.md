# Prompt template (draft)

System/user prompt used for main runs — freeze after pilot; store exact string + date in the notebook.

```
You are a linguistic annotator. You receive a JSON list of tokens in order.
Return a JSON list of the same length. Each item must be an object:
  {"tok_id": <int>, "upos": <UD UPOS tag>, "lemma": <string>}
Use only these UPOS tags:
ADJ ADP ADV AUX CCONJ DET INTJ NOUN NUM PART PRON PROPN PUNCT SCONJ SYM VERB X
Do not add, remove, or split tokens. Temperature must be treated as 0 (deterministic).
Tokens:
<TOKEN_LIST_JSON>
```
