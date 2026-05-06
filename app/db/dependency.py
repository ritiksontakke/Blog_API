from db.database import SessionLocal
from models import teacher

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()