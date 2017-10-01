from keeponmockin.example0 import nightly_report
from mock import patch, sentinel, Mock, call
import pytest


@patch("keeponmockin.example0.find_models", return_value=[sentinel.model1,
                                                          sentinel.model2])
@patch("keeponmockin.example0.send_email")
def test_nightly_report_no_failures(mock_send_email, mock_find_models):
    # Arrange
    mock_engine = Mock(name="mock_engine")
    
    # Act
    nightly_report(mock_engine)
    
    # Assert
    mock_send_email.assert_called_once_with("support@example.com",
                                            "Nightly Report Status",
                                            "Ran 2 models, 0 failed.")
    
    mock_find_models.assert_called_once_with(taggedwith='nightly')
    
    assert mock_engine.mock_calls == [call.schedule_simulation(sentinel.model1),
                                      call.schedule_simulation(sentinel.model2),
                                      call.wait_for_result(sentinel.model1),
                                      call.wait_for_result(sentinel.model2)]


@patch("keeponmockin.example0.find_models", return_value=[sentinel.model1,
                                                          sentinel.model2])
@patch("keeponmockin.example0.send_email")
def test_nightly_report_one_failure(mock_send_email, mock_find_models):
    # Arrange
    mock_engine = Mock(name="mock_engine")
    mock_engine.wait_for_result.side_effect = [True, False]

    # Act
    nightly_report(mock_engine)

    # Assert
    mock_send_email.assert_called_once_with("support@example.com",
                                            "Nightly Report Status",
                                            "Ran 2 models, 1 failed.")
    
    mock_find_models.assert_called_once_with(taggedwith='nightly')
    
    assert mock_engine.mock_calls == [call.schedule_simulation(sentinel.model1),
                                      call.schedule_simulation(sentinel.model2),
                                      call.wait_for_result(sentinel.model1),
                                      call.wait_for_result(sentinel.model2)]


@pytest.mark.xfail
@patch("keeponmockin.example0.find_models", return_value=[sentinel.model1,
                                                          sentinel.model2])
@patch("keeponmockin.example0.send_email")
def test_nightly_report_duff_assert(mock_send_email, mock_find_models):
    # Arrange
    mock_engine = Mock(name="mock_engine")
    
    # Act
    nightly_report(mock_engine)
    
    # Assert
    mock_send_email.assert_clled_once_with("support@example.com",
                                           "Nightly Report Status",
                                           "Ran 2000 models, 0 failed.")


@pytest.mark.xfail
@patch("keeponmockin.example0.find_models", return_value=[sentinel.model1,
                                                          sentinel.model2])
@patch("keeponmockin.example0.send_email", autospec=True)
def test_nightly_report_duff_assert2(mock_send_email, mock_find_models):
    # Arrange
    mock_engine = Mock(name="mock_engine")
    
    # Act
    nightly_report(mock_engine)
    
    # Assert
    mock_send_email.asert_called_once_with("support@example.com",
                                           "Nightly Report Status",
                                           "Ran 2000 models, 0 failed.")
