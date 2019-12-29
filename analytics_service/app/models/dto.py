# Standard library
from typing import Dict
import json

# Internal modules
from dataclasses import dataclass


@dataclass
class MonthStatsDTO:
    yearmonth: str
    article_count: int
    word_mean: int
    word_median: int

    def to_json(self) -> str:
        return(
            json.dumps(
                self.to_dict()
            )
        )
    
    def to_dict(self) -> Dict:
        return dict(
            yearmonth=self.yearmonth,
            article_count=self.article_count,
            word_mean=self.word_mean,
            word_median=self.word_median
        )
