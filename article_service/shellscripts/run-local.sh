export FLASK_APP=run.py
export FLASK_ENV=development
#flask run --port 8080
exec gunicorn -b localhost:5000 --access-logfile - --error-logfile - run:app