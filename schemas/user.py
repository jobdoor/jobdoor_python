from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    name: str
    age: int


# Properties to receive via API on creation
class UserCreate(UserBase):
    pass


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True
        
# Additional properties to return via API
class User(UserInDBBase):
    pass





