import pytest
from selenium.webdriver.common.by import By
from pages.github_login import AuthPage
from test_data.login_list import *


@pytest.mark.positive
def test_auth_positive(browser):
    auth = AuthPage(browser)
    auth.open_url('https://github.com/login')
    auth.auth(login_positive())
    actual = browser.find_element(By.CSS_SELECTOR, '.AppHeader').tag_name
    assert (actual == 'header'), f"\nОжидаемый рез-т: шапка глав.страницы.\nФактический рез-т: что-то не то, '{actual}'"


@pytest.mark.negative
def test_auth_negative(browser):
    auth = AuthPage(browser)
    auth.open_url('https://github.com/login')
    auth.auth(login_negative())
    actual = browser.find_element(By.CSS_SELECTOR, '.flash.flash-full.flash-error  .js-flash-alert').text
    assert (actual == 'Incorrect username or password.'), f"\nОжидаемый рез-т: алерт неправильный пароль или логин\n" \
                                                          f"Фактический рез-т: что-то не то, '{actual}'"
