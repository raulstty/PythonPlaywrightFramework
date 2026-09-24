from playwright.sync_api import APIResponse

from api.base_client import BaseClient
from config.setting import ROOMS_SITE_URL


class RoomsClient(BaseClient):
    URL = f"{ROOMS_SITE_URL}/api/room/"
    
    def get_rooms(self) -> APIResponse:
        return self.get(self.URL)
        
        

    