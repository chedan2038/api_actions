from pydantic import BaseModel, Field


class CommonData(BaseModel):
    year: int
    price: float
    CPUmodel: str = Field(alias="CPU model")
    Harddisksize: str = Field(alias="Hard disk size")


class CommonIND(BaseModel):
    id: str
    name: str
    data: CommonData
