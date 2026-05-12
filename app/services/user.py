from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserUpdate
)
from app.repository.user import UserRepository

from app.auth.hashing import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import create_access_token


class UserService:

    def __init__(self, db: Session):

        self.db = db
        self.user_repository = UserRepository()

    def create_user(self, user: UserCreate):

        existing_user = self.user_repository.get_user_by_email(
            self.db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        # Password Hashing
        user.password = hash_password(
            user.password
        )

        return self.user_repository.create_user(
            self.db,
            user
        )

    def login_user(self, email: str, password: str):

        existing_user = self.user_repository.get_user_by_email(
            self.db,
            email,
        )

        if not existing_user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Password Verify
        if not verify_password(
            password,
            existing_user.password_hash
        ):

            raise HTTPException(
                status_code=400,
                detail="Invalid password"
            )

        # JWT Token
        access_token = create_access_token({
            "user_id": existing_user.id,
            "role" : "admin"
        })

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    def get_user(self, user_id: int):

        user = self.user_repository.get_user(
            self.db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    def update_user(
        self,
        user_id: int,
        user_data: UserUpdate
    ):

        # Hash Password While Updating
        if user_data.password:

            user_data.password = hash_password(
                user_data.password
            )

        user = self.user_repository.update_user(
            self.db,
            user_id,
            user_data
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    def delete_user(self, user_id: int):

        user = self.user_repository.delete_user(
            self.db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "message": "User deleted successfully"
        }