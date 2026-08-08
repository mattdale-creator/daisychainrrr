# Decision Log process

**Updated:** 2026-08-08

1. Detect material decision (see MATERIALITY_THRESHOLD.md).
2. Within 7 days, append to `registers/decisions/LOG.md` and `feed.json`.
3. Fields: ID, date, title, options considered, rationale, outcome, roles.
4. Capture dissent if raised in writing.
5. Monthly completeness audit by Governance Custodian (founder until role filled).
6. Quarterly public summary in domain report.

## Technical
- Append-only Markdown + JSON feed
- Prefer git history as integrity layer; future: signed transparency log
