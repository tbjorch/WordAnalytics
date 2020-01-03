# Standard library
from collections import Counter

# Internal modules
from statistics_service.tests.rpc_mock import (
    mock_get_200_short,
    mock_post_200,
    mock_post_400,
    mock_put_200,
    mock_get_400,
    mock_get_404
)
from statistics_service.app.service.calculator_service import (
    calculate_monthstats
)
from statistics_service.app.service.cleansing_service import (
    _create_wordlist,
    _remove_stop_words
)
from statistics_service.tests import CustomTestClient
from statistics_service.utils.initiate_stopword_db import (
    load_stopwords_into_db
)

# 3rd party modules
import requests

test_text = "Det 1 här ? är 2938 . - polisen"


def test_create_word_list() -> None:
    expected = ["det", "här", "är", "polisen"]
    actual = _create_wordlist(test_text)
    assert actual == expected


def test_remove_stop_words() -> None:
    with CustomTestClient():
        load_stopwords_into_db()
        expected = ["polisen"]
        c: Counter = _remove_stop_words(
            Counter(["det", "här", "är", "polisen"])
        )
        assert list(c.keys()) == expected


def test_calculator_service(monkeypatch) -> None:
    with CustomTestClient():
        load_stopwords_into_db()
        monkeypatch.setattr(requests, "get", mock_get_200_short)
        stats = calculate_monthstats("201912")
        assert stats.article_count == 3
        assert stats.word_mean == 17
        assert stats.word_median == 19


def test_initiating_calculator_service(monkeypatch) -> None:
    with CustomTestClient() as c:
        load_stopwords_into_db()
        monkeypatch.setattr(requests, "get", mock_get_200_short)
        monkeypatch.setattr(requests, "post", mock_post_200)
        monkeypatch.setattr(requests, "put", mock_put_200)
        res = c.get('/v1/statistics/monthstats/201912')
        assert res.status_code == 200
        data = res.get_json()
        assert data["message"] == "Monthstat record successfully added"


def test_initiating_calculator_service_bad_request_getting_article_data(monkeypatch) -> None:
    with CustomTestClient() as c:
        load_stopwords_into_db()
        monkeypatch.setattr(requests, "get", mock_get_400)
        res = c.get('/v1/statistics/monthstats/201912')
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Bad request message"


def test_initiating_calculator_service_bad_request_posting_monthstat_data(monkeypatch) -> None:
    with CustomTestClient() as c:
        load_stopwords_into_db()
        monkeypatch.setattr(requests, "get", mock_get_200_short)
        monkeypatch.setattr(requests, "post", mock_post_400)
        res = c.get('/v1/statistics/monthstats/201912')
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Bad request message"


def test_initiating_calculator_service_not_found(monkeypatch) -> None:
    with CustomTestClient() as c:
        load_stopwords_into_db()
        monkeypatch.setattr(requests, "get", mock_get_404)
        res = c.get('/v1/statistics/monthstats/201912')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == "No articles exist for the provided yearmonth"
