# Standard library 
import json

# Internal modules
from article_service.app import app, db
from article_service.app.models import MonthStats


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
        article_count=9800,
        word_mean=120,
        word_median=75
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


def test_get_monthstat_data_not_found() -> None:
    with app.test_client() as c:
        res = c.get('/v1/analytics/monthstats/201812')
        assert res.status_code == 404
        data = res.get_json()
        assert data["description"] == \
            "No monthly statistics available for provided yearmonth"


def test_post_monthstat_data_invalid_yearmonth_future() -> None:
    with app.test_client() as c:
        yearmonth = "210012"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=9800,
                    word_mean=200,
                    word_median=80
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Year value cannot be in the future"


def test_post_monthstat_data_invalid_yearmonth_month() -> None:
    with app.test_client() as c:
        yearmonth = "201933"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=9800,
                    word_mean=200,
                    word_median=80
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Value must be in interval 1-12"


def test_post_monthstat_data_missing_json_headers() -> None:
    with app.test_client() as c:
        yearmonth = "201912"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=9800,
                    word_mean=200,
                    word_median=80
                )
            )
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Posted data is expected to be in JSON format"


def test_post_monthstat_data_invalid_type_1() -> None:
    with app.test_client() as c:
        yearmonth = "201912"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count="9800",
                    word_mean=200,
                    word_median=80
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_monthstat_data_invalid_type_2() -> None:
    with app.test_client() as c:
        yearmonth = "201912"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=9800,
                    word_mean="200",
                    word_median=80
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_monthstat_data_invalid_type_3() -> None:
    with app.test_client() as c:
        yearmonth = "201912"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=9800,
                    word_mean=200,
                    word_median="80"
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 400
        data = res.get_json()
        assert data["description"] == "Incorrect type on incoming values"


def test_post_monthstat_data_already_exists() -> None:
    monthstat = MonthStats(
        yearmonth="201909",
        article_count=5000,
        word_mean=140,
        word_median=78
        )
    db.session.add(monthstat)
    db.session.commit()
    with app.test_client() as c:
        yearmonth = "201909"
        res = c.post(
            f'/v1/analytics/monthstats',
            data=json.dumps(
                dict(
                    yearmonth=yearmonth,
                    article_count=7000,
                    word_mean=200,
                    word_median=80
                )
            ),
            headers={'Content-Type': 'application/json'}
        )
        assert res.status_code == 403
        data = res.get_json()
        assert data["description"] == "Monthstat record already exist. Use PUT request if wanting to update."
    db.session.delete(monthstat)
    db.session.commit()
