from typing import  List
from abc import abstractmethod, ABC
from domain.database.models.customer_model import Customer

class ICustomerRepository(ABC):
    
    @abstractmethod
    async def get_customer_by_email(self, email: str) -> Customer | None:
        pass
