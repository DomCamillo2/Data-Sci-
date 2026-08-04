# Plan — Linguistic loci of annotation disagreement (Kafka DE/EN)

**Team:** Dominik Soballa, Luca Bouché (joint work)  
**Framing:** Corpus / Language Use question — **not** a model bake-off  
**Tools:** SpaCy + local Ollama LLM as two automatic annotators  

## One-sentence topic

Where in the grammar do automatic annotators disagree on literary Kafka text, and does that profile differ between German and English?

## RQ & hypotheses

| ID | Content |
|----|---------|
| RQ | Which linguistic categories show the strongest automatic-annotation disagreement, and does the profile differ DE vs EN? |
| H1 | Disagreement uneven across UPOS (loci) |
| H2 | DE vs EN disagreement profiles differ |
| H3 | Overall agreement ≫ chance, ≪ ceiling (structured, not noise) |

## Non-goals

- “Which model is better?” as main claim  
- Human gold, deps/NER, fine-tuning  

## Methods (unchanged technically, reframed)

1. SpaCy tokenize + sample (done: `tokens_{de,en}_sample.csv`)  
2. LLM labels same tokens (Ollama `llama3.2:3b`, T=0)  
3. Analyse **per-category disagreement** first; overall scores second  
4. Bootstrap CIs; qualitative linguistic examples  
5. Notebook report emphasising loci + DE/EN  

## Reproducibility (Session 12)

Raw archive, documented transforms, seed 42, README, pinned requirements, model IDs.

## Deliverable

Jupyter narrative answering H1–H3 + GitHub for Dellert.

## Docs

- Proposal: `proposal/PROPOSAL_DRAFT.md`  
- Execution: `IMPLEMENTATION_PLAN.md`  
- Deep dive history: `reports/L1_DEEP_DIVE.md` (updated framing)
