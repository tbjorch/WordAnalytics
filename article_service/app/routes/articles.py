from article_service.app import app
from article_service.app.controller import article as controller
from article_service.utils import ok_response


@app.route('/v1/articles', methods=['GET'])
def get_article():
    return "Hi from Articles"


@app.route('/v1/articles', methods=['POST'])
def post_article():
    controller.create_article()
    return ok_response()


@app.route('/v1/articles/<id>', methods=['DELETE'])
def delete_article():
    pass
