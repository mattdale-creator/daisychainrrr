"""Query-layer hardening skeleton for public ttlink (founding turn 16)."""
from __future__ import annotations
from collections import defaultdict
import time
from typing import Dict, List, Set, Optional


# Public policy defaults (also docs/security/CANARY_QUERYGUARD_POLICY.md)
DEFAULT_POLICY = {
    "window_sec": 60.0,
    "hard_limit": 120,
    "suspicious_limit": 30,
    "unique_span_burst": 40,
    "note": "Offline CLI verify remains unlimited; hosted throttles bulk extract only.",
}


class QueryGuard:
    """Rate limit + abuse signals. Does not destroy transparency; throttles bulk extraction."""

    def __init__(
        self,
        window_sec: float = DEFAULT_POLICY["window_sec"],
        hard_limit: int = DEFAULT_POLICY["hard_limit"],
        suspicious_limit: int = DEFAULT_POLICY["suspicious_limit"],
        unique_span_burst: int = DEFAULT_POLICY["unique_span_burst"],
    ):
        self.window_sec = window_sec
        self.hard_limit = hard_limit
        self.suspicious_limit = suspicious_limit
        self.unique_span_burst = unique_span_burst
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.spans: Dict[str, List[tuple[float, str]]] = defaultdict(list)
        self.suspicious: Set[str] = set()
        self.blocked_total = 0
        self.allowed_total = 0

    def allow(self, client_id: str, query_cost: float = 1.0, span: Optional[str] = None) -> bool:
        now = time.time()
        window = [t for t in self.requests[client_id] if now - t < self.window_sec]
        self.requests[client_id] = window
        if len(window) >= self.hard_limit:
            self.suspicious.add(client_id)
            self.blocked_total += 1
            return False
        if client_id in self.suspicious and len(window) >= self.suspicious_limit:
            self.blocked_total += 1
            return False
        if span is not None:
            sp = [(t, s) for t, s in self.spans[client_id] if now - t < self.window_sec]
            sp.append((now, span[:200]))
            self.spans[client_id] = sp
            unique = {s for _, s in sp}
            if len(unique) >= self.unique_span_burst:
                self.suspicious.add(client_id)
                self.blocked_total += 1
                return False
        for _ in range(max(1, int(query_cost))):
            self.requests[client_id].append(now)
        self.allowed_total += 1
        return True

    def stats(self) -> dict:
        return {
            "allowed": self.allowed_total,
            "blocked": self.blocked_total,
            "suspicious_clients": len(self.suspicious),
            "policy": self.policy(),
        }

    def policy(self) -> dict:
        return {
            "window_sec": self.window_sec,
            "hard_limit": self.hard_limit,
            "suspicious_limit": self.suspicious_limit,
            "unique_span_burst": self.unique_span_burst,
            "offline_cli_unlimited": True,
            "paywall": False,
        }
