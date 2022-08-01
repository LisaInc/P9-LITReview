from django.test import Client
from django.urls import reverse, resolve

import pytest
from pytest_django.asserts import assertTemplateUsed
from authentication.models import User


class TestAuth:
    client = Client()

    @pytest.mark.django_db
    def test_login_logout(self):

        user = User.objects.create(
            first_name="Test",
            last_name="User",
            username="TestUser",
            email="testuser@email.com",
        )
        user.set_password("TestPassword")
        user.save()
        user_data = {
            "username": "TestUser",
            "password": "TestPassword",
        }
        response = self.client.post("/", user_data)

        assert response.url == "/flow"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == "TestUser"

        response = self.client.get(reverse("logout"))

        assert response.url == "/"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == ""

    @pytest.mark.django_db
    def test_login_invalid_login_valid(self):
        user = User.objects.create(
            first_name="Test",
            last_name="User",
            username="TestUser",
            email="testuser@email.com",
        )
        user.set_password("TestPassword")
        user.save()

        user_data = {
            "username": "TestUser",
            "password": "wrongpassword",
        }
        response = self.client.post("/", user_data)

        assert "<p>Identifiants invalides.</p>" in response.content.decode()
        assert response.status_code == 200
        assert response.wsgi_request.user.username == ""

        user_data = {
            "username": "TestUser",
            "password": "TestPassword",
        }
        response = self.client.post("/", user_data)

        assert response.url == "/flow"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == "TestUser"

    @pytest.mark.django_db
    def test_signup_logout(self):

        user = {
            "first_name": "Test",
            "last_name": "User",
            "username": "TestUser",
            "email": "testuser@email.com",
            "password1": "TestPassword",
            "password2": "TestPassword",
        }
        response = self.client.post("/signup", user)
        assert response.url == "/flow"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == "TestUser"

        response = self.client.get(reverse("logout"))

        assert response.url == "/"
        assert response.status_code == 302
        assert response.wsgi_request.user.username == ""
