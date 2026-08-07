# Domain purchase attempt result

**UTC:** 2026-08-07T18:31:30.593383+00:00
**Account:** `03bac8b3a49fc4605ede89f35f792819` (Md@0265.au)

## Pre-buy check (both available)

| Domain | Registrable | Registration | Renewal |
|--------|-------------|----------------|---------|
| **ttllms.com** | yes | **USD 10.46** | USD 10.46 |
| **ttllms.org** | yes | **USD 8.50** | USD 11.20 |

## API register attempts

| Domain | State | Error |
|--------|-------|-------|
| ttllms.com | **failed** | `billing_auth_failed` — Failed to charge your payment method |
| ttllms.org | **failed** | `billing_auth_failed` — Failed to charge your payment method |

No domain was purchased. No charge should have succeeded (auth failed).

## Token capability notes

- Registrar domain-check: **works**
- Registrar register: **works until billing**
- Accounts / zones / Pages list: **works**
- `/user/tokens/verify`: returns Invalid (ignore; token still works for account APIs)
- R2 list buckets: needs **Enable R2** in dashboard once

## Next

Fix default payment method in Cloudflare Billing, then re-run `./ops/one_shot_ttllms.sh` or ask agent to retry both domains.

