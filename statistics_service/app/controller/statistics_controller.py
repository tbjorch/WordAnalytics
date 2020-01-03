# Internal modules
from statistics_service.app.service import calculator_service as service
from statistics_service.app.rpc import post_monthstats_to_article_service
from statistics_service.utils import make_json_response

# 3rd party modules
import flask


def calculate_yearmonth_data(YYYYmm: str) -> flask.Response:
    stats = service.calculate_monthstats(YYYYmm)
    message = post_monthstats_to_article_service(YYYYmm, stats)
    return make_json_response({"message": message})
