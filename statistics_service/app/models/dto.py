# Standard library
from collections import Counter
from dataclasses import dataclass
from typing import Optional, List
import json


@dataclass
class ArticleDTO:
    id: str
    headline: str
    body: str
    word_count: int
    cleaned_text: Optional[Counter] = None
    cleaned_text_len: int = 0

    def __init__(self, id, headline, body) -> None:
        self.id = id
        self.headline = headline
        self.body = body
        self.word_count = len(self.headline.split()) + len(self.body.split())

    def add_clean_text(self, cleaned_text) -> None:
        self.cleaned_text = cleaned_text
        self.cleaned_text_len = sum(cleaned_text.values())

    def to_json(self) -> str:
        return json.dumps(
            dict(
                id=self.id,
                headline=self.headline,
                body=self.body,
                word_count=self.word_count,
            )
        )


@dataclass
class MonthStatsDTO:
    yearmonth: str
    article_count: int
    word_mean: int
    word_median: int
    top_100_words: Counter

    def to_json(self) -> str:
        return json.dumps(
            dict(
                yearmonth=self.yearmonth,
                article_count=self.article_count,
                word_mean=self.word_mean,
                word_median=self.word_median,
                # top_100_words=self.top_100_words,
            )
        )