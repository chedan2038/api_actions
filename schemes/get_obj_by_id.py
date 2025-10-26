from pydantic import BaseModel


class Data(BaseModel):
    price: float
    color: str


class GetObjModel(BaseModel):
    id: str
    name: str
    data: Data
