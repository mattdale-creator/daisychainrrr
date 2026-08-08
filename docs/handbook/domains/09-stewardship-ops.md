# Domain 9 — Stewardship & continuity (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead / Stewardship Custodian when staffed  
**Normative:** `docs/specs/09-stewardship.md`  
**Covenant (draft):** `continuity/COVENANT.md`  
**Inventory:** `continuity/ASSET_INVENTORY.md`  
**Triggers:** `docs/specs/artefacts/09/CHANGE_OF_CONTROL_TRIGGERS.md`

## Purpose
Public core must survive founder absence, acquisition pressure, or account loss.

## Current honest state
- Covenant is **DRAFT unsigned** (pre-entity) — tombstone, not failure to disclose.
- Asset inventory lists domains, GitHub, Pages, nano releases, vault path.
- Production multi-sig keys: **not yet** (demo keys ≠ production root of trust).

## Procedure — keep inventory current (each release)

1. Open `continuity/ASSET_INVENTORY.md`.
2. Add/update rows for new public releases, domains, keys, critical accounts.
3. Confirm free-core items marked continuity-protected.
4. Commit with release.

## Procedure — change-of-control trigger

Triggers include: acquisition, insolvency filing, loss of domain/GitHub/signing access without succession, material leadership change without succession plan.

1. Public notice as soon as lawful.
2. Freeze unauthorized free-core closure.
3. Follow draft covenant intent: no quiet withdrawal of already-released bone.
4. Domain 1 + Domain 5 logs as applicable.
5. Advance signed covenant when entity exists (legal counsel).

## Procedure — annual continuity attestation (when entity exists)

1. Use `docs/specs/artefacts/09/ANNUAL_CONTINUITY_ATTESTATION.md`.
2. Confirm escrow/backup/key arrangements still adequate.
3. Publish attestation hash if using seals.

## Commands
```bash
cat continuity/COVENANT.md
cat continuity/ASSET_INVENTORY.md
```

## RACI
Stewardship Custodian R; board/entity A once formed; technical leads C for key/backup implementability.

## Done when
- [x] Draft covenant + inventory public
- [ ] Entity-signed covenant
- [ ] Multi-party production key design implemented
