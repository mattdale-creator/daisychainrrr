# Autonomous readiness inventory

**Updated:** 2026-08-07 19:13 UTC  
**Contact:** md@0265.au  
**Vault:** `/Users/hattr/Downloads/TTLLMS.com BUILD`

## Live status

| Item | Status |
|------|--------|
| ttllms.com registered | YES (active ~2027-08-07) |
| ttllms.org registered | YES (active ~2027-08-07) |
| Public DNS A for ttllms.com / www | YES (Cloudflare anycast IPs) |
| Pages custom domain ttllms.com | **active** |
| Pages custom domain www.ttllms.com | **active** |
| Pages project deploy | YES (ttllms / ttllms.pages.dev) |
| Site content (TTLLM landing) | YES |
| ttllms.org / www.org DNS | **NO** (Pages still pending CNAME) |
| Free-core code + tests | YES (5 passed) |
| Founding conversation freeze | YES (`02-founding-conversation`, `09-precompact-snapshots`) |
| Proof RIP evidence | YES (`03-proof-rip`) |
| Grok account export | YES (`04-grok-account-export`) |
| BIND import files (.txt) | YES (`05-dns-bind-import`) |
| Precompact skill + hooks | YES (freeze/inject auto; new-session handoff **dormant**) |
| CF API token (Pages/Registrar/zones list) | YES in `ops/secrets.local.env` |
| CF API DNS write | **NO** (403) — dashboard DNS OK for .com |
| R2 | **NO** — enable once in CF dashboard |
| Email Routing API | **NO** (403) — set in dashboard if wanted |
| GitHub push | YES (mattdale-creator) |
| GitHub `workflow` scope | **NO** — Actions YAML not pushable |
| OpenRouter / Mailjet in agent env | YES (optional) |

## What agent can do autonomously **now**

- Edit free-core code, specs, site under vault
- Deploy Pages: `export` secrets then `npx wrangler pages deploy site --project-name=ttllms`
- Run tests, seal manifests
- Precompact freeze `/precompact-path-preserve`
- Git commit/push (except workflow files)
- Read founding/proof packs

## Human 1–2 minute items remaining (only blockers for full autonomy)

1. **ttllms.org DNS** — Import `05-dns-bind-import/ttllms.org.txt` (same as .com) so .org goes active  
2. **Optional: Zone DNS Edit on API token** — so agent can fix DNS without dashboard  
3. **Optional: Enable R2** in dashboard — then agent can create buckets with existing S3 keys  
4. **Optional: Email Routing** `@ttllms.com` → md@0265.au in dashboard  
5. **Optional: `gh auth refresh -s workflow`** — push GitHub Actions  

## Primary URL

**https://ttllms.com** (should serve site once local DNS resolves; public DNS already points at CF)

## Commands cheat sheet

```bash
cd "/Users/hattr/Downloads/TTLLMS.com BUILD/01-repo/daisychainrrr"
set -a && source ops/secrets.local.env && set +a
npx wrangler pages deploy site --project-name=ttllms --branch=main --commit-dirty=true
python3 -m pytest -q
python3 ~/.grok/skills/precompact-path-preserve/scripts/preserve_and_inject.py now
```
