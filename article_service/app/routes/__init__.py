from article_service.app import app
import article_service.app.routes.articles
import article_service.app.routes.urls
from flask import make_response, jsonify


@app.route('/v1/health')
def hello_world():
    data = {"message": "ok"}
    return make_response(jsonify(data), 200)
