import requests

from config import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class UpdateObject(BaseEndpoint):

    def update_object(self, obj_id, json):
        self.response = requests.put(BASE_LINK + f'/objects/{obj_id}', json=json)
        self.response_json = self.response.json()
