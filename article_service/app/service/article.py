# 3rd party modules
from werkzeug.exceptions import NotFound

# Internal modules
from article_service.app.models.dto import CreateArticleDTO
from article_service.app.service.url import assert_url_exists
from article_service.app.repository import article_repo


def create_url(dto: CreateArticleDTO) -> None:
    # Check that corresponding url exists in db, else
    # this scrape is not valid
    assert_url_exists(dto.article_id)
    article_repo.insert(dto)
