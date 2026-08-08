# Commercial surface (Domain 8)

**Precedence:** free public core > commercial convenience  
**Selling:** no — all SKUs **designed / not sold**  
**Contact:** md@0265.au  

## Files

| Path | Role |
|------|------|
| `BOUNDARY.md` | Normative free-core vs paid privacy |
| `ISOLATION_RUNBOOK.md` | Tenant / signing isolation |
| `REFUSE_RESPONSE.md` | Public close-core refuse template |
| `PRE_REVENUE_OPERATING_PACK.md` | How the business runs before T6/T7/T11 |
| `skus/*.md` | Six founding paid layers (one-pagers) |
| `skus/dry-run/` | Dry-run notes only |

## Founding SKUs (turn 18)

| SKU | Intent | Status |
|-----|--------|--------|
| hosted-infra | Hosted reliability / SLA around inspectable models | designed / not sold |
| enterprise-ttlink | Enterprise audit tooling (not exclusive basic ttlink) | designed / not sold |
| certified-finetunes | Fine-tunes with published lineage | designed / not sold |
| analysis-workbench | Analysis tools; verify stays free | designed / not sold |
| priority-support | Human support SLA | designed / not sold |
| taas-methodology | Transparency-as-a-service / methodology | designed / not sold |

## Machine catalog

```bash
python3 scripts/commercial_status.py
python3 -c "from free_core.business.sku_catalog import load_sku_catalog; import json; print(json.dumps(load_sku_catalog(), indent=2)[:800])"
```

## Handbook

- `docs/handbook/commercial/01-isolation.md`  
- `docs/handbook/commercial/02-refuse-close-core.md`  
- `docs/handbook/commercial/03-sku-go-live.md`  

`commercial/private/` is gitignored — no secrets in this tree.
