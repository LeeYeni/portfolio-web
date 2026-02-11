from pydantic import BaseModel

class EmailRequest(BaseModel):
    organization: str
    email: str

class EmailResponse(BaseModel):
    message: str