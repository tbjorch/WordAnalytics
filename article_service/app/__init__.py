# Standard library
import json
import os

# Third party modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db_host: str = os.environ["PGDB_URI"]
db_port: str = os.environ["PGDB_PORT"]
db_user: str = os.environ["PGDB_USER"]
db_pw: str = os.environ["PGDB_PW"]
db_name: str = os.environ["PGDB_DB_NAME"]
db_conn_str: str = \
    f"postgresql://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}"

#  f"postgresql://root:asd123@localhost:5432/articleservice"
app.config["SQLALCHEMY_DATABASE_URI"] = db_conn_str
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


import article_service.app.routes


@app.errorhandler(HTTPException)
def exception_handler(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
