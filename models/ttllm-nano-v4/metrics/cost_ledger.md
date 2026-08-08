# Cost ledger — ttllm-nano-v4

**Generated:** 2026-08-08T13:35:36Z

| Item | Value |
|------|-------|
| Device | mps |
| Steps | 400 |
| Wall seconds | 89.8 |
| Est. energy @20W | 0.0005 kWh |
| Checkpoint storage bytes | 48,680,600 |
| Data tree bytes | 4,324,032 |
| Code tree bytes | 19,304 |
| Cloud GPU invoice | $0 (local) |
| Data license cost | $0 (public domain PG where used) |

## Honesty
This ledger is the actual cost of the nano demonstration.
It does **not** validate multi-million-dollar scale training quotes.
Scale budgets: `docs/placeholders/capital/SCALE_BUDGET_FILLED_EXAMPLE.md` (Grok example).

## Hyperparams tip
```json
{
  "steps": 400,
  "n_layer": 4,
  "n_embd": 128,
  "seed": 42,
  "device": "mps",
  "corpus_sha256": "b26077bd9f598f145ded5693c2ad5ce02e61695a9644555cb8361194ffc5c5b0"
}
```

