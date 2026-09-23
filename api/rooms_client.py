from playwright.sync_api import APIResponse

from api.base_client import BaseClient


class RoomsClient(BaseClient):
    URL = "https://automationintesting.online/api/room/"
    
    def get_rooms(self) -> APIResponse:
        return self.get(self.URL)
        
        

    