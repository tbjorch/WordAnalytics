rm -rf .pytest_cache
export PYTHONPATH="/Users/tobj/Devprojects/WordAnalytics/"
export ENVIRONMENT="dev"
export ARTICLE_SERVICE_URI="http://localhost"
export ARTICLE_SERVICE_PORT="5000"
echo "Running pytest..."
pytest -v
export MYPYPATH="/Users/tobj/Devprojects/WordAnalytics/analytics_service"
echo "Running mypy checks..."
mypy --ignore-missing-imports .