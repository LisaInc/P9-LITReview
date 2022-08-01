from authentication.models import User

import pytest


@pytest.mark.django_db
def test_user():
    user = User.objects.create(username="username", password="psw")
    assert str(user) == "username"
    assert user.password == "psw"
