"""
Public stream schema — the binary itself, streamed.

Not a Matrix aesthetic. Real events: data shards, checkpoints, linkages,
decision logs. Soft tissue is forbidden here.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict, field
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import json


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


@dataclass
class StreamEvent:
    schema: str = "ttllm.stream_event.v1"
    event_type: str = ""  # data_shard | checkpoint | ttlink_hit | decision | loss_metric | release
    timestamp_utc: str = field(default_factory=utcnow)
    artefact_sha256: Optional[str] = None
    payload: Dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)


def demo_events() -> List[StreamEvent]:
    return [
        StreamEvent(event_type="decision", payload={
            "decision_id": "D-0001",
            "summary": "Publish founding conversation as first public act",
            "ethos": "down_to_the_bone",
        }),
        StreamEvent(event_type="release", payload={
            "name": "daisychainrrr free public core scaffold",
            "version": "0.1.0",
        }),
    ]
