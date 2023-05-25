from sqlalchemy import Boolean
from typing import Optional

from sqlalchemy import Boolean, Column, Integer, String
from db.base_class import Base

class User(Base):
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    age= Column(Integer)