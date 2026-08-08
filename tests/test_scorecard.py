from free_core.release.scorecard import build_scorecard

def test_scorecard_contains_tombstone():
    md = build_scorecard(
        "test",
        [("Data", "MET", "ok")],
        ["not frontier"],
        merkle_root="abc",
    )
    assert "not frontier" in md
    assert "abc" in md
    assert "MET" in md
