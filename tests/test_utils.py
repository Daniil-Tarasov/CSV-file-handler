from src.utils import calculate_average_gdp


def test_calculate_average_gdp():
    country_gdps = {
        "US": [25000, 23000],
        "China": [18000, 17700]
    }
    avgs = calculate_average_gdp(country_gdps)
    assert len(avgs) == 2
    assert avgs[0][0] == "US"
    assert avgs[0][1] == 24000.0
    assert avgs[1][1] == 17850.0
