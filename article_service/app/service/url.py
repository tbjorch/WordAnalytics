# Standard library
from typing import List

# 3rd party modules
from werkzeug.exceptions import NotFound

# Internal modules
from article_service.app.models.dto import (
    CreateUrlDTO,
    UrlDTO,
    SetUrlScrapedDTO
)
from article_service.app.models import Url
from article_service.app.repository import url_repo
from article_service.app.service.utils import assert_valid_yearmonth


def create_url(dto: CreateUrlDTO) -> None:
    assert_valid_yearmonth(dto.yearmonth)
    url = Url(
        id=dto.id,
        yearmonth=dto.yearmonth,
        url=dto.url,
        undesired_url=dto.undesired_url
    )
    url_repo.save(url)


def get_url_by_id(id: str) -> UrlDTO:
    url: Url = url_repo.find_by_id(id)
    if url is None:
        raise NotFound("No url exist with the provided id")
    url_dto = UrlDTO(
        url_id=url.id,
        url=url.url,
        yearmonth=url.yearmonth,
        undesired_url=url.undesired_url,
        payed_content=url.payed_content,
        scraped_at=url.scraped_at,
        created_at=url.created_at,
    )
    return url_dto


def get_unscraped_urls() -> []:
    urls: [] = url_repo.find_unscraped()
    if len(urls) == 0:
        raise NotFound("No unscraped Urls in the database")
    return [UrlDTO(
        url_id=url.id,
        url=url.url,
        yearmonth=url.yearmonth,
        undesired_url=url.undesired_url,
        payed_content=url.payed_content,
        scraped_at=url.scraped_at,
        created_at=url.created_at
        ).todict() for url in urls]


def set_url_to_scraped(dto: SetUrlScrapedDTO) -> None:
    url: Url = assert_url_exists(dto.url_id)
    url_repo.flag_url_is_scraped(url, dto.scraped_at)


def get_urls_by_yearmonth(yearmonth: str) -> List[UrlDTO]:
    assert_valid_yearmonth(yearmonth)
    urls: List[Url] = url_repo.find_by_yearmonth(yearmonth)
    if len(urls) == 0:
        raise NotFound("No urls available at provided yearmonth")
    return [UrlDTO(
        url_id=url.id,
        url=url.url,
        yearmonth=url.yearmonth,
        undesired_url=url.undesired_url,
        payed_content=url.payed_content,
        scraped_at=url.scraped_at,
        created_at=url.created_at
        ).todict() for url in urls]


def assert_url_exists(id: str) -> Url:
    url: Url = url_repo.find_by_id(id)
    if url is None:
        raise NotFound("No url exist with the provided id")
    return url
