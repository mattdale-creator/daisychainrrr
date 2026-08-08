# Domain 7 artefacts — Supply chain

| Artefact | Path |
|----------|------|
| Dependency register | DEPENDENCY_REGISTER.md |
| Dependency change log | DEPENDENCY_CHANGE_LOG.md |
| Materiality for deps | MATERIALITY_FOR_DEPS.md |
| Risk summary | SUPPLY_CHAIN_RISK_SUMMARY.md |
| Live lock | `registers/supply-chain/SUPPLY_LOCK.json` |
| Builder | `scripts/build_supply_lock.py` |
| Handbook | `docs/handbook/domains/07-supply-chain-ops.md` |

Runtime deps of free_core are intentionally minimal; extras are declared in `pyproject.toml`.
