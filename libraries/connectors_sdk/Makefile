.PHONY: test

install:
	uv sync --all-extras

build:
	uv build

.venv: install

.venv/bin/pytest: .venv

.venv/bin/ruff: .venv

lint: .venv/bin/ruff
	$< check src

test: .venv/bin/pytest
	$< test

clean:
	rm -rf .venv dist connectors/connectors.egg-info
