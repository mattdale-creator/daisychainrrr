"""Collect verified public stream tips for all nano releases.

Product is the proof: every tip is re-hashed with StreamLog.verify_chain
before it is published to the site. Free public core — never paywalled.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from free_core.stream.log import StreamLog


def _repo_root(start: Path | None = None) -> Path:
    if start is None:
        start = Path.cwd()
    start = Path(start).resolve()
    for p in [start, *start.parents]:
        if (p / "manifests" / "FREE_CORE_SEAL.json").exists() or (p / "free_core").is_dir():
            return p
    return start


def collect_nano_stream_tips(repo: Path | None = None) -> Dict[str, Any]:
    """Return tip index for every models/ttllm-nano* public_log.json."""
    root = _repo_root(repo)
    models = root / "models"
    nanos: List[Dict[str, Any]] = []
    all_ok = True
    if models.is_dir():
        for d in sorted(models.glob("ttllm-nano*")):
            if not d.is_dir():
                continue
            log_path = d / "stream" / "public_log.json"
            entry: Dict[str, Any] = {
                "name": d.name,
                "stream_path": str(log_path.relative_to(root)) if log_path.is_file() else None,
                "present": log_path.is_file(),
            }
            if not log_path.is_file():
                entry["chain_ok"] = False
                entry["reason"] = "missing public_log.json"
                all_ok = False
                nanos.append(entry)
                continue
            log = StreamLog.load(log_path)
            ver = log.verify_chain()
            entry["chain_ok"] = bool(ver.get("ok"))
            entry["count"] = ver.get("count", len(log.events))
            entry["tip"] = ver.get("tip")
            if log.events:
                last = log.events[-1]
                entry["last_event_type"] = last.get("event_type")
                entry["last_timestamp_utc"] = last.get("timestamp_utc")
            if not entry["chain_ok"]:
                entry["break_at"] = ver.get("break_at")
                entry["reason"] = ver.get("reason")
                all_ok = False
            # Site-relative mirror path when published under site/demo/
            site_key = d.name.replace("ttllm-", "")  # nano, nano-v2, ...
            entry["site_log"] = f"demo/{site_key}/public_log.json"
            nanos.append(entry)

    return {
        "schema": "ttllm.nano_stream_tips.v1",
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ethos": "hash-chained public streams — real process events, not a screensaver",
        "all_chain_ok": all_ok,
        "nano_count": len(nanos),
        "nanos": nanos,
        "verify": "python3 -c \"from free_core.stream.log import StreamLog; from pathlib import Path; print(StreamLog.load(Path('models/ttllm-nano/stream/public_log.json')).verify_chain())\"",
        "publish": "python3 scripts/publish_nano_stream_tips.py",
    }


def write_nano_stream_tips(
    repo: Path | None = None,
    dest: Optional[Path] = None,
    copy_logs: bool = True,
) -> Dict[str, Any]:
    """Write site/demo/nano_stream_tips.json and optionally mirror logs into site/demo/nano*."""
    root = _repo_root(repo)
    tips = collect_nano_stream_tips(root)
    if dest is None:
        dest = root / "site" / "demo" / "nano_stream_tips.json"
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if copy_logs:
        import json
        import shutil

        models = root / "models"
        for d in sorted(models.glob("ttllm-nano*")):
            if not d.is_dir():
                continue
            src = d / "stream" / "public_log.json"
            if not src.is_file():
                continue
            site_key = d.name.replace("ttllm-", "")
            out_dir = root / "site" / "demo" / site_key
            out_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, out_dir / "public_log.json")

    import json

    dest.write_text(json.dumps(tips, indent=2) + "\n", encoding="utf-8")
    tips["wrote"] = str(dest.relative_to(root))
    return tips
