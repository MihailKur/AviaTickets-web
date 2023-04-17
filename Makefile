include .env
export


## Format all
fmt: format
format: isort black


## Check code quality
chk: check
lint: check
check: flake black_check isort_check

mypy:
	mypy core aviatickets


## Sort imports
isort:
	isort core aviatickets

isort_check:
	isort --check-only core aviatickets


## Format code
black:
	black --config pyproject.toml core aviatickets

black_check:
	black --config pyproject.toml --diff --check core aviatickets


# Check pep8
flake:
	flake8 --config .flake8 core aviatickets
