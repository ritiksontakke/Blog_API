from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)
    name : Mapped[str] = mapped_column(String)
    username : Mapped[str] = mapped_column(String)
    email : Mapped[str] = mapped_column(String, unique = True, nullable = False)
    password_hash : Mapped[str] = mapped_column(String, nullable= False)

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # models/user.py

    posts = relationship("Post", back_populates="user")

    comments = relationship("Comment", back_populates="user")