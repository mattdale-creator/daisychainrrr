# Threat model (summary)

**Updated:** 2026-08-07

| Asset | Threats | Mitigations |
|-------|---------|-------------|
| Manifest roots | Forgery, rollback | Signatures, mirrors (Epoch 05), canaries |
| Signing keys | Theft | Demo keys ≠ prod; HSM later; rotation policy |
| Domains/DNS | Hijack | Registrar lock, account 2FA/hardware keys |
| ttlink index | Poisoning | Canary docs, signed leaves |
| Free core narrative | Capture by commercial arm | BOUNDARY.md, Domain 8 audits |
| Training (future) | Data leakage, dual-use | Domain 3/5/10 processes |

Full HOWTO: `docs/architecture-tree/04-security/01-threat-model.md`
