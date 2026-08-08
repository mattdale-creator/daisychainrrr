# Checkpoint publication policy (pre-scale + nano)

**Updated:** 2026-08-08  
**Domain:** 4 Evaluation · 7 Supply · release handbook

## Nano (current)
| Rule | Value |
|------|--------|
| Interval | Dense: every `--ckpt-every` steps (default 100) |
| Format | `.pt` under `models/*/checkpoints/` |
| Seal | Included in release/checkpoint manifests when present |
| Cost | Local Mac — publish all dense ckpts |

## Scale (when capital exists) — decide before train
Use this template in a Domain 1 decision:

| Field | Decision |
|-------|----------|
| Target model | |
| Public checkpoint interval | e.g. every N steps or every $X compute |
| Cold storage SLA | days online / archive tier |
| Verify cost note | approximate third-party re-hash cost |
| Exclusions | what is NOT published and why (must not hide free-core bone) |

## Non-negotiable
- At least one public final weight set for any TTLLM-marketed model
- Intermediate density may be cost-limited but **interval must be public before train**
- No silent deletion of already-published checkpoints (Domain 3 process)

## Related
- `docs/handbook/release/04-train-scaleup.md`
- `docs/handbook/release/03-train-nano.md`
