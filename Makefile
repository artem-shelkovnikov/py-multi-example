PYTHON?=python3

.venv/bin/python:
	$(PYTHON) -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install --upgrade build

.venv/bin/connectors_service:
	.venv/bin/pip install -r libraries/connectors/requirements/lib.txt
	.venv/bin/pip install --editable libraries/connectors
	.venv/bin/pip install -r apps/connectors_service/requirements/app.txt
	.venv/bin/pip install --editable apps/connectors_service

.venv/bin/connectors_cli:
	.venv/bin/pip install -r libraries/connectors/requirements/lib.txt
	.venv/bin/pip install --editable libraries/connectors
	.venv/bin/pip install -r apps/connectors_cli/requirements/app.txt
	.venv/bin/pip install --editable apps/connectors_cli

.venv/bin/connectors_agent_component:
	.venv/bin/pip install -r libraries/connectors/requirements/lib.txt
	.venv/bin/pip install --editable libraries/connectors
	.venv/bin/pip install -r apps/connectors_agent_component/requirements/app.txt
	.venv/bin/pip install --editable apps/connectors_agent_component 

install: .venv/bin/python .venv/bin/connectors_service .venv/bin/connectors_agent_component

clean:
	rm -rf .venv include elasticsearch_connector.egg-info .coverage site-packages pyvenv.cfg include.site.python*.greenlet

agent: .venv/bin/python .venv/bin/connectors_agent_component
	.venv/bin/connectors_agent_component

cli: .venv/bin/python .venv/bin/connectors_cli
	.venv/bin/connectors_cli

run: .venv/bin/python .venv/bin/connectors_service .venv/bin/connectors_cli .venv/bin/connectors_agent_component
	.venv/bin/connectors_service
	.venv/bin/connectors_cli
	.venv/bin/connectors_agent_component
