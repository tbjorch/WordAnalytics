# 3rd party modules
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from werkzeug.exceptions import Forbidden

# Internal modules
from article_service.app import db
from article_service.app.models import MonthStats
from article_service.app.models.dto import MonthStatsDTO


def find(YYYYmm: str) -> MonthStats:
    return MonthStats.query.filter_by(yearmonth=YYYYmm).first()


def save(month_stats: MonthStats) -> None:
    db.session.add(month_stats)
    db.session.commit()
