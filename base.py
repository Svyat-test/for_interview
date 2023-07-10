from selenium import webdriver


class Base:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def open_url(self, url=''):
        self.browser.get(url)
