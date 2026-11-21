"""Shared pytest fixtures.

Usage:
    pytest                      # headless Chrome
    pytest --browser firefox    # headless Firefox
    pytest --headed             # watch the browser
Failed tests leave a screenshot and HTML dump in ./artifacts/.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest
from selenium import webdriver

ARTIFACTS = Path("artifacts")


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", default="chrome", choices=("chrome", "firefox"))
    parser.addoption("--headed", action="store_true", help="Show the browser window")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    """Expose each phase's result on the test item so fixtures can see it."""
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())


@pytest.fixture
def driver(request: pytest.FixtureRequest):
    browser = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if not headed:
            options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        if not headed:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        options.add_argument("--log-level=2")
        drv = webdriver.Chrome(options=options)

    yield drv

    report = getattr(request.node, "rep_call", None)
    if report is not None and report.failed:
        ARTIFACTS.mkdir(exist_ok=True)
        name = re.sub(r"[^\w.-]+", "_", request.node.name)
        drv.save_screenshot(str(ARTIFACTS / f"{name}.png"))
        (ARTIFACTS / f"{name}.html").write_text(drv.page_source, encoding="utf-8")

    drv.quit()