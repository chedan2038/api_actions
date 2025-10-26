import requests

from config import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class GetObjectById(BaseEndpoint):
    def get_by_id(self, obj_id: str):
        self.response = requests.get(BASE_LINK + f'/objects/{obj_id}')
        self.response_json = self.response.json()
