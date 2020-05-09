# Standard library
from typing import List

# 3rd party modules
from werkzeug.exceptions import NotFound, BadRequest
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Internal modules
from user_service.app.models.dto import UserDTO, CreateUserDTO, CredentialsDTO
from user_service.app.repository import user_repo as repo
from user_service.app.models.User import User
from user_service.utils.auth import create_jwt_token


def get_all_users() -> List[UserDTO]:
    users: List[User] = repo.find_all()
    if len(users) == 0:
        raise NotFound("No users exist in the database")
    return [
        UserDTO(
            id=user.id,
            username=user.username,
            created_at=user.created_at
            ) for user in users
            ]


def get_user_by_id(id: int) -> UserDTO:
    user = _assert_user_exist(id)
    return UserDTO(
        id=user.id,
        username=user.username,
        created_at=user.created_at
    )


def create_user(user: CreateUserDTO) -> None:
    _assert_valid_username(user.username)
    _assert_valid_password(user.password)
    _assert_password_match(user.password, user.rep_password)
    pw_hash: str = _hash_password(user.password)
    user_record = User(username=user.username, password_hash=pw_hash)
    repo.save(user_record)


def login(credentials: CredentialsDTO) -> None:
    try:
        user = _assert_user_exist_by_username(credentials.username)
        _verify_password(credentials)
        return create_jwt_token(user.id, user.username)
    except VerifyMismatchError:
        raise BadRequest("Username or password don't match")
    except NotFound:
        raise BadRequest("Username or password don't match")


def delete_user(id: int) -> None:
    user = _assert_user_exist(id)
    repo.delete(user)


def _assert_user_exist(id: int) -> User:
    user = repo.find_by_id(id)
    if user is None:
        raise NotFound("No user exist with the provided id")
    return user


def _assert_user_exist_by_username(username: str) -> User:
    user = repo.find_by_username(username)
    if user is None:
        raise NotFound("No user exist with the provided username")
    return user


def _assert_valid_username(username: str) -> None:
    for part in username.split():
        if not part.isalnum():
            raise BadRequest(
                "Username should only consist of alphanumeric characters"
                )


def _hash_password(raw_pw: str) -> str:
    ph = PasswordHasher()
    return ph.hash(raw_pw)


def _verify_password(credentials: CredentialsDTO) -> None:
    user = repo.find_by_username(credentials.username)
    ph = PasswordHasher()
    ph.verify(user.password_hash, credentials.password)
    if ph.check_needs_rehash(user.password_hash):
        repo.update_pw_hash(user, ph.hash(credentials.password))


def _assert_valid_password(pw: str) -> None:
    _assert_spec_char_in_string(pw)
    _assert_number_char_in_string(pw)
    _assert_upper_char_in_string(pw)
    _assert_lower_char_in_string(pw)
    if len(pw) < 8:
        raise BadRequest("Password length must be atleast 8 characters")


def _assert_spec_char_in_string(pw: str) -> None:
    special_characters: str = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    for char in pw:
        if char in special_characters:
            return
    raise BadRequest("Missing special character in password")


def _assert_upper_char_in_string(pw: str) -> None:
    for char in pw:
        if char.isupper():
            return
    raise BadRequest("Missing uppercase character in password")


def _assert_lower_char_in_string(pw: str) -> None:
    for char in pw:
        if char.islower():
            return
    raise BadRequest("Missing lowercase character in password")


def _assert_number_char_in_string(pw: str) -> None:
    for char in pw:
        if char.isnumeric():
            return
    raise BadRequest("Missing numeric character in password")


def _assert_password_match(pw1, pw2) -> None:
    if not (pw1 == pw2):
        raise BadRequest("Passwords do not match")
