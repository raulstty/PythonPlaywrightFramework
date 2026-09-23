
from playwright.sync_api import Page ,Playwright
from api.posts_client import PostsClient
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

def pytest_addoption(parser):
    parser.addoption(
        "--api-base-url",
        default="https://jsonplaceholder.typicode.com",
        help = "base url for the API under test"
    )
    
@pytest.fixture(scope="session")
def api_context(playwright: Playwright, pytestconfig):
    context = playwright.request.new_context(
        base_url=pytestconfig.getoption("--api-base-url")
    )
    yield context
    context.dispose()
    
@pytest.fixture
def posts_client(api_context) -> PostsClient:
    return PostsClient(api_context)
    
    
