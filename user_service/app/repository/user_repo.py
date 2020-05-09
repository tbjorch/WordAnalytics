# Standard library
from typing import List

# Internal modules
from user_service.app.models.User import User
from user_service.app import db


def find_all() -> List[User]:
    return User.query.all()


def find_by_id(id: int) -> User:
    return User.query.filter_by(id=id).first()


def find_by_username(username: str) -> User:
    return User.query.filter_by(username=username).first()


def save(user: User) -> None:
    db.session.add(user)
    db.session.commit()


def update_pw_hash(user: User, hash: str) -> None:
    user.password_hash = hash
    save(user)


def delete(user: User) -> None:
    db.session.delete(user)
    db.session.commit()
