# Standard library
from typing import List
from statistics import mean, median, stdev
from collections import Counter

# Internal modules
from statistics_service.app.rpc import (
    get_articles_by_yearmonth,
)
from statistics_service.app.service.cleansing_service import clean_text
from statistics_service.app.models.dto import ArticleDTO, MonthStatsDTO


def calculate_monthstats(YYYYmm: str) -> MonthStatsDTO:
    articles: List[ArticleDTO] = get_articles_by_yearmonth(YYYYmm)
    dto_list: List[ArticleDTO] = [clean_text(article) for article in articles]
    word_count_list: List[int] = [dto.word_count for dto in dto_list]
    c: Counter = sum((dto.cleaned_text for dto in dto_list), Counter())
    monthstats: MonthStatsDTO = MonthStatsDTO(
        yearmonth=YYYYmm,
        article_count=len(articles),
        word_mean=int(round(mean(word_count_list))),
        word_median=int(round(median(word_count_list))),
        top_100_words=dict(c.most_common(100))
    )
    return monthstats
