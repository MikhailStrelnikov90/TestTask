import datetime
from pydantic import BaseModel, Field
from pydantic.networks import HttpUrl


class Support(BaseModel):
    url: HttpUrl
    text: str


class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: HttpUrl


class DefaultListUsers(BaseModel):
    page: int = Field(...)
    per_page: int = Field(...)
    total: int = Field(...)
    total_pages: int = Field(...)
    data: list[Data] = Field(...)
    support: Support = Field(...)


class DefaultSingleUser(BaseModel):
    data: Data = Field(...)
    support: Support = Field(...)


class DefaultCreateUser(BaseModel):
    name: str = Field(...)
    job: str = Field(...)
    id: str = Field(...)
    created_at: datetime.datetime = Field(alias='createdAt')


class DefaultCreateUserWithoutName(BaseModel):
    job: str = Field(...)
    id: str = Field(...)
    created_at: datetime.datetime = Field(alias='createdAt')


class DefaultCreateUserWithoutJob(BaseModel):
    name: str = Field(...)
    id: str = Field(...)
    created_at: datetime.datetime = Field(alias='createdAt')


class DefaultCreateUserWithoutData(BaseModel):
    id: str = Field(...)
    created_at: datetime.datetime = Field(alias='createdAt')


class DefaultUpdateUser(BaseModel):
    name: str = Field(...)
    job: str = Field(...)
    updated_at: datetime.datetime = Field(alias='updatedAt')


class DefaultRegister(BaseModel):
    id: int = Field(...)
    token: str = Field(...)


class DefaultLogin(BaseModel):
    token: str = Field(...)
