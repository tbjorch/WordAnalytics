# Standard library
import json
from datetime import datetime

# Internal modules
from article_service.app import db
from article_service.app.models import Url
from article_service.tests import CustomTestClient


def test_health_endpoint() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/health')
        data = res.get_json()
        assert res.status_code == 200
        assert data["message"] == "ok"


def test_post_url_correct() -> None:
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
        assert data["description"] == \
            "Yearmonth value must be 6 characters length in format YYYYMM"


def test_get_url_by_id_correct() -> None:
    with CustomTestClient() as c:
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


def test_get_url_nonexisting() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/urls/nonexisting')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No url exist with the provided id"


def test_get_urls_unscraped_correct() -> None:
    with CustomTestClient() as c:
        url1 = Url(
            id="abc123",
            url="www.test1.org",
            yearmonth="201912",
            undesired_url=True,
            scraped_at=datetime.utcnow()
        )
        url2 = Url(
            id="qwe987",
            url="www.test2.net",
            yearmonth="201912",
            undesired_url=False,
            payed_content=False,
        )
        url3 = Url(
            id="try345",
            url="another.test3.com",
            yearmonth="200503",
            undesired_url=False,
            payed_content=False,
        )
        db.session.add(url1)
        db.session.add(url2)
        db.session.add(url3)
        db.session.commit()
        res = c.get('/v1/urls/unscraped')
        assert res.status_code == 200
        data = res.get_json()
        assert len(data) == 2
        assert data[0]["url_id"] == "qwe987"
        assert data[0]["url"] == "www.test2.net"
        assert data[0]["yearmonth"] == "201912"
        assert data[1]["url_id"] == "try345"
        assert data[1]["url"] == "another.test3.com"
        assert data[1]["yearmonth"] == "200503"


def test_get_urls_unscraped_not_found() -> None:
    with CustomTestClient() as c:
        res = c.get('/v1/urls/unscraped')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No unscraped Urls in the database"


def test_put_urls_unscraped_correct() -> None:
    with CustomTestClient() as c:
        url = Url(
            id="abc123",
            url="www.test1.org",
            yearmonth="201912"
        )
        db.session.add(url)
        db.session.commit()
        assert Url.query.filter_by(id="abc123").first().scraped_at is None
        time_scraped = datetime.utcnow()
        res = c.put(
            '/v1/urls/abc123/unscraped',
            data=json.dumps({
                "scraped_at": time_scraped.__str__(),
                }),
            content_type="application/json"
            )
        assert res.status_code == 200
        record = Url.query.filter_by(id="abc123").first()
        assert record.scraped_at == time_scraped


def test_put_urls_unscraped_nonexisting_url() -> None:
    with CustomTestClient() as c:
        time_scraped = datetime.utcnow()
        res = c.put(
            '/v1/urls/abc123/unscraped',
            data=json.dumps({
                "scraped_at": time_scraped.__str__(),
                }),
            content_type="application/json"
            )
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No url exist with the provided id"


def test_get_urls_by_yearmonth() -> None:
    with CustomTestClient() as c:
        url1 = Url(
            id="abc123",
            url="www.test1.org",
            yearmonth="201912",
            undesired_url=True,
            scraped_at=datetime.utcnow()
        )
        url2 = Url(
            id="qwe987",
            url="www.test2.net",
            yearmonth="201912",
            undesired_url=False,
            payed_content=False,
        )
        url3 = Url(
            id="try345",
            url="another.test3.com",
            yearmonth="200503",
            undesired_url=False,
            payed_content=False,
        )
        db.session.add(url1)
        db.session.add(url2)
        db.session.add(url3)
        db.session.commit()
        res = c.get('/v1/urls/yearmonth/201912')
        assert res.status_code == 200
        data = res.get_json()
        assert len(data) == 2
        assert data[0]["url_id"] == "abc123"
        assert data[0]["url"] == "www.test1.org"
        assert data[0]["yearmonth"] == "201912"
        assert data[1]["url_id"] == "qwe987"
        assert data[1]["url"] == "www.test2.net"
        assert data[1]["yearmonth"] == "201912"
