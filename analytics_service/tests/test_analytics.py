# Internal modules
from analytics_service.app import app, db
from analytics_service.app.models import MonthStats


def test_get_yearmonth_data_correct() -> None:
    with app.test_client() as c:
        res = c.get("/v1/analytics/yearmonthdata/201912")
        assert res.status_code == 200


def test_get_yearmonth_data_invalid_month_value_1() -> None:
    with app.test_client() as c:
        res = c.get("/v1/analytics/yearmonthdata/201913")
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Value must be in interval 1-12"


def test_get_yearmonth_data_invalid_month_value_2() -> None:
    with app.test_client() as c:
        res = c.get("/v1/analytics/yearmonthdata/201900")
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Value must be in interval 1-12"


def test_get_yearmonth_data_invalid_year_value_1() -> None:
    with app.test_client() as c:
        res = c.get("/v1/analytics/yearmonthdata/199910")
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Year value cannot be earlier than 2000"


def test_get_yearmonth_data_invalid_year_value_2() -> None:
    with app.test_client() as c:
        res = c.get("/v1/analytics/yearmonthdata/220010")
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Year value cannot be in the future"


def test_get_monthstat_data_correct() -> None:
    monthStat = MonthStats(
        yearmonth="201912",
        articleCount=9800,
        wordMean=120,
        wordMedian=75
        )
    db.session.add(monthStat)
    db.session.commit()

    with app.test_client() as c:
        res = c.get('/v1/analytics/monthstats/201912')
        assert res.status_code == 200
        data = res.get_json()
        print(data)
        assert data["yearmonth"] == "201912"
        assert data["article_count"] == 9800
        assert data["word_mean"] == 120
        assert data["word_median"] == 75
    db.session.delete(monthStat)
    db.session.commit()
