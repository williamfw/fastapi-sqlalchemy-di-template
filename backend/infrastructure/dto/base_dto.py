from datetime import datetime
from pydantic import BaseModel

class BaseRequest(BaseModel):
    pass

class BaseResponse(BaseModel):
    creation_date: datetime
    update_date: None | datetime   
