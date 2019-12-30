# Standard library
from datetime import datetime
from typing import List, Optional

# Internal modules
from article_service.app import db
from article_service.app.models import Url


def save(url: Url) -> None:
    db.session.add(url)
    db.session.commit()


def find_by_id(id: str) -> Url:
    url = Url.query.filter_by(id=id).first()
    return url


def find_unscraped() -> Optional[List[Url]]:
    urls = Url.query.filter_by(
        undesired_url=False,
        scraped_at=None,
        payed_content=False
    ).all()
    return urls


def flag_url_is_scraped(url: Url, scraped_at: datetime) -> None:
    url.scraped_at = scraped_at
    db.session.commit()


def find_by_yearmonth(yearmonth: str) -> Optional[List[Url]]:
    return Url.query.filter_by(yearmonth=yearmonth).all()
