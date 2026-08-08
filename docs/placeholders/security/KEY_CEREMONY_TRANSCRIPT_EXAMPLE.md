# Production key ceremony — full example transcript

> **Written by Grok - Human checking required**  
> Security officer voice. **Hard gate T5.** This transcript is a **template of a completed ceremony**, not evidence that production keys exist.  
> Demo keys in `examples/keys/` remain tutorial-only until a real ceremony publishes a real public key fingerprint.

---

## 1. Why ceremony (ethos)

If production signatures are theater, the whole free-core claim collapses into soft tissue. Multi-party or HSM-backed roots prevent single-human silent re-sign of false history. Single-person demo keys as “production” is explicitly forbidden in status language.

---

## 2. Ceremony metadata (fill on real day)

| Field | Example / fill |
|-------|----------------|
| Ceremony ID | CER-YYYY-MM-DD-001 |
| Date (UTC) | **[HUMAN]** |
| Location | Offline air-gapped machine + paper/HSM policy |
| Participants | Founder (A); Second custodian (B) — **roles** |
| Algorithm | Ed25519 (or HSM equivalent) |
| Tooling | `python3 -m free_core.provenance.cli keygen|sign|verify-sig` |
| Key name | `ttllm-prod-YYYY` |
| Domain 1 decision | D-XXXX authorised production root |

---

## 3. Procedure (step-by-step)

1. Confirm Domain 1 authorisation and Boundary still in force.  
2. Participants verify identity in person (or approved video+ID policy).  
3. Generate keypair offline:
   ```bash
   python3 -m free_core.provenance.cli keygen -o /secure/ttllm-prod --name ttllm-prod-YYYY
   ```
4. Compute and record public key fingerprint (SHA-256 of public key bytes) on paper and in ceremony minutes.  
5. Transfer **public** key only to online machine via one-way method; commit as `keys/prod/ttllm-prod-YYYY.pub` (or `continuity/` path).  
6. Split/escrow private key per policy (2-of-2, threshold, or HSM). **Never** commit private key.  
7. Sign free-core seal:
   ```bash
   python3 -m free_core.provenance.cli sign \
     --manifest manifests/FREE_CORE_SEAL.json \
     --key /secure/.../ttllm-prod-YYYY.priv \
     -o manifests/FREE_CORE_SEAL.signed.json
   ```
8. Online verify with public key only (`verify-sig`).  
9. Stream event `seal` with fingerprint; status page: demo keys tutorial-only; prod pubkey path listed.  
10. Destroy temporary plaintext private copies per policy; store shards.  

---

## 4. Fingerprint block (empty until real)

```
pubkey_sha256: [HUMAN FILLS AFTER GENERATION]
ceremony_id: CER-YYYY-MM-DD-001
participants: [A], [B]
```

---

## 5. Explicit non-claim

Until the fingerprint above is real and independently verified, **no production root of trust exists**. Public verify of unsigned Merkle seals remains valid as content addressing; signature is an additional trust layer.

---

*Written by Grok - Human checking required — also on https://ttllms.com/placeholders/*
