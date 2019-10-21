import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene.api import browser
from selene import config

options = Options()
options.add_argument('--no-sandbox')
chrome = webdriver.Chrome(chrome_options=options)
config.timeout = 10
browser.set_driver(chrome)
chrome.set_window_size("1920", "1080")

@pytest.fixture(scope='session')
def setup():
    yield
    chrome.quit()
