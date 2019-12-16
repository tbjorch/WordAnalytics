from article_service.app import app
from flask import Response
from article_service.app.controller import url as controller


@app.route('/v1/urls', methods=['GET'])
def get_all_urls() -> Response:
    return Response("Hello from urls", 200)


@app.route('/v1/urls/<id>', methods=['GET'])
def get_url(id: str) -> Response:
    return controller.get_url_by_id(id)


@app.route('/v1/urls/unscraped', methods=['GET'])
def get_unscraped_urls() -> Response:
    return controller.get_unscraped_urls()


@app.route('/v1/urls/<id>/unscraped', methods=['PUT'])
def update_unscraped_urls(id: str) -> Response:
    return controller.set_url_to_scraped(id)


@app.route('/v1/urls', methods=['POST'])
def post_url() -> Response:
    return controller.create_url()


@app.route('/v1/urls/<id>', methods=['DELETE'])
def delete_url() -> Response:
    pass
