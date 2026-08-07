# ttllms.org DNS pending

Pages project already has custom domains:
- ttllms.org — **pending** (CNAME record not set)
- www.ttllms.org — **pending** (CNAME record not set)

API token lacks Zone DNS Edit (403). Human action in Cloudflare dashboard:

1. Zone ttllms.org → DNS
2. CNAME `ttllms.org` → `ttllms.pages.dev` (proxied) — or apex method Cloudflare recommends
3. CNAME `www` → `ttllms.pages.dev` (proxied)

Or import vault BIND file: `05-dns-bind-import/ttllms.org.txt` (use `.txt` not `.zone`).

R2 still requires dashboard enable (API 10042).
