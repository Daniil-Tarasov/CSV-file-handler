from unittest.mock import patch, mock_open

import pytest

from src.reader import get_data_from_csv


@pytest.fixture
def sample_csv_content():
    """Пример CSV данных из запроса."""
    return """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
United States,2023,25462,2.1,3.4,3.7,339,North America
United States,2022,23315,2.1,8.0,3.6,338,North America
China,2023,17963,5.2,2.5,5.2,1425,Asia
China,2022,17734,3.0,2.0,5.6,1423,Asia
Germany,2023,4086,-0.3,6.2,3.0,83,Europe
"""


@patch('builtins.print')
def test_file_not_found(mock_print):
    """Тест отсутствующего файла."""
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = get_data_from_csv(['missing.csv'])

    mock_print.assert_called_with("Файл не найден: missing.csv")
    assert result == {}


def test_empty_csv():
    """Тест пустого CSV."""
    empty_csv = "country,year,gdp"

    with patch('builtins.open', mock_open(read_data=empty_csv)):
        result = get_data_from_csv(['empty.csv'])

    assert result == {}


def test_read_csv_data(tmp_path, sample_csv_content):
    """Тест чтения CSV файла."""
    file_path = tmp_path / "test_data.csv"
    file_path.write_text(sample_csv_content, encoding="utf-8")

    data = get_data_from_csv([str(file_path)])

    assert "United States" in data
    assert len(data["United States"]) == 2
    assert sum(data["United States"]) == 25462 + 23315
    assert "China" in data
    assert "Germany" in data
