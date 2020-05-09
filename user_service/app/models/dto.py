# Standard library
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

# 3rd party
from werkzeug.exceptions import BadRequest


@dataclass
class UserDTO:
    id: int
    username: str
    created_at: datetime

    def to_dict(self) -> Dict:
        return(
            dict(
                id=self.id,
                username=self.username,
                created_at=self.created_at
            )
        )


@dataclass
class CreateUserDTO:
    username: str
    password: str
    rep_password: str

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "CreateUserDTO":
        username = raw["username"]
        password = raw["password"]
        rep_password = raw["rep_password"]
        if not(
            isinstance(username, str) and
            isinstance(password, str) and
            isinstance(rep_password, str)
        ):
            raise BadRequest("Incorrect type on incoming values")
        return cls(
            username=username,
            password=password,
            rep_password=rep_password
        )


@dataclass
class CredentialsDTO:
    username: str
    password: str

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "CredentialsDTO":
        username = raw["username"]
        password = raw["password"]
        if not(
            isinstance(username, str) and
            isinstance(password, str)
        ):
            raise BadRequest("Incorrect type on incoming values")
        return cls(
            username=username,
            password=password
        )