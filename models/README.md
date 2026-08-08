# Models

## ttllm-nano (0.1.0-nano)
Character-level GPT on Project Gutenberg train slices. Dense checkpoints, metrics, seals, ttlink, stream.

## ttllm-nano-v2 (0.2.0-nano-bpe)
Same verifiable data + **pure-Python BPE** tokenizer, denser model, val perplexity in metrics, process eval pack.

| Artefact | v1 | v2 |
|----------|----|----|
| Code | `ttllm-nano/code/` | `ttllm-nano-v2/code/` |
| Tokenizer | char meta.json | `bpe.json` + `tokens.bin` |
| Checkpoints | `ttllm-nano/checkpoints/` | `ttllm-nano-v2/checkpoints/` |
| Eval | basic | `eval_pack.py` (ppl + BPE roundtrip + ttlink) |

**Neither is frontier-scale.** Tombstones required on all public claims.
