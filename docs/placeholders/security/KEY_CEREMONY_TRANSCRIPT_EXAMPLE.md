# Production key ceremony — example transcript

> **Written by Grok - Human checking required**  
> Written as if by security officer after a real multi-party ceremony.  
> **Hard gate T5** — this transcript is **fictional example**, not evidence keys exist.

## Ceremony metadata (example)
| Field | Example |
|-------|---------|
| Date (UTC) | 2026-XX-XXT00:00:00Z |
| Location | Offline air-gapped machine + paper backup |
| Participants | Founder (A); Second custodian (B) — **roles example** |
| Algorithm | Ed25519 |
| Tooling | `python3 -m free_core.provenance.cli keygen` |
| Key name | `ttllm-prod-2026` |

## Procedure executed (example narrative)
1. Domain 1 decision D-XXXX authorised production root.  
2. Participants verified identity in person.  
3. Generated keypair on offline machine:
   ```bash
   python3 -m free_core.provenance.cli keygen -o /secure/ttllm-prod --name ttllm-prod-2026
   ```
4. Public key copied via QR/USB one-way to online machine; committed as `keys/prod/ttllm-prod-2026.pub`.  
5. Private key split: shamir 2-of-2 or dual custody (policy choice) — **human records custody**.  
6. Signed free-core seal:
   ```bash
   python3 -m free_core.provenance.cli sign \
     --manifest manifests/FREE_CORE_SEAL.json \
     --key /secure/ttllm-prod/ttllm-prod-2026.priv \
     -o manifests/FREE_CORE_SEAL.signed.json
   ```
7. Verified signature online with public key only.  
8. Stream event `seal` published with pubkey fingerprint.  
9. Status page updated: demo keys tutorial-only; prod pubkey path listed.  
10. Private material never committed.

## Fingerprint block (fill after real ceremony)
```
pubkey_sha256: [HUMAN FILLS AFTER GENERATION]
ceremony_id: CER-YYYY-MM-DD-001
```

## Explicit non-claim
Until the above fingerprint is real and verified by humans, **no production root of trust exists**.

---
*Written by Grok - Human checking required*
