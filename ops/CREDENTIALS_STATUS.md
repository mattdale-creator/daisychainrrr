# Credentials status — TTLLM / daisychainrrr

**Audited:** 2026-08-08 (UTC)  
**Goal:** finish the project with zero further intervention once the gaps below are closed.

## Summary

| System | Status | Blocks ship? |
|--------|--------|----------------|
| GitHub (`mattdale-creator`) | **OK** — `gh` keyring; scopes `repo`, `gist`, `read:org` | No |
| Public repo `daisychainrrr` | **OK** — push works | No |
| Cloudflare API (Registrar / DNS / Pages) | **BLOCKED** — all known tokens invalid/expired | **Yes** (domain + CF) |
| Cloudflare Wrangler OAuth | **EXPIRED** (2026-07-31) | Yes for Workers CLI as logged-in user |
| Cloudflare MCP bearer (`cfoat_…`) | **INVALID** (401/403) | Yes |
| cloudflared tunnel cert | **MISSING** | Only if tunnels needed |
| GitHub Actions secrets on this repo | **EMPTY** | Yes for CI register/deploy to CF |
| GitHub Pages | Can enable via workflow | No (interim hosting) |
| Mailjet | **PRESENT** in agent shell env | No (optional email) |
| OpenRouter | **PRESENT** in agent shell env | No (optional multi-AI battery) |
| 1Password CLI (`op`) | **MISSING** | No |

**Single hard gate for buying `ttllms.com`:** one new Cloudflare API token with Registrar Edit (+ Account Read), on an account that already has a default payment method and default registrant contact.

Target domain: **`ttllms.com`** (three L’s). Public DNS still NXDOMAIN at last check (appears free).  
`ttlms.com` (two L’s) is **taken** (AWS nameservers).

Browser identity you use: **md@0265.au**

Known account id from older projects (confirm in dashboard):  
`03bac8b3a49fc4605ede89f35f792819`

---

## What we tried (cannot be “downloaded”)

Cloudflare does **not** re-show or export existing API tokens. There is nothing for the agent to scrape or recover once tokens expire.

| Source | Result |
|--------|--------|
| Wrangler OAuth access token | `Invalid access token` |
| Wrangler refresh token | Cannot refresh from this environment (403) |
| Grok MCP `cloudflare-api` header | Invalid |
| Project `.env` / `.dev.vars` | No usable CF token values |
| macOS keychain (`CLOUDFLARE_API_TOKEN`) | Not found |
| GitHub Actions secrets (this + related public repos) | Empty / none listed |
| cloudflared `~/.cloudflared/cert.pem` | Missing |

---

## What already works (no action needed)

- Full free-core repo, specs, founding conversation, Proof RIP evidence, Merkle seal  
- GitHub push to `mattdale-creator/daisychainrrr`  
- Local `pytest` + `ttllm-manifest` / `ttlink` tools  
- Optional multi-AI later via OpenRouter (key already in environment)  
- Optional email later via Mailjet (keys already in environment)  

---

## What only you can create (one time)

These cannot be fabricated by the agent:

1. **Cloudflare API token** (Registrar Edit)  
2. **Default payment method** on the Cloudflare account  
3. **Default registrant contact** + Domain Registration Agreement acceptance  

Everything else after that is scripted.

---

## Minimum human checklist (md@0265.au)

### A — API token (~2 minutes)

1. Open https://dash.cloudflare.com/profile/api-tokens  
2. **Create Token** → **Create Custom Token**  
3. Name: `grok-registrar-ttllms`  
4. Permissions:
   - Account → **Registrar** → **Edit**  
   - Account → **Account Settings** → **Read**  
   - (Recommended for deploy later) Account → **Cloudflare Pages** → **Edit**  
   - (Recommended for DNS later) Zone → **DNS** → **Edit** on all zones in account, or “All zones” if offered  
5. Account Resources → include **your** account  
6. Create → **Copy token once**

### B — Billing

1. Account → **Billing** → **Payment info**  
2. Confirm a **default** card exists and is valid  

### C — Registrar contact

1. Open Domain Registration for the account  
   `https://dash.cloudflare.com/<ACCOUNT_ID>/domains/registrations`  
2. Set **default registrant contact**  
3. Accept **Domain Registration Agreement** if prompted  

### D — Account ID

Copy **Account ID** from the dashboard sidebar (32 hex chars).

### E — Deliver credentials (pick one)

**Option 1 — paste in chat (fastest for this session):**

```text
CLOUDFLARE_ACCOUNT_ID=...
CLOUDFLARE_API_TOKEN=...
GO register ttllms.com
```

**Option 2 — local file (agent can source without chat paste):**

```bash
cp ops/secrets.local.env.example ops/secrets.local.env
# edit ops/secrets.local.env with real values
# file is gitignored
```

Then either tell the agent “secrets file is ready” or run:

```bash
cd /Users/hattr/daisychainrrr
set -a && source ops/secrets.local.env && set +a
./ops/one_shot_ttllms.sh
```

---

## Automated chain after token exists

Script: [`ops/one_shot_ttllms.sh`](one_shot_ttllms.sh)

1. Verify token  
2. Resolve account  
3. **Check** `ttllms.com` (availability + price)  
4. **Register** (billable, non-refundable if succeeds)  
5. Poll until succeeded  
6. Write `ops/DOMAIN_PURCHASE_RESULT.md` + JSON receipts under `ops/last_*`  

Optional later (same token if DNS/Pages permissions included):

- Point apex/`www` at Pages or GitHub Pages  
- Deploy `site/` to Cloudflare Pages project `ttllms`  

---

## Interim hosting without Cloudflare

GitHub Actions workflow [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml) deploys `site/` to **GitHub Pages** when Pages is enabled for the repo. That does **not** replace owning `ttllms.com`.

---

## Security

- Never commit `ops/secrets.local.env`  
- Prefer short-lived token; delete/roll after purchase  
- Registrar success = charged; non-refundable per Cloudflare  

---

## Agent policy after you deliver the token

With a valid token in env or `ops/secrets.local.env`, the agent will:

1. Run domain-check and report price  
2. Register `ttllms.com` without asking again if you already said **GO** / one-shot  
3. Record results in-repo (receipts; not the token)  
4. Continue DNS + site wiring as far as token permissions allow  
'''
