#!/usr/bin/env bash
# One-shot: check + register ttllms.com on Cloudflare Registrar.
# BILLABLE. Non-refundable once registration succeeds.
set -euo pipefail

DOMAIN="${DOMAIN:-ttllms.com}"
API="https://api.cloudflare.com/client/v4"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p ops

if [[ -f ops/secrets.local.env ]]; then
  set -a
  # shellcheck disable=SC1091
  source ops/secrets.local.env
  set +a
fi

TOKEN="${CLOUDFLARE_API_TOKEN:-}"
ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-}"

if [[ -z "$TOKEN" ]]; then
  echo "ERROR: set CLOUDFLARE_API_TOKEN (see ops/CREDENTIALS_STATUS.md)"
  exit 1
fi

auth_hdr=( -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" )

echo "== 1. Verify token =="
curl -sS "${API}/user/tokens/verify" "${auth_hdr[@]}" | tee ops/last_token_verify.json | python3 -c "
import sys, json
d = json.load(sys.stdin)
assert d.get('success'), d
print('token status:', (d.get('result') or {}).get('status'))
"

if [[ -z "$ACCOUNT_ID" ]]; then
  echo "== 2. Resolve account =="
  ACCOUNT_ID=$(curl -sS "${API}/accounts?per_page=20" "${auth_hdr[@]}" | python3 -c "
import sys, json
d = json.load(sys.stdin)
assert d.get('success'), d
r = d['result']
assert r, 'no accounts on token'
print(r[0]['id'])
print('using account', r[0].get('name'), file=sys.stderr)
")
else
  echo "== 2. Using ACCOUNT_ID from env =="
fi
echo "ACCOUNT_ID=$ACCOUNT_ID"
printf '%s\n' "$ACCOUNT_ID" > ops/last_account_id.txt

echo "== 3. Domain check ${DOMAIN} =="
curl -sS -X POST "${API}/accounts/${ACCOUNT_ID}/registrar/domain-check" "${auth_hdr[@]}" \
  --data "{\"domains\":[\"${DOMAIN}\"]}" | tee ops/last_check.json | python3 -c "
import sys, json
d = json.load(sys.stdin)
assert d.get('success'), d
x = d['result']['domains'][0]
print('name=', x.get('name'))
print('registrable=', x.get('registrable'))
print('reason=', x.get('reason'))
print('pricing=', x.get('pricing'))
assert x.get('registrable') is True, f'not registrable: {x}'
"

echo "== 4. REGISTER ${DOMAIN} (charges default payment method) =="
curl -sS -X POST "${API}/accounts/${ACCOUNT_ID}/registrar/registrations" "${auth_hdr[@]}" \
  --data "{\"domain_name\":\"${DOMAIN}\"}" | tee ops/last_registration.json | python3 -m json.tool || true

echo "== 5. Poll registration status =="
ok=0
for i in $(seq 1 18); do
  curl -sS "${API}/accounts/${ACCOUNT_ID}/registrar/registrations/${DOMAIN}/registration-status" "${auth_hdr[@]}" \
    | tee ops/last_registration_status.json \
    | python3 -c "
import sys, json
d = json.load(sys.stdin)
r = d.get('result') or {}
print('state=', r.get('state'), 'completed=', r.get('completed'))
st = r.get('state')
if st in ('failed', 'blocked', 'action_required'):
    raise SystemExit(3)
if st == 'succeeded' or r.get('completed') is True:
    raise SystemExit(0)
raise SystemExit(10)
" && { ok=1; break; } || ec=$?
  if [[ ${ec:-0} -eq 3 ]]; then
    echo "Registration terminal failure — see ops/last_registration_status.json"
    exit 3
  fi
  if [[ ${ec:-0} -eq 0 ]]; then
    ok=1
    echo "Registration succeeded"
    break
  fi
  sleep 5
done

if [[ "$ok" -ne 1 ]]; then
  echo "WARNING: poll timed out — check ops/last_registration_status.json"
fi

echo "== 6. Fetch registration resource =="
curl -sS "${API}/accounts/${ACCOUNT_ID}/registrar/registrations/${DOMAIN}" "${auth_hdr[@]}" \
  | tee ops/last_registration_resource.json | python3 -m json.tool || true

echo "== 7. Zone lookup =="
curl -sS "${API}/zones?name=${DOMAIN}" "${auth_hdr[@]}" \
  | tee ops/last_zones.json | python3 -m json.tool | head -60 || true

python3 - <<'PY'
import json
from pathlib import Path
from datetime import datetime, timezone

root = Path(".")
parts = [
    "# Domain purchase result",
    "",
    f"**UTC:** {datetime.now(timezone.utc).isoformat()}",
    "",
]
for name in [
    "last_account_id.txt",
    "last_token_verify.json",
    "last_check.json",
    "last_registration.json",
    "last_registration_status.json",
    "last_registration_resource.json",
    "last_zones.json",
]:
    p = root / "ops" / name
    parts.append(f"## {name}")
    if not p.exists():
        parts.append("_missing_")
        parts.append("")
        continue
    text = p.read_text()
    if name.endswith(".json"):
        try:
            text = json.dumps(json.loads(text), indent=2)
        except Exception:
            pass
    parts.append("```")
    parts.append(text[:8000])
    parts.append("```")
    parts.append("")
(root / "ops" / "DOMAIN_PURCHASE_RESULT.md").write_text("\n".join(parts) + "\n")
print("Wrote ops/DOMAIN_PURCHASE_RESULT.md")
PY

echo "DONE."
