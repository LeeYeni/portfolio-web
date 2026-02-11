from pydantic import BaseModel

class ChatRequest(BaseModel):
    uuid: str
    prompt: str

class ChatbotResponse(BaseModel):
    message: str