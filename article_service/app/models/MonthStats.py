# Standard library
from dataclasses import dataclass

# Internal modules
from article_service.app import db


@dataclass
class MonthStats(db.Model):
    __tablename__ = "MonthStats"
    yearmonth: str = db.Column(
        db.String(6),
        primary_key=True
        )
    article_count: int = db.Column(
        db.Integer,
        nullable=True
        )
    word_mean: int = db.Column(
        db.Integer,
        nullable=True
    )
    word_median: int = db.Column(
        db.Integer,
        nullable=True
    )
