import pytest
from pytest_factoryboy import register
from .factories import PlayerFactory
from rest_framework.test import APIClient
from django.test import Client

register(PlayerFactory)


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def logged_user():
    logged_user = Client()
    return logged_user
