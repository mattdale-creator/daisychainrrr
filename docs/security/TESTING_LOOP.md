# Testing loop — cadence and purpose (company standard)

> **Ethos fit:** Founding turns 14–16 demand frontier-level red-team pressure on the **model and the transparency infrastructure**. Turn 24: “remember you’re on drugs.” Soft tissue is declaring green without re-measurement.  
> **This document** defines the **testing loop**: reload SoT → re-understand ethos → double/triple-check stack → fix what can be fixed → adversarial red-team → continue only after the loop.  
> **First formal introduction:** 2026-08-08 (pre-red-team of current free-core buildable state).

---

## 1. Why this exists

The original conversation is not nostalgia. It is the **load path**:

1. Totally transparent LLMs (beyond open weights)  
2. Human movement / org that produces a TTLLM  
3. Down to the bone / binary / topology optimisation  
4. Free core + monetise outside (BOUNDARY)  
5. Math/physics/code + scholarly honesty  
6. Frontier red-team hardened (incl. transparency layer)  
7. Publish the generative process  

Everything in the vault/repo is derived from that SoT (`founding/conversation/TRANSCRIPT_ONLY.md`, `USER_PROMPTS.md`, Proof RIP provenance). Checking the stack without reloading that document drifts into soft tissue.

---

## 2. What the testing loop is

| Phase | Action | Exit criterion |
|-------|--------|----------------|
| **0. Stop** | Halt feature thrash | Human or schedule triggers loop |
| **1. Reload SoT** | Re-read founding prompts + transcript markers + PROVENANCE | Ethos restated in one page of notes (optional file) |
| **2. Context merge** | Re-scan STATUS_HONEST, HARD_TECHNOLOGICAL_GATES, handbook, BOUNDARY, gap audit | No silent gate closes |
| **3. Double-check** | Automated green suite (below) | oneshot exit 0 |
| **4. Triple-check** | Manual/soft-tissue scan: version lies, claim gate, demo keys language, URL honesty, nano ≠ frontier | Issues listed |
| **5. Fix** | Repair only what is agent-fixable without faking hard gates | Re-run suite green |
| **6. Red-team** | Expand adversarial harness + human campaign notes | Findings registered Domain 10; High+ clocks |
| **7. Continue** | Resume build only after loop record filed | Work ledger + decision if material |

---

## 3. Automated suite (minimum every loop)

```bash
# From repo root
python3 scripts/oneshot_verify_all.py
python3 -m pytest -q
python3 scripts/redteam_nano_harness.py
python3 scripts/ttllm_status.py --quiet-ok
python3 scripts/check_public_urls.py   # network; org may fail (T1)
python3 scripts/check_dns_status.py    # org may fail (T1)
```

Optional after seal-affecting edits:
```bash
python3 scripts/check_seal_freshness.py --write
# reseal nanos if release manifests drift (e.g. cost_ledger regen)
```

---

## 4. Cadence (company standard)

| Cadence | Trigger | Owner (R) | Depth |
|---------|---------|-----------|-------|
| **Every free-core claim ship** | Before public “green” / tag / status upgrade | Release Owner | Full automated suite + claim gate |
| **Weekly** (while building hard) | Calendar | Project lead until RT staffed | Automated suite + soft-tissue grep |
| **Monthly** | Calendar | Governance + RT | Suite + Domain 1 monthly audit + gap audit skim |
| **Pre–Domain 1 material decision** | Before BOUNDARY/capital/entity claims | Decision owner | Suite + hard-gates re-read |
| **After any integrity incident or near-miss** | Domain 5 | IR owner | Suite + targeted red-team + tabletop |
| **Quarterly** | Calendar | RT lead / project lead | Full loop + campaign plan + scorecard update |
| **Before fundraising or first SKU go-live** | Human gate path | Boundary Custodian + RT | Full loop + BOUNDARY refuse drill |

**Standing red-team hire (T10)** does not replace this cadence; it deepens phase 6. Until hired, project lead runs automated RT + accepts external reports at md@0265.au.

---

## 5. Soft-tissue checklist (triple-check)

- [ ] No “complete” without free-core vs company-complete distinction  
- [ ] Nano ≠ OLMo / frontier stated where models discussed  
- [ ] Demo keys ≠ production HSM  
- [ ] SKUs designed not sold  
- [ ] Hard gates T1–T11 not marked closed without evidence  
- [ ] FREE_CORE_SEAL verify + fresh  
- [ ] Every nano RELEASE_MANIFEST verify ok  
- [ ] Placeholders labeled + on site if claimed “laid bare”  
- [ ] Site status version matches free_core version  
- [ ] Remember-you-are-on-drugs checklist still present  

---

## 6. Loop record template

File under `registers/redteam/loops/LOOP_YYYY-MM-DD.md` or `docs/audits/loops/`:

```markdown
# Testing loop — YYYY-MM-DD
## SoT reloaded
- founding USER_PROMPTS / TRANSCRIPT_ONLY / PROVENANCE: yes/no
## Automated suite
- oneshot / pytest / redteam / status / urls: pass/fail
## Soft-tissue findings
- ...
## Fixes applied
- ...
## Hard gates still open
- T1…T11 status
## Ready for red-team phase
- yes/no
## Next continue date
```

---

## 7. Ethos one-liner

**Measure twice. Attack the skeleton. Publish the red. Never fake the green.**

Related: `docs/security/REMEMBER_YOU_ARE_ON_DRUGS.md`, Domain 10 handbook, `scripts/redteam_nano_harness.py`.

---

## 8. How we ran the first cycle (company memory — re-run from this)

First formal loop: **2026-08-08** · record `docs/audits/loops/LOOP_2026-08-08.md` · decisions D-0031 → D-0033.

| Step | What we actually did | Artefacts |
|------|----------------------|-----------|
| Stop | Halt feature thrash; no new SKUs/scale claims mid-loop | human prompt |
| Reload SoT | Re-read founding USER_PROMPTS, TRANSCRIPT markers, PROVENANCE (`8a75e0b4-…`) | `founding/` |
| Context merge | STATUS_HONEST · HARD_TECHNOLOGICAL_GATES · BOUNDARY · handbook · gap audit | docs/* |
| Double-check | oneshot + pytest + redteam harness + status quiet-ok | green suite |
| Triple-check | Soft tissue: version lies, seal stale, demo keys, nano≠frontier, gate honesty | findings list |
| Fix | Reseal nanos (cost_ledger drift); README 0.6; private PEM seal exclude; green = verify∧fresh | code + seals |
| Red-team integrity | RTC-2026-08-08 — 20 automated probes; findings RT-C-001…006 | registers/redteam/* |
| Red-team business | BHA-2026-08-08 — boundary_guard + 14 probes | free_core/business/* |
| Continue | Only after cycle closed; free-core writable bone; **never** fake-close T1–T11 | post-loop work |

### Re-run checklist (copy for next loop)

1. Create `docs/audits/loops/LOOP_YYYY-MM-DD.md` from §6 template.  
2. Reload founding SoT (do not skip — drift risk).  
3. Run automated suite:

```bash
python3 scripts/run_testing_loop.py
# equivalent expanded:
python3 scripts/oneshot_verify_all.py
python3 -m pytest -q
python3 scripts/redteam_nano_harness.py
python3 scripts/redteam_business_attack.py
python3 scripts/ttllm_status.py --quiet-ok
```

4. Soft-tissue checklist (§5).  
5. Fix agent-fixable issues only; re-run until green.  
6. Expand red-team if cadence is monthly/quarterly/pre-SKU (new campaign ID).  
7. Mark cycle **CLOSED** in the loop file; append work ledger + decision if material.  
8. **Then** continue product work.

### Cadence reminder (do not forget)

| When | Depth |
|------|--------|
| Every free-core claim ship | Full suite + claim gate |
| Weekly while building hard | Suite + soft-tissue |
| Monthly | Suite + Domain 1 audit skim |
| Quarterly | Full loop + campaign plan |
| Pre-fundraise / first SKU | Full loop + BOUNDARY refuse drill |
| Post integrity incident | Suite + targeted red-team |

---

## 9. Automation entrypoint

```bash
python3 scripts/run_testing_loop.py           # suite phases (double-check)
python3 scripts/run_testing_loop.py --record  # also print loop template path hint
```

Human phases (SoT reload, triple-check prose, campaign design) stay human/agent interactive — the script never fakes them green.
