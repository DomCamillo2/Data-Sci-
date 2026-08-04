# Grade Rubric — L1 SpaCy vs LLM (Session 12 mapping)

| Area | Weak | Adequate | Strong (1,0 path) |
|------|------|----------|-------------------|
| RQ | “Test ChatGPT on Kafka” | Mentions POS | Agreement + DE/EN + categories |
| Framing | SpaCy = truth | Vague “reference” | Explicit reference≠gold |
| Design | Free LLM tokenize | Partial align | Fixed SpaCy tokens → JSON labels |
| Hypotheses | None | H1 only | H1–H3 pre-registered |
| Metrics | Screenshots | Accuracy only | Acc + κ + confusion + bootstrap |
| Languages | EN only | Pooled DE+EN | Separate DE/EN tables |
| Repro | Unpinned API | requirements only | Model IDs, T=0, seed, prompt in repo |
| Limitations | Missing | Generic | Domain, dual error, scheme mapping |
| Proposal fidelity | Extra tasks surprise | Minor drift | Matches proposal / logged amend |

## Instructor signals

- Replication / careful evaluation valued over novelty theatre.  
- Stick to proposal.  
- Reproducibility checklist = free points.
