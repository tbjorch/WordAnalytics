# Internal modules
from statistics_service.app.service import calculator_service as service

# 3rd party modules
import flask


def calculate_yearmonth_data(YYYYmm: str) -> flask.Response:
    return service.calculate_monthstats(YYYYmm)
