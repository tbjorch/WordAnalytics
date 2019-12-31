# Standard library
from typing import List, Dict, Any

# 3rd party modules
import flask

# Internal modules
from utils import (
    get_required_data_from_request,
    make_json_response
    )
from article_service.app.models.dto import CreateArticleDTO, ArticleDTO
from article_service.app.service import article as service


def create_article() -> None:
    request_data = get_required_data_from_request("id", "headline", "body")
    dto: CreateArticleDTO = CreateArticleDTO.fromdict(request_data)
    service.create_url(dto)


def get_article_by_id(id: str) -> flask.Response:
    dto: ArticleDTO = service.get_article_by_id(id)
    return make_json_response(dto.to_dict())


def get_articles_by_yearmonth(yearmonth: str) -> flask.Response:
    dto_list: List[ArticleDTO] = service.get_articles_by_yearmonth(yearmonth)
    return_list: List[Dict[str, Any]] = (
        [article.to_dict() for article in dto_list]
        )
    return make_json_response(return_list)
