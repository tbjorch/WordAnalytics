# Standard library
from typing import List
from datetime import datetime

# Internal modules
from analytics_service.app.repository import analytics_repo
from analytics_service.app.models.dto import MonthStatsDTO

# 3rd party modules
from werkzeug.exceptions import BadRequest


def most_frequent_words(YYYYmm: str) -> List:
    _assert_valid_yearmonth(YYYYmm)
    print(YYYYmm)
    pass


# Antal artiklar på en månad
# Ord per artikel en månad (median och medel), alt. kolla på
# möjlighet att representera som någon form av histogram el. dylikt
def monthly_statistics(YYYYmm: str) -> MonthStatsDTO:
    """ Returns number of articles on a given month,
    average number of words in the articles, and median number
    of words in the articles. """
    _assert_valid_yearmonth(YYYYmm)
    return analytics_repo.get_monthdata(YYYYmm)


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
