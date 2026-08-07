# DNS records required (token cannot write DNS yet)

**Status:** Cloudflare API token has Pages + Registrar + zone list, but **DNS record list/edit returns 403 Authentication error**.

Pages custom domains are attached but stuck on: `CNAME record not set`.

## Primary zone: ttllms.com

Zone ID: `4f6b122b7a63280290b3a321071e4049`

Dashboard → **ttllms.com** → **DNS** → **Records** → add:

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `@` | `ttllms.pages.dev` | Proxied (orange cloud) |
| CNAME | `www` | `ttllms.pages.dev` | Proxied |

## Secondary zone: ttllms.org

Zone ID: `01c9852c3864cf80765c835091147fef`

| Type | Name | Target | Proxy |
|------|------|--------|-------|
| CNAME | `@` | `ttllms.pages.dev` | Proxied |
| CNAME | `www` | `ttllms.pages.dev` | Proxied |

## After DNS is saved

1. Wait 1–5 minutes  
2. Workers & Pages → **ttllms** → Custom domains → should become **Active**  
3. Open https://ttllms.com  

Live already: https://ttllms.pages.dev  

## So the agent can do DNS next time

1. https://dash.cloudflare.com/profile/api-tokens  
2. Edit your token (or create new)  
3. Add: **Zone → DNS → Edit**  
4. Zone Resources: **Include → All zones** from the account  
5. Save; put the new token value into `ops/secrets.local.env` as `CLOUDFLARE_API_TOKEN=`  
6. Tell the agent: **DNS token updated — apply CNAMEs**

Or run:

```bash
cd /Users/hattr/daisychainrrr
set -a && source ops/secrets.local.env && set +a
./ops/apply_dns_ttllms.sh
```
