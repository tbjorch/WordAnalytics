# standard library
import json

# Internal modules
from user_service.utils.auth import create_jwt_token, decode_jwt_token
from user_service.tests import CustomTestClient
from user_service.app.models import User
from user_service.app import db


def test_token() -> None:
    token: bytes = create_jwt_token(1, "JohnnyBravo")
    assert isinstance(token, bytes)
    decoded_token = decode_jwt_token(token)
    print(decoded_token[2])
    assert decoded_token == (1, "JohnnyBravo", None)


def test_authorization_correct() -> None:
    user = User(id=1, username="Jane", password_hash="asd")
    with CustomTestClient() as c:
        db.session.add(user)
        db.session.commit()
        token: bytes = create_jwt_token(1, "Jane", ["ADMIN"])
        payload = dict(roles=["ADMIN"])
        res = c.post(
            '/v1/authorize',
            data=json.dumps(payload),
            content_type="application/json",
            headers={"Authorization": token})
        assert res.status_code == 200
        data = res.get_json()
        print(data)
        assert data["status_code"] == 200
        assert data["message"] == "User is authorized"


def test_authorization_unauthorized() -> None:
    user = User(id=1, username="Jane", password_hash="asd")
    with CustomTestClient() as c:
        db.session.add(user)
        db.session.commit()
        token: bytes = create_jwt_token(1, "Jane", ["USER"])
        payload = dict(roles=["ADMIN"])
        res = c.post(
            '/v1/authorize',
            data=json.dumps(payload),
            content_type="application/json",
            headers={"Authorization": token})
        assert res.status_code == 200
        data = res.get_json()
        assert data["status_code"] == 401
        assert data["message"] == "User is unauthorized"
