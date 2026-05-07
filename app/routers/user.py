# app/routers/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)

from app.db.dependency import get_db

from app.services.user import (
    create_user_service,
    login_user_service,
    get_user_service,
    get_all_users_service,
    update_user_service,
    delete_user_service
)


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

    return create_user_service(db, user)


@UserRouter.post("/login")
def login_account(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    return login_user_service(db, user)


@UserRouter.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_user_service(db, user_id)


@UserRouter.get("/")
def get_all_users(
    db: Session = Depends(get_db)
):

    return get_all_users_service(db)


@UserRouter.put("/{user_id}")
def update_user(
    user_id: int,
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    return update_user_service(
        db,
        user_id,
        user_data
    )


@UserRouter.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return delete_user_service(db, user_id)