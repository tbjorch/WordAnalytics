rm -rf .pytest_cache
export PYTHONPATH="/Users/tobj/Devprojects/WordAnalytics/"
export ENVIRONMENT="dev"
echo "Running pytest..."
pytest -v
export MYPYPATH="/Users/tobj/Devprojects/WordAnalytics/user_service"
echo "Running mypy checks..."
mypy --ignore-missing-imports .