from django.urls import reverse, resolve


def test_login_url():
    url = reverse("login")
    assert resolve(url).view_name == "login"
    assert url == "/"


def test_signup_url():
    url = reverse("signup")
    assert resolve(url).view_name == "signup"
    assert url == "/signup"


def test_logout_url():
    url = reverse("logout")
    assert resolve(url).view_name == "logout"
    assert url == "/logout/"
