# Standard library
from typing import List
from datetime import datetime

# Internal modules
from article_service.app.repository import analytics_repo
from article_service.app.models.dto import MonthStatsDTO
from article_service.app.models import MonthStats

# 3rd party modules
from werkzeug.exceptions import BadRequest, NotFound, Forbidden


def most_frequent_words(YYYYmm: str) -> List:
    _assert_valid_yearmonth(YYYYmm)
    pass


def monthly_statistics(YYYYmm: str) -> MonthStatsDTO:
    """ Returns number of articles on a given month,
    average number of words in the articles, and median number
    of words in the articles. """
    _assert_valid_yearmonth(YYYYmm)
    data: MonthStats = analytics_repo.find(YYYYmm)
    if data:
        dto: MonthStatsDTO = MonthStatsDTO(
            yearmonth=data.yearmonth,
            article_count=data.article_count,
            word_mean=data.word_mean,
            word_median=data.word_median
        )
        return dto
    else:
        raise NotFound(
            "No monthly statistics available for provided yearmonth"
            )


def create_monthstat_record(dto: MonthStatsDTO) -> None:
    _assert_valid_yearmonth(dto.yearmonth)
    _assert_record_doesnt_exist(dto.yearmonth)
    monthstat = MonthStats(
        yearmonth=dto.yearmonth,
        article_count=dto.article_count,
        word_mean=dto.word_mean,
        word_median=dto.word_median
    )
    analytics_repo.save(monthstat)


def update_monthstat_record(dto: MonthStatsDTO) -> None:
    _assert_valid_yearmonth(dto.yearmonth)
    monthstat_record = _assert_record_exist(dto.yearmonth)
    monthstat_record.article_count = dto.article_count
    monthstat_record.word_mean = dto.word_mean
    monthstat_record.word_median = dto.word_median
    analytics_repo.save(monthstat_record)


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
    if analytics_repo.find(YYYYmm) is not None:
        raise Forbidden(
            f"Monthstat record already exist. "
            f"Use PUT request if wanting to update."
            )


def _assert_record_exist(YYYYmm: str) -> MonthStats:
    monthstat: MonthStats = analytics_repo.find(YYYYmm)
    if monthstat is None:
        raise NotFound("No record available for yearmonth value")
    return monthstat
