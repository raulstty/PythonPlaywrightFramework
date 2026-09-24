from playwright.sync_api import Locator

from config.setting import ROOMS_SITE_URL
from pages.base_page import BasePage


class RoomsPage(BasePage):
    URL = f"{ROOMS_SITE_URL}/"
    def __init__(self, page):
        super().__init__(page)
        self.room_cards = page.locator("div.card").filter(has=page.locator("h5.card-title"))
    def open(self):
        self.navigate(self.URL)
    
    def room_card(self, room_type:str)->Locator:
        return self.room_cards.filter(
                has=self.page.get_by_role("heading", name=room_type, exact=True)
            )
    
    
