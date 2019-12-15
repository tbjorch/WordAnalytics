from typing import Dict
from flask import request, make_response, jsonify
import flask


def get_required_data_from_request(*required_fields: str) -> Dict:
    """Checks request body for required data to be posted
    and returns as a dict. Throws TypeError if request is not in json format,
    and ValueError if required field is missing or if request contains
    additional invalid fields."""
    if not request.is_json:
        raise TypeError("Posted data is expected to be in JSON format")
    else:
        data = request.get_json()
        if len(data) != len(required_fields):
            raise ValueError(
                f"Expected {len(required_fields)} fields but got {len(data)}"
                )
        for field in required_fields:
            if field not in data:
                raise ValueError(
                    f"Required field {field} is missing in request body"
                    )
        return data


def ok_response() -> flask.Response:
    return make_response(jsonify(message="ok"), 200)
