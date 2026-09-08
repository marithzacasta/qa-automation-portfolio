from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_successful_login(page): # QUE QUIERO PROBAR
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(page)

    login_page.login("Admin", "admin123")

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")


def test_invalid_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(page)

    login_page.login("hola", "nose123")

    expect(login_page.mensaje_error).to_have_text("Invalid credentials")