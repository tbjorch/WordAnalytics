from dataclasses import dataclass
from datetime import datetime
import json


@dataclass
class AddUrlDTO:
    id: str
    url: str
    yearmonth: str
    undesired_url: bool

    def to_json(self) -> str:
        return json.dumps(
            dict(
                id=self.id,
                url=self.url,
                yearmonth=self.yearmonth,
                undesired_url=self.undesired_url
            )
        )


@dataclass
class ArticleDTO:
    id: str
    headline: str
    body: str

    def to_json(self) -> str:
        return json.dumps(
            dict(
                id=self.id,
                headline=self.headline,
                body=self.body,
            )
        )


@dataclass
class UrlDTO:
    id: str
    url: str
    yearmonth: str
    payed_content: bool
    undesired_url: bool
    scraped_at: datetime
    created_at: datetime
