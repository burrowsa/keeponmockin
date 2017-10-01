from mock import patch, MagicMock, call
from keeponmockin.example5 import calculate_headcount
import pytest


def test_calculate_headcount():
    with patch("keeponmockin.example5.staff_members", return_value=["Alice",
                                                                    "Bob",
                                                                    "Chris"]) as mock_staff:
        assert calculate_headcount() == 3
    mock_staff.assert_called_once_with()   


@pytest.mark.skipif("sys.version_info[0] < 3")
def test_calculate_headcount_mock_overload():
    mock_staff = MagicMock()
    mock_iterable = mock_staff.return_value 
    mock_iterator = mock_iterable.__iter__.return_value
    mock_iterator.__iter__.side_effect = lambda: mock_iterator
    mock_iterator.__next__.side_effect = ["Rod", "Jane", "Freddy"]
         
    with patch("keeponmockin.example5.staff_members", mock_staff):
        assert calculate_headcount() == 3

    assert mock_staff.mock_calls == [call(),
                                     ('().__iter__', (), {}),
                                     ('().__iter__().__iter__', (), {}),
                                     ('().__iter__().__next__', (), {}),
                                     ('().__iter__().__next__', (), {}),
                                     ('().__iter__().__next__', (), {}),
                                     ('().__iter__().__next__', (), {})]

