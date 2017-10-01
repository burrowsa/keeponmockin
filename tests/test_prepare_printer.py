from keeponmockin.example8 import prepare_printer
from mock import patch, PropertyMock
import pytest


@pytest.mark.xfail
def test_prepare_printer_obvious_way():
    with patch("keeponmockin.example8.Printer.online") as mock_online:
        prepare_printer()
    
    mock_online.assert_called_once_with(True)


def test_prepare_printer():
    with patch("keeponmockin.example8.Printer.online",
               new_callable=PropertyMock) as mock_online:
        prepare_printer()
    
    mock_online.assert_called_once_with(True)


def test_prepare_printer_assert_on_state():
    with patch("keeponmockin.example8.Printer.online", False):
        printer = prepare_printer()
        assert printer.online == True
    
