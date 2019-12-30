# Standard library
from typing import List

# Internal modules
from article_service.app import db
from article_service.app.models import Article, Url


def save(article: Article) -> None:
    db.session.add(article)
    db.session.commit()


def find_by_id(id: str) -> Article:
    return Article.query.filter_by(id=id).first()


def find_by_yearmonth(yearmonth: str) -> List[Article]:
    return (
        db.session.query(Article)
        .filter(Article.id == Url.id)
        .filter(Url.yearmonth == yearmonth)
        .all()
    )
