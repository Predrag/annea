import os
import sys
import pytest
from playwright.sync_api import sync_playwright, Browser, Page, expect
from typing import Generator
import subprocess
import time

expect.set_options(timeout=1000)


@pytest.fixture(scope="session", autouse=True)
def start_server():
    root_dir = os.path.dirname(os.path.abspath(__file__))  # .../annea/tests
    root_dir = os.path.abspath(os.path.join(root_dir, ".."))  # .../annea
    proc = subprocess.Popen([sys.executable, "-m", "http.server", "8080"], cwd=root_dir)
    time.sleep(1)
    yield
    proc.terminate()
    proc.wait()


@pytest.fixture
def browser() -> Generator[Browser, None, None]:
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute("data-testid")
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Generator[Page, None, None]:
    page = browser.new_page()
    yield page
    page.close()

