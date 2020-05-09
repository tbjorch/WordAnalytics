# 3rd party modules
import flask

# Internal modules
from user_service.app import app
from user_service.utils import ok_response
import user_service.app.routes.user_routes
import user_service.app.routes.auth_routes


@app.route('/v1/health')
def healthcheck() -> flask.Response:
    return ok_response()
