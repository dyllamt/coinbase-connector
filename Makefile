# source code and unit testing

.PHONY: install
install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt -U
	pip install -e . --no-deps

.PHONY: black
black:
	black src --line-length=120
	black tests --line-length=120

.PHONY: isort
isort:
	isort src --profile black --line-length=120
	isort tests --profile black --line-length=120

.PHONY: flake8
flake8:
	flake8 src --count --show-source --statistics

.PHONY: mypy
mypy:
	mypy --ignore-missing-imports src

.PHONY: test_format
test_format:
	make install
	make black
	make isort
	make flake8
	make mypy

.PHONY: test_unit
test_unit:
	make install
	pytest tests/unit/

# deployment and integration testing

.PHONY: docker-build
docker-build:
	docker build -t coinbase-connector .

.PHONY: test_integration
test_integration:
	pytest tests/integration/
