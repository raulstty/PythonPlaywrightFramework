import json
from pathlib import Path
import re

from playwright.sync_api import Page, expect
import pytest

from pages.login_page import LoginPage

DATA_FILE = Path(__file__).parent / "data" / "login_test_data.json"
with open(DATA_FILE) as f:
    invalid_login_cases = json.load(f)
    

    
def test_playwright_homepage_url2(home_page: Page):
    print(f"\nObject id: {id(home_page)}")
    assert "Playwright" in home_page.title()
    
def test_playwright_homepage_title(home_page: Page):
    print(f"\nObject id: {id(home_page)}")
    assert "Playwright" in home_page.title()
    
def test_successful_login(login_page: LoginPage):
    login_page.login("student", "Password123")
    expect(login_page.page).to_have_url(re.compile(r"/logged-in-successfully/"))
    
@pytest.mark.parametrize(
    "case",
    invalid_login_cases,
    ids=[case["username"] for case in invalid_login_cases],
)
def test_invalid_login_shows_error_message(login_page: LoginPage, case):
    login_page.login(case["username"], case["password"])
    expect(login_page.error_message).to_have_text(case["expected_error"]) 