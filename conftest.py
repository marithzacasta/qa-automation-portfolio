import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright, expect

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

@pytest.fixture(scope="function")
def logged_in_page(page):
    page.goto("/web/index.php/auth/login")

    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    page.goto("/web/index.php/pim/viewEmployeeList")

    return page