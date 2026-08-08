# Seal & verify (human handbook)

**Updated:** 2026-08-08  
**Owner (R):** Provenance Owner (project lead until staffed)  
**Tools:** `python3 -m free_core.provenance.cli` (prog name: `ttllm-manifest`)

## Purpose
Anyone — insider or stranger — can re-hash and verify free-core claims. Seals are the product of proof, not marketing.

## What gets sealed

| Scope | Path | How |
|-------|------|-----|
| Free public core (repo) | `manifests/FREE_CORE_SEAL.json` | `seal-repo` / `build_public_artefacts.py` |
| Model release | `models/<name>/manifests/RELEASE_MANIFEST.json` | `seal_release.py` or `seal_model_tree` |
| Checkpoints (optional) | `models/<name>/manifests/CHECKPOINTS_MANIFEST.json` | pipeline with `include_ckpts` |
| Stream log | `*/stream/public_log.json` | hash-chained events |
| ttlink index | `*/ttlink/index.json` | content-addressed docs + canary |

## Commands — hash / build / verify

```bash
# SHA-256 file or tree
python3 -m free_core.provenance.cli hash path/to/file_or_dir

# Build Merkle manifest for a directory
python3 -m free_core.provenance.cli build path/to/dir -o path/to/MANIFEST.json

# Verify manifest against base directory (exit 0 = ok)
python3 -m free_core.provenance.cli verify \
  --manifest manifests/FREE_CORE_SEAL.json --base .

# Seal free public core of this repo
python3 -m free_core.provenance.cli seal-repo .

# Inclusion proof for a leaf
python3 -m free_core.provenance.cli proof \
  --manifest manifests/FREE_CORE_SEAL.json \
  --path README.md --check
```

## Commands — keys (demo only)

```bash
python3 -m free_core.provenance.cli keygen -o keys --name ttllm
python3 -m free_core.provenance.cli sign \
  --manifest manifests/FREE_CORE_SEAL.json \
  --key keys/ttllm.priv -o manifests/FREE_CORE_SEAL.signed.json
python3 -m free_core.provenance.cli verify-sig \
  --signed manifests/FREE_CORE_SEAL.signed.json \
  --pubkey keys/ttllm.pub --base .
```

**Tombstone:** Demo keys are **not** production roots of trust. Production requires multi-party / HSM design (Domain 9 + gate `04-entity-covenant`). Never commit private keys.

## Commands — stream + ttlink + canary

```bash
python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
python3 -m free_core.stream.cli append path/to/public_log.json   # if CLI supports; else use StreamLog in seal scripts

python3 -m free_core.ttlink.cli index path/to/corpus -o path/to/index.json
python3 -m free_core.ttlink.cli query "Alice" --index models/ttllm-nano/ttlink/index.json
python3 -m free_core.ttlink.cli stats --index models/ttllm-nano/ttlink/index.json
python3 -m free_core.ttlink.cli canary-check --index models/ttllm-nano/ttlink/index.json
```

## Full green path (daily / pre-release)

```bash
python3 -m pytest -q
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
python3 -m free_core.provenance.cli verify --manifest manifests/FREE_CORE_SEAL.json --base .
make demo   # if examples present
```

## When verify fails

1. Read JSON output: mismatched paths / hashes.
2. Do **not** force-edit the manifest to match bad files.
3. Either restore known-good files from git **or** re-seal intentionally after honest change.
4. If public claim already shipped with old root: Domain 5 incident if integrity story broke for outsiders.
5. Log decision if claim language must change.

## Staleness rule
Any commit that changes sealed paths must either:
- re-run seal + verify before claiming green, or
- tombstone “seal stale until reseal” on status page.

## RACI
Provenance Owner R; Release Owner C; public I via published roots.

## Done when
- [ ] Verify exits 0 for claimed manifests
- [ ] Stream chain verifies
- [ ] Canary present where claimed
- [ ] No private keys in git
