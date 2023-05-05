from pydantic import BaseModel, Field
from pydantic.color import Color
from utils.models.users_model import Support


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: Color
    pantone_value: str


class DefaultListResource(BaseModel):
    page: int = Field(...)
    per_page: int = Field(...)
    total: int = Field(...)
    total_pages: int = Field(...)
    data: list[Data] = Field(...)
    support: Support = Field(...)


class DefaultSingleResource(BaseModel):
    data: Data = Field(...)
    support: Support = Field(...)
