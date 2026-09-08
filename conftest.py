import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture # PREPARAR EL ENTORNO
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        yield page

        browser.close()
