from mock import patch, sentinel, Mock
from keeponmockin.example2 import is_non_string_sequence
from collections import Sequence
import pytest


def test_is_non_string_sequence1():
    with patch("keeponmockin.example2.isinstance", return_value=False) as mock_isinstance:  # Older versions of mock require create=True
        assert is_non_string_sequence(sentinel.obj) == False
    mock_isinstance.assert_called_once_with(sentinel.obj, Sequence)
    

@pytest.mark.xfail(run=False)
def test_is_non_string_sequence():
    with patch("builtins.isinstance", return_value=False) as mock_isinstance:
        assert is_non_string_sequence(sentinel.obj) == False
    mock_isinstance.assert_called_once_with(sentinel.obj, Sequence)    


@pytest.mark.xfail(run=False)
def test_is_non_string_sequence_does_not_work_in_py3_stack_overflow_in_py2():
    with patch("__builtin__.isinstance", return_value=False) as mock_isinstance:
        assert is_non_string_sequence(sentinel.obj) == False
    mock_isinstance.assert_called_once_with(sentinel.obj, Sequence)


def test_is_non_string_sequence_also_works_in_both_py2_and_3():
    test_obj = Mock(name="test_obj", spec=list)
    assert is_non_string_sequence(test_obj) == True
