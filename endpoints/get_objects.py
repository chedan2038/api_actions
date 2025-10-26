import allure
import requests

from config import BASE_LINK
from endpoints.base_endpoint import BaseEndpoint


class GetObjectsEndpoint(BaseEndpoint):

    def get_list_of_all_objects(self):
        with allure.step('Запрос на получение всех объектов'):
            self.response = requests.get(BASE_LINK + '/objects')
        self.response_json = self.response.json()
