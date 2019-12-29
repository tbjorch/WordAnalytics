# Internal modules
from article_service.app.service import yearmonth
from article_service.utils import (
    make_json_response,
    get_required_data_from_request,
    ok_response
    )
from article_service.app.models.dto import MonthStatsDTO

# 3rd party modules
import flask


def get_yearmonth_data(YYYYmm: str) -> flask.Response:
    return yearmonth.most_frequent_words(YYYYmm)


def get_monthstat_data(YYYYmm: str) -> flask.Response:
    data = yearmonth.monthly_statistics(YYYYmm)
    return make_json_response(data.to_dict())


def post_monthstat_data() -> flask.Response:
    data = get_required_data_from_request(
        "yearmonth",
        "article_count",
        "word_mean",
        "word_median"
    )
    dto = MonthStatsDTO.fromdict(data)
    yearmonth.create_monthstat_record(dto)
    return ok_response()
