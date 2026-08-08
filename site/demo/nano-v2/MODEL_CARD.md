# Model card — ttllm-nano-v2

**Version:** 0.2.0-nano-bpe  
**Intent:** Improve nano transparency shape with BPE tokenizer + denser model, same verifiable PG data.

## Architecture
n_layer=6, n_head=4, n_embd=192, params=3099648

## Tokenizer
Pure-Python BPE over UTF-8 bytes (`data/processed/bpe.json`).

## Data
Same Project Gutenberg public-domain mixture as ttllm-nano v1 — see `data/DATA_CARD.md`.

## Reproduce
```bash
python3 models/ttllm-nano-v2/code/prepare_bpe.py
python3 models/ttllm-nano-v2/code/train.py --steps 1500
python3 models/ttllm-nano-v2/code/eval_pack.py
python3 models/ttllm-nano-v2/code/seal_release.py
```

## Not a frontier model
Tombstone: not OLMo-scale. Process skeleton is the product.
