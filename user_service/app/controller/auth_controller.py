# Standard library
from typing import Dict

# 3rd party modules
import flask
from flask import request

# Internal modules
from user_service.utils import get_required_data_from_request
from user_service.app.service import auth_service as service


def authorize() -> flask.Response:
    data: Dict = get_required_data_from_request("roles")
    token: bytes = request.headers.get("Authorization")
    return service.authorize(data["roles"], token)
