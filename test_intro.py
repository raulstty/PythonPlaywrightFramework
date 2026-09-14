from playwright.sync_api import Page

from pages.login_page import LoginPage

    
def test_playwright_homepage_url2(home_page: Page):
    print(f"\nObject id: {id(home_page)}")
    assert "Playwright" in home_page.title()
    
def test_playwright_homepage_title(home_page: Page):
    print(f"\nObject id: {id(home_page)}")
    assert "Playwright" in home_page.title()
    
def test_successful_login(login_page: LoginPage):
    login_page.login("student", "Password123")
    assert "logged-in-successfully" in login_page.page.url