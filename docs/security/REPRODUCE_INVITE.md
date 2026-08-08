# Third-party reproduce invite

**Updated:** 2026-08-08  
**Contact:** md@0265.au  
**Ethos:** Others must be able to re-hash and verify without paying.

## What we publish (free core)
- Weights/checkpoints for public nanos (where trained)
- Training code + hyperparameters
- DATA_CARD with source URLs and hashes
- Merkle manifests + optional demo signatures
- Basic ttlink indexes for public corpora
- Public stream logs
- free_core verification tools

## What you can do offline (no account)
```bash
git clone https://github.com/mattdale-creator/daisychainrrr
cd daisychainrrr
python3 -m pip install -e ".[dev,crypto]"
python3 scripts/public_verify_harness.py
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
python3 scripts/redteam_nano_harness.py
```

## Recompute costs (honest)
| Artefact | Cost class |
|----------|------------|
| Re-hash free core seal | seconds–minutes on laptop |
| Re-verify nano stream/ttlink | seconds |
| Retrain nano from prepare_data | minutes–hours on M1/CPU |
| Retrain OLMo-class | **not published yet** — capital gate; multi-GPU/$ |

## Partner lab path
Email md@0265.au with: lab name, what you will re-run, intended public write-up. We will not require NDAs that silence integrity findings (Domain 10).

## Tombstone
No funded reproduce grants yet. This invite is process bone, not a grant program.
