from typing import List, TYPE_CHECKING
from ..models import Routing, CreateRoutingRequest, UpdateRoutingRequest

if TYPE_CHECKING:
    from ..client import Hisend

class RoutingResource:
    def __init__(self, client: 'Hisend'):
        self.client = client

    def list(self, domain_id: int) -> List[Routing]:
        return self.client.request("GET", f"/domains/{domain_id}/routing")

    def create(self, domain_id: int, data: CreateRoutingRequest) -> Routing:
        return self.client.request("POST", f"/domains/{domain_id}/routing", json=data)

    def update(self, domain_id: int, routing_id: int, data: UpdateRoutingRequest) -> Routing:
        return self.client.request("PUT", f"/domains/{domain_id}/routing/{routing_id}", json=data)

    def get(self, domain_id: int, routing_id: int) -> Routing:
        return self.client.request("GET", f"/domains/{domain_id}/routing/{routing_id}")

    def delete(self, domain_id: int, routing_id: int) -> None:
        self.client.request("DELETE", f"/domains/{domain_id}/routing/{routing_id}")
