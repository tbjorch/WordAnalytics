from article_service.app import app
from flask import Response
from article_service.app.controller import url_controller


@app.route('/v1/urls', methods=['GET'])
def get_url() -> Response:
    return "Hello from urls"


@app.route('/v1/urls', methods=['POST'])
def post_url() -> Response:
    return url_controller.create_url()


@app.route('/v1/urls/<id>', methods=['DELETE'])
def delete_url() -> Response:
    pass
