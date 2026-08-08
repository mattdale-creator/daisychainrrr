# Eventuality leaf fill report

**Date:** 2026-08-08  
**Action:** Replaced thin checklist stubs with path-semantic full procedures.

## Before
- ~10,038 files, median ~220 bytes
- ~85% under 400 bytes
- Typical content: `- [ ] Done` or empty detect checklists

## After
- Same file count
- Median ~1855 bytes, mean ~2122
- ~10,037 files over 900 bytes
- ~9,698 over 1500 bytes
- ~9,892 files rewritten with:
  - What / why
  - Detection signals
  - Ordered response steps
  - Prevention controls
  - Tests/drills with real commands
  - Owner / RACI
  - Links to registers, BOUNDARY, free_core verify tools

## Method
Path-semantic generator (`scripts/fill_eventuality_leaves.py` pattern) maps
layer × threat × phase × actor × leaf-type (and domain/supply-chain variants)
to instructional templates bound to real repo paths.

## Honesty
Leaves share structural templates specialized by path tokens — not 10k uniquely
hand-written novels. They are **real procedures** (commands, registers, owners),
not empty boxes. Further human specialization still improves quality; this removes
the “structure without content” defect.
