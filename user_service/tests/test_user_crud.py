# Standard library
import json

# Internal modules
from user_service.tests import CustomTestClient
from user_service.app import db
from user_service.app.models import User
from user_service.utils.auth import create_jwt_token


def test_healthcheck() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/health')
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "ok"


def test_delete_user_correct() -> None:
    user = User(
        id=1,
        username="Jane",
        password_hash="123"
    )
    with CustomTestClient() as c:
        db.session.add(user)
        db.session.commit()
        token: bytes = create_jwt_token(1, "Jane", "ADMIN")
        res = c.delete("/v1/users/1", headers={'Authorization': token})
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "User successfully deleted"


def test_delete_user_nonexisting() -> None:
    user = User(
        id=1,
        username="Jane",
        password_hash="123"
    )
    with CustomTestClient() as c:
        db.session.add(user)
        db.session.commit()
        token: bytes = create_jwt_token(1, "Jane", "ADMIN")
        res = c.delete("/v1/users/2", headers={'Authorization': token})
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No user exist with the provided id"


def test_delete_user_unauthorized() -> None:
    user = User(
        id=1,
        username="Jane",
        password_hash="123"
    )
    with CustomTestClient() as c:
        db.session.add(user)
        db.session.commit()
        token: bytes = create_jwt_token(1, "Jane", "USER")
        res = c.delete("/v1/users/1", headers={'Authorization': token})
        assert res.status_code == 401
        data = res.get_json()
        assert data["description"] == "You don't have permission"


def test_get_all_users_existing() -> None:
    with CustomTestClient() as c:
        user1 = User(username="John Doe", password_hash="qwasdw")
        db.session.add(user1)
        db.session.commit()
        res = c.get('/v1/users')
        data = res.get_json()
        assert res.status_code == 200
        assert data[0]["id"] == 1
        assert data[0]["username"] == "John Doe"


def test_get_all_users_nonexisting() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/users')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No users exist in the database"


def test_get_user_by_id_correct() -> None:
    with CustomTestClient() as c:
        user1 = User(username="John Doe", password_hash="qwasdw")
        db.session.add(user1)
        db.session.commit()
        res = c.get(f'/v1/users/{1}')
        assert res.status_code == 200
        data = res.get_json()
        assert data["username"] == "John Doe"


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
        user = {
            "username": "Jane Dane",
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
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
        user = {
            "username": True,
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
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
        user = {
            "qwe": "asd",
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Required field username is missing in request body"


def test_post_user_badrequest3() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd&/123",
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Username should only consist of alphanumeric characters"


def test_post_user_badrequest_pw_mismatch() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "asd123QW!",
            "rep_password": "asd123QWE!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Passwords do not match"


def test_post_user_badrequest_pw_too_short() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "asd1W!",
            "rep_password": "asd1W!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Password length must be atleast 8 characters"


def test_post_user_badrequest_pw_missing_upper() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "asd1asdas!",
            "rep_password": "asd1asdas!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Missing uppercase character in password"


def test_post_user_badrequest_pw_missing_lower() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "ASD1ASD!",
            "rep_password": "ASD1ASD!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Missing lowercase character in password"


def test_post_user_badrequest_pw_missing_special() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "ASD1ASDq",
            "rep_password": "ASD1ASDq"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Missing special character in password"


def test_post_user_badrequest_pw_missing_number() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "asd123",
            "password": "ASDASDq%",
            "rep_password": "ASDASDq%"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Missing numeric character in password"


def test_user_login_correct() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "Johnny",
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
        )
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "User successfully created"
        res2 = c.post(
            '/v1/login',
            data=json.dumps({"username": "Johnny", "password": "asd123QWE!"}),
            content_type="application/json"
        )
        assert res2.status_code == 200
        assert res2.headers['Authorization'] is not None
        data = res2.get_json()
        assert data["message"] == "Successfully logged in"


def test_user_login_incorrect_pw() -> None:
    with CustomTestClient() as c:
        user = {
            "username": "Johnny",
            "password": "asd123QWE!",
            "rep_password": "asd123QWE!"
            }
        res = c.post(
            '/v1/users',
            data=json.dumps(user),
            content_type="application/json"
        )
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "User successfully created"
        res2 = c.post(
            '/v1/login',
            data=json.dumps({"username": "Johnny", "password": "asd123QWEa"}),
            content_type="application/json"
        )
        assert res2.status_code == 400
        data = res2.get_json()
        assert data["description"] == "Username or password don't match"


def test_user_login_nonexisting_username() -> None:
    with CustomTestClient() as c:
        res2 = c.post(
            '/v1/login',
            data=json.dumps({"username": "qwe", "password": "asd123QWEa"}),
            content_type="application/json"
        )
        assert res2.status_code == 400
        data = res2.get_json()
        assert data["description"] == "Username or password don't match"
