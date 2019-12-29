source venv/bin/activate
export ENVIRONMENT="prod"
exec gunicorn -b :5000 --access-logfile - --error-logfile - run:app