# Standard library
from typing import List, Optional

# 3rd party modules
from werkzeug.exceptions import NotFound

# Internal modules
from article_service.app.models.dto import CreateArticleDTO, ArticleDTO
from article_service.app.models import Article
from article_service.app.service.url import assert_url_exists
from article_service.app.repository import article_repo


def create_url(dto: CreateArticleDTO) -> None:
    # Check that corresponding url exists in db, else
    # this scrape is not valid
    assert_url_exists(dto.article_id)
    article_repo.insert(dto)


def get_article_by_id(id: str) -> ArticleDTO:
    article: Article = _assert_article_by_id_exists(id)
    print(article)
    return ArticleDTO(
        article_id=article.id,
        headline=article.headline,
        body=article.body,
        created_at=article.created_at.__str__()
    )


def get_articles_by_yearmonth(yearmonth: str) -> List[ArticleDTO]:
    print(yearmonth)
    article_list: List[Article] = (
        _assert_article_by_yearmonth_exists(yearmonth)
        )
    dto_list: List[ArticleDTO] = [ArticleDTO(
        article_id=article.id,
        headline=article.headline,
        body=article.body,
        created_at=article.created_at.__str__()
        ) for article in article_list]
    print(dto_list)
    return dto_list


def _assert_article_by_id_exists(id: str) -> None:
    """ Asserts if article exists by id, else throws NotFound error"""
    article: Article = article_repo.find_by_id(id)
    if article is None:
        raise NotFound("No article exist with the provided id")
    return article


def _assert_article_by_yearmonth_exists(yearmonth: str) -> None:
    """ Asserts if article exists by yearmonth, else throws NotFound error"""
    article_list: Optional[List[Article]] = (
        article_repo.find_by_yearmonth(yearmonth)
        )
    print(article_list)
    if len(article_list) == 0:
        raise NotFound("No articles exist for the provided yearmonth")
    return article_list
