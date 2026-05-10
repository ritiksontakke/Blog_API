from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate


# class 

def create_user(db : Session, user : UserCreate):

    new_user = User(
        name = user.name,
        username = user.username,
        email = user.email,
        password_hash = user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user_by_email(db : Session, email : str):
    return db.query(User).filter(User.email == email).first()

def get_user(db : Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session):

    return db.query(User).all

def update_user(db : Session, user_id : int, user_data : UserCreate):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None
    
    user.name = user_data.name
    user.username = user_data.username
    user.email = user_data.email
    user.password_hash = user_data.password

    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, user_id: int):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user