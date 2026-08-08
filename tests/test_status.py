from free_core.status import collect_status
from free_core import __version__


def test_status_schema():
    st = collect_status()
    assert st["schema"] == "ttllm.project_status.v1"
    assert st["free_core_version"] == __version__
    assert "seal" in st
    assert st["ethos"]["free_public_core_never_paywalled"] is True
    assert st["ethos"]["nano_is_not_frontier"] is True
