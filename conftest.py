import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        # browser.close()
        yield page