# Public claim gate — Domain 4

**Normative for any public capability or integrity claim.**

## Required before claim
1. Evaluation protocol version published (or explicit “process-only / no capability claim”)
2. Contamination analysis **or** honest residual uncertainty note
3. Raw results archive path **or** explicit third-party benchmark limitation
4. Checkpoint / release merkle root linkage
5. Scorecard row for Domain 4 (MET / PARTIAL / TOMBSTONE)

## Nano policy (current)
- **Do not** make frontier capability claims.
- Allowed: process claims (“trained on hashed PG slices”, “seal verifies”, “ttlink exact span”).
- Required tombstones: nano ≠ OLMo-class; not multi-TB ttlink.

## Gate procedure
1. Draft claim sentence.  
2. Map each factual atom to artefact path + hash.  
3. If any atom lacks artefact → rewrite claim or tombstone.  
4. Run `python3 scripts/public_verify_harness.py` and `redteam_nano_harness.py`.  
5. Log Domain 1 if claim language is material to public product.

## Failure mode
Marketing adjectives without tasks_run rows = soft tissue = Domain 4 PARTIAL/TOMBSTONE until fixed.
