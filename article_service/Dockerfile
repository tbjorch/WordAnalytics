FROM python:3.7.3-alpine

RUN adduser -D article_user

WORKDIR /home/article_service

RUN apk add --no-cache python3-dev postgresql-dev gcc musl-dev

RUN python -m venv venv

COPY app app
COPY ../utils ../utils
COPY requirements.txt requirements.txt
COPY run.py shellscripts/run.sh  ./
RUN chmod +x run.sh

RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

ENV FLASK_APP run.py
ENV PYTHONPATH /home

RUN chown -R article_user:article_user ./
USER article_user

EXPOSE 5000

CMD sh run.sh