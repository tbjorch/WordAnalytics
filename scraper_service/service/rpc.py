# Standard library
from typing import List
import os
import logging
from datetime import datetime
import json

# 3rd party modules
import requests
from requests import Response

# Internal modules
from scraper_service.dto import UrlDTO, AddUrlDTO, ArticleDTO

article_service_uri: str = os.environ["ARTICLE_SERVICE_URI"]
port: str = os.environ["ARTICLE_SERVICE_PORT"]


def get_unscraped_urls() -> List[UrlDTO]:
    resp: Response = requests.get(
        f'http://{article_service_uri}:{port}/v1/urls/unscraped'
        )
    return [_convert_to_url_dto(url) for url in resp.json()]


def get_urls_by_yearmonth(yearmonth: str) -> List:
    resp: Response = requests.get(
        f'http://{article_service_uri}:{port}/v1/urls/yearmonth/{yearmonth}'
        )
    if resp.status_code == 404:
        return []
    return [_convert_to_url_dto(url) for url in resp.json()]


def post_url(url: AddUrlDTO) -> None:
    resp: Response = requests.post(
        f'http://{article_service_uri}:{port}/v1/urls',
        data=url.to_json(),
        headers={
            'Content-Type': 'application/json'
        }
    )
    if resp.status_code != 200:
        logging.error(
            f"ERROR when posting url to article microservice: {resp.json()}"
            )


def post_article(article: ArticleDTO) -> None:
    resp: Response = requests.post(
        f'http://{article_service_uri}:{port}/v1/articles',
        data=article.to_json(),
        headers={
            'Content-Type': 'application/json'
        }
    )
    if resp.status_code != 200:
        logging.error(
            f"ERROR when posting article to microservice: {resp.json()}"
            )


def set_url_flag_to_scraped(url_id: str, scraped_at: datetime) -> None:
    resp: Response = requests.put(
        f'http://{article_service_uri}:{port}/v1/urls/{url_id}/unscraped',
        data=json.dumps({"scraped_at": scraped_at.__str__()}),
        headers={
            'Content-Type': 'application/json'
        }
    )
    if resp.status_code != 200:
        logging.error(
            f"ERROR when posting url scraped \
                flag to microservice: {resp.json()}"
            )


def _convert_to_url_dto(url) -> UrlDTO:
    return UrlDTO(
        id=url["url_id"],
        url=url["url"],
        yearmonth=url["yearmonth"],
        payed_content=url["payed_content"],
        undesired_url=url["undesired_url"],
        scraped_at=url["scraped_at"],
        created_at=url["created_at"],
    )
