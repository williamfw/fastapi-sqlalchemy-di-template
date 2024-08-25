from infrastructure.dto.base_dto import BaseResponse, BaseRequest

class JobInsertRequest(BaseRequest):
    description: str
    customer_id: int
    
    class Config:
        orm_mode = True

class JobUpdateRequest(BaseRequest):
    id: int
    description: str
    customer_id: int
    
    class Config:
        orm_mode = True

class JobResponse(BaseResponse):
    id: int
    description: str
    is_completed: bool
    customer_id: int