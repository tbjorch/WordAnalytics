# Standard library
from typing import List

# 3rd party modules
from werkzeug.exceptions import NotFound, BadRequest

# Internal modules
from user_service.app.models.dto import UserDTO, CreateUserDTO
from user_service.app.repository import user_repo as repo
from user_service.app.models.User import User


def get_all_users() -> List[UserDTO]:
    users: List[User] = repo.find_all()
    if len(users) == 0:
        raise NotFound("No users exist in the database")
    return [
        UserDTO(
            id=user.id,
            name=user.name,
            created_at=user.created_at
            ) for user in users
            ]


def get_user_by_id(id: int) -> UserDTO:
    user = _assert_user_exist(id)
    return UserDTO(
        id=user.id,
        name=user.name,
        created_at=user.created_at
    )


def create_user(user: CreateUserDTO) -> None:
    _assert_valid_name(user.name)
    user_record = User(name=user.name)
    print("Hello")
    repo.save(user_record)


def delete_user(id: int) -> None:
    user = _assert_user_exist(id)
    repo.delete(user)


def _assert_user_exist(id: int) -> User:
    user = repo.find_by_id(id)
    if user is None:
        raise NotFound("No user exist with the provided id")
    return user


def _assert_valid_name(name: str) -> None:
    for part in name.split():
        if not part.isalpha():
            raise BadRequest(
                "Name should only consist of alphabetic characters"
                )
