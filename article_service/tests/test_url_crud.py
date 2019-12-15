# Standard library
import json

# Internal modules
from article_service.app import app, db
from article_service.app.models import Url



def test_health_endpoint() -> None:
    with app.test_client() as c:
        res = c.get('/v1/health')
        data = res.get_json()
        assert res.status_code == 200
        assert data["message"] == "ok"


def test_post_url_correct() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": "201912",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        data = res.get_json()
        assert res.status_code == 200
        assert data["message"] == "ok"


def test_post_url_invalid_type_url() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": 123,
                "yearmonth": "201912",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        data = res.get_json()
        assert res.status_code == 400
        assert data["description"] == "Incorrect type on incoming values"


def test_post_url_invalid_type_id() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": 123,
                "url": "www.test.org",
                "yearmonth": "201912",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        data = res.get_json()
        assert res.status_code == 400
        assert data["description"] == "Incorrect type on incoming values"


def test_post_url_invalid_type_yearmonth() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": 123,
                "undesired_url": True
                }),
            content_type="application/json"
            )
        data = res.get_json()
        assert res.status_code == 400
        assert data["description"] == "Incorrect type on incoming values"


def test_post_url_invalid_type_undesired_url() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": 123,
                "yearmonth": "201912",
                "undesired_url": "True"
                }),
            content_type="application/json"
            )
        data = res.get_json()
        assert res.status_code == 400
        assert data["description"] == "Incorrect type on incoming values"


def test_post_url_yearmonth_before_2000() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": "199912",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Year value cannot be earlier than 2000"


def test_post_url_yearmonth_future_year() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": "210012",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Year value cannot be in the future"


def test_post_url_yearmonth_invalid_month() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": "201013",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Value must be in interval 1-12"


def test_post_url_yearmonth_too_short_value() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/urls',
            data=json.dumps({
                "id": "asd123",
                "url": "www.test.org",
                "yearmonth": "20101",
                "undesired_url": True
                }),
            content_type="application/json"
            )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Yearmonth value must be 6 characters length in format YYYYMM"


def test_get_url_correct():
    url1 = Url(
        id="abc123",
        url="www.test1.org",
        yearmonth="201912",
        undesired_url=True,
    )
    url2 = Url(
        id="qwe987",
        url="www.test2.net",
        yearmonth="200506",
        undesired_url=False,
        payed_content=True,
    )
    db.session.add(url1)
    db.session.add(url2)
    db.session.commit()

    with app.test_client() as c:
        res = c.get('/v1/urls/abc123')
        data = res.get_json()
        assert data["url_id"] == "abc123"
        assert data["url"] == "www.test1.org"
        assert data["yearmonth"] == "201912"
        assert data["undesired_url"] is True
        assert data["payed_content"] is False
        assert res.status_code == 200

        res2 = c.get('/v1/urls/qwe987')
        data = res2.get_json()
        assert data["url_id"] == "qwe987"
        assert data["url"] == "www.test2.net"
        assert data["yearmonth"] == "200506"
        assert data["undesired_url"] is False
        assert data["payed_content"] is True
        assert res.status_code == 200


def test_get_url_nonexisting():
    with app.test_client() as c:
        res = c.get('/v1/urls/nonexisting')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No url exist with the provided id"
