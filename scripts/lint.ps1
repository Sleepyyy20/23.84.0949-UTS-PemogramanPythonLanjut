# Run formatting and lint checks (requires black and flake8 installed)
python -m black . --check
python -m flake8 .
