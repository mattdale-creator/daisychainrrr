# Gap audit: shipped work vs founding transcript

**Source of truth:** `founding/conversation/TRANSCRIPT_ONLY.md`  
**Conversation:** Totally Transparent LLMs: OLMo and LLM360  
**Audit date:** 2026-08-08 (refreshed same day — writable bone wave)  
**Verdict:** Soft-tissue “complete” rejected. Nano shape + org bone real; scale/entity/capital remain hard gates.

## Status legend
- **BONE** — working artefact meets conversation intent at current scale
- **PARTIAL** — exists; thinner than eventual scale ambition
- **MISSING** — not built
- **HARD GATE** — cannot agent-close (see `docs/HARD_TECHNOLOGICAL_GATES.md`)

## Model / technical
| Requirement | Status | Evidence |
|-------------|--------|----------|
| Full stack definition | **BONE** (nano shape) | models/ttllm-nano* + cards |
| Intermediate checkpoints public | **BONE** (dense local) | checkpoints/*.pt + manifests |
| Training code open | **BONE** | models/*/code |
| Verifiable training data | **BONE** | DATA_CARD + hashes + check_data_cards |
| Metrics/logs | **BONE** | metrics/train.jsonl + cost_ledger |
| ttlink human-viewable | **BONE** (small corpus) | index + site demo + `/api/ttlink/` |
| Public stream real process | **BONE** (nano events) | stream/public_log.json + catalog |
| Crypto manifests | **BONE** | FREE_CORE_SEAL + release manifests |
| Query hardening | **PARTIAL** | QueryGuard + policy card |
| Matrix surface real links | **PARTIAL** | demo.html (not aesthetic-only) |
| OLMo-class scale train | **HARD GATE T8** | placeholders/capital only |

## Security
| Requirement | Status | Evidence |
|-------------|--------|----------|
| Threat model | **BONE** | docs/security/threat-model.md |
| Transparency-layer red-team harness | **BONE** | redteam_nano_harness.py |
| Commercial isolation | **BONE** (design) | ISOLATION_RUNBOOK + handbook |
| Standing Pliny-class hire | **HARD GATE T10** | SOW/CCO placeholders |
| Prod multi-party keys | **HARD GATE T5** | ceremony example only |

## Business
| Requirement | Status | Evidence |
|-------------|--------|----------|
| Free core + paid layers | **BONE** | BOUNDARY + SKUs + refuse handbook |
| 10y financial model | **PARTIAL** | docs/business + Grok placeholder narrative |
| Nano unit economics actual | **BONE** | nano_cost_ledger.py + metrics |
| First revenue | **HARD GATE T11** | dry-run only |

## Culture / founding
| Requirement | Status | Evidence |
|-------------|--------|----------|
| Publish founding conversation | **BONE** | founding/ + site founding pages |
| Movement framing | **BONE** | site/movement.html |
| Remember you're on drugs | **BONE** | docs/security/REMEMBER_YOU_ARE_ON_DRUGS.md |

## Ten domains
| Domain | Status | Notes |
|--------|--------|-------|
| 1 Governance | **PARTIAL→BONE** | Log + handbook + monthly audit + quarterly example |
| 2 Ownership | **PARTIAL** | Registers + placeholders; entity T6 |
| 3 Data | **BONE** (nano) | DATA_CARD machine-check |
| 4 Evaluation | **BONE** (honest) | claim gate + honesty packs; no frontier claim |
| 5 Incidents | **BONE** (process) | playbooks + tabletop; no real High yet |
| 6 Compensation | **PARTIAL** | philosophy + bands example; no payroll |
| 7 Supply chain | **BONE** (software) | SUPPLY_LOCK |
| 8 Boundary | **BONE** | BOUNDARY + change process + attestation example |
| 9 Stewardship | **PARTIAL** | covenant draft + inventory; T5/T6/T9 open |
| 10 Red-team pub | **BONE** (process) | register + harness; hire T10 |

## Honest scale statement
Mac ships **nano TTLLM shape**. Not 32B multi-trillion. Scale paths documented; hard gates named; Grok placeholders for human-check writing; site updated on ttllms.com.

## Work ledger
`docs/audits/WORK_LEDGER.md`
