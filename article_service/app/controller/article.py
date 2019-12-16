from article_service.utils import get_required_data_from_request
from article_service.app.models.dto import CreateArticleDTO
from article_service.app.service import article as service


def create_article() -> None:
    request_data = get_required_data_from_request("id", "headline", "body")
    dto = CreateArticleDTO.fromdict(request_data)
    service.create_url(dto)
