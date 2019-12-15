from datetime import datetime
from article_service.app import db


class Url(db.Model):
    __tablename__ = "Urls"
    id: str = db.Column(db.String(6), primary_key=True)
    url: str = db.Column(db.String(200), nullable=False, unique=True)
    yearmonth: str = db.Column(db.String(6), nullable=False)
    payed_content: bool = db.Column(db.Boolean, nullable=False, default=False)
    undesired_url: bool = db.Column(db.Boolean, nullable=False, default=False)
    scraped_at: datetime = db.Column(db.DateTime, nullable=True)
    created_at: datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
        )

    def __repr__(self) -> str:
        return (
            f"Url(id={self.id} "
            f"url={self.url} "
            f"yearmonth={self.yearmonth} "
            f"payed_content={self.payed_content} "
            f"undesired_url={self.undesired_url} "
            f"scraped_at={self.scraped_at} "
            f"created_at={self.created_at})"
        )