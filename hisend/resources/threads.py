from typing import List, TYPE_CHECKING
from ..models import Thread, Email

if TYPE_CHECKING:
    from ..client import Hisend

class ThreadsResource:
    def __init__(self, client: 'Hisend'):
        self.client = client

    def list(self) -> List[Thread]:
        return self.client.request("GET", "/threads")

    def get_emails(self, thread_id: int) -> List[Email]:
        return self.client.request("GET", f"/threads/{thread_id}/emails")
