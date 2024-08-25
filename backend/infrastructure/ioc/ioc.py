from sqlalchemy.ext.asyncio import AsyncSession

from domain.interfaces.repositories.i_customer_repository import ICustomerRepository
from domain.database.repositories.customer_repository import CustomerRepository 

from domain.interfaces.repositories.i_job_repository import IJobRepository
from domain.database.repositories.job_repository import JobRepository

from domain.interfaces.services.i_customer_service import ICustomerService
from domain.interfaces.services.i_job_service import IJobService

from domain.services.customer_service import CustomerService
from domain.services.job_service import JobService

from infrastructure.database.database_session_manager import get_sync_session

import inject

class IoC():

    def config(self, binder):
        binder.bind_to_provider(AsyncSession, get_sync_session)
        
        binder.bind(ICustomerRepository, CustomerRepository)        
        binder.bind(ICustomerService, CustomerService)

        binder.bind(IJobRepository, JobRepository)        
        binder.bind(IJobService, JobService)

    def register_ioc(self):
        inject.configure(self.config)
