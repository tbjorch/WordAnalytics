from analytics_service.app import db


class MonthStats(db.Model):
    __tablename__ = "MonthStats"
    yearmonth: str = db.Column(
        db.String(6),
        primary_key=True
        )
    articleCount: int = db.Column(
        db.Integer,
        nullable=True
        )
    wordMean: int = db.Column(
        db.Integer,
        nullable=True
    )
    wordMedian: int = db.Column(
        db.Integer,
        nullable=True
    )
