import re

from playwright.sync_api import Page, expect

from config.setting import ROOMS_SITE_URL
from pages.admin_page import AdminPage


def test_admin_starts_logged_in(admin_page: AdminPage):
    admin_page.open()
    expect(admin_page.username_input).to_have_count(0)
    expect(admin_page.page).to_have_url(re.compile(r"admin/rooms"))


def test_admin_is_logged_in_again_without_a_new_login(admin_page: AdminPage):
    admin_page.open()
    expect(admin_page.username_input).to_have_count(0)


def test_normal_page_has_no_saved_session(page: Page):
    page.goto(AdminPage.URL)
    expect(page.locator("#username")).to_be_visible()


def test_session_storage_read_write(page: Page):
    page.goto(f"{ROOMS_SITE_URL}/")
    page.evaluate("sessionStorage.setItem('theme', 'dark')")
    assert page.evaluate("sessionStorage.getItem('theme')") == "dark"