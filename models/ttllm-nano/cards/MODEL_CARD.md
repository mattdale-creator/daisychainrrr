# Model card — ttllm-nano

## Intent
Mac-local **minimal TTLLM** that demonstrates the transparency *shape* required by the founding conversation: public data, code, dense checkpoints, metrics, sealed manifests, ttlink, stream.

## Architecture
Character-level GPT: n_layer=4, n_head=4, n_embd=128, block_size=128

## Training
See `metrics/hyperparams.json` and `metrics/train.jsonl`.

## Data
See `data/DATA_CARD.md`. Project Gutenberg public domain.

## How to sample
```bash
python3 models/ttllm-nano/code/generate.py --prompt "Alice " --tokens 200
```

## What this is not
A competitor to OLMo-scale systems. It is the bone of the process at nano scale.
