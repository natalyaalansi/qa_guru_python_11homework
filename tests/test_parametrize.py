import pytest
from selene.support.shared import browser

@pytest.fixture(params=[(1920, 1080), (600, 800)])
def browser_open(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    browser.open('https://github.com')

@pytest.mark.parametrize('browser_open', [(1920, 1080)], indirect=True)
def test_github_desktop(browser_open):
    browser.element('.HeaderMenu-link--sign-in').click()

@pytest.mark.parametrize('browser_open', [(600, 800)], indirect=True)
def test_github_mobile(browser_open):
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()