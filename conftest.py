import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    """Google Chrome Version 88.0.4324.182"""
    browser: webdriver = webdriver.Chrome()
    yield browser
    browser.quit()
