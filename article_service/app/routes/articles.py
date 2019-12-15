from article_service.app import app


@app.route('/v1/articles', methods=['GET'])
def get_article():
    return "Hi from Articles"


@app.route('/v1/articles', methods=['POST'])
def post_article():
    pass


@app.route('/v1/articles/<id>', methods=['DELETE'])
def delete_article():
    pass
