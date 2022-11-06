import pytest
from selene.support.shared import browser

@pytest.fixture(params=[{'setup': 'desktop', 'width': 1920, 'height': 1080},
                        {'setup': 'mobile', 'width': 600, 'height': 800}])

def browser_open(request):
    browser.config.window_width = request.param['width']
    browser.config.window_height = request.param['height']
    browser.open('https://github.com/')
    return request.param['setup']

def test_github_desktop(browser_open):
    if browser_open == 'mobile':
        pytest.skip('mobile size')
    browser.element('.HeaderMenu-link--sign-in').click()

def test_github_mobile(browser_open):
    if browser_open == 'desktop':
        pytest.skip('desktop size')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()

