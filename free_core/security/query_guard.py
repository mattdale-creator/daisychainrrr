"""Query-layer hardening skeleton for public ttlink (founding turn 16)."""
from __future__ import annotations
from collections import defaultdict
import time
from typing import Dict, List, Set


class QueryGuard:
    """Rate limit + abuse signals. Does not destroy transparency; throttles bulk extraction."""

    def __init__(self, window_sec: float = 60.0, hard_limit: int = 120, suspicious_limit: int = 30):
        self.window_sec = window_sec
        self.hard_limit = hard_limit
        self.suspicious_limit = suspicious_limit
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.suspicious: Set[str] = set()
        self.blocked_total = 0
        self.allowed_total = 0

    def allow(self, client_id: str, query_cost: float = 1.0) -> bool:
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
        # cost: append multiple ticks for heavy queries
        for _ in range(max(1, int(query_cost))):
            self.requests[client_id].append(now)
        self.allowed_total += 1
        return True

    def stats(self) -> dict:
        return {
            "allowed": self.allowed_total,
            "blocked": self.blocked_total,
            "suspicious_clients": len(self.suspicious),
        }
