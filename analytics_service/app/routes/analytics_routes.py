# 3rd party modules
import flask

# Internal modules
from analytics_service.app import app
from analytics_service.app.controller import analytics_controller as controller


@app.route('/v1/analytics/yearmonthdata/<yearmonth>', methods=["GET"])
def get_yearmonth_data(yearmonth: str) -> flask.Response:
    return controller.get_yearmonth_data(yearmonth)


@app.route('/v1/analytics/monthstats/<yearmonth>', methods=["GET"])
def get_monthstat_data(yearmonth: str) -> flask.Response:
    return controller.get_monthstat_data(yearmonth)