# Standard library
from datetime import datetime

# 3rd party modules
from werkzeug.exceptions import BadRequest, NotFound

# Internal modules
from article_service.app.models.dto import (
    CreateUrlDTO,
    UrlDTO,
    SetUrlScrapedDTO
)
from article_service.app.models import Url
from article_service.app.repository import url_repo


def create_url(url_dto: CreateUrlDTO) -> None:
    _assert_valid_yearmonth(url_dto.yearmonth)
    url_repo.insert(url_dto)


def get_url_by_id(id: str) -> UrlDTO:
    url: Url = url_repo.get_by_id(id)
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
    urls: [] = url_repo.get_unscraped()
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
    url: Url = _assert_url_exists(dto.url_id)
    url_repo.flag_url_is_scraped(url, dto.scraped_at)


def _assert_valid_yearmonth(yearmonth: int) -> None:
    if len(yearmonth) != 6:
        raise BadRequest(
            "Yearmonth value must be 6 characters length in format YYYYMM"
            )
    year: int = int(yearmonth[0:4])
    month: int = int(yearmonth[4:])
    if year > datetime.utcnow().year:
        raise BadRequest("Year value cannot be in the future")
    if year < 2000:
        raise BadRequest("Year value cannot be earlier than 2000")
    if month not in range(1, 13):
        raise BadRequest("Value must be in interval 1-12")


def _assert_url_exists(id: str) -> Url:
    url: Url = url_repo.get_by_id(id)
    if url is None:
        raise NotFound("No url exist with the provided id")
    return url
