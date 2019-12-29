# Standard library
from typing import List, Optional
from datetime import datetime

# Internal modules
from article_service.app.repository import analytics_repo
from article_service.app.models.dto import MonthStatsDTO

# 3rd party modules
from werkzeug.exceptions import BadRequest, NotFound, Forbidden


def most_frequent_words(YYYYmm: str) -> List:
    _assert_valid_yearmonth(YYYYmm)
    pass


def monthly_statistics(YYYYmm: str) -> Optional[MonthStatsDTO]:
    """ Returns number of articles on a given month,
    average number of words in the articles, and median number
    of words in the articles. """
    _assert_valid_yearmonth(YYYYmm)
    data: MonthStatsDTO = analytics_repo.get_monthdata(YYYYmm)
    if data is None:
        raise NotFound(
            "No monthly statistics available for provided yearmonth"
            )
    return data


def create_monthstat_record(dto: MonthStatsDTO) -> None:
    _assert_valid_yearmonth(dto.yearmonth)
    _assert_record_doesnt_exist(dto.yearmonth)
    analytics_repo.insert_monthstats(dto)


def _assert_valid_yearmonth(YYYYmm: str) -> None:
    if len(YYYYmm) != 6:
        raise BadRequest(
            "Yearmonth value must be 6 characters length in format YYYYMM"
            )
    year: int = int(YYYYmm[0:4])
    month: int = int(YYYYmm[4:])
    if year > datetime.utcnow().year:
        raise BadRequest("Year value cannot be in the future")
    if year < 2000:
        raise BadRequest("Year value cannot be earlier than 2000")
    if month not in range(1, 13):
        raise BadRequest("Value must be in interval 1-12")


def _assert_record_doesnt_exist(YYYYmm: str) -> None:
    if analytics_repo.get_monthdata(YYYYmm) is not None:
        raise Forbidden("Monthstat record already exist. Use PUT request if wanting to update.")
