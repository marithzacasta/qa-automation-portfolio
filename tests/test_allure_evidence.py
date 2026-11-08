
import allure
from playwright.sync_api import expect


def test_attach_screenshot(page):
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
        wait_until="domcontentloaded",
    )

    # Esperar a que el formulario de login sea visible
    username = page.get_by_placeholder("Username")
    expect(username).to_be_visible(timeout=15000)

    # Capturar la página después de comprobar que cargó
    screenshot = page.screenshot(full_page=True)

   # Adjuntar la captura al resultado de Allure
    allure.attach(
        screenshot,
        name="Captura de pantalla - Login OrangeHRM",
        attachment_type=allure.attachment_type.PNG,
    )
