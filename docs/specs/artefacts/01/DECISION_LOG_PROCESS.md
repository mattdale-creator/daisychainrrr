# Decision log process — Domain 1

## Where
- Human log: `registers/decisions/LOG.md` (append-only table)  
- Machine feed: `registers/decisions/feed.json`  

## When (materiality)
Log within **7 days** if the decision affects free public core, BOUNDARY, public training, transparency policy, ownership/funding, domains/DNS/signing keys, High+ incidents, or roles with release/security authority.  
See `MATERIALITY_THRESHOLD.md`.

## How
1. Assign next `D-NNNN`  
2. Date UTC, title, options, rationale, outcome, roles  
3. Mirror fact to `feed.json`  
4. Commit without secrets  
5. If BOUNDARY/core claims change → scorecard + consider stream event  

## Monthly
Use `MONTHLY_AUDIT_CHECKLIST.md` and file under `audits/`.

## Handbook
`docs/handbook/domains/01-governance-ops.md`
