# Pre-revenue operating pack (business bone)

**Updated:** 2026-08-09  
**Ethos:** Free public core never paywalled · monetise outside · product is the proof  
**Selling today:** **No** (hard gates T6 entity · T7 bank/KYC · T11 counterparty)  
**Contact:** md@0265.au  

## Purpose

Run a real **business process** before the first invoice — without soft-tissue claims that we are “already selling.”

## What the business is (pre-revenue)

| Layer | State |
|-------|--------|
| Free public core | **Shipped** — free_core, nanos, site, seals, public proof |
| Paid SKUs | **Designed / not sold** — six founding layers |
| BOUNDARY | **Normative** — free core > commercial convenience |
| Refuse path | **Scripted** — `REFUSE_RESPONSE.md` |
| Legal entity | **Open hard gate T6** |
| Bank / Stripe / invoice | **Open hard gates T7 / T11** |

## Daily / weekly pre-revenue ops

1. **Keep free-core green**  
   `python3 scripts/public_proof.py` · `python3 scripts/oneshot_verify_all.py`  
2. **Commercial integrity**  
   `python3 scripts/commercial_status.py`  
3. **Answer interest** at md@0265.au with BOUNDARY + SKU designs; never exclusive bone.  
4. **Refuse close-core** with public template; log material pressure.  
5. **Ship proof** to ttllms.com / GitHub when free-core or commercial process improves.  

## Interest intake (not a sale)

When someone writes “we want to buy / invest / partner”:

| Path | Action |
|------|--------|
| Wants free core closed or exclusive | **Refuse** → `REFUSE_RESPONSE.md` |
| Wants hosted SLA / tooling / support / methodology | Capture need; mark **interest only**; no SOW until T6+T7 |
| Wants to fund scale train | Point to hard gate T8 + placeholders/capital; no fake raise claim |
| Wants to verify | Point to unpaid `public_proof.py` / demo / stream |

**Do not** issue invoices, “reserved capacity,” or “early bird exclusive weights.”

## First-sale gate (future)

Only after:

1. Entity exists (T6)  
2. Bank/payment path exists (T7)  
3. `docs/handbook/commercial/03-sku-go-live.md` checklist complete  
4. Isolation runbook reviewed  
5. Domain 1 decision logged if material  
6. SKU status flip to live **only then**  

## Machine checks

```bash
python3 scripts/commercial_status.py
python3 scripts/redteam_business_attack.py
python3 -c "from free_core.business.sku_catalog import catalog_ok; assert catalog_ok()"
```

## Public surfaces

- https://ttllms.com/commercial.html  
- https://ttllms.com/economics.html  
- https://ttllms.com/status  

## Tombstone

Pre-revenue is not failure. **Fake revenue is failure.** Soft tissue is a defect.
