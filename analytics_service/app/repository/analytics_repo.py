from analytics_service.app import db
from analytics_service.app.models import MonthStats
from analytics_service.app.models.dto import MonthStatsDTO


def get_monthdata(YYYYmm: str) -> MonthStatsDTO:
    data = MonthStats.query.filter_by(yearmonth=YYYYmm).first()
    dto = MonthStatsDTO(
        yearmonth=data.yearmonth,
        article_count=data.articleCount,
        word_mean=data.wordMean,
        word_median=data.wordMedian
    )
    return dto
