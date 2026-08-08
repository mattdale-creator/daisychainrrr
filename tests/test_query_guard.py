from free_core.security.query_guard import QueryGuard

def test_rate_limit():
    g = QueryGuard(window_sec=60, hard_limit=5, suspicious_limit=2)
    for _ in range(5):
        assert g.allow("a") is True
    assert g.allow("a") is False
    assert g.stats()["blocked"] >= 1
