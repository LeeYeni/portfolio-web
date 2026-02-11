from pydantic import BaseModel
from datetime import datetime

class GuestBookRequest(BaseModel):
    uuid: str
    message: str

class GuestBookResponse(BaseModel):
    nickname: str
    message: str
    created_at: datetime

class NicknameResponse(BaseModel):
    uuid: str
    nickname: str