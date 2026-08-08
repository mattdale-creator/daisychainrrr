# Domain 1 — Governance operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R):** project lead (md@0265.au) until Governance Custodian staffed  
**Accountable (A):** project lead  
**Normative plan:** `docs/specs/01-governance.md`  
**Artefacts:** `docs/specs/artefacts/01/`  
**Register:** `registers/decisions/LOG.md`, `registers/decisions/feed.json`

## Purpose
Make material decisions public and auditable so the org cannot claim radical honesty while retaining a private decision layer.

## When to use
- Any **material** decision (see materiality below)
- Monthly completeness audit
- Quarterly governance report

## Materiality (must log within 7 days)
Use `docs/specs/artefacts/01/MATERIALITY_THRESHOLD.md`. In short, log if the decision affects:
free public core, BOUNDARY, public training runs, transparency policy, ownership/funding, domains/DNS/signing keys, High+ incidents, or roles with release/security authority.

## Procedure — log a material decision

1. Open `registers/decisions/LOG.md`.
2. Append a row:
   - **ID:** next `D-NNNN`
   - **Date (UTC)**
   - **Title**
   - **Options considered**
   - **Rationale**
   - **Outcome**
   - **Roles** (who decided)
3. Append the same fact to `registers/decisions/feed.json` (machine-readable feed).
4. If the decision changes BOUNDARY or free-core claims, update scorecards and consider a public stream event.
5. Commit with a clear message (no secrets in commit).

### Example log line
```
| D-0022 | 2026-08-08 | Example decision | A / B | Ethos-aligned reason | Chose A | project lead |
```

## Procedure — monthly audit

1. Open `docs/specs/artefacts/01/MONTHLY_AUDIT_CHECKLIST.md` (or this section).
2. Check last 30 days of git commits / releases for material decisions without log rows.
3. Backfill any missing rows (note “backfilled” in rationale).
4. Confirm no permanent secret exceptions without expiry (`EXCEPTION_HANDLING.md`).
5. Record audit completion in decision log if gaps were found.

## Procedure — quarterly report

1. Copy `docs/specs/artefacts/01/QUARTERLY_REPORT_TEMPLATE.md` to a dated file under `docs/specs/artefacts/01/reports/` (create dir if needed).
2. Fill score MET/PARTIAL/TOMBSTONE with evidence.
3. Link decision IDs from the quarter.
4. Run verification suite (exit codes only, no secrets):
```bash
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
python3 scripts/domain_scorecard_all.py
```
5. Update `docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md` Domain 1 row.

## Severity / timeline
- Decision log: **≤7 days** after material decision
- Missing log discovered later: backfill same day + note

## Commands
```bash
# From repo root
ls registers/decisions/
python3 scripts/domain_scorecard_all.py
```

## RACI
| Role | R | A | C | I |
|------|---|---|---|---|
| Project lead | ✓ | ✓ | | |
| Future Governance Custodian | ✓ | | ✓ | |
| Public (via log) | | | | ✓ |

## Done when
- [x] Charter exists: `docs/specs/artefacts/01/GOVERNANCE_CHARTER.md`
- [x] Log path known and used
- [ ] Monthly audit executed at least once with dated note
- [ ] Quarterly report filed for current period

## Related
- Eventualities catalog: `docs/architecture-tree/eventualities/domain-artefact-failures/d01/`
- Handbook index: `docs/handbook/00-HANDBOOK-INDEX.md`
