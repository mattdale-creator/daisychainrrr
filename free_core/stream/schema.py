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
    event_type: str = ""  # data_shard | checkpoint | ttlink_hit | decision | loss_metric | release | seal | site_deploy
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
        StreamEvent(event_type="decision", payload={
            "decision_id": "D-0002",
            "summary": "Free public core never paywalled; commercial only outside BOUNDARY",
            "ref": "commercial/BOUNDARY.md",
        }),
        StreamEvent(event_type="release", payload={
            "name": "daisychainrrr free public core",
            "version": "0.2.0",
            "tag": "v0.2.0-build",
        }),
        StreamEvent(event_type="seal", payload={
            "manifest": "manifests/FREE_CORE_SEAL.json",
            "note": "Merkle seal of free public core artefacts",
        }),
        StreamEvent(event_type="site_deploy", payload={
            "url": "https://ttllms.com",
            "project": "ttllms",
        }),
        StreamEvent(event_type="architect", payload={
            "tree": "docs/architecture-tree/",
            "status": "architect-complete",
        }),
    ]
