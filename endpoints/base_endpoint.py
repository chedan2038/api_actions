from typing import Type

import allure
from pydantic import BaseModel


class BaseEndpoint:

    def __init__(self):
        self.response = None
        self.response_json = None

    def check_status_code(self, code: int) -> None:
        """
        Проверка статус кода
        :param code:
        """

        with allure.step('Проверка статус кода'):
            assert self.response.status_code == code, (f'Ожидаемый код не совпадает с фактическим'
                                                       f' \n res: {self.response.status_code}\n exp: {code}')

    def response_is_as_expected(self, expected_json: dict, exclude: list[str] = None) -> None:
        """
        Проверка на соответствие ожидаемого и фактического ответа
        :param exclude: список ключей исключаемых из ответа
        :param expected_json:
        """

        response_json = self.response_json
        if exclude is not None:
            for k in exclude:
                response_json.pop(k)

        assert response_json == expected_json, (
            f'Несовпадение ожидаемого и фактического ответа: \n res: {response_json} \n exp: {expected_json}')

    def check_field(self, path: str, expected_value) -> None:
        """
        Проверка поля
        :param path:
        :param expected_value:
        """

        keys = path.split(".")
        current = self.response_json
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                assert False, f'Поле по пути: "{path}" не найдено'
        assert str(current) == str(expected_value), (f'Поле по пути: "{path}" содержит некорректное значение.'
                                                     f' \n res: {current}\n exp: {expected_value}')

    def validate(self, schema: Type[BaseModel]) -> None:
        """
        Валидация по схеме
        :param schema:
        """

        with allure.step('Валидация ответа'):
            schema.model_validate(self.response_json)
