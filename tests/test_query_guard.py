from free_core.security.query_guard import QueryGuard, DEFAULT_POLICY


def test_rate_limit():
    g = QueryGuard(window_sec=60, hard_limit=5, suspicious_limit=2)
    for _ in range(5):
        assert g.allow("a") is True
    assert g.allow("a") is False
    assert g.stats()["blocked"] >= 1


def test_unique_span_burst():
    g = QueryGuard(window_sec=60, hard_limit=1000, unique_span_burst=5)
    for i in range(4):
        assert g.allow("b", span=f"span-{i}") is True
    assert g.allow("b", span="span-4") is False
    pol = g.policy()
    assert pol["paywall"] is False
    assert pol["offline_cli_unlimited"] is True
    assert DEFAULT_POLICY["hard_limit"] == 120


def test_policy_export():
    g = QueryGuard()
    assert "hard_limit" in g.stats()["policy"]

