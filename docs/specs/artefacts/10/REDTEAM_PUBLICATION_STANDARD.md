# Red-Team Publication Standard (v0.1)

## Classification
- **Critical:** integrity of public skeleton (manifest forge, index poison, key compromise)
- **High:** significant model or infra exploit with public impact
- **Medium / Low:** limited impact; may batch in periodic summary

## Default
Significant findings are published. Heavy redaction requires formal, time-limited exemption logged in Domain 5/10 registers.

## Timelines
- Register entry: within 7 days of confirmation for High+
- Technical report: within 30 days subject to active exploit exemption

## Nano automated harness
`scripts/redteam_nano_harness.py` exercises transparency-layer integrity (tamper detection), not jailbreak theatre for a char-LM.
