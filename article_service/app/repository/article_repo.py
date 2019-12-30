# Standard library
from typing import List

# Internal modules
from article_service.app import db
from article_service.app.models.dto import CreateArticleDTO, ArticleDTO
from article_service.app.models import Article, Url


def insert(dto: CreateArticleDTO) -> None:
    article = Article(
        id=dto.article_id,
        headline=dto.headline,
        body=dto.body,
    )
    db.session.add(article)
    db.session.commit()


def find_by_id(id: str) -> ArticleDTO:
    article = Article.query.filter_by(id=id).first()
    return article


def find_by_yearmonth(yearmonth: str) -> List[Article]:
    return (
        db.session.query(Article)
        .filter(Article.id == Url.id)
        .filter(Url.yearmonth == yearmonth)
        .all()
    )
