from fastapi import FastAPI
from . import models, crud
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/features/")
def read_features(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_features(db, skip=skip, limit=limit)