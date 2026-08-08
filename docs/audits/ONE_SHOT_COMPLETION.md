# One-shot completion report

**Generated:** 2026-08-08T09:57:28Z  
**Ethos:** down to the bone — free public core never paywalled

## What this Mac completed

### Software free core
- free_core package: provenance (Merkle, proofs, sign), ttlink, stream log, QueryGuard, shards, canary, scorecard, release pipeline, local HTTP server, CLI tools
- Tests: pytest suite + redteam harness
- FREE_CORE_SEAL merkelizes public tree

### Models (nano shape of TTLLM — NOT frontier scale)
| Release | Data | Notes |
|---------|------|-------|
| ttllm-nano | PG PD | char LM dense ckpts |
| ttllm-nano-v2 | PG + BPE | denser, ppl metrics |
| ttllm-nano-v3 | 6 PG sources | canary ttlink |
| ttllm-nano-v4 | 6 PG sources | iteration train |

Each: public code, data cards+hashes, checkpoints, metrics, stream, ttlink, scorecard, Merkle seals.

### Transparency domains 1–10
- Full founding conversation plans in docs/specs/
- Operational artefact packs under docs/specs/artefacts/
- Registers live under registers/
- Master domain scorecard published

### Architecture / eventualities
- HOWTO tree + massive eventuality matrices under docs/architecture-tree/eventualities/

### Site
- https://ttllms.com multipage: definition, free-core, demo, nano, models, transparency, founding, founding-prompts, stream, contact, architecture

### Commercial
- BOUNDARY.md, isolation runbook, 6 SKU one-pagers (designed, not sold)

## Explicitly NOT complete (human/capital gates)
Documented in ops/HUMAN_GATES.md:
1. Cloudflare Zone DNS Edit (ttllms.org CNAME)
2. R2 dashboard enable
3. Workers routes / workers.dev subdomain token scope
4. Legal entity + signed continuity covenant
5. Capital for 32B-class training
6. Standing Pliny-class red team hire
7. Production HSM multi-party keys
8. Live revenue / enterprise customers

## Tombstones (required honesty)
- Nano models are not OLMo/32B multi-trillion releases
- Production FM-index / infini-gram at corpus scale not shipped
- Pages Function API routing may still need CF project config; client-side demo + local server + worker source are bone

## Ethos statement
We do not claim company-complete or model-complete. We claim **everything this Mac and available credentials can ship is public, sealed, and not soft tissue.**
