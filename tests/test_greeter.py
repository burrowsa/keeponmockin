from mock import patch
from keeponmockin.example1 import greeter
import pytest


def test_greeter():
    with patch("keeponmockin.example1.print") as mock_print:  # Older versions of mock require create=True
        greeter("World")
    mock_print.assert_called_once_with("Hello World!")


@pytest.mark.skipif("sys.version_info[0] < 3")
def test_greeter_works_in_py3():
    with patch("builtins.print") as mock_print:
        greeter("World")
    mock_print.assert_called_once_with("Hello World!")


@pytest.mark.skipif("sys.version_info[0] >= 3")
def test_greeter_works_in_py2():
    with patch("__builtin__.print") as mock_print:
        greeter("World")
    mock_print.assert_called_once_with("Hello World!")
