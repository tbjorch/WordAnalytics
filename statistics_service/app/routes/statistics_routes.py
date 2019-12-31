# 3rd party modules
import flask

# Internal modules
from statistics_service.app import app
from statistics_service.app.controller import (
    statistics_controller as controller
)


@app.route('/v1/statistics/monthstats/<yearmonth>', methods=["GET"])
def get_yearmonth_data(yearmonth: str) -> flask.Response:
    return controller.calculate_yearmonth_data(yearmonth)
