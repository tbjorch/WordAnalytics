# 3rd party modules
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from werkzeug.exceptions import Forbidden

# Internal modules
from article_service.app import db
from article_service.app.models import MonthStats
from article_service.app.models.dto import MonthStatsDTO


def get_monthdata(YYYYmm: str) -> MonthStatsDTO:
    data: MonthStats = MonthStats.query.filter_by(yearmonth=YYYYmm).first()
    if data:
        dto: MonthStatsDTO = MonthStatsDTO(
            yearmonth=data.yearmonth,
            article_count=data.article_count,
            word_mean=data.word_mean,
            word_median=data.word_median
        )
        return dto
    else:
        return None


def insert_monthstats(dto: MonthStatsDTO) -> None:
    data = MonthStats(
        yearmonth=dto.yearmonth,
        article_count=dto.article_count,
        word_mean=dto.word_mean,
        word_median=dto.word_median
    )
    print(data)
    try:
        db.session.add(data)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise Forbidden("Monthstat record already exist. Use PUT request if wanting to update.")
    except FlushError:  # Not sure if this is required because of using sqlite in memory for tests?
        db.session.rollback()
        raise Forbidden("Monthstat record already exist. Use PUT request if wanting to update.")