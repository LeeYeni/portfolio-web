from pydantic import BaseModel, HttpUrl, ConfigDict
from src.entity.credential import CredentialCategory
from datetime import date
from typing import Optional

class CredentialBase(BaseModel):
    category: CredentialCategory
    name: str
    description: Optional[str] = None
    issuer: str
    issued_date: date
    pdf_url: HttpUrl
    notion_url: Optional[HttpUrl] = None

class AddCredentialRequest(CredentialBase):
    pass

class UpdateCredentialRequest(CredentialBase):
    id: int
    category: Optional[CredentialCategory] = None
    name: Optional[str] = None
    issuer: Optional[str] = None
    issued_date: Optional[date] = None
    pdf_url: Optional[HttpUrl] = None

class CredentialResponse(CredentialBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DeleteCredentialResponse(BaseModel):
    is_deleted: bool