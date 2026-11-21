import pytest

from upass.exceptions import NotEligibleError
from upass.pages import UPassHomePage, SfuMfaPage


# Sample HTML snippets
ELIGIBLE = """
<input type="checkbox" id="chk_1"
       onclick="document.getElementById('requestButton').disabled = false">
<button id="requestButton" disabled
        onclick="document.body.dataset.done = '1'">Request</button>
"""

STUCK_DISABLED = """
<input type="checkbox" id="chk_1">
<button id="requestButton" disabled>Request</button>
"""

NO_CHECKBOX = """
<div class="status">Able to request as of 01-01-27</div>
"""


def load(driver, tmp_path, html):
    f = tmp_path / "page.html"
    f.write_text(html)
    driver.get(f.as_uri())
    return UPassHomePage(driver, timeout=2)


def test_can_request_when_checkbox_present(driver, tmp_path):
    assert load(driver, tmp_path, ELIGIBLE).can_request()


def test_cannot_request_when_checkbox_missing(driver, tmp_path):
    assert not load(driver, tmp_path, NO_CHECKBOX).can_request()


def test_request_clicks_button(driver, tmp_path):
    page = load(driver, tmp_path, ELIGIBLE)
    page.request_upass()
    assert driver.execute_script("return document.body.dataset.done") == "1"


def test_request_raises_when_button_stays_disabled(driver, tmp_path):
    page = load(driver, tmp_path, STUCK_DISABLED)
    with pytest.raises(NotEligibleError):
        page.request_upass()