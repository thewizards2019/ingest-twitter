PYTHON=python3
PKG_NAME=app

ROOT_DIR:=$(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
VENV=$(ROOT_DIR)/venv
flake8=$(VENV)/bin/flake8
pip=$(VENV)/bin/pip3
pytest=$(VENV)/bin/pytest
bandit=$(VENV)/bin/bandit
black=$(VENV)/bin/black
python=$(VENV)/bin/$(PYTHON)

$(VENV):
	cp scripts/pre-commit .git/hooks/
	$(PYTHON) -m venv $(VENV)

$(VENV)/bin/$(PKG_NAME): $(VENV)
	$(pip) install .

venv: $(VENV)

install: $(VENV)/bin/$(PKG_NAME)

dev-install: $(pytest)

$(pytest): $(VENV)
	$(pip) install -e .[dev]

lint: $(pytest)
	$(black) $(PKG_NAME)
	$(flake8) $(PKG_NAME)

test: $(pytest)
	$(pytest) -v --cov-branch --cov=tests/unit --cov-report=term
	coverage report -m --fail-under=50

scan:
	$(bandit) -lll -r app/

run:
	$(PKG_NAME) run

clean:
	rm -rf $(VENV)
	rm -rf dist
	rm -rf $(PKG_NAME).egg-info

docker-start-dev-env:
	docker build -t ingest-twitter .
	docker run --entrypoint /bin/sh -v $(CURDIR):/src --name ingest-twitter-dev-env -itd ingest-twitter
	docker exec ingest-twitter-dev-env pip3 install -e .[dev]
	docker attach ingest-twitter-dev-env

docker-stop-dev-env:
	docker stop ingest-twitter-dev-env
	docker rm ingest-twitter-dev-env

docker-build:
	docker build -t ingest-twitter .

docker-run:
	docker container run -p 5000:5000 --name ingest-twitter -td ingest-twitter 
	docker ps -l

docker-stop:
	docker stop ingest-twitter

docker-remove:
	docker rmi -f ingest-twitter
