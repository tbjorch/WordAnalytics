# Standard library
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

# 3rd party
from werkzeug.exceptions import BadRequest


@dataclass
class UserDTO:
    id: int
    name: str
    created_at: datetime

    def to_dict(self) -> Dict:
        return(
            dict(
                id=self.id,
                name=self.name,
                created_at=self.created_at
            )
        )


@dataclass
class CreateUserDTO:
    name: str

    @classmethod
    def from_dict(cls, raw: Dict[str, Any]) -> "CreateUserDTO":
        name = raw["name"]
        if not(isinstance(name, str)):
            raise BadRequest("Incorrect type on incoming values")
        return cls(
            name=name
        )
