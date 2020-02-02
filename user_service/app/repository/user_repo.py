# Standard library
from typing import List

# Internal modules
from user_service.app.models.User import User
from user_service.app import db


def find_all() -> List[User]:
    return User.query.all()


def find_by_id(id: int) -> User:
    return User.query.filter_by(id=id).first()


def save(user: User) -> None:
    db.session.add(user)
    db.session.commit()


def delete(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
