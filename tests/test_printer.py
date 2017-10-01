from keeponmockin.example7 import Printer
from mock import sentinel, patch
import pytest


@pytest.mark.xfail
def test_printer_obvious_way():
    printer = Printer()
    with patch.object(printer, "online", False):
        with pytest.raises(RuntimeError) as err:
            printer.submit_job(sentinel.job)
        
        assert str(err.value) == "Printer is offline"


def test_printer():
    printer = Printer()
    with patch("keeponmockin.example7.Printer.online", False):
        with pytest.raises(RuntimeError) as err:
            printer.submit_job(sentinel.job)
        
        assert str(err.value) == "Printer is offline"
