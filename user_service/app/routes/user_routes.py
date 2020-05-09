import flask
from user_service.app.controller import user_controller as controller
from user_service.app import app
from user_service.utils.auth import authorized


@app.route('/v1/users', methods=["GET"])
def get_all_users() -> flask.Response:
    return controller.get_all_users()


@app.route('/v1/users/<id>', methods=["GET"])
def get_user_by_id(id: int) -> flask.Response:
    return controller.get_user_by_id(id)


@app.route('/v1/users', methods=["POST"])
def create_user() -> flask.Response:
    return controller.create_user()


@app.route('/v1/users/<id>', methods=["DELETE"])
@authorized("ADMIN")
def delete_user_by_id(id: int) -> flask.Response:
    return controller.delete_user(id)


@app.route('/v1/login', methods=["POST"])
def login() -> flask.Response:
    return controller.login()
