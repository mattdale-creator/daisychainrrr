# Black-hat business attack campaign — BHA-2026-08-08

**Framing:** Hostile commercial actor lens for **defense** (Domain 8 / 10). Not criminal instruction.  
**Code:** `free_core/business/boundary_guard.py` · `scripts/redteam_business_attack.py` · `tests/test_business_boundary.py`  
**JSON:** `registers/redteam/campaign_BHA-2026-08-08.json`

## Personas simulated (in code)

| Persona | Goal if successful | Probe IDs |
|---------|-------------------|-----------|
| Investor capture | Close-core terms | BH-001, BH-007, BH-011 |
| Open-washing | Fake TTLLM brand without bone | BH-001, BH-012 |
| Free-rider | Clone free core, starve commercial | BH-005 (by design) |
| Customer coercion | Exclusive weights / paid verify | BH-001, BH-008, BH-010 |
| Reputation FUD / self-own | False SKU-live or complete | BH-009, BH-001 |
| Single-human kill | Undocumented founder SPOF | BH-006 |
| Verify paywall | Break unpaid proof path | BH-002, BH-003, BH-004-* |

## Results (final)

| Metric | Value |
|--------|-------|
| Probes | 14 |
| Passed | 14 |
| High/Critical failed | 0 |

## Real code surfaces

1. **Pattern engine** — forbidden claim regexes with defensive-section parsing (negation / “Not TTLLM” / non-goals).  
2. **SKU status scanner** — fails if any SKU marked live/sold without honesty.  
3. **Offline verify** — FREE_CORE_SEAL + `public_verify_harness` must pass without auth.  
4. **Live HTTP** — status/free-core/hard-gates return 200 without login wall.  
5. **Isolation + refuse** — required docs with precedence/signing language.  

## Business attack tree (residual — not software-fixable)

| Attack | Residual |
|--------|----------|
| Capital starvation while free core is free | T8 / free-rider by design |
| Investor side letter post-entity | Process + counsel; term sheet pack |
| Single-human ops kill | T9 second custodian |
| Competitor ships open-weights + marketing “transparent” | Market; our bone is public proof |
| Domain/DNS hijack | T1/T3 human gates |
| False “SKU sold” on site by future edit | Caught by this scanner on CI/local |

## Reproduce

```bash
python3 scripts/redteam_business_attack.py
python3 -m pytest -q tests/test_business_boundary.py
```
