from free_core.stream.catalog import EVENT_TYPES, required_for_class, catalog_markdown


def test_event_types_nonempty():
    assert "release" in EVENT_TYPES
    assert "incident_opened" in EVENT_TYPES


def test_nano_required():
    req = required_for_class("nano")
    assert "data_prepared" in req
    assert "release" in req
    assert "ttlink_index_sealed" in req


def test_catalog_md():
    md = catalog_markdown()
    assert "Stream event catalog" in md
    assert "`release`" in md
