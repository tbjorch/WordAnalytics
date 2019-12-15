echo "Running pytest..."
python -m pytest -v article_service/tests/
export MYPYPATH="/Users/tobj/Devprojects/WordAnalytics/article_service/"
echo "Running mypy checks..."
mypy --ignore-missing-imports article_service