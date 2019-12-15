from article_service.app import db
from article_service.app.models.dto import CreateUrlDTO, UrlDTO
from article_service.app.models import Url


def insert_url(url_dto: CreateUrlDTO) -> None:
    url = Url(
        id=url_dto.id,
        url=url_dto.url,
        yearmonth=url_dto.yearmonth,
        undesired_url=url_dto.undesired_url
    )
    db.session.add(url)
    db.session.commit()


def get_url(id: str) -> Url:
    url = Url.query.filter_by(id=id).first()
    return url
