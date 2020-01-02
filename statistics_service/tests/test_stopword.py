# Internal modules
from statistics_service.tests import CustomTestClient
from statistics_service.app.repository import stopword_repo
from statistics_service.utils.initiate_stopword_db import (
    load_stopwords_into_db
)


def test_adding_initial_stopwords() -> None:
    with CustomTestClient():
        load_stopwords_into_db()
        stopwords = stopword_repo.find_all()
        assert len(stopwords) == 518
