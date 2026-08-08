# stale · d08 · log · detect

**Path:** `eventualities/domain-artefact-failures/d08/log/stale/detect.md`  
**Updated:** 2026-08-08  
**Leaf type:** detect — how we notice this failure mode early

## Purpose
How we notice this failure mode early for: Domain 08 artefact **log** under threat **artefact exists but is outdated relative to current release**.

## Detection procedure
1. Identify the expected healthy state for this path (file path, hash, scorecard MET, public URL).
2. Run automated checks where applicable:
   - Manifests: `python3 -m free_core.provenance.cli verify --manifest <path> --base .`
   - Stream: `python3 -m free_core.stream.cli verify <public_log.json>`
   - Canary: `python3 -m free_core.ttlink.cli canary-check --index <index.json>`
   - Suite: `python3 scripts/oneshot_verify_all.py` and `python3 scripts/redteam_nano_harness.py`
3. Compare published claims (site, README, scorecard) to artefacts under `docs/specs/artefacts/08/, docs/specs/08-*.md`.
4. Phase lens (**before public release or claim**): ensure the check runs at the right gate (pre-release checklist, release seal, post-release monitor, incident, acquisition freeze).
5. Actor lens (**project lead / founder**): record who reported or who could conceal the issue; escalate if incentive misalignment (Domain 6 / 8).

## Positive detection criteria
- Any verify failure, hash mismatch, missing free-core path, paywalled verification, or silent gap without tombstone.
- Scorecard says MET while artefact missing/stub.

## Output of detection
Write a one-paragraph incident/note with: path `domain-artefact-failures/d08/log/stale/detect.md`, evidence command output, severity guess (Low–Critical per Domain 5 thresholds).


## Artefacts / tools
- Paths: `docs/specs/artefacts/08/, docs/specs/08-*.md`
- Registers: registers/ + docs/specs/artefacts/08/
- Verify suite: `scripts/oneshot_verify_all.py`, `scripts/redteam_nano_harness.py`

## Done when
- [x] Written procedure exists (this file)
- [ ] Owner has executed once (drill or real)
- [ ] Linked failure mode cannot recur without detection

## Related
Parent node README; `docs/specs/`; `commercial/BOUNDARY.md`; `STATUS_HONEST.md`
