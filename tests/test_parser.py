import sys
from unittest.mock import patch
from src.parser import parse_arguments


def test_parse_arguments_valid():
    """Тест валидных аргументов."""
    test_args = ['script.py', '--files', 'file1.csv', 'file2.csv', '--report', 'average-gdp']

    with patch.object(sys, 'argv', test_args):
        result = parse_arguments()

    assert result.files == ['file1.csv', 'file2.csv']
    assert result.report == 'average-gdp'


def test_parse_arguments_multiple_files():
    """Тест нескольких файлов."""
    test_args = ['script.py', '--files', 'file1.csv', 'file2.csv', 'file3.csv', '--report', 'average-gdp']

    with patch.object(sys, 'argv', test_args):
        result = parse_arguments()

    assert len(result.files) == 3
    assert result.files[0] == 'file1.csv'
    assert result.report == 'average-gdp'
