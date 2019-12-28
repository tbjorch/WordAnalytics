# Standard library
import json

# Internal modules
from article_service.app import app, db
from article_service.app.models import Url


def test_post_article_correct() -> None:
    url = Url(
        id="abc123",
        url="test",
        yearmonth="201910",
        undesired_url=False
    )
    db.session.add(url)
    db.session.commit()
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": "abc123",
                "body": "This is my article body text",
                "headline": "Breaking News!!"
            }),
            content_type="application/json"
        )
        assert res.status_code == 200
    db.session.delete(url)
    db.session.commit()


def test_post_article_non_existing_corresponding_url() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": "abc123",
                "body": "This is my article body text",
                "headline": "Breaking News!!"
            }),
            content_type="application/json"
        )
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No url exist with the provided id"


def test_post_article_invalid_type_id() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": 123,
                "body": "This is my article body text",
                "headline": "Breaking News!!"
            }),
            content_type="application/json"
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_article_invalid_type_body() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": 123,
                "body": "This is my article body text",
                "headline": "Breaking News!!"
            }),
            content_type="application/json"
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_article_invalid_type_headline() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": 123,
                "body": "This is my article body text",
                "headline": "Breaking News!!"
            }),
            content_type="application/json"
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_article_too_many_fields() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": "123",
                "body": "This is my article body text",
                "headline": "Breaking News!!",
                "extrafield": "should not be allowed",
            }),
            content_type="application/json"
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Expected 3 fields but got 4"


def test_post_article_not_json() -> None:
    with app.test_client() as c:
        res = c.post(
            '/v1/articles',
            data=json.dumps({
                "id": "123",
                "body": "This is my article body text",
                "headline": "Breaking News!!",
                "extrafield": "should not be allowed",
            })
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == \
            "Posted data is expected to be in JSON format"
