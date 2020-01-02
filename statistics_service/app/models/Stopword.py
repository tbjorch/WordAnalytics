# Standard library
from datetime import datetime

# Internal modules
from statistics_service.app import db


class Stopword(db.Model):
    __tablename__ = "stopwords"
    id: int = db.Column(
        db.Integer,
        primary_key=True
    )
    word: str = db.Column(
        db.String(20),
        nullable=False
    )
    created_at: datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
