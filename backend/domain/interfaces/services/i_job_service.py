from typing import  List
from abc import abstractmethod, ABC
from domain.dto.job_dto import JobInsertRequest, JobUpdateRequest
from domain.database.models.job_model import Job

class IJobService(ABC):
    
    @abstractmethod
    async def get(self, job_id: int) -> Job:
        pass

    @abstractmethod
    async def create(self, job: JobInsertRequest) -> Job:
        pass

    @abstractmethod
    async def update(self, job: JobUpdateRequest) -> Job:
        pass
    
    @abstractmethod
    async def delete(self, job_id: int) -> bool:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Job]:
        pass