# Gap audit: shipped work vs founding transcript

**Source of truth:** `founding/conversation/TRANSCRIPT_ONLY.md`  
**Conversation:** Totally Transparent LLMs: OLMo and LLM360 (`8a75e0b4-…`)  
**Audit date:** 2026-08-08  
**Verdict:** Prior “complete” claims were soft tissue. This document lists bone still missing or partial.

## Status legend
- **BONE** — working artefact meets conversation intent at current scale
- **PARTIAL** — exists but thin vs transcript
- **MISSING** — not built
- **MINIMAL-LOCAL** — Mac-scale substitute for capital-bound full system (honest scale)

## Model / technical (turns 1, 4, 9–13, 16)

| Requirement | Prior | Target now |
|-------------|-------|------------|
| Full stack definition (data+code+ckpts+metrics+trace) | PARTIAL docs | BONE via nano release + card |
| Intermediate checkpoints public | MISSING | MINIMAL-LOCAL dense ckpts |
| Training code open | MISSING | BONE `models/ttllm-nano/code/` |
| Verifiable training data | MISSING (demo corpus only) | BONE hashed public-domain corpus |
| Metrics/logs | MISSING | BONE metrics JSONL |
| ttlink human-viewable | PARTIAL toy index | BONE index over real train corpus + shard seals |
| Public stream of real process | PARTIAL demo events | BONE stream of train/seal events |
| Crypto manifests + signatures | PARTIAL | BONE + shard proofs + signed releases |
| Query hardening | MISSING | PARTIAL QueryGuard + tests |
| Index shard integrity | MISSING | PARTIAL sharded index binding |
| Matrix surface over real links | MISSING aesthetic | PARTIAL site demo (links real) |

## Security (turns 14–17)

| Requirement | Prior | Target now |
|-------------|-------|------------|
| Threat model published | PARTIAL | Expand + train-specific |
| Frontier red-team of transparency layer | MISSING | MINIMAL-LOCAL automated adversarial harness |
| Commercial isolation design | PARTIAL prose | BONE isolation checklist + config stubs |
| Red-team findings publication | PARTIAL thin | Full Domain 10 artefacts + empty register ready |

## Business (turns 12, 18–23)

| Requirement | Prior | Target now |
|-------------|-------|------------|
| Free core + paid layers | PARTIAL | Deep BOUNDARY + SKU eventualities |
| 10y financial model | PARTIAL summary | Full tables + assumption ledger + scenarios |
| Scholarly / sales / MBA plan | PARTIAL | Expand to conversation depth |
| Unit economics math/physics | PARTIAL | Nano actual cost ledger + scale-up model |

## Culture / founding (turns 2–8, 24–29)

| Requirement | Prior | Target now |
|-------------|-------|------------|
| Publish founding conversation | PARTIAL in repo | Site page + sealed pack |
| Movement framing (not vs-person identity) | PARTIAL | Full pages |
| Remember you're on drugs | PARTIAL | Wired into eval/redteam checklists |

## Ten domains (turns 30–46)

| Domain | Transcript depth | Prior ship | Target |
|--------|------------------|------------|--------|
| 1 Governance | Full plan | ~12–60 lines | Full plan + Decision Log infra + charter |
| 2 Ownership/funding | Full plan | thin | Full plan + ownership artefacts |
| 3 Data governance | Full plan | thin | Full plan + legal log + data cards |
| 4 Evaluation | Full plan | thin | Full plan + nano eval archive |
| 5 Incidents | Full plan | thin | Full plan + incident log |
| 6 Compensation | Full plan | thin | Full plan + bands philosophy |
| 7 Supply chain | Full plan | thin | Full plan + dependency register |
| 8 Boundary | Full plan | BOUNDARY.md partial | Full plan + attestation |
| 9 Stewardship | Full plan | draft covenant | Full plan + inventory ops |
| 10 Red-team publication | Full plan | thin | Full plan + register |

## Honest scale statement
This Mac can ship a **nano TTLLM** that satisfies the *shape* of total transparency (data, code, dense checkpoints, metrics, sealed manifests, ttlink, stream, evals). It cannot ship 32B multi-trillion training. Scale-up paths are documented; nano is not cosplay of 32B.

## Work ledger
See `docs/audits/WORK_LEDGER.md` (updated as work proceeds).
