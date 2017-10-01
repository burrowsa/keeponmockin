from keeponmockin.example6 import equals_one_hundred, equals_one_thousand
from mock import MagicMock, call
import pytest

@pytest.mark.xfail
def test_equals_one_hundred_and_one_thousand_obvious_way():
    mock_value = MagicMock(name="mock_value")
    equals_one_hundred(mock_value)
    equals_one_thousand(mock_value)
    
    assert mock_value.mock_calls == [call.__eq__(100),
                                     call.__eq__(1000),]


def test_equals_one_hundred_and_one_thousand():
    mock_value = MagicMock(name="mock_value")
    equals_one_hundred(mock_value)
    equals_one_thousand(mock_value)
    
    assert mock_value.mock_calls == [("__eq__", (100,), {}),
                                     ("__eq__", (1000,), {})]
