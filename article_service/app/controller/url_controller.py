import flask
from article_service.app.service import url_service
from article_service.utils import get_required_data_from_request, ok_response
from article_service.app.models.dto import CreateUrlDTO


def create_url() -> flask.Response:
    request_data = get_required_data_from_request(
        "id",
        "url",
        "yearmonth",
        "undesired_url",
    )
    url_dto = CreateUrlDTO.fromdict(request_data)
    url_service.create_url(url_dto)
    return ok_response()
