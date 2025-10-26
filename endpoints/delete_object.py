import requests

from config import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_object(self, obj_id: str):
        self.response = requests.delete(BASE_LINK + f'/objects/{obj_id}')
        self.response_json = self.response.json()
