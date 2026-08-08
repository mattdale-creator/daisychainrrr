import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def test_example_lineage_shape():
    p = REPO / "examples/finetune_lineage/EXAMPLE_LINEAGE.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    assert data["schema"] == "ttllm.finetune_lineage.v1"
    assert data["boundary_ref"] == "commercial/BOUNDARY.md"
    assert data["customer_private"]["weights"] is True
    assert data["delta"]["private_weights_published"] is False
    schema = json.loads((REPO / "free_core/schemas/finetune_lineage.schema.json").read_text())
    for key in schema["required"]:
        assert key in data
