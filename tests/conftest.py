import pytest
from .test_data import LoginData

@pytest.fixture(params=LoginData.INVALID_USERS)
def invalid_user(request):
    return request.param

@pytest.fixture
def valid_user():
    return LoginData.VALID_USER