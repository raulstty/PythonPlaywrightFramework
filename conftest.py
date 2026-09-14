
from playwright.sync_api import Page
import pytest

from pages.login_page import LoginPage


@pytest.fixture
def home_page(page: Page):
    page.goto("https://playwright.dev")
    return page

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.navigate(login.PATH)
    return login