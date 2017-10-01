from os import environ


def get_alert_email_address():
    return "{}@example.com".format(environ["ALERT_USER"])


def load_user(username):
    pass


user_cache = {}


def get_user(username):
    if username not in user_cache:
        user_cache[username] = load_user(username)

    return user_cache[username]
