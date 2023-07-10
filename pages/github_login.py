import requests
from selenium.webdriver.common.by import By
from base import Base
from object_test_data.login import *
from object_test_data.resource import *


def get_auth(api: Url, user: User):
    data = {'commit': 'Sign in', 'login': user.login, 'password': user.password}
    response = requests.post(url=api.url, json=data)
    if response.status_code == 200:
        return response.status_code
    else:
        return response.status_code


class AuthPage(Base):
    def auth(self, user: User):
        self.browser.find_element(By.ID, 'login_field').send_keys(user.login)
        self.browser.find_element(By.ID, 'password').send_keys(user.password)
        self.browser.find_element(By.CSS_SELECTOR, '[value="Sign in"]').click()


