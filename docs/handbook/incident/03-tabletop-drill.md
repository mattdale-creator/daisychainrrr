# Tabletop drill (transparency integrity)

**Updated:** 2026-08-08  
**Owner (R):** Incident Response Owner  
**Example completed drill:** `registers/incidents/TABLETOP_2026-08-08.md`  
**Cadence:** at least quarterly once org has more than one person; founding: after material stack changes

## Purpose
Exercise detection → classify → log → tombstone → reseal → stream **without** waiting for a real breach. Drills are synthetic; they do **not** open fake production incidents in the public log unless clearly marked drill.

## Scenario bank (pick one)
1. Public Merkle root mismatches files after bad deploy
2. Signing key suspected leaked
3. ttlink index poisoned (extra doc, wrong hash)
4. Stream chain broken by manual JSON edit
5. Commercial tenant data almost published into free core
6. Scorecard claims MET while harness fails

## Drill procedure (90 minutes)

### Prep (10 min)
- Assign roles: Incident Owner, Provenance, Comms, Scribe
- Confirm repo checkout and working verify baseline:
```bash
python3 scripts/oneshot_verify_all.py
python3 scripts/redteam_nano_harness.py
```

### Inject (5 min)
Facilitator states scenario + fake "detection time". No real production sabotage required if dry-run; optional local tamper in a **throwaway branch**.

### Respond (45 min)
1. Classify High/Critical using Domain 5 thresholds.
2. Draft register row (in drill notes file, not necessarily production INCIDENT_LOG unless you want a marked drill row).
3. Run verify commands; show how mismatch is detected.
4. Decide tombstone language for status page.
5. Plan reseal from known-good commit **or** intentional re-seal after fix.
6. Draft 72h public ack (3–5 sentences).
7. Check commercial isolation: would tenant data leak? Would public fix break customers?

### Debrief (30 min)
- What was slow or ambiguous?
- Which handbook section was wrong or missing?
- Open Domain 1 decisions if process change needed.
- Write drill record under `registers/incidents/TABLETOP_YYYY-MM-DD.md`.

## Drill record template
```markdown
# Tabletop drill — <title>
**Date:** YYYY-MM-DD
**Scenario:** …
**Participants:** …
## Steps exercised
1. …
## Detection commands
```bash
…
```
## Outcome
## Handbook gaps found
## Follow-ups (decision IDs if any)
```

## Do not
- Tamper production seals without a recovery plan
- Publish drill as real incident without "drill" labeling
- Skip debrief write-up (tribal knowledge returns)

## RACI
Incident Owner R for drill execution; domain owners C; public I only if publishing drill summary voluntarily.

## Done when
- [ ] Dated drill file written
- [ ] At least one detection command demonstrated
- [ ] Follow-ups assigned or explicitly "none"
