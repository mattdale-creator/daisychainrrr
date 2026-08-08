# Production key ceremony runbook (draft)

## Principles
1. Demo keys in `examples/keys/` are **not** production.
2. Production requires multi-party or HSM policy after entity exists.
3. Only **public** keys are committed; private material offline / HSM.

## Ceremony outline (when wall 6 opens)
1. Domain 1 decision: key policy + participants.
2. Generate Ed25519 (or HSM-backed) keypair offline:
   ```bash
   python3 -m free_core.provenance.cli keygen -o /secure/path --name ttllm-prod
   ```
3. Split / escrow private key per policy (threshold or HSM).
4. Publish `ttllm-prod.pub` under `keys/prod/` or `continuity/`.
5. Sign `manifests/FREE_CORE_SEAL.json` → `FREE_CORE_SEAL.signed.json`.
6. Public stream event `seal` with pubkey fingerprint.
7. Mark demo keys as tutorial-only on status page.
8. Document recovery in ASSET_INVENTORY.

## Verify
```bash
python3 -m free_core.provenance.cli verify-sig \
  --signed manifests/FREE_CORE_SEAL.signed.json \
  --pubkey keys/prod/ttllm-prod.pub --base .
```
