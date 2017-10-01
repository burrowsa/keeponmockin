from mock import patch, mock_open, sentinel, call
from keeponmockin.example3 import count_words, count_words_alt
from io import StringIO
import pytest


TEST_PARAMETERS = ("file_contents, expected_count",
                   [(u"", 0),
                    (u"hello", 1),
                    (u"hello world", 2),
                    (u"""
                   
                   
                     """, 0),
                    (u" hello  world ", 2),
                    (u""" hello
                   
                   
                     world """, 2),
                   ])


@pytest.mark.parametrize(*TEST_PARAMETERS)
def test_count_words(file_contents, expected_count):
    with patch("keeponmockin.example3.open", mock_open(read_data=file_contents)) as mock_file:
        assert count_words(sentinel.filename) == expected_count
    assert mock_file.mock_calls[0] == call(sentinel.filename)


@pytest.mark.parametrize(*TEST_PARAMETERS)
def test_count_words_less_fragile(file_contents, expected_count):
    with patch("keeponmockin.example3.open", return_value=StringIO(file_contents)) as mock_file:
        assert count_words(sentinel.filename) == expected_count
    assert mock_file.mock_calls[0] == call(sentinel.filename)


@pytest.mark.parametrize(*TEST_PARAMETERS)
@pytest.mark.xfail(run=False)
def test_count_alt_words(file_contents, expected_count):
    with patch("keeponmockin.example3.open", mock_open(read_data=file_contents)) as mock_file:
        assert count_words_alt(sentinel.filename) == expected_count
    assert mock_file.mock_calls[0] == call(sentinel.filename)


@pytest.mark.parametrize(*TEST_PARAMETERS)
def test_count_words_alt_less_fragile(file_contents, expected_count):
    with patch("keeponmockin.example3.open", return_value=StringIO(file_contents)) as mock_file:
        assert count_words_alt(sentinel.filename) == expected_count
    assert mock_file.mock_calls[0] == call(sentinel.filename)
