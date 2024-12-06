from sqlalchemy.orm import Session
from . import models

def get_features(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Feature).offset(skip).limit(limit).all()