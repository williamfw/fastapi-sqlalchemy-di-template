from fastapi import APIRouter

from domain.dto.customer_dto import CustomerInsertRequest, CustomerUpdateRequest, CustomerResponse 
from domain.services.customer_service import CustomerService  

import inject

class CustomerController():
    
    @inject.autoparams()
    def __init__(self, customer_service: CustomerService):
        self._customer_service = customer_service
        self._router = APIRouter()

        self._router.post("/customers/", response_model=CustomerResponse)(self.create)
        self._router.put("/customers/", response_model=CustomerResponse)(self.update)
        self._router.get("/customers/", response_model=list[CustomerResponse])(self.get_all)
        self._router.get("/customers/{customer_id}", response_model=CustomerResponse)(self.get)
        self._router.delete("/customers/{customer_id}")(self.delete)

    async def create(self, customer: CustomerInsertRequest):
        return await self._customer_service.create(customer)
    
    async def update(self, customer: CustomerUpdateRequest):
        return await self._customer_service.update(customer)

    async def get_all(self, skip: int = 0, limit: int = 100):
        return await self._customer_service.get_all(skip=skip, limit=limit)

    async def get(self, customer_id: int):
        return await self._customer_service.get(customer_id=customer_id)
    
    async def delete(self, customer_id: int):
        return await self._customer_service.delete(customer_id)
    