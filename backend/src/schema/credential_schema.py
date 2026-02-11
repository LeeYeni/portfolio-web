from pydantic import BaseModel

class CredentialResponse(BaseModel):
    category: str
    name: str
    description: str
    issuer: str
    issued_date: str
    pdf_url: str
    notion_url: str