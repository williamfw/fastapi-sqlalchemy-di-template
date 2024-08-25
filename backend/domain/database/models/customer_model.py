from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from infrastructure.model.base_model import BaseModel

class Customer(BaseModel):
    __tablename__ = "customers"

    name = Column(String)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)

    jobs = relationship("Job", back_populates="customer")
    