from free_core.stream.schema import StreamEvent, demo_events
from free_core.stream.log import StreamLog

def test_hash_chain(tmp_path):
    log = StreamLog()
    for e in demo_events():
        log.append(e)
    assert log.verify_chain()["ok"] is True
    path = tmp_path / "log.json"
    log.save(path)
    log2 = StreamLog.load(path)
    assert log2.verify_chain()["ok"] is True
    # tamper
    log2.events[1]["payload"]["hacked"] = True
    assert log2.verify_chain()["ok"] is False

def test_append_prev():
    log = StreamLog()
    a = log.append(StreamEvent(event_type="a", payload={"n": 1}))
    b = log.append(StreamEvent(event_type="b", payload={"n": 2}))
    assert b["prev_hash"] == a["event_hash"]
    assert b["seq"] == 1
