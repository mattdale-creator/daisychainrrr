# Human gates + hard tech gates

**Updated:** 2026-08-08  
**Hard inventory:** `docs/HARD_TECHNOLOGICAL_GATES.md`  
**Writable examples:** `docs/placeholders/00-INDEX.md` (each **Written by Grok - Human checking required**)  
**Site:** https://ttllms.com/hard-gates · https://ttllms.com/placeholders

## Hard gates (cannot close by writing)

| ID | Gate | Status | Close action |
|----|------|--------|--------------|
| T1 | Zone DNS Edit / ttllms.org records | OPEN — org unresolved | `docs/placeholders/ops/DNS_ORG_APPLY_PACKET.md` then dashboard/token |
| T2 | R2 enable | OPEN | `docs/placeholders/ops/R2_ENABLE_AND_FIRST_BUCKET.md` |
| T3 | Valid CF token scopes | PARTIAL — Pages deploy works; token verify may fail | Rotate token |
| T4 | GitHub `workflow` scope | OPEN | `docs/placeholders/ops/GITHUB_WORKFLOW_SCOPE_PACKET.md` |
| T5 | Prod multi-party / HSM keys | OPEN | `docs/placeholders/security/KEY_CEREMONY_TRANSCRIPT_EXAMPLE.md` then real ceremony |
| T6 | Entity filing | OPEN | `docs/placeholders/legal/ENTITY_FORMATION_PACK_EXAMPLE.md` + counsel |
| T7 | Bank / payments KYC | OPEN | After entity |
| T8 | Capital transfer | OPEN | Pitch pack in placeholders/capital |
| T9 | Second custodian consent | OPEN | `docs/placeholders/org/SECOND_CUSTODIAN_APPOINTMENT.md` |
| T10 | Standing red-team hire | OPEN | SOW + CCO role placeholders |
| T11 | Real customer payment | OPEN | MSA + go-live placeholders |

## Already agent-built (not gates)
- free_core, nanos, handbook, seals, public verify, Pages site on **ttllms.com**, JSON API `/api/ttlink/`, walls, placeholders library

Site redeploy: `npx wrangler pages deploy site --project-name=ttllms`
