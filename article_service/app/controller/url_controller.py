# 3rd party modules
import flask
from flask import jsonify

# Internal modules
from article_service.app.service import url_service
from article_service.utils import get_required_data_from_request, ok_response, make_json_response
from article_service.app.models.dto import CreateUrlDTO, UrlDTO


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


def get_url_by_id(id: str) -> flask.Response:
    url_dto: UrlDTO = url_service.get_url_by_id(id)
    return make_json_response(url_dto.todict())
