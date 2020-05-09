# Standard library
from typing import Dict

# 3rd party modules
from flask import request, make_response, jsonify
import flask
from werkzeug.exceptions import BadRequest


def get_required_data_from_request(*required_fields: str) -> Dict:
    """Checks request body for required data to be posted
    and returns as a dict. Throws TypeError if request is not in json format,
    and ValueError if required field is missing or if request contains
    additional invalid fields."""
    if not request.is_json:
        raise BadRequest("Posted data is expected to be in JSON format")
    else:
        data = request.get_json()
        if len(data) != len(required_fields):
            raise BadRequest(
                f"Expected {len(required_fields)} fields but got {len(data)}"
                )
        for field in required_fields:
            if field not in data:
                raise BadRequest(
                    f"Required field {field} is missing in request body"
                    )
        return data


def ok_response() -> flask.Response:
    return make_response(jsonify(message="ok"), 200)


def make_json_response(return_data: Dict, headers=None) -> flask.Response:
    response = make_response(jsonify(return_data), 200)
    if headers:
        response.headers['Authorization'] = f"Bearer {headers}"
    response.content_type = "application/json"
    return response
