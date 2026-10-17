from playwright.sync_api import expect


def test_assert(page):
    page.goto("/web/index.php/auth/login")

    assert page.title() == "OrangeHRM"


def test_expect(page):
    page.goto("/web/index.php/auth/login")

    expect(page.locator("input[name='username']")).to_be_visible()