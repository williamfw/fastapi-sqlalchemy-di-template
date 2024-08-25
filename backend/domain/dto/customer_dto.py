from typing import List, Optional
from infrastructure.dto.base_dto import BaseResponse, BaseRequest
from domain.dto.job_dto import JobResponse

class CustomerInsertRequest(BaseRequest):
    name: str
    email: str
    phone_number: str
    is_active: bool

    class Config:
        orm_mode = True

class CustomerUpdateRequest(BaseRequest):
    id: int
    name: str
    email: str
    phone_number: str
    is_active: bool

    class Config:
        orm_mode = True

class CustomerResponse(BaseResponse):
    id: int
    name: str
    email: str
    phone_number: str
    is_active: bool

    #jobs: Optional[List[JobResponse]] = None
    