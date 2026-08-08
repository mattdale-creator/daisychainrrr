# Red-team campaign RTC-2026-08-08

**Date:** 2026-08-08  
**Framing:** Constructive QA (founding turns 14–16)  
**Scope:** Free-core transparency layer + claim honesty + status API + BOUNDARY language + live demo API  
**Out of scope:** Illegal content, social engineering, faking hard-gate close, attacking third parties  

## Ethos
Product is the proof. Attack the skeleton. Publish the red. Do not declare green without re-measure.

## Method
1. Baseline: `redteam_nano_harness.py`, `oneshot_verify_all.py`  
2. Expanded campaign: `scripts/redteam_campaign_2026_08_08.py` (20 probes)  
3. Manual: live POST `/api/ttlink/`, seal leaf inventory for private keys, status claim grep  
4. Fixes for High findings; re-verify  

## Outcomes
- **High+ integrity controls** (tamper detect, stream chain, seal verify, nano manifests, BOUNDARY, claim gate, hard-gates honesty): **held** after reseal.  
- **Findings registered:** RT-C-001 … RT-C-005 (see FINDINGS_REGISTER.md).  
- **Remediation:** exclude private PEMs from free-core seal; document verify∧fresh; cost_ledger reseal warning already present.  

## Residual risk
- Tutorial demo private key still in git history/public repo for demos (accepted residual; not prod root).  
- No standing human red-team (T10).  
- Hosted API has no auth (by design for free demo) — QueryGuard only in Python reference, not necessarily on Pages Function (see residual below).  

### RT-C-006 (added) — Pages Function QueryGuard
**Severity:** Medium  
**Finding:** Live `POST /api/ttlink/` returns exact matches without server-side QueryGuard (Function is static index + open CORS). Bulk extract of demo corpus is possible.  
**Remediation (writable):** Document honesty on demo page; optional future rate limit on Function. Free-core offline verify unaffected.  
**Residual:** Demo corpus is intentionally public; multi-TB production index not present.  

## Ready to continue build
Yes, after this campaign record + green suite. Next loops: weekly automated + expand campaign probes.

## Commands to reproduce
```bash
python3 scripts/redteam_nano_harness.py
python3 scripts/redteam_campaign_2026_08_08.py
python3 scripts/oneshot_verify_all.py
```
