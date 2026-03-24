from typing import List, TYPE_CHECKING
from ..models import Domain, AddDomainRequest

if TYPE_CHECKING:
    from ..client import Hisend

class DomainsResource:
    def __init__(self, client: 'Hisend'):
        self.client = client

    def list(self) -> List[Domain]:
        return self.client.request("GET", "/domains")

    def get(self, domain_id: int) -> Domain:
        return self.client.request("GET", f"/domains/{domain_id}")

    def verify(self, domain_id: int) -> Domain:
        return self.client.request("GET", f"/domains/{domain_id}/verify")

    def add(self, data: AddDomainRequest) -> Domain:
        return self.client.request("POST", "/domains", json=data)

    def delete(self, domain_id: int) -> None:
        self.client.request("DELETE", f"/domains/{domain_id}")
