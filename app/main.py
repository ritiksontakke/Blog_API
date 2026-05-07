# app/main.py

from fastapi import FastAPI

from app.db.database import Base, engine

from app.routers.user import UserRouter
from app.routers.post import PostRouter
from app.routers.comment import CommentRouter


app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(UserRouter)

app.include_router(PostRouter)

app.include_router(CommentRouter)