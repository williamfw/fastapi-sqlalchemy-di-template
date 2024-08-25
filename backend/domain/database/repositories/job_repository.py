from typing import List
from infrastructure.repository.base_repository import BaseRepository
from domain.interfaces.repositories.i_job_repository import IJobRepository
from domain.database.models.job_model import Job
from sqlalchemy import select

class JobRepository(BaseRepository[Job], IJobRepository):
    
    def __init__(self):
        super().__init__(model=Job)

    async def get_all(self, customer_id: int, skip: int, limit: int) -> List[Job] | None:
        async with self.session as session:
            statement = select(self.model).where(self.model.customer_id==customer_id).offset(skip).limit(limit)
            result = await session.execute(statement)
            return result.scalars().all()