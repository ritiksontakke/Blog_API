from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserLogin
from app.repository.user import UserRepository


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

        return self.user_repository.create_user(
            self.db,
            user
        )

    def login_user(self, user: UserLogin):

        existing_user = self.user_repository.get_user_by_email(
            self.db,
            user.email
        )

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

    def get_all_users(self):

        return self.user_repository.get_all_users(
            self.db
        )

    def update_user(
        self,
        user_id: int,
        user_data: UserCreate
    ):

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