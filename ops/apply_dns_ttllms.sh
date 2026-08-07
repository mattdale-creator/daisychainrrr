#!/usr/bin/env bash
# Apply CNAME records for Pages custom domains. Requires Zone.DNS Edit on token.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
if [[ -f ops/secrets.local.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source ops/secrets.local.env
  set +a
fi
: "${CLOUDFLARE_API_TOKEN:?set CLOUDFLARE_API_TOKEN}"
API="https://api.cloudflare.com/client/v4"
AUTH=(-H "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" -H "Content-Type: application/json")
ZCOM=4f6b122b7a63280290b3a321071e4049
ZORG=01c9852c3864cf80765c835091147fef

upsert() {
  local ZONE="$1"
  local NAME="$2"
  local CONTENT="$3"
  local FQDN="$4"
  echo "== upsert CNAME ${FQDN} -> ${CONTENT} =="
  EXIST=$(curl -sS "${API}/zones/${ZONE}/dns_records?type=CNAME&name=${FQDN}" "${AUTH[@]}")
  RID=$(echo "$EXIST" | python3 -c "import sys,json; d=json.load(sys.stdin); r=d.get('result') or []; print(r[0]['id'] if r else '')")
  BODY=$(NAME="$NAME" CONTENT="$CONTENT" python3 -c 'import json,os; print(json.dumps({"type":"CNAME","name":os.environ["NAME"],"content":os.environ["CONTENT"],"proxied":True,"ttl":1}))')
  if [[ -n "$RID" ]]; then
    curl -sS -X PUT "${API}/zones/${ZONE}/dns_records/${RID}" "${AUTH[@]}" --data "$BODY" | python3 -m json.tool | head -40
  else
    curl -sS -X POST "${API}/zones/${ZONE}/dns_records" "${AUTH[@]}" --data "$BODY" | python3 -m json.tool | head -40
  fi
}

upsert "$ZCOM" "@" "ttllms.pages.dev" "ttllms.com"
upsert "$ZCOM" "www" "ttllms.pages.dev" "www.ttllms.com"
upsert "$ZORG" "@" "ttllms.pages.dev" "ttllms.org"
upsert "$ZORG" "www" "ttllms.pages.dev" "www.ttllms.org"

echo "Done. Check Pages custom domains in a few minutes."
