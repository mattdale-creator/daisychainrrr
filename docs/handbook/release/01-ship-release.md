# Release — full ship path (nano → public claim)

**Updated:** 2026-08-08  
**Owner (R):** Release Owner (project lead until staffed)  
**Accountable (A):** project lead  
**Related:** [02-seal-and-verify](02-seal-and-verify.md) · [03-train-nano](03-train-nano.md) · [05-scorecard-tombstones](05-scorecard-tombstones.md)

## Purpose
Ship a **public free-core claim** only when artefacts, seals, evals, and honest tombstones are complete. Nano releases prove the *shape* of transparency — not frontier capability.

## Preconditions
- [ ] Working tree on intended commit (no secrets in files to be sealed)
- [ ] `ops/secrets.local.env` not staged/committed
- [ ] Domain 1 decision if this release changes BOUNDARY, claim language, or public training policy
- [ ] Data path legal (Domain 3): DATA_CARD / public-domain sources for nano

## Procedure — ship a nano-class release

### 1. Train (or reuse sealed model tree)
```bash
# From repo root
make nano-data
make nano-train          # or: python3 models/ttllm-nano/code/train.py --steps 800
```
For v2/v3/v4, use the matching `models/ttllm-nano-vN/` tree and Makefile targets where present.

### 2. Seal the model tree
```bash
make nano-seal
# equivalent:
python3 models/ttllm-nano/code/seal_release.py
```
Expect under `models/ttllm-nano/`:
- `manifests/RELEASE_MANIFEST.json` (+ optional checkpoints manifest)
- `ttlink/index.json`, `binding.json`, shards
- `stream/public_log.json`
- eval pack / scorecard artefacts under `evals/` or `cards/`

### 3. Verify model + free core
```bash
python3 -m free_core.provenance.cli verify \
  --manifest models/ttllm-nano/manifests/RELEASE_MANIFEST.json \
  --base models/ttllm-nano

python3 -m free_core.stream.cli verify models/ttllm-nano/stream/public_log.json
python3 -m free_core.ttlink.cli stats --index models/ttllm-nano/ttlink/index.json
python3 scripts/redteam_nano_harness.py
python3 -m pytest -q
```

### 4. Re-seal free public core (repo-wide)
Any change to `free_core/`, `docs/`, `registers/`, `commercial/`, `site/`, etc. invalidates `manifests/FREE_CORE_SEAL.json`.

```bash
python3 -m free_core.provenance.cli seal-repo .
# or rebuild via:
python3 scripts/build_public_artefacts.py

python3 -m free_core.provenance.cli verify \
  --manifest manifests/FREE_CORE_SEAL.json --base .
```
Optional sign (demo keys only — not production root of trust):
```bash
# keys/ must exist and must NOT be committed if private
python3 -m free_core.provenance.cli sign \
  --manifest manifests/FREE_CORE_SEAL.json \
  --key keys/ttllm.priv \
  -o manifests/FREE_CORE_SEAL.signed.json
python3 -m free_core.provenance.cli verify-sig \
  --signed manifests/FREE_CORE_SEAL.signed.json \
  --pubkey keys/ttllm.pub \
  --base .
```

### 5. Scorecard + tombstones
```bash
python3 scripts/domain_scorecard_all.py
```
Write/update release scorecard (see [05-scorecard-tombstones](05-scorecard-tombstones.md)).  
**Must include:** nano ≠ frontier; any missing domain as PARTIAL/TOMBSTONE with reason.

### 6. Public surface
- Update `STATUS_HONEST.md` if claim level changed
- Site pages: `site/nano.html`, `site/status.html`, `site/models.html` as needed
- Stream: ensure public log event includes `release` + merkle root
- Tag only after verify green:
```bash
git status   # no secrets
git add -A   # review carefully
git commit -m "release: ttllm-nano claim sealed + verified"
git tag -a vX.Y.Z -m "release claim summary"
# push only when remote policy allows
```

### 7. Deploy site (Pages)
Human/CI deploys `site/` to Cloudflare Pages project **ttllms**. Confirm:
- https://ttllms.pages.dev/status
- https://ttllms.com/status (if DNS active)

## Forbidden claims
| Claim | Allowed only if… |
|-------|------------------|
| "OLMo-scale open" | Full data mix + scale training published — **not** nano |
| "Production multi-TB ttlink" | Real shards + infra — **not** demo index |
| "Company complete" | Entity + capital gates closed — **never** from agent alone |
| Green verify while harness fails | Never |

## RACI
| Role | R | A | C | I |
|------|---|---|---|---|
| Release Owner | ✓ | | ✓ | |
| Project lead | | ✓ | | |
| Domain 8 Boundary | | | ✓ | |
| Public (via seals/stream) | | | | ✓ |

## Done when
- [ ] Model tree sealed and verify ok
- [ ] FREE_CORE_SEAL verify ok
- [ ] Red-team harness `all_pass: true`
- [ ] Scorecard has honest tombstones
- [ ] STATUS_HONEST reflects reality
- [ ] No secrets in commit

## Related failure catalog
`docs/architecture-tree/eventualities/` — refine after real drills, not before.
