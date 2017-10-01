from mock import patch, mock_open, sentinel, call
from keeponmockin.example4 import generate_file
from io import StringIO
from contextlib import contextmanager


def test_generate_file():
    with patch("keeponmockin.example4.open", mock_open()) as mock_file:
        generate_file(sentinel.filename)
    assert mock_file.mock_calls == [call(sentinel.filename, "w"),
                                    call().__enter__(),
                                    call().write("hello world\n"),
                                    call().writelines(["hello moon\n", "hello space\n"]),
                                    call().write("hello universe\n"),
                                    call().__exit__(None, None, None)]


@contextmanager
def defeat_context(x):
    yield x

def test_generate_file_less_fragile():
    with StringIO() as test_buffer:
        with patch("keeponmockin.example4.open", return_value=defeat_context(test_buffer)) as mock_file:
            generate_file(sentinel.filename)
        assert mock_file.mock_calls[0] == call(sentinel.filename, "w")
        assert test_buffer.getvalue() == """hello world
hello moon
hello space
hello universe
"""
