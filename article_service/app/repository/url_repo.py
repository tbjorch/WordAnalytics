# Standard library
from datetime import datetime

# Internal modules
from article_service.app import db
from article_service.app.models.dto import CreateUrlDTO
from article_service.app.models import Url


def insert(url_dto: CreateUrlDTO) -> None:
    url = Url(
        id=url_dto.id,
        url=url_dto.url,
        yearmonth=url_dto.yearmonth,
        undesired_url=url_dto.undesired_url
    )
    db.session.add(url)
    db.session.commit()


def get_by_id(id: str) -> Url:
    url = Url.query.filter_by(id=id).first()
    return url


def get_unscraped() -> [Url]:
    urls = Url.query.filter_by(
        undesired_url=False,
        scraped_at=None,
        payed_content=False
    ).all()
    return urls


def flag_url_is_scraped(url: Url, scraped_at: datetime) -> None:
    url.scraped_at = scraped_at
    db.session.commit()


def get_by_yearmonth(yearmonth: str) -> None:
    urls = Url.query.filter_by(yearmonth=yearmonth).all()
    return urls
