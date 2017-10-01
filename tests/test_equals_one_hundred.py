from keeponmockin.example6 import equals_one_hundred
from mock import MagicMock


def test_equals_one_hundred():
    mock_value = MagicMock(name="mock_value")
    equals_one_hundred(mock_value)
    
    mock_value.__eq__.assert_called_once_with(100)


