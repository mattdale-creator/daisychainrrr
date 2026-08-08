# Inclusion proof (human recipe)

**Updated:** 2026-08-08  
**Purpose:** Prove a specific public file is inside `FREE_CORE_SEAL` without trusting a webpage alone.

## Preconditions
- Clone of the public repo (or vault copy)
- Python 3.10+ with free_core importable (`pip install -e .` or `PYTHONPATH=.`)

## Recipe

```bash
# From repo root
python3 -m free_core.provenance.cli verify \
  --manifest manifests/FREE_CORE_SEAL.json --base .
# must exit 0

# Prove README.md is in the seal
python3 -m free_core.provenance.cli proof \
  --manifest manifests/FREE_CORE_SEAL.json \
  --path README.md --check
```

Expected shape (fields may vary slightly):
```json
{
  "leaf_hash": "<64 hex>",
  "proof": [ ... ],
  "path": "README.md"
}
{
  "verified": true,
  "expected_root": "<merkle_root from FREE_CORE_SEAL>"
}
```

## Any other sealed path
```bash
python3 -m free_core.provenance.cli proof \
  --manifest manifests/FREE_CORE_SEAL.json \
  --path commercial/BOUNDARY.md --check
```

List leaves:
```bash
python3 -c "import json; m=json.load(open('manifests/FREE_CORE_SEAL.json')); print('\\n'.join(sorted(x['path'] for x in m['leaves'])[:30]))"
```

## Model release proof
```bash
python3 -m free_core.provenance.cli verify \
  --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json \
  --base models/ttllm-nano
python3 -m free_core.provenance.cli proof \
  --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json \
  --path data/DATA_CARD.md --check
```

## Harness (automated)
```bash
python3 scripts/public_verify_harness.py
```

## Failure
- `verified: false` → do not trust the claim; Domain 5 if public green was asserted.
- Path not in manifest → file not part of that seal (maybe different seal scope).

## Related
- `docs/handbook/release/02-seal-and-verify.md`
- `free_core/provenance/proof.py`
