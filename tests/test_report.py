from unittest.mock import patch

from src.report import generate_average_gdp_report, generate_report


SAMPLE_DATA = {
    'United States': [25462, 23315, 22994],
    'China': [17963, 17734, 17734],
    'Germany': [4086, 4072, 4257]
}


def test_generate_average_gdp_report_valid_data():
    """Тест с валидными данными."""
    with patch('src.report.calculate_average_gdp') as mock_calc:
        mock_calc.return_value = [
            ('United States', 23923.67),
            ('China', 18110.33),
            ('Germany', 4138.33)
        ]

        result = generate_average_gdp_report(SAMPLE_DATA)

    assert "country" in result
    assert "gdp" in result
    assert "United States" in result
    assert "23923.67" in result


def test_generate_report_valid_type():
    """Тест валидного типа отчета."""
    with patch('src.report.generate_average_gdp_report') as mock_report:
        mock_report.return_value = "ТЕСТ ТАБЛИЦА"

        result = generate_report(SAMPLE_DATA, "average-gdp")

    assert result == "ТЕСТ ТАБЛИЦА"
    mock_report.assert_called_once_with(SAMPLE_DATA)


def test_generate_report_invalid_type():
    """Тест несуществующего типа отчета."""
    result = generate_report(SAMPLE_DATA, "nonexistent")
    expected = "Отчет 'nonexistent' не реализован. Доступно: ['average-gdp']"
    assert result == expected
