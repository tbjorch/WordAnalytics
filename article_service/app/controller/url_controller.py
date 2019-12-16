# 3rd party modules
import flask

# Internal modules
from article_service.app.service import url_service
from article_service.utils import (
    get_required_data_from_request,
    ok_response, 
    make_json_response,
)
from article_service.app.models.dto import (
    CreateUrlDTO,
    UrlDTO,
    SetUrlScrapedDTO
)


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


def get_unscraped_urls() -> flask.Response:
    unscraped_urls = url_service.get_unscraped_urls()
    return make_json_response(unscraped_urls)


def set_url_to_scraped(id: str) -> flask.Response:
    request_data = get_required_data_from_request("scraped_at")
    dto = SetUrlScrapedDTO.fromdict(request_data, id)
    print(type(dto.scraped_at))
    print(dto.scraped_at)
    url_service.set_url_to_scraped(dto)
    return ok_response()
