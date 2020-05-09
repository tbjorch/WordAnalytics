source venv/bin/activate
export ENVIRONMENT="prod"
exec gunicorn -b :6000 --timeout 300 --access-logfile - --error-logfile - run:app