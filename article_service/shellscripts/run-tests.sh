rm -rf .pytest_cache
echo "Running pytest..."
# python -m pytest -v tests/
export PYTHONPATH="/Users/tobj/Devprojects/WordAnalytics/"
pytest
export MYPYPATH="/Users/tobj/Devprojects/WordAnalytics/"
echo "Running mypy checks..."
mypy --ignore-missing-imports run.py