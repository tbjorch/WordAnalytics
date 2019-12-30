# Standard library
import json
from datetime import datetime

# Internal modules
from article_service.app import db
from article_service.app.models import Url, Article
from article_service.tests import CustomTestClient


def test_post_article_correct() -> None:
    with CustomTestClient() as c:
        url = Url(
            id="abc123",
            url="test",
            yearmonth="201910",
            undesired_url=False
        )
        db.session.add(url)
        db.session.commit()
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


def test_post_article_non_existing_corresponding_url() -> None:
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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
    with CustomTestClient() as c:
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


def test_get_article_by_id_correct() -> None:
    with CustomTestClient() as c:
        url = Url(
            id="qaz987",
            url="test",
            yearmonth="201910",
            undesired_url=False
        )
        article = Article(
            id="qaz987",
            headline="This is my headline",
            body="This is a body text to my article in this test.",
            created_at=datetime.utcnow()
        )
        db.session.add(url)
        db.session.add(article)
        db.session.commit()
        article_id = "qaz987"
        res = c.get(f'/v1/articles/id/{article_id}')
        assert res.status_code == 200
        data = res.get_json()
        assert data["article_id"] == "qaz987"
        assert data["headline"] == "This is my headline"
        assert data["body"] == \
            "This is a body text to my article in this test."
        assert data["created_at"] == article.created_at.__str__()


def test_get_article_by_id_not_found() -> None:
    with CustomTestClient() as c:
        article_id = "askdkf"
        res = c.get(f'/v1/articles/id/{article_id}')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No article exist with the provided id"


def test_get_articles_by_yearmonth_correct() -> None:
    with CustomTestClient() as c:
        url_1 = Url(
            id="qaz987",
            url="test",
            yearmonth="201910",
            undesired_url=False
        )
        article_1 = Article(
            id="qaz987",
            headline="This is my headline",
            body="This is a body text to my article in this test.",
            created_at=datetime.utcnow()
        )
        url_2 = Url(
            id="abc123",
            url="test2",
            yearmonth="201911",
            undesired_url=False
        )
        article_2 = Article(
            id="abc123",
            headline="This is my headline for another article",
            body="This is a body text to my other article that i want to find",
            created_at=datetime.utcnow()
        )
        url_3 = Url(
            id="uhn768",
            url="test3",
            yearmonth="201910",
            undesired_url=False
        )
        article_3 = Article(
            id="uhn768",
            headline="This",
            body="This is a body text.",
            created_at=datetime.utcnow()
        )
        db.session.add(url_1)
        db.session.add(url_2)
        db.session.add(url_3)
        db.session.add(article_1)
        db.session.add(article_2)
        db.session.add(article_3)
        db.session.commit()
        res = c.get(f'/v1/articles/yearmonth/201910')
        assert res.status_code == 200
        data = res.get_json()
        assert data[0]["article_id"] == "qaz987"
        assert data[0]["headline"] == "This is my headline"
        assert data[0]["body"] == \
            "This is a body text to my article in this test."
        assert data[0]["created_at"] == article_1.created_at.__str__()
        assert data[1]["article_id"] == "uhn768"
        assert data[1]["headline"] == "This"
        assert data[1]["body"] == "This is a body text."
        assert data[1]["created_at"] == article_3.created_at.__str__()


def test_get_articles_by_yearmonth_not_found() -> None:
    with CustomTestClient() as c:
        res = c.get(f'/v1/articles/yearmonth/201910')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == \
            "No articles exist for the provided yearmonth"
