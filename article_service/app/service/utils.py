# Standard library
from datetime import datetime

# 3rd party modules
from werkzeug.exceptions import BadRequest


def assert_valid_yearmonth(yearmonth: int) -> None:
    if len(yearmonth) != 6:
        raise BadRequest(
            "Yearmonth value must be 6 characters length in format YYYYMM"
            )
    year: int = int(yearmonth[0:4])
    month: int = int(yearmonth[4:])
    if year > datetime.utcnow().year:
        raise BadRequest("Year value cannot be in the future")
    if year < 2000:
        raise BadRequest("Year value cannot be earlier than 2000")
    if month not in range(1, 13):
        raise BadRequest("Value must be in interval 1-12")