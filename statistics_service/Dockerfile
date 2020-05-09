FROM python:3.7.3-alpine

RUN adduser -D statistics_user

WORKDIR /home/statistics_service

RUN python -m venv venv

COPY app app
COPY utils utils
COPY requirements.txt requirements.txt
COPY run.py shellscripts/run.sh  ./
RUN chmod +x run.sh

RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

ENV FLASK_APP run.py
ENV PYTHONPATH /home

RUN chown -R statistics_user:statistics_user ./
USER statistics_user

EXPOSE 6000

CMD sh run.sh