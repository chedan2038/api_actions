import pytest

from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from test_data.payloads import create_object_payload


@pytest.fixture()
def obj_id():
    """
    Создается новый объект и возвращается его id.
    По окончании теста объект удаляется
    :return: str
    """


    obj = CreateObject()
    del_obj = DeleteObject()

    obj.create_object(create_object_payload)
    yield obj.response_json['id']
    del_obj.delete_object(obj.response_json['id'])
