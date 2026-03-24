from typing import List, Any, Dict, TYPE_CHECKING
from ..models import Email, SendEmailRequest

if TYPE_CHECKING:
    from ..client import Hisend

class EmailsResource:
    def __init__(self, client: 'Hisend'):
        self.client = client

    def list(self) -> List[Email]:
        return self.client.request("GET", "/emails")

    def get(self, email_id: int) -> Email:
        return self.client.request("GET", f"/emails/{email_id}")

    def send(self, data: SendEmailRequest) -> Email:
        return self.client.request("POST", "/emails", json=data)

    def send_batch(self, data: List[SendEmailRequest]) -> Dict[str, List[Any]]:
        return self.client.request("POST", "/emails/batch", json=data)
