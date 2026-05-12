from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)

from app.db.dependency import get_db

from app.services.user import UserService

from app.auth.current_user import get_current_user


UserRouter = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@UserRouter.post(
    "/create-account",
    response_model=UserResponse
)
def create_account(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    user_service = UserService(db)

    return user_service.create_user(user)


@UserRouter.post("/login")
def login_account(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user_service = UserService(db)

    return user_service.login_user(
        request.username,
        request.password
    )


# Protected Route
@UserRouter.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    user_service = UserService(db)

    return user_service.get_user(user_id)


# Protected Route
@UserRouter.put("/{user_id}")
def update_user(
    user_id: int,
    user_data: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    user_service = UserService(db)

    return user_service.update_user(
        user_id,
        user_data
    )


# Protected Route
@UserRouter.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    user_service = UserService(db)

    return user_service.delete_user(user_id)