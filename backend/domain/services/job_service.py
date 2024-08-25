from fastapi import HTTPException
from typing import List
from domain.database.models.job_model import Job
from domain.interfaces.services.i_job_service import IJobService
from domain.dto.job_dto import JobInsertRequest, JobUpdateRequest
from domain.database.repositories.job_repository import JobRepository

import inject

class JobService(IJobService):

    @inject.autoparams()
    def __init__(self, repository: JobRepository):
        self._repository = repository

    async def create(self, job: JobInsertRequest) -> Job:
        return await self._repository.create(data=job.model_dump())
    
    async def update(self, job: JobUpdateRequest) -> Job:
        return await self._repository.update(data=job.model_dump())
    
    async def delete(self, job_id: int) -> bool | None:
        return await self._repository.delete(job_id)

    async def get(self, job_id: int) -> Job | None:
        db_job = await self._repository.get(job_id)
        if db_job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        return db_job

    async def get_all(self, customer_id: int, skip: int = 0, limit: int = 100) -> List[Job] | None:
        db_jobs = await self._repository.get_all(customer_id, skip, limit)
        return db_jobs        
