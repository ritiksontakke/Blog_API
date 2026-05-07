# services/user.py

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin
from app.repository.user import (
    create_user,
    get_user,
    get_all_users,
    update_user,
    delete_user,
    get_user_by_email
)


def create_user_service(db: Session, user: UserCreate):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return create_user(db, user)


def login_user_service(db: Session, user: UserLogin):

    existing_user = get_user_by_email(db, user.email)

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if existing_user.password_hash != user.password:
        raise HTTPException(
            status_code=400,
            detail="Invalid password"
        )

    return {
        "message": "Login Successful"
    }


def get_user_service(db: Session, user_id: int):

    user = get_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def get_all_users_service(db: Session):

    return get_all_users(db)


def update_user_service(
    db: Session,
    user_id: int,
    user_data: UserCreate
):

    user = update_user(db, user_id, user_data)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def delete_user_service(db: Session, user_id: int):

    user = delete_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }