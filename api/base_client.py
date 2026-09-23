from playwright.sync_api import APIRequestContext, APIResponse


class BaseClient:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        
    def get(self,path:str,params: dict | None = None) -> APIResponse :
        return self.request.get(path,params =params)
    
    def post(self,path:str, payload : dict) ->APIResponse:
        return self.request.post(path, data=payload)
    