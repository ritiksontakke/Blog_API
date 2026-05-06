from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin , UserResponse
from app.db.dependency import get_db

UserRouter = APIRouter(
    tags=["Users"]
)

@UserRouter.post("/create_account")
def CreateAccount():
    return("account is created")

@UserRouter.post("login")
def LoginAccount():
    return("user login succefully")

@UserRouter.get("/{user_id}")
def GetUser(user_id : int):
    return("user")

@UserRouter.get("/")
def GetAllUser():
    return("aa")

@UserRouter.put("{user_id}")
def UpdateUser(user_id : int):
    return ("aa")

@UserRouter.delete("/{user_id}")
def delete_user(user_id: int):

    return {
        "message": f"User {user_id} deleted"
    }