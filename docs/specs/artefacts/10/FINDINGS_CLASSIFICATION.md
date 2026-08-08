# Red-team findings classification — Domain 10

| Class | Definition | Publication |
|-------|------------|-------------|
| **Critical** | Public skeleton integrity (manifest, stream chain, keys, index poison) | Register ASAP; coordinate Domain 5; detail per exemption rules |
| **High** | Significant exploit or process failure with public impact | Register entry ≤7 days of confirmation |
| **Medium** | Limited impact; reproducible but contained | May batch in periodic summary |
| **Low** | Noise / purely theoretical without practical path | Periodic summary |

## Default
**Publish.** Permanent suppression forbidden. Time-limited security exemption only (logged expiry).

## Surfaces in scope
Provenance · stream · ttlink/canary/QueryGuard · claim honesty · BOUNDARY isolation · org process (decision log gaps)

## Related
- Harness: `scripts/redteam_nano_harness.py`  
- Handbook: `docs/handbook/incident/02-redteam-publication.md`  
- SOW example: `docs/placeholders/security/REDTEAM_SOW_FILLED_EXAMPLE.md` (**Written by Grok - Human checking required**)
