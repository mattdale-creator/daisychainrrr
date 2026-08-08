# Domain 04 · checklist · private-when-should-be-public

**Path:** `eventualities/domain-artefact-failures/d04/checklist/private-when-should-be-public/README.md`  
**Updated:** 2026-08-08  
**Ethos:** down to the bone — org transparency equals model transparency.

## What this eventuality is
Domain **04** requires operational artefacts (founding turns 37–46).  
Here the **checklist** artefact is compromised by: **Domain transparency artefact is hidden without logged exception**.

## Why it matters
If Domain 04 artefacts are missing, stale, private-without-exception, or incomplete, the organisation can claim radical honesty while retaining soft tissue. That violates the free-core ethos.

## Normative source
- Full plan: `docs/specs/04-*.md`
- Artefact directory: `docs/specs/artefacts/04/`
- Registers: `registers/`

## Detection signals
1. Scorecard or quarterly report lists PARTIAL/TOMBSTONE without linked artefact path.
2. File missing under `docs/specs/artefacts/04/` or empty critical fields.
3. Public claim references Domain 04 compliance without log evidence.
4. Exception for non-publication lacks Domain 1 log entry + expiry.

## Immediate response
1. Stop any public claim that depends on the broken artefact.
2. Log: Domain 1 decision if process change; Domain 5 incident if integrity of public proof; Domain 3 if data-related.
3. Either **fill the artefact** with real content or publish a **tombstone** explaining the gap.
4. Update `docs/specs/artefacts/MASTER_DOMAIN_SCORECARD.md` and any release scorecard.
5. Emit stream event `domain_gap` or `tombstone` if a public release is affected.
6. Re-run `python3 scripts/domain_scorecard_all.py`.

## Prevention
- Release checklist requires Domain 04 row with artefact link.
- CI/manual gate: refuse “MET” without file existence + min size / required headings.
- Monthly Domain 1 audit of artefact completeness.
- No commercial launch without Domain 8 boundary review when relevant.

## Tests / drills
- [ ] File exists and has non-stub content (>800 bytes, named sections)
- [ ] Linked from master scorecard
- [ ] Tabletop once per year per domain (Domain 5 style)
- [ ] `python3 scripts/oneshot_verify_all.py` still green after changes

## Owner
**Primary:** project lead (md@0265.au) until Domain custodian role is staffed.  
**Backup:** first engineering hire with free-core mandate.

## Related
- Eventuality leaf procedures in sibling `detect.md` / `respond.md` / `prevent.md`
- Founding domain plan and BOUNDARY if commercial pressure appears
