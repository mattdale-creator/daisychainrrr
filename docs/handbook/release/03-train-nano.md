# Train nano (local Mac / laptop)

**Updated:** 2026-08-08  
**Owner (R):** Training Owner (project lead until staffed)  
**Honesty:** nano ≠ frontier. Output is a **transparency shape**, not an OLMo competitor.

## Purpose
Reproduce end-to-end: public-domain data → dense checkpoints → metrics → seal → ttlink → stream.

## Environment
- Python 3.10+ recommended
- PyTorch with **MPS** on Apple Silicon (falls back to CPU)
- From repo root after `python3 -m pip install -e ".[dev,crypto]"` (or project deps)

## Procedure — ttllm-nano (v1)

```bash
# 1. Data: Project Gutenberg public-domain slices + DATA_CARD hashes
python3 models/ttllm-nano/code/prepare_data.py
# or: make nano-data

# 2. Train (default ~800 steps, dense ckpts every 100)
python3 models/ttllm-nano/code/train.py --steps 800
# options: --batch-size 32 --block-size 128 --n-layer 4 --n-head 4 --n-embd 128
#          --lr 3e-4 --ckpt-every 100 --eval-every 50 --seed 42
# or: make nano-train

# 3. Optional smoke generation
python3 models/ttllm-nano/code/generate.py --prompt "Alice " --tokens 80

# 4. Seal
python3 models/ttllm-nano/code/seal_release.py
# or: make nano-seal

# 5. Verify
python3 -m free_core.provenance.cli verify \
  --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json \
  --base models/ttllm-nano
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
```

One-shot: `make nano-all` (data + train + seal + generate).

## Artefacts produced
| Path | Content |
|------|---------|
| `data/raw/*.trainslice.txt` | Source slices + provenance via prepare_data |
| `data/processed/corpus.txt`, `meta.json` | Char-level train corpus |
| `data/DATA_CARD.md` | Licenses / URLs / hashes |
| `checkpoints/*.pt` | Dense intermediates |
| `metrics/train.jsonl`, `hyperparams.json` | Loss curve + hyperparams |
| `manifests/RELEASE_MANIFEST.json` | Merkle seal |
| `ttlink/index.json` | Queryable public corpus index |
| `stream/public_log.json` | Process events |

## Variants (v2–v4)
Use matching trees under `models/ttllm-nano-v2` … `v4`. Example v2:
```bash
make nano-v2-data
make nano-v2-train
make nano-v2-seal
```
Prefer `free_core.release.pipeline.seal_model_tree` for consistent reseal:
```bash
make reseal-nanos
```

## Domain 3 checklist (every train)
- [ ] Sources public-domain or licensed for redistribution
- [ ] DATA_CARD lists URL, license, hash
- [ ] No private/customer data in public train mix
- [ ] Capability claims match eval pack (tombstone if not competitive)

## Failure modes
| Symptom | Action |
|---------|--------|
| MPS OOM / hang | Lower batch/block size; or CPU |
| prepare_data network fail | Retry; document offline cache path if used |
| Seal without train metrics | Incomplete stream; re-run train or tombstone metrics |
| Claiming "trained at scale" | **Forbidden** — use [04-train-scaleup](04-train-scaleup.md) only with capital |

## RACI
Training Owner R; Domain 3 C for data; Release Owner C for ship.

## Done when
- [ ] Checkpoints + metrics on disk
- [ ] Seal verify green
- [ ] Tombstone language present on scorecard if capability not claimed
