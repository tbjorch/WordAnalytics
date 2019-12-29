# Internal modules
from analytics_service.app.service import yearmonth
from analytics_service.utils import make_json_response

# 3rd party modules
import flask


def get_yearmonth_data(YYYYmm: str) -> flask.Response:
    return yearmonth.most_frequent_words(YYYYmm)


def get_monthstat_data(YYYYmm: str) -> flask.Response:
    data = yearmonth.monthly_statistics(YYYYmm)
    return make_json_response(data.to_dict())
