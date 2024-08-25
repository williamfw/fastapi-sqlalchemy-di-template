from infrastructure.repository.base_repository import BaseRepository

from domain.database.models.customer_model import Customer
from domain.interfaces.repositories.i_customer_repository import ICustomerRepository
from sqlalchemy import select

class CustomerRepository(BaseRepository[Customer], ICustomerRepository):
    
    def __init__(self):
        super().__init__(model=Customer)
    
    async def get_customer_by_email(self, email: str) -> Customer | None:
        async with self.session as session:
            statement = select(Customer).where(Customer.email==email)
            return await session.scalar(statement)
