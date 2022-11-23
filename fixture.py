from smtpd import Options

import pytest
from selene import browser


@pytest.fixture()
def open_chome():
    browser.open_url('http://google.com/ncr')
    options = Options()
    options.add_argument('--window-size=1900,1000')
    return options



