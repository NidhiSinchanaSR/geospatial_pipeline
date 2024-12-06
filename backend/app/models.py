from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)