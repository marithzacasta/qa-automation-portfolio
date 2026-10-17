import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_successful_login(page): # QUE QUIERO PROBAR
    page.goto("/web/index.php/auth/login")

    login_page = LoginPage(page)

    login_page.login("Admin", "admin123")

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")


@pytest.mark.parametrize("usuario, contraseña", [
    ("IncorrectUser", "admin123"),
    ("Admin", "incorrect123"),
    ("IncorrectUser", "incorrect123"),
])
def test_invalid_login(page, usuario, contraseña):
    page.goto("/web/index.php/auth/login")

    login_page = LoginPage(page)

    login_page.login(usuario, contraseña)

    expect(login_page.mensaje_error).to_have_text("Invalid credentials")


def test_empty_username(page):
    page.goto("/web/index.php/auth/login")

    Login_page = LoginPage(page)

    Login_page.login("", "admin123")

    expect(Login_page.username_required).to_have_text("Required")


def test_empty_password(page):
    page.goto("/web/index.php/auth/login")

    login_page = LoginPage(page)

    login_page.login("Admin", "")

    expect(login_page.password_required).to_have_text("Required")