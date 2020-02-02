# Standard library
import json

# Internal modules
from user_service.tests import CustomTestClient
from user_service.app import db
from user_service.app.models import User


def test_healthcheck() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/health')
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "ok"


def test_get_all_users_existing() -> None:
    with CustomTestClient() as c:
        user1 = User(name="John Doe")
        db.session.add(user1)
        db.session.commit()
        res = c.get('/v1/users')
        data = res.get_json()
        assert res.status_code == 200
        assert data[0]["id"] == 1
        assert data[0]["name"] == "John Doe"


def test_get_all_users_nonexisting() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/users')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No users exist in the database"


def test_get_user_by_id_correct() -> None:
    with CustomTestClient() as c:
        user1 = User(name="John Doe")
        db.session.add(user1)
        db.session.commit()
        res = c.get(f'/v1/users/{1}')
        assert res.status_code == 200
        data = res.get_json()
        assert data["name"] == "John Doe"


def test_get_user_by_id_nonexisting() -> None:
    with CustomTestClient() as c:
        res = c.get(f'/v1/users/{123}')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No user exist with the provided id"


def test_get_user_by_id_badrequest() -> None:
    with CustomTestClient() as c:
        res = c.get(f'/v1/users/asdqwe')
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "User id is expected in numerical form"


def test_post_user_correct() -> None:
    with CustomTestClient() as c:
        user = {"name": "Jane Dane"}
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
        )
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "User successfully created"


def test_post_user_badrequest() -> None:
    with CustomTestClient() as c:
        user = {"name": True}
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_user_badrequest2() -> None:
    with CustomTestClient() as c:
        user = {"qwe": "asd"}
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Required field name is missing in request body"


def test_post_user_badrequest3() -> None:
    with CustomTestClient() as c:
        user = {"name": "asd123"}
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Name should only consist of alphabetic characters"


def test_delete_user_correct() -> None:
    with CustomTestClient() as c:
        user = User(name="Jane Dane")
        db.session.add(user)
        db.session.commit()
        db_entry = User.query.all()
        assert len(db_entry) == 1
        assert db_entry[0].name == "Jane Dane"
        res = c.delete("/v1/users/1")
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "User successfully deleted"


def test_delete_user_nonexisting() -> None:
    with CustomTestClient() as c:
        res = c.delete("/v1/users/1")
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No user exist with the provided id"
