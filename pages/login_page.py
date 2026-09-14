from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/practice-test-login/"
    def __init__(self,page: Page):
        super().__init__(page)
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.error_message = page.locator("#error")
        
    def login(self,username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
        
    def get_error_message(self) -> str:
        return self.error_message.inner_text()