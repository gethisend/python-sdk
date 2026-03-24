import unittest
from unittest.mock import patch, MagicMock

from hisend import Hisend

class TestHisendClient(unittest.TestCase):
    def setUp(self):
        self.api_key = "test_api_key_123"
        self.client = Hisend(api_key=self.api_key)

    @patch("hisend.client.requests.Session.request")
    def test_request_headers_and_url(self, mock_request):
        # Setup mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'{"id": 1, "name": "example.com"}'
        mock_response.json.return_value = {"id": 1, "name": "example.com"}
        mock_request.return_value = mock_response

        # Call method
        result = self.client.domains.get(1)

        # Assertions
        mock_request.assert_called_once_with(
            "GET",
            "https://api.hisend.app/v1/domains/1",
            json=None
        )
        
        # Check session headers
        headers = self.client.session.headers
        self.assertEqual(headers["Authorization"], f"Bearer {self.api_key}")
        self.assertEqual(headers["Content-Type"], "application/json")
        
        # Check result
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "example.com")

if __name__ == "__main__":
    unittest.main()
