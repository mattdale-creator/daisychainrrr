# Scale training budget — filled example (illustrative USD)

> **Written by Grok - Human checking required**  
> Written as if by training lead planning first serious public run.  
> Numbers are **illustrative order-of-magnitude**, not quotes.

## Target (example)
| Field | Example |
|-------|---------|
| Class | Dense public LM, transparency-first (OLMo-class ambition, not claim of parity) |
| Params | e.g. 7B class first milestone |
| Public checkpoints | Every N steps (Domain 1 freeze before train) |
| Data | Mixture manifest `ttllm.data_mixture.v1` published |

## Budget sketch (example)
| Line | Low | High | Notes |
|------|-----|------|-------|
| GPU hours | $80k | $400k | Cluster choice |
| Storage + egress | $5k | $40k | R2/public downloads |
| Data licensing / curation | $10k | $100k | Domain 3 |
| Eng labor (6 mo) | $150k | $400k | |
| Red team standing | $40k | $120k | |
| Legal / entity | $15k | $50k | |
| **Total** | **~$300k** | **~$1.1M** | First serious epoch |

## Non-claims
Does not authorise spend. Nano laptop train is not a line item substitute for this table.

---
*Written by Grok - Human checking required*
