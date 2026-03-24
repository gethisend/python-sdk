import requests
from typing import Any, Dict, Optional

class HisendError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code

class Hisend:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.hisend.app/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        
        # Initialize resources (to be assigned after imports)
        self.emails = None
        self.domains = None
        self.routing = None
        self.threads = None
        
        self._init_resources()
        
    def _init_resources(self):
        from .resources.emails import EmailsResource
        from .resources.domains import DomainsResource
        from .resources.routing import RoutingResource
        from .resources.threads import ThreadsResource
        
        self.emails = EmailsResource(self)
        self.domains = DomainsResource(self)
        self.routing = RoutingResource(self)
        self.threads = ThreadsResource(self)

    def request(self, method: str, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.base_url}{endpoint}"
        
        # map 'from_' to 'from' if it exists in the json request data
        if json and "from_" in json:
            json["from"] = json.pop("from_")
            
        response = self.session.request(method, url, json=json)
        
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            error_message = response.text
            try:
                error_data = response.json()
                error_message = error_data.get("message", error_message)
            except ValueError:
                pass
            raise HisendError(f"API request failed: {error_message}", status_code=response.status_code) from e
            
        if response.content:
            return response.json()
        return None
