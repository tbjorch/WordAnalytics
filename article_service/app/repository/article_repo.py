# Internal modules
from article_service.app import db
from article_service.app.models.dto import CreateArticleDTO
from article_service.app.models import Article


def insert(dto: CreateArticleDTO) -> None:
    article = Article(
        id=dto.article_id,
        headline=dto.headline,
        body=dto.body,
    )
    db.session.add(article)
    db.session.commit()
