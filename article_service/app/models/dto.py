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


@dataclass
class SetUrlScrapedDTO:
    url_id: str
    scraped_at: datetime

    @classmethod
    def fromdict(cls, raw: Dict[str, Any], id: str) -> "SetUrlScrapedDTO":
        id = id
        time_scraped = datetime.strptime(
            raw["scraped_at"],
            '%Y-%m-%d %H:%M:%S.%f'
        )
        if not (isinstance(id, str) and isinstance(time_scraped, datetime)):
            raise BadRequest("Incorrect type on incoming values")
        return cls(url_id=id, scraped_at=time_scraped)


@dataclass
class CreateArticleDTO:
    article_id: str
    headline: str
    body: str

    @classmethod
    def fromdict(cls, raw: Dict[str, Any]) -> "CreateArticleDTO":
        article_id = raw["id"]
        headline = raw["headline"]
        body = raw["body"]
        if not(
            isinstance(article_id, str)
            and isinstance(headline, str)
            and isinstance(body, str)
        ):
            raise BadRequest("Incorrect type on incoming values")
        return cls(article_id=article_id, headline=headline, body=body)


@dataclass
class MonthStatsDTO:
    yearmonth: str
    article_count: int
    word_mean: int
    word_median: int

    def to_dict(self) -> Dict:
        return dict(
            yearmonth=self.yearmonth,
            article_count=self.article_count,
            word_mean=self.word_mean,
            word_median=self.word_median
        )

    @classmethod
    def fromdict(cls, raw: Dict[str, Any]) -> "MonthStatsDTO":
        yearmonth = raw["yearmonth"]
        article_count = raw["article_count"]
        word_mean = raw["word_mean"]
        word_median = raw["word_median"]
        if not(
            isinstance(yearmonth, str)
            and isinstance(article_count, int)
            and isinstance(word_mean, int)
            and isinstance(word_median, int)
        ):
            raise BadRequest("Incorrect type on incoming values")
        return cls(
            yearmonth=yearmonth,
            article_count=article_count,
            word_mean=word_mean,
            word_median=word_median
        )