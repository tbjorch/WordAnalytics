# Standard library
from datetime import datetime
# from typing import List

# Internal modules
from user_service.app import db
# from user_service.app.models import Role


class User(db.Model):
    __tablename__ = "Users"
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(50), nullable=False, unique=True)
    password_hash: str = db.Column(db.String(100), nullable=False)
    created_at: datetime = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow)
