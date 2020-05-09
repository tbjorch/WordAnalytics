export FLASK_APP=run.py
export FLASK_ENV=development
export ENVIRONMENT=dev
export ARTICLE_SERVICE_URI=http://localhost
export ARTICLE_SERVICE_PORT=5000
export INITIAL_VALUES="201909,201908,201907"
#flask run --port 8080
exec gunicorn -b localhost:5001 --timeout 300 --access-logfile - --error-logfile - run:app