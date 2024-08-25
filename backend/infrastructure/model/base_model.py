from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

class BaseModel(declarative_base()):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, onupdate=datetime.now)