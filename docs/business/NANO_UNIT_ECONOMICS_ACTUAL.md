# Nano unit economics — actual (not scale cosplay)

**Updated:** 2026-08-08  
**Generator:** `python3 scripts/nano_cost_ledger.py --write`

## Purpose
Founding turn 13 demanded math/physics/code. Nano trains on a Mac produce **real** wall-clock and storage numbers. Those numbers must not be inflated into “we trained at OLMo cost.”

## How to refresh
```bash
python3 scripts/nano_cost_ledger.py --write
```
Per-model ledgers: `models/ttllm-nano*/metrics/cost_ledger.md`

## Interpretation
| Quantity | Meaning |
|----------|---------|
| Wall seconds | Real train time on device (often MPS) |
| Est. kWh | Order-of-magnitude laptop power model |
| Checkpoint bytes | Dense intermediate storage honesty |
| $0 cloud GPU | Local demo — scale still capital gate T8 |

## Scale cross-link
Illustrative multi-hundred-k to ~$1M first-epoch sketches live in  
`docs/placeholders/capital/SCALE_BUDGET_FILLED_EXAMPLE.md`  
(**Written by Grok - Human checking required**). Not invoices.

## Ethos
Publish the cheap truth. Soft tissue is claiming frontier economics from nano wall_sec.
