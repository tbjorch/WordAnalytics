from article_service.app import app
import json


def test_health_endpoint():
    with app.test_client() as c:
        res = c.get('/v1/health')
        data = res.get_json()
        assert res.status_code == 200
        assert data["message"] == "ok"


def test_post_url_correct():
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
        print(data)
        assert res.status_code == 200
        assert data["message"] == "ok"


def test_post_url_yearmonth_before_2000():
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


def test_post_url_yearmonth_future_year():
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


def test_post_url_yearmonth_invalid_month():
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


def test_post_url_yearmonth_too_short_value():
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
