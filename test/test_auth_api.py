import pytest
from pages.github_login import *
from test_data.resource import *
from test_data.login_list import *


@pytest.mark.api
def test_get_auth_mock_positive(monkeypatch):
    """
    Тест на успешную авторизацию
    :param monkeypatch:
    :return: мокированные данные
    """
    class MockResponse(object):
        def __init__(self):
            self.status_code = 200
            self.url = api_login()

        def json(self):
            return {'data': 'auth success'}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'post', mock_get)
    assert get_auth(api_login(), login_positive()) == 200


@pytest.mark.api
def test_get_auth_mock_negative():
    request = get_auth(api_login(), login_negative())
    assert request == 403, f'Получили: {request}, ожидали: 403'







