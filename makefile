.PHONY: test test-verbose
.PHONY: clean clean-pyc help
.PHONY: run
.PHONY: validate-saved-data validate-crawled-data
.PHONY: format lint check pre-commit pre-commit-manual


POETRY ?= poetry
TEST_DIR ?= hkjv_crawler/tests
PYTHONPATH ?= $(shell pwd)


### Run tests ###
test:  ## Run tests
	PYTHONPATH=$(PYTHONPATH) poetry run pytest $(TEST_DIR)

test-verbose:  ## Run tests with verbose output
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -vv $(TEST_DIR)


### Run application ###
# Need to add


### Code quality checks ###
format:  ## Format code using black and ruff
	$(POETRY) run black hkjv_crawler
	$(POETRY) run ruff format hkjv_crawler

lint:  ## Lint code using ruff
	$(POETRY) run ruff check hkjv_crawler
	$(POETRY) run mypy hkjv_crawler

check: format lint test  ## Run all code quality checks

pre-commit:  ## Run pre-commit checks
	$(POETRY) run pre-commit run --all-files

pre-commit-manual:  ## Run pre-commit checks including manual stages
	$(POETRY) run pre-commit run --hook-stage manual --all-files


### Utilities ###
clean: clean-pyc

clean-pyc:  ## Remove python cache files
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-21s\033[0m %s\n", $$1, $$2}'
