from datetime import datetime
from sqlalchemy import ForeignKey, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class Post(Base):
    __tablename__ = "posts"

    id : Mapped[int] = mapped_column(primary_key=True, index=True)

    title : Mapped[str] = mapped_column(String, nullable=False)

    content : Mapped[str] = mapped_column(String, nullable=False)

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))

    created_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # models/post.py

    user = relationship("User",back_populates="posts")

    comments = relationship("Comment",back_populates="post")