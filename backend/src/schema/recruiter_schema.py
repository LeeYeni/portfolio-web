from pydantic import BaseModel
from datetime import datetime

class RecruiterResponse(BaseModel):
    id: int
    organization: str
    email: str
    created_at: datetime

class DeleteRecruiterResponse(BaseModel):
    is_deleted: bool