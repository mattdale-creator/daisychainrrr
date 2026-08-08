"""Normative stream event catalog — which events are required per release class."""
from __future__ import annotations
from typing import Dict, List, Any

# event_type → definition
EVENT_TYPES: Dict[str, Dict[str, Any]] = {
    "decision": {
        "description": "Material Domain 1 decision referenced publicly",
        "required_payload": ["decision_id", "summary"],
        "nano": "optional",
        "scale": "required_when_material",
    },
    "data_prepared": {
        "description": "Training data mixture prepared and carded",
        "required_payload": ["card"],
        "nano": "required",
        "scale": "required",
    },
    "training_started": {
        "description": "Training run began",
        "required_payload": ["hyper"],
        "nano": "required",
        "scale": "required",
    },
    "loss_metric": {
        "description": "Periodic or final loss/metric sample",
        "required_payload": [],
        "nano": "recommended",
        "scale": "required",
    },
    "checkpoint_saved": {
        "description": "Public intermediate checkpoint written",
        "required_payload": ["path"],
        "nano": "optional",
        "scale": "required_on_interval",
    },
    "training_finished": {
        "description": "Training run completed",
        "required_payload": [],
        "nano": "recommended",
        "scale": "required",
    },
    "release": {
        "description": "Public release claim with merkle root",
        "required_payload": ["name", "version"],
        "nano": "required",
        "scale": "required",
    },
    "seal": {
        "description": "Merkle seal of free core or release tree",
        "required_payload": ["manifest"],
        "nano": "recommended",
        "scale": "required",
    },
    "ttlink_index_sealed": {
        "description": "ttlink index sealed for public corpus",
        "required_payload": ["docs"],
        "nano": "required",
        "scale": "required",
    },
    "site_deploy": {
        "description": "Public site deploy",
        "required_payload": ["url"],
        "nano": "optional",
        "scale": "optional",
    },
    "architect": {
        "description": "Architecture tree / handbook milestone",
        "required_payload": ["tree"],
        "nano": "optional",
        "scale": "optional",
    },
    "incident_opened": {
        "description": "High/Critical incident opened (public-safe)",
        "required_payload": ["incident_id", "severity"],
        "nano": "on_incident",
        "scale": "on_incident",
    },
    "claim_tombstoned": {
        "description": "Public claim tombstoned due to integrity or honesty",
        "required_payload": ["claim", "reason"],
        "nano": "on_incident",
        "scale": "on_incident",
    },
    "incident_mitigated": {
        "description": "Incident mitigation applied",
        "required_payload": ["incident_id"],
        "nano": "on_incident",
        "scale": "on_incident",
    },
    "incident_closed": {
        "description": "Incident closed with residual risk note",
        "required_payload": ["incident_id", "residual"],
        "nano": "on_incident",
        "scale": "on_incident",
    },
    "incident_drill": {
        "description": "Synthetic tabletop drill (not a production incident)",
        "required_payload": ["scenario"],
        "nano": "optional",
        "scale": "optional",
    },
    "boundary_attestation": {
        "description": "Domain 8 boundary attestation published",
        "required_payload": ["period"],
        "nano": "optional",
        "scale": "annual_when_selling",
    },
    "redteam_finding": {
        "description": "Significant red-team finding registered",
        "required_payload": ["finding_id", "severity"],
        "nano": "on_finding",
        "scale": "on_finding",
    },
}


def required_for_class(release_class: str = "nano") -> List[str]:
    """Return event types marked required for a release class."""
    out = []
    key = "nano" if release_class == "nano" else "scale"
    for et, meta in EVENT_TYPES.items():
        if meta.get(key) == "required":
            out.append(et)
    return out


def catalog_markdown() -> str:
    lines = [
        "# Stream event catalog (normative)",
        "",
        "Generated from `free_core.stream.catalog.EVENT_TYPES`.",
        "",
        "| event_type | description | nano | scale | required_payload |",
        "|------------|-------------|------|-------|------------------|",
    ]
    for et, meta in EVENT_TYPES.items():
        payload = ", ".join(meta.get("required_payload") or []) or "—"
        lines.append(
            f"| `{et}` | {meta['description']} | {meta['nano']} | {meta['scale']} | {payload} |"
        )
    lines += [
        "",
        "## Nano minimum set",
        "",
        ", ".join(f"`{x}`" for x in required_for_class("nano")),
        "",
        "## Scale minimum set",
        "",
        ", ".join(f"`{x}`" for x in required_for_class("scale")),
        "",
        "*Soft tissue forbidden: inventing events without artefacts.*",
        "",
    ]
    return "\n".join(lines)
