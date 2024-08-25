from fastapi import HTTPException
from typing import List
from domain.database.models.customer_model import Customer
from domain.interfaces.services.i_customer_service import ICustomerService
from domain.dto.customer_dto import CustomerInsertRequest, CustomerUpdateRequest
from domain.database.repositories.customer_repository import CustomerRepository

import inject

class CustomerService(ICustomerService):

    @inject.autoparams()
    def __init__(self, repository: CustomerRepository):
        self._repository = repository

    async def get(self, customer_id: int) -> Customer:
        db_customer = await self._repository.get(customer_id)
        if db_customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")
        return db_customer

    async def create(self, customer: CustomerInsertRequest) -> Customer:
        db_customer = await self._repository.get_customer_by_email(email=customer.email)
        if db_customer:
            raise HTTPException(status_code=400, detail="Email already registered")
        return await self._repository.create(data=customer.model_dump())
    
    async def update(self, customer: CustomerUpdateRequest) -> Customer:
        db_customer = await self._repository.get_customer_by_email(email=customer.email)
        if db_customer and db_customer.email != customer.email:
            raise HTTPException(status_code=400, detail="Email already registered")
        return await self._repository.update(data=customer.model_dump())

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Customer] | None:
        return await self._repository.get_all(skip=skip, limit=limit)

    async def delete(self, customer_id: int) -> bool:
        return await self._repository.delete(customer_id)

        
