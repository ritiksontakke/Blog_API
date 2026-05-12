from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate
)

class UserRepository:

    def create_user(
        self,
        db: Session,
        user: UserCreate
    ):

        new_user = User(
            name=user.name,
            username=user.username,
            email=user.email,
            password_hash=user.password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    def get_user_by_email(
        self,
        db: Session,
        email: str
    ):

        return db.query(User).filter(
            User.email == email
        ).first()

    def get_user(
        self,
        db: Session,
        user_id: int
    ):

        return db.query(User).filter(
            User.id == user_id
        ).first()

    def get_all_users(self, db: Session):

        return db.query(User).all()

    def update_user(
        self,
        db: Session,
        user_id: int,
        user_data: UserUpdate
    ):

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if not user:
            return None

        if user_data.name:
            user.name = user_data.name

        if user_data.username:
            user.username = user_data.username

        if user_data.email:
            user.email = user_data.email

        if user_data.password:
            user.password_hash = user_data.password

        db.commit()
        db.refresh(user)

        return user

    def delete_user(
        self,
        db: Session,
        user_id: int
    ):

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user