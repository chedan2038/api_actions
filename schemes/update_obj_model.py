from datetime import datetime

from pydantic import BaseModel

from schemes._common_model import CommonData


class UpdateObjectModel(BaseModel):
    id: str
    name: str
    data: CommonData
    updatedAt: datetime
