# Domain 7 — Supply-chain operations (human handbook)

**Updated:** 2026-08-08  
**Owner (R/A):** project lead / Infrastructure lead when staffed  
**Normative:** `docs/specs/07-supply-chain.md`  
**Register:** `registers/supply-chain/DEPENDENCY_REGISTER.md`

## Purpose
Material dependencies of free core must be visible (hosting, data sources, training stack, signing).

## Procedure — add or change a material dependency

1. Open `registers/supply-chain/DEPENDENCY_REGISTER.md`.
2. Add/update: name, category, role, disclosure notes.
3. If risk material: update risk summary artefact under `docs/specs/artefacts/07/`.
4. Domain 1 decision if change affects public verification path.
5. For compute of a model release: fill compute provenance note template at release time.
6. Annual attestation when process matures.

## Procedure — provider incident (outage, takeover, license change)

1. Use severity from Domain 5 if public proof surfaces break.
2. Follow eventuality catalog under `docs/architecture-tree/eventualities/supply-chain-deep/<provider>/`.
3. Log Domain 7 change and Domain 5 incident as needed.
4. Prefer failover that keeps free core public; never “fix” by closing bone.
5. Stream event `supply_chain` without secrets.

## Current material deps (verify register is source of truth)
Cloudflare Pages/DNS, GitHub, Project Gutenberg, Apple Silicon + PyTorch + Python, free_core first-party.

## Commands
```bash
cat registers/supply-chain/DEPENDENCY_REGISTER.md
python3 scripts/oneshot_verify_all.py
```

## RACI
Infrastructure lead R for register accuracy; security consult on account-takeover class risks.
