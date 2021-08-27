#! /bin/sh
set -e
alias python="poetry run python"
poetry run find . -name '*.py' -exec pyupgrade --py38-plus {} +
python -m black tests pytest_hpfeeds
python -m isort tests pytest_hpfeeds
python -m flake8 tests pytest_hpfeeds
python -m pytest --cov=. tests
