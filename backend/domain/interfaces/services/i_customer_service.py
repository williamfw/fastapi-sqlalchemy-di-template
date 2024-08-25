from typing import  List
from abc import abstractmethod, ABC
from domain.database.models.customer_model import Customer
from domain.dto.customer_dto import CustomerInsertRequest, CustomerUpdateRequest

class ICustomerService(ABC):
    
    @abstractmethod
    async def get(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    async def create(self, customer: CustomerInsertRequest) -> Customer:
        pass

    @abstractmethod
    async def update(self, customer: CustomerUpdateRequest) -> Customer:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Customer]:
        pass

    @abstractmethod
    async def delete(self, customer_id: int) -> bool:
        pass