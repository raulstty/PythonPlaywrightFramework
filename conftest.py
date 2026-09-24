
from playwright.sync_api import Page ,Playwright, expect
from api.posts_client import PostsClient
from api.rooms_client import RoomsClient
import pytest
import re

from pages.login_page import LoginPage
from pages.rooms_page import RoomsPage
from pages.admin_page import AdminPage


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
    
@pytest.fixture
def rooms_client(api_context) -> RoomsClient:
    return RoomsClient(api_context)

@pytest.fixture
def rooms_page(page:Page) ->RoomsPage:
    return RoomsPage(page)

@pytest.fixture(scope="session")
def admin_storage_state(browser,tmp_path_factory) ->str:
    state_file = tmp_path_factory.mktemp("auth") / "admin_state.json"
    context = browser.new_context()
    admin = AdminPage(context.new_page())
    admin.open()
    admin.login("admin","password")
    expect(admin.page).to_have_url(re.compile(r"admin/rooms"))
    context.storage_state(path=state_file)
    context.close()
    return str(state_file)

@pytest.fixture
def admin_page(browser, admin_storage_state):
    context = browser.new_context(storage_state=admin_storage_state)
    yield AdminPage(context.new_page())
    context.close()
    
