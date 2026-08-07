"""Append-only public stream with hash chaining."""
from __future__ import annotations
import json
from pathlib import Path
from typing import List, Optional, Dict, Any
from .schema import StreamEvent, utcnow
from free_core.provenance.hashing import sha256_bytes


class StreamLog:
    def __init__(self):
        self.events: List[dict] = []

    def append(self, event: StreamEvent) -> dict:
        prev = self.events[-1]["event_hash"] if self.events else None
        body = {
            "schema": event.schema,
            "event_type": event.event_type,
            "timestamp_utc": event.timestamp_utc or utcnow(),
            "artefact_sha256": event.artefact_sha256,
            "payload": event.payload,
            "prev_hash": prev,
            "seq": len(self.events),
        }
        # hash without event_hash field
        raw = json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
        body["event_hash"] = sha256_bytes(raw)
        self.events.append(body)
        return body

    def verify_chain(self) -> Dict[str, Any]:
        prev = None
        for i, e in enumerate(self.events):
            if e.get("prev_hash") != prev:
                return {"ok": False, "break_at": i, "reason": "prev_hash mismatch"}
            if e.get("seq") != i:
                return {"ok": False, "break_at": i, "reason": "seq mismatch"}
            check = {k: v for k, v in e.items() if k != "event_hash"}
            raw = json.dumps(check, sort_keys=True, separators=(",", ":")).encode()
            if sha256_bytes(raw) != e.get("event_hash"):
                return {"ok": False, "break_at": i, "reason": "event_hash mismatch"}
            prev = e["event_hash"]
        return {"ok": True, "count": len(self.events), "tip": prev}

    def save(self, path: Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema": "ttllm.stream_log.v1",
            "count": len(self.events),
            "tip": self.events[-1]["event_hash"] if self.events else None,
            "events": self.events,
        }
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "StreamLog":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        log = cls()
        log.events = data.get("events", [])
        return log
