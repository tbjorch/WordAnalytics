from datetime import datetime
from article_service.app import db


class Article(db.Model):
    __tablename__ = "Articles"
    id: str = db.Column(
        db.String(6),
        db.ForeignKey("Urls.id"),
        primary_key=True
        )
    headline: str = db.Column(db.String(300), nullable=False)
    body: str = db.Column(db.Text, nullable=False)
    created_at: datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)
