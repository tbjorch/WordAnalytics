# 3rd party modules
import flask

# Internal modules
from user_service.app import app
from user_service.app.controller import auth_controller as controller


@app.route('/v1/authorize', methods=["POST"])
def authorize_user() -> flask.Response:
    return controller.authorize()
