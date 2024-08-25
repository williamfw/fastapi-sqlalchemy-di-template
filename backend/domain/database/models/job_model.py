from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.model.base_model import BaseModel

class Job(BaseModel):
    __tablename__ = "jobs"
    
    description = Column(String)
    is_completed = Column(Boolean, default=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="jobs")