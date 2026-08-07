
.PHONY: test seal install lint tree

install:
	pip install -e ".[dev]"

test:
	python -m pytest -q

seal:
	python -m free_core.provenance.cli seal-repo .

tree:
	@find . -type f -not -path './.git/*' | sort

lint:
	python -m compileall free_core tests
