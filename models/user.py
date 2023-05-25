from sqlalchemy import Boolean
from typing import Optional

from sqlmodel import Field, SQLModel
from db.base import Base


class User(Base):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: Optional[int] = None