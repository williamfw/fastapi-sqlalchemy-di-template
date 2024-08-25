from fastapi import APIRouter, HTTPException
from domain.services.job_service import JobService
from domain.dto.job_dto import JobInsertRequest, JobUpdateRequest, JobResponse 

import inject

class JobController():

    @inject.autoparams()
    def __init__(self, job_service: JobService):
        self._service = job_service
        self._router = APIRouter()
        
        self._router.post("/customers/jobs/", response_model=JobResponse)(self.create)
        self._router.put("/customers/jobs/", response_model=JobResponse)(self.update)
        self._router.delete("/customers/jobs/{job_id}")(self.delete)
        self._router.get("/customers/{customer_id}/jobs/", response_model=list[JobResponse])(self.get_all)
        self._router.get("/customers/jobs/{job_id}", response_model=JobResponse)(self.get)
    
    async def create(self, job: JobInsertRequest):
        return await self._service.create(job)
    
    async def update(self, job: JobUpdateRequest):
        return await self._service.update(job)

    async def delete(self, job_id: int):
        return await self._service.delete(job_id)
    
    async def get_all(self, customer_id: int):
        return await self._service.get_all(customer_id)

    async def get(self, job_id: int):
        db_job = await self._service.get(job_id)
        if db_job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        return db_job