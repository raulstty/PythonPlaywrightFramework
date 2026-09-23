from playwright.sync_api import APIResponse

from api.base_client import BaseClient


class PostsClient(BaseClient):
    PATH ="/posts"
    
    def get_post(self, post_id: int) -> APIResponse:
        return self.get(f"{self.PATH}/{post_id}")
    
    def list_posts(self, user_id: int | None = None) ->APIResponse:
        params = {"userId": user_id} if user_id is not None else None
        return self.get(self.PATH,params=params)
    
    def create_post(self,payload:dict) ->APIResponse:
        return self.post(self.PATH, payload)
        
    