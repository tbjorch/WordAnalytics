# Standard library
from datetime import datetime

# Internal modules
from user_service.app import db


class Role(db.Model):
    __tablename__ = "Roles"
    id: int = db.Column(db.Integer, primary_key=True)
    role_name: str = db.Column(db.String(50), nullable=False)
    created_at: datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)
