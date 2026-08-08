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
