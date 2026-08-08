# Total Transparency Specification — Master

**Status:** Normative  
**Source:** Founding conversation turns 30–46  

## Scope

Together with the free public core (weights, data, checkpoints, code, ttlink, cryptographic provenance, public stream) and the commercial boundary rules, these ten domains complete the map of total transparency for both the model stack and the organisation that produces it.

## Domains

| # | Domain | Spec | Artefacts dir | Register |
|---|--------|------|---------------|----------|
| 1 | Governance and Decision-Making | [01-governance.md](01-governance.md) | artefacts/01-governance/ | registers/decisions/ |
| 2 | Ownership, Funding, and Influence | [02-ownership-funding.md](02-ownership-funding.md) | artefacts/02-ownership/ | registers/ownership/ |
| 3 | Data Governance and Legal Response | [03-data-governance.md](03-data-governance.md) | artefacts/03-data/ | registers/legal/ |
| 4 | Evaluation and Benchmarking | [04-evaluation.md](04-evaluation.md) | artefacts/04-evaluation/ | models/*/evals/ |
| 5 | Incident, Failure, and Red-Team Disclosure | [05-incident-disclosure.md](05-incident-disclosure.md) | artefacts/05-incidents/ | registers/incidents/ |
| 6 | Internal Incentives and Compensation | [06-compensation.md](06-compensation.md) | artefacts/06-compensation/ | — |
| 7 | Supply-Chain and Dependency Transparency | [07-supply-chain.md](07-supply-chain.md) | artefacts/07-supply-chain/ | registers/supply-chain/ |
| 8 | Boundary Rules (Public Core ↔ Commercial) | [08-boundary-rules.md](08-boundary-rules.md) | ../commercial/ | — |
| 9 | Stewardship and Continuity | [09-stewardship.md](09-stewardship.md) | ../continuity/ | — |
| 10 | Red-Team Findings Publication | [10-red-team-publication.md](10-red-team-publication.md) | artefacts/10-redteam/ | registers/redteam/ |

## Release scorecard rule

Every public model release (including nano) must ship a `TRANSPARENCY_SCORECARD.md` with met / partial / tombstone per domain.

## Nested eventualities

Deep failure-mode and process trees: `docs/architecture-tree/eventualities/`.

## Non-negotiable

No commercial feature may require the public core to become opaque.
