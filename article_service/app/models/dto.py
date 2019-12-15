# Standard library
from typing import Dict, Any
from dataclasses import dataclass
from datetime import datetime

# 3rd party modules
from werkzeug.exceptions import BadRequest


@dataclass
class CreateUrlDTO:
    id: str
    url: str
    yearmonth: str
    undesired_url: bool

    @classmethod
    def fromdict(cls, raw: Dict[str, Any]) -> "CreateUrlDTO":
        id = raw["id"]
        url = raw["url"]
        yearmonth = raw["yearmonth"]
        undesired_url = raw["undesired_url"]
        if not (
            isinstance(id, str)
            and isinstance(url, str)
            and isinstance(yearmonth, str)
            and isinstance(undesired_url, bool)
        ):
            raise BadRequest("Incorrect type on incoming values")
        return cls(
            id=id,
            url=url,
            yearmonth=yearmonth,
            undesired_url=undesired_url,
        )


@dataclass
class UrlDTO:
    url_id: str
    url: str
    yearmonth: str
    undesired_url: bool
    payed_content: bool
    scraped_at: datetime
    created_at: datetime

    def todict(self) -> Dict[str, Any]:
        return dict(
            url_id=self.url_id,
            url=self.url,
            yearmonth=self.yearmonth,
            undesired_url=self.undesired_url,
            payed_content=self.payed_content,
            scraped_at=self.scraped_at,
            created_at=self.created_at
        )
