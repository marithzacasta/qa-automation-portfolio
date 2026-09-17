import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function") # PREPARAR EL ENTORNO
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        context = browser.new_context(  # Esto significa que Playwright ahora sabe cuál es la URL base de nuestra aplicación.
            base_url="https://opensource-demo.orangehrmlive.com"
        )

        page = context.new_page()

        yield page

        browser.close()
