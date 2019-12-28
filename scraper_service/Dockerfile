FROM python:3.7-alpine

RUN adduser -D scraper_user

WORKDIR /home/scraper_service

RUN apk add --no-cache build-base libxml2 libxml2-dev libxslt-dev

RUN python -m venv venv

COPY dto dto
COPY service service
COPY requirements.txt run.py shellscripts/run.sh ./

RUN venv/bin/pip install -r requirements.txt

RUN chown -R scraper_user:scraper_user ./
USER scraper_user

ENV PYTHONPATH /home

CMD sh run.sh