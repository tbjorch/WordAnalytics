export PYTHONPATH="/Users/tobj/Devprojects/WordAnalytics/"
export FLASK_APP=run.py
export FLASK_ENV=development
export ENVIRONMENT=dev
exec gunicorn -b localhost:5000 --timeout 300 --access-logfile - --error-logfile - run:app