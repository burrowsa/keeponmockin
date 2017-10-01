from keeponmockin.example9 import get_user
from mock import patch, sentinel


@patch.dict("keeponmockin.example9.user_cache", clear=True)
def test_get_email_address_not_cached():
    with patch("keeponmockin.example9.load_user", return_value=sentinel.user) as mock_load_user:
        assert sentinel.user == get_user(sentinel.username)
        assert sentinel.user == get_user(sentinel.username)
        assert sentinel.user == get_user(sentinel.username)
        mock_load_user.assert_called_once_with(sentinel.username)


@patch.dict("keeponmockin.example9.user_cache", {sentinel.username: sentinel.user})
def test_get_email_address_cached():
    with patch("keeponmockin.example9.load_user") as mock_load_user:
        assert sentinel.user == get_user(sentinel.username)
        mock_load_user.assert_not_called()



