PYTHON?=python3

init_venv:
	uv venv --allow-existing

.venv: init_venv
	uv pip install -e \
		libraries/connectors_sdk \
		libraries/elastic_connectors \
		libraries/external_contribution_connector \
		apps/connectors_service \
		apps/connectors_cli \
		apps/connectors_agent_component

install: .venv 

clean:
	rm -rf .venv include .coverage site-packages pyvenv.cfg include.site.python*.greenlet

agent: .venv
	.venv/bin/connectors_agent_component

cli: .venv
	.venv/bin/connectors_cli run

service: 
	.venv/bin/connectors_service

run: agent cli service
