import pytest
from pages.login_page import LoginPage
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="function") # PREPARAR EL ENTORNO
def page(request):
    with sync_playwright() as p:
        browser = request.config.getoption("browser")

        if browser == "chromium":
            browser_instance = p.chromium.launch()
        elif browser == "firefox":
            browser_instance = p.firefox.launch()
        elif browser == "webkit":
            browser_instance = p.webkit.launch()
        else:
            raise pytest.UsageError(
                f"Navegador no soportado: {browser}"
            )

        context = browser_instance.new_context(  # Esto significa que Playwright ahora sabe cuál es la URL base de nuestra aplicación.
            base_url="https://opensource-demo.orangehrmlive.com"
        )

        page = context.new_page()
        

        yield page

        context.close()
        browser_instance.close()

@pytest.fixture(scope="function")
def logged_in_page(page):
    page.goto("/web/index.php/auth/login")

    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")

    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    page.goto("/web/index.php/pim/viewEmployeeList")

    return page


def pytest_addoption(parser): # Hook de Pytest para registrar opciones personalizadas.
    parser.addoption(
        "--browser", # Nombre de la opción que escribiremos en la terminal.
        action="store", # Guarda el valor que escribamos después de la opción.
        default="chromium", # Usa Chromium si no especificamos un valor.
        choices=["chromium", "firefox", "webkit"],
        help="Selecciona el navegador para ejecutar las pruebas" # Describe la opción cuando consultamos la ayuda de Pytest.
    )