#!/usr/bin/env python3
"""Probe public URL inventory — honesty about what HTTP actually returns.

Reads ops/public_url_inventory.json (or default inventory).
Exit 0 if all required probes match; non-zero if required fail.
Optional probes may fail without failing the run when --strict-optional off.
"""
from __future__ import annotations
import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

DEFAULT_INVENTORY = {
    "schema": "ttllm.public_url_inventory.v1",
    "updated": "2026-08-08",
    "note": "Unpaid public surface. Tombstone routes that lie.",
    "probes": [
        {
            "id": "pages_root",
            "url": "https://ttllms.pages.dev/",
            "method": "GET",
            "expect_status": [200],
            "expect_body_contains": ["ttllm", "TTLLM", "transparent", "bone"],
            "required": True,
        },
        {
            "id": "pages_status",
            "url": "https://ttllms.pages.dev/status",
            "method": "GET",
            "expect_status": [200],
            "expect_body_contains": ["Honest", "status", "gates"],
            "required": True,
        },
        {
            "id": "pages_security_txt",
            "url": "https://ttllms.pages.dev/security.txt",
            "method": "GET",
            "expect_status": [200],
            "expect_body_contains": ["Contact:", "md@0265.au"],
            "required": True,
        },
        {
            "id": "com_root",
            "url": "https://ttllms.com/",
            "method": "GET",
            "expect_status": [200],
            "required": False,
            "tombstone_if_fail": "DNS/custom domain may still be human-gated",
        },
        {
            "id": "com_status",
            "url": "https://ttllms.com/status",
            "method": "GET",
            "expect_status": [200],
            "required": False,
        },
        {
            "id": "org_root",
            "url": "https://ttllms.org/",
            "method": "GET",
            "expect_status": [200],
            "required": False,
            "tombstone_if_fail": "ttllms.org DNS pending — see docs/handbook/gates/01-dns-org.md",
        },
        {
            "id": "pages_ttlink_api_get",
            "url": "https://ttllms.pages.dev/api/ttlink",
            "method": "GET",
            "expect_status": [200],
            "expect_content_type_substr": "json",
            "required": False,
            "tombstone_if_fail": "Pages Functions routing may 405/HTML — gate 03",
        },
        {
            "id": "github_repo",
            "url": "https://github.com/mattdale-creator/daisychainrrr",
            "method": "GET",
            "expect_status": [200],
            "required": True,
        },
    ],
}


def probe(entry: dict, timeout: float = 15.0) -> dict:
    url = entry["url"]
    method = entry.get("method", "GET").upper()
    req = urllib.request.Request(url, method=method, headers={"User-Agent": "ttllm-url-probe/1.0"})
    result = {
        "id": entry.get("id"),
        "url": url,
        "ok": False,
        "status": None,
        "error": None,
        "content_type": None,
        "required": bool(entry.get("required")),
    }
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(200_000)
            result["status"] = resp.status
            result["content_type"] = resp.headers.get("Content-Type", "")
            text = body.decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        result["status"] = e.code
        try:
            text = e.read(50_000).decode("utf-8", errors="replace")
        except Exception:
            text = ""
        result["content_type"] = e.headers.get("Content-Type", "") if e.headers else ""
        result["error"] = f"HTTPError {e.code}"
    except Exception as e:
        result["error"] = str(e)
        return result

    expect = entry.get("expect_status") or [200]
    if result["status"] not in expect:
        result["error"] = result.get("error") or f"status {result['status']} not in {expect}"
        return result
    ct_need = entry.get("expect_content_type_substr")
    if ct_need and ct_need.lower() not in (result.get("content_type") or "").lower():
        result["error"] = f"content-type {result.get('content_type')!r} missing {ct_need!r}"
        return result
    for frag in entry.get("expect_body_contains") or []:
        if frag.lower() not in text.lower():
            result["error"] = f"body missing {frag!r}"
            return result
    result["ok"] = True
    return result


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inventory", default=str(REPO / "ops/public_url_inventory.json"))
    ap.add_argument("--write-default", action="store_true", help="Write default inventory file")
    ap.add_argument("--timeout", type=float, default=15.0)
    ap.add_argument("--offline", action="store_true", help="Skip network; only validate inventory schema")
    args = ap.parse_args(argv)

    inv_path = Path(args.inventory)
    if args.write_default or not inv_path.exists():
        inv_path.parent.mkdir(parents=True, exist_ok=True)
        inv_path.write_text(json.dumps(DEFAULT_INVENTORY, indent=2) + "\n", encoding="utf-8")
        print("WROTE", inv_path)
        if args.write_default and args.offline:
            return 0

    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    probes = inv.get("probes") or []
    if args.offline:
        print("OFFLINE probes", len(probes))
        return 0 if probes else 1

    fails_required = []
    fails_optional = []
    for entry in probes:
        r = probe(entry, timeout=args.timeout)
        tag = "OK" if r["ok"] else "FAIL"
        print(f"{tag} {r['id']} status={r['status']} {r.get('error') or ''}".strip())
        if not r["ok"]:
            if r["required"]:
                fails_required.append(r)
            else:
                fails_optional.append(r)
                if entry.get("tombstone_if_fail"):
                    print("  TOMBSTONE:", entry["tombstone_if_fail"])

    print("SUMMARY required_fail", len(fails_required), "optional_fail", len(fails_optional))
    return 1 if fails_required else 0


if __name__ == "__main__":
    raise SystemExit(main())
