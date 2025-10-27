import allure
import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object_by_Id import GetObjectById
from endpoints.get_objects import GetObjectsEndpoint
from endpoints.update_object import UpdateObject
from schemes.adding_obj_model import AddingObjectModel
from schemes.get_obj_by_id import GetObjModel
from schemes.obj_list_model import ItemsObjectsListModel
from schemes.update_obj_model import UpdateObjectModel
from test_data.payloads import *


@allure.feature('Objects')
@allure.story('Get objects')
def test_get_all_objects():
    """
    а) Получить список объектов /objects и убедиться, что статус 200 и это JSON-массив с элементами, у которых есть id и name.
    """

    g = GetObjectsEndpoint()

    g.get_list_of_all_objects()
    g.check_status_code(200)
    g.validate(ItemsObjectsListModel)


@allure.feature('Objects')
@allure.story('Get objects')
def test_get_by_id():
    """
    б) Получить конкретный зарезервированный объект /objects/4 и проверить ожидаемые поля.
    """

    g = GetObjectById()

    g.get_by_id('4')
    g.check_status_code(200)
    g.validate(GetObjModel)


@allure.feature('Objects')
@allure.story('Create objects')
def test_create():
    """
    Создай объект с name и вложенным data (несколько типов: число, строка, bool). Проверь:
    - 200/201 (см. фактический код)
    - В ответе есть id и createdAt
    - GET по id возвращает тот же name/data.
    """

    c = CreateObject()
    g = GetObjectById()

    c.create_object(create_object_payload)
    c.check_status_code(200)
    c.validate(AddingObjectModel)
    g.get_by_id(c.response_json['id'])
    g.response_is_as_expected(create_object_payload, ['id'])


@allure.feature('Objects')
@allure.story('Update objects')
def test_update(obj_id):
    """
    Сделай PUT /objects/{id} с полной заменой name и data, проверь updatedAt и соответствие полей после GET.
    """

    u = UpdateObject()
    g = GetObjectById()

    u.update_object(obj_id, update_object_payload)
    u.validate(UpdateObjectModel)
    g.get_by_id(obj_id)
    g.check_field('name', 'Apple MacBook Pro 77')
    g.check_field('data.year', '2077')
    g.check_field('data.price', '2000.99')
    g.check_field('data.CPU model', 'Intel Core i27')
    g.check_field('data.Hard disk size', '100 TB')


@allure.feature('Objects')
@allure.story('Delete objects')
def test_delete(obj_id):
    """
    Удали созданный объект и подтвердить, что повторный GET даёт 404/соответствующую ошибку (проверяйте фактическое поведение API).
    """

    d = DeleteObject()
    g = GetObjectById()

    d.delete_object(obj_id)
    d.check_status_code(200)
    g.get_by_id(obj_id)
    g.check_status_code(404)


@allure.feature('Objects')
@allure.story('Create objects')
@pytest.mark.parametrize('payload', [create_phone_payload, create_laptop_payload, create_headset_payload])
def test_create_params(payload):
    """
    Параметризируй создание разных «товаров» (телефон/ноутбук/наушники) с разными наборами data и проверь корректность чтения.
    """

    c = CreateObject()
    g = GetObjectById()

    c.create_object(payload)
    c.check_status_code(200)
    g.get_by_id(c.response_json['id'])
    g.response_is_as_expected(payload, ['id'])
