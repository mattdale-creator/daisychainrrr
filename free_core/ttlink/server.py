"""Minimal local HTTP API for ttlink queries (stdlib only).

  python3 -m free_core.ttlink.server --index examples/ttlink_index.json --port 8765
"""
from __future__ import annotations
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse
from .index import TtlinkIndex
from free_core.security.query_guard import QueryGuard

INDEX: TtlinkIndex | None = None
GUARD = QueryGuard(hard_limit=60)


class Handler(BaseHTTPRequestHandler):
    def _json(self, code: int, obj: dict):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/health", "/v1/health"):
            return self._json(200, {"ok": True, "service": "ttlink-ref"})
        if path in ("/v1/ttlink/stats", "/stats"):
            assert INDEX is not None
            return self._json(200, INDEX.stats())
        self._json(404, {"error": "not_found"})

    def do_POST(self):
        path = urlparse(self.path).path
        if path not in ("/v1/ttlink/query", "/query"):
            return self._json(404, {"error": "not_found"})
        n = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(n) if n else b"{}"
        try:
            req = json.loads(raw.decode() or "{}")
        except json.JSONDecodeError:
            return self._json(400, {"error": "invalid_json"})
        client = req.get("client_id") or self.client_address[0]
        if not GUARD.allow(str(client)):
            return self._json(429, {"error": "rate_limited", "guard": GUARD.stats()})
        span = req.get("span") or ""
        assert INDEX is not None
        hits = INDEX.query(
            span,
            max_hits=int(req.get("max_hits") or 20),
            case_sensitive=bool(req.get("case_sensitive", True)),
        )
        self._json(200, {"hits": [h.__dict__ for h in hits], "count": len(hits)})

    def log_message(self, fmt, *args):
        pass


def main(argv=None):
    global INDEX
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default="examples/ttlink_index.json")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args(argv)
    INDEX = TtlinkIndex.load(Path(args.index))
    print(f"ttlink server on http://{args.host}:{args.port} docs={len(INDEX.docs)}")
    HTTPServer((args.host, args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
