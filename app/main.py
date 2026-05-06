from fastapi import FastAPI
from app.db.database import Base,engine
from app.routers.user import UserRouter

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(UserRouter)