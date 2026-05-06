from pydantic import BaseModel , EmailStr , field_validator

# Inheritance

class UserBase(BaseModel):
    username : str
    email : EmailStr

class UserCreate(UserBase):
    password : str

    @field_validator
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