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

.PHONY: test-format
test_format:
	make black
	make isort
	make flake8
	make mypy

.PHONY: test-unit
test_unit:
	pytest tests/unit/

# containerization and integration testing

.PHONY: docker-build
docker-build:
	docker build -t coinbase-connector .

.PHONY: test-integration
test_integration:
	pytest tests/integration/

# chart packaging and publishing


