# manifest · tampered · pre-release

**Path:** `cross-product/manifest/tampered/pre-release`

## What goes wrong
The **manifest** layer is **tampered** during **pre-release**.

## Ethos test
Does this leave soft tissue between the public and the binary? If yes, it is a defect.

## Actors who may cause or detect
founder, contributor, customer, attacker, investor, regulator, journalist

## Free core impact
If `manifest` is part of free public core, Domain 5/8 apply. Scorecard tombstone required if public claim relies on it.

## Response chain
1. detect → 2. register (decision/incident/legal/redteam) → 3. tombstone claims → 4. remediate → 5. re-seal manifests → 6. stream event
