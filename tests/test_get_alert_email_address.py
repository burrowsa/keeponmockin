from keeponmockin.example9 import get_alert_email_address
from mock import patch


def test_get_email_address():
    with patch.dict("keeponmockin.example9.environ", {"ALERT_USER": "jblogs"}):
        assert get_alert_email_address() == "jblogs@example.com"
