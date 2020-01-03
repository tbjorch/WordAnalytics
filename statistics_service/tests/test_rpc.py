# Standard library
from typing import List
from collections import Counter


# Internal modules
from statistics_service.app.rpc import (
    get_articles_by_yearmonth,
    post_monthstats_to_article_service,
)
from statistics_service.app.models.dto import ArticleDTO, MonthStatsDTO
from statistics_service.tests.rpc_mock import (
    mock_get_200,
    mock_get_400,
    mock_get_404,
    mock_get_500,
    mock_post_200,
    mock_put_200
)
from statistics_service.tests import CustomTestClient

# 3rd party modules
import requests
from pytest import fail
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError


def test_get_articles_by_yearmonth_correct(monkeypatch) -> None:
    with CustomTestClient():
        monkeypatch.setattr(requests, "get", mock_get_200)
        articles: List[ArticleDTO] = get_articles_by_yearmonth("201912")
        assert len(articles) == 10
        assert type(articles[0]) == ArticleDTO


def test_get_articles_by_yearmonth_bad_request(monkeypatch) -> None:
    with CustomTestClient():
        monkeypatch.setattr(requests, "get", mock_get_400)
        try:
            get_articles_by_yearmonth("201912")
        except BadRequest as e:
            assert e.description == "Bad request message"
        except Exception as e:
            print(e)
            fail("Did not get bad request")


def test_get_articles_by_yearmonth_not_found(monkeypatch) -> None:
    with CustomTestClient():
        monkeypatch.setattr(requests, "get", mock_get_404)
        try:
            get_articles_by_yearmonth("201912")
        except NotFound as e:
            assert e.description == \
                "No articles exist for the provided yearmonth"
        except Exception as e:
            print(e)
            fail("Did not get not found")


def test_get_articles_by_yearmonth_ISE(monkeypatch) -> None:
    with CustomTestClient():
        monkeypatch.setattr(requests, "get", mock_get_500)
        try:
            get_articles_by_yearmonth("201912")
        except InternalServerError as e:
            assert e.description == \
                "Internal server error"
        except Exception as e:
            print(e)
            fail("Did not get Internal server error")


def test_post_articles_correct(monkeypatch) -> None:
    with CustomTestClient():
        monkeypatch.setattr(requests, "post", mock_post_200)
        monkeypatch.setattr(requests, "put", mock_put_200)
        try:
            stats = MonthStatsDTO(
                yearmonth="201912",
                article_count=2000,
                word_mean=200,
                word_median=100,
                top_100_words=Counter()
            )
            message = post_monthstats_to_article_service(
                "201912",
                stats
            )
        except Exception as e:
            print(e)
            fail("Did not get bad request")
        assert message == "Monthstat record successfully added"
