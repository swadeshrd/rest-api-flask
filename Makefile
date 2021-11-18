SHELL = bash

VENV_DIR = venv
VENV_BASE_DIR = ${VENV_DIR}/bin

.PHONY: build
build: clean
	@echo $$'\e[1;32m'### Building$$'\e[0m'

	Python -m venv ${VENV_DIR}

	${VENV_BASE_DIR}/python -m pip install --upgrade pip
	${VENV_BASE_DIR}/python -m pip install -e .

	test -d /home/servers/rest_flask/logs/gunicorn || mkdir -p /home/servers/rest_flask/logs/gunicorn
	@echo $$'\e[1;32m'### Completed$$'\e[0m'

clean:
	@echo $$'\e[1;32m'### Cleaning$$'\e[0m'

	find . -name "README.md" -exec rm -f {} \;
	find . -name ".gitignore" -exec rm -f {} \;
	find . -name ".tifignore" -exec rm -f {} \;
	find . -name ".isort.cfg" -exec rm -f {} \;
	find . -name "pyproject.toml" -exec rm -f {} \;
	find . -name "pyproject.toml" -exec rm -f {} \;
	find . -name "vscode_settings.json" -exec rm -f {} \;
	find . -name "dev.txt" -exec rm -f {} \;
	find . -name "test.txt" -exec rm -f {} \;
	find . -type d -name venv -exec rm -rf {} \; || true
	find . -type d -name deployment -exec rm -rf {} \; || true
	find . -type d -name logs -exec rm -rf {} \; || true
	find . -type d -name ".vscode" -exec rm -rf {} \; || true
	find . -type d -name "*.egg-info" -exec rm -rf {} \; || true