# 3rd party modules
import flask

# Internal modules
from article_service.app import app
from article_service.app.controller import article as controller
from utils import ok_response


@app.route('/v1/articles/yearmonth/<yearmonth>', methods=['GET'])
def get_article_by_yearmonth(yearmonth: str) -> flask.Response:
    return controller.get_articles_by_yearmonth(yearmonth)


@app.route('/v1/articles/id/<id>', methods=['GET'])
def get_article_by_id(id: str) -> flask.Response:
    return controller.get_article_by_id(id)


@app.route('/v1/articles', methods=['POST'])
def post_article():
    controller.create_article()
    return ok_response()


@app.route('/v1/articles/<id>', methods=['DELETE'])
def delete_article():
    pass
