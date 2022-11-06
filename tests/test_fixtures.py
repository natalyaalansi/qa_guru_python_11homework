import pytest
from selene.support.shared import browser

@pytest.fixture(scope='function')
def desktop():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open('https://github.com')
    yield

@pytest.fixture(scope='function')
def mobile():
    browser.config.window_height = 800
    browser.config.window_width = 600
    browser.open('https://github.com')
    yield

def test_github_desktop(desktop):
    browser.element('.HeaderMenu-link--sign-in').click()

def test_github_mobile(mobile):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()