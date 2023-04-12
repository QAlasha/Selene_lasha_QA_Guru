import time

import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def open_browser():
    browser.open('https://google.com')
    yield browser


@pytest.fixture(autouse=True)
def size_browser():
    browser.config.window_width = 700
    browser.config.window_height = 500
    time.sleep(3)
    browser.quit()
