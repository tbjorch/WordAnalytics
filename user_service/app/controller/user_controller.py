# Standard library
import flask
from typing import List, Dict

# 3rd party modules
from werkzeug.exceptions import BadRequest

# Internal modules
from user_service.utils import (
    make_json_response,
    get_required_data_from_request
    )
from user_service.app.service import user as service
from user_service.app.models.dto import UserDTO, CreateUserDTO


def get_all_users() -> flask.Response:
    users: List[UserDTO] = service.get_all_users()
    return make_json_response(users)


def get_user_by_id(id: int) -> flask.Response:
    try:
        id = int(id)
    except ValueError:
        raise BadRequest("User id is expected in numerical form")
    user: UserDTO = service.get_user_by_id(id)
    return make_json_response(user)


def create_user() -> flask.Response:
    data: Dict = get_required_data_from_request("name")
    user: CreateUserDTO = CreateUserDTO.from_dict(data)
    service.create_user(user)
    return make_json_response({"message": "User successfully created"})


def delete_user(id: int) -> flask.Response:
    try:
        id = int(id)
    except ValueError:
        raise BadRequest("User id is expected in numerical form")
    service.delete_user(id)
    return make_json_response({"message": "User successfully deleted"})
