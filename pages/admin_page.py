from config.setting import ROOMS_SITE_URL
from pages.base_page import BasePage


class AdminPage(BasePage):
    URL = f"{ROOMS_SITE_URL}/admin"
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        
    def open(self):
        self.navigate(self.URL)
        
    def login(self, username:str , password:str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        print("LOGGING IN NOW")
    