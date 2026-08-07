from free_core.stream.schema import demo_events
import json

def test_demo_events_json():
    for e in demo_events():
        data = json.loads(e.to_json())
        assert data["schema"] == "ttllm.stream_event.v1"
