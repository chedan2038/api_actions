import requests

from config import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):

    def create_object(self, json: dict):
        self.response = requests.post(BASE_LINK + '/objects', json=json)
        self.response_json = self.response.json()
