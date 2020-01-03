# Standard library
import os
from typing import List, Optional
import logging

# 3rd party modules
import requests
from requests.exceptions import RequestException
from werkzeug.exceptions import (
    BadRequest,
    NotFound,
    InternalServerError,
    Forbidden
)

# Internal modules
from statistics_service.app.models.dto import ArticleDTO, MonthStatsDTO


article_service_uri: str = os.environ["ARTICLE_SERVICE_URI"]
port: str = os.environ["ARTICLE_SERVICE_PORT"]


def get_articles_by_yearmonth(yearmonth: str) -> List[ArticleDTO]:
    res = requests.get(
        f'{article_service_uri}:{port}/v1/articles/yearmonth/{yearmonth}'
    )
    if (res.status_code == 200):
        logging.info(
            f"Fetched articles month {yearmonth} from article service"
        )
        articles = res.json()
        dto_list = [ArticleDTO(
            id=article["article_id"],
            headline=article["headline"],
            body=article["body"])
            for article in articles]
    else:
        logging.warning(
            f"Could not fetch articles. Received status code {res.status_code}"
        )
        logging.warning(f"Message received: {res.json()}")
        if res.status_code == 400:
            raise BadRequest(res.json()["description"])
        elif res.status_code == 404:
            raise NotFound(res.json()["description"])
        elif res.status_code == 500:
            raise InternalServerError(res.json()["description"])
    return dto_list


def post_monthstats_to_article_service(yearmonth: str, stats: MonthStatsDTO) -> Optional[str]:
    try:
        res = requests.post(
            f'{article_service_uri}:{port}/v1/analytics/monthstats',
            data=stats.to_json(),
            headers={"Content-Type": "application/json"}
        )
        if res.status_code == 200:
            return res.json()["message"]
        elif res.status_code == 400:
            logging.warning(BadRequest(res.json()["description"]))
            raise BadRequest(res.json()["description"])
        elif res.status_code == 403:
            logging.warning(Forbidden(res.json()["description"]))
            logging.info("Trying PUT request instead")
            try:
                res = requests.put(
                    f'{article_service_uri}:{port}/v1/analytics/monthstats/{yearmonth}',
                    data=stats.to_json(),
                    headers={"Content-Type": "application/json"}
                )
            except Exception as e:
                logging.error(e)
                raise Exception(res.json()["description"])
        elif res.status_code == 404:
            logging.warning(NotFound(res.json()["description"]))
            raise NotFound(res.json()["description"])
        else:
            logging.error("Program couldn't handle response")
            logging.error(f"data received: {res.json()}")
            raise InternalServerError("Program couldn't handle response")
    except RequestException as e:
        logging.error("Something went wrong when posting to article service")
        logging.error(e)
        raise InternalServerError(
            "Something went wrong when posting to article service"
        )
    return None
