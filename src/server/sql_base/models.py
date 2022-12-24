from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int]


class Expedition(BaseModelModify):
    firm_id: int
    date: str
    location: str


class Firm(BaseModelModify):
    title: str
    location: str


class Fossil(BaseModelModify):
    expedition_id: int
    name: str
    date: str
    age: str
    quantity: int


class Personnel(BaseModelModify):
    position_id: int
    user_id: Optional[int]
    name: str
    surname: str
    phone: str
    date: str


class Position(BaseModelModify):
    post: str


class User(BaseModelModify):
    personnel_id: int
    login: str
    password: str
