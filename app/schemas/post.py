from pydantic import BaseModel

class PostBase(BaseModel): # inheritance
    title : str  #encapsulation
    content : str

class PostUpdate(PostBase):
    pass

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True