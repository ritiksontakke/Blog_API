from pydantic import BaseModel , EmailStr , field_validator
from typing import Optional


# Inheritance

class UserBase(BaseModel):
    name : str 
    username : str
    email : EmailStr

class UserCreate(UserBase):
    password : str

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):

        if len(value) < 8 :
            raise ValueError("Password to short")
        return value

class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserResponse(UserBase):
    id : int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):

    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
