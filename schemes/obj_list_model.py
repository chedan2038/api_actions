from typing import Optional, List

from pydantic import BaseModel, RootModel, Field


class Data(BaseModel):
    color: Optional[str] = None
    capacity: Optional[str] = None
    capacityGB: Optional[int] = None
    price: Optional[float] = None
    generation: Optional[str] = None
    year: Optional[int] = None
    CPUmodel: Optional[str] = Field(default=None, alias="CPU model")
    Harddisksize: Optional[str] = Field(default=None, alias="Hard disk size")
    StrapColour: Optional[str] = None
    CaseSize: Optional[str] = None
    Color: Optional[str] = None
    Description: Optional[str] = None
    Capacity: Optional[str] = None
    Screensize: Optional[float] = None
    Generation: Optional[str] = None
    Price: Optional[str] = None


class ObjectsListModel(BaseModel):
    id: str
    name: str
    data: Optional[Data] = None


class ItemsObjectsListModel(RootModel[List[ObjectsListModel]]):
    pass
