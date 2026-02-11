from fastapi import APIRouter
from src.schema.chatbot_schema import ChatRequest, ChatbotResponse
# from src.service.chatbot_service import ChatbotService

router = APIRouter(
    prefix="/api/chatbot",
    tags=["Chatbot"]
)

@router.post("/start", response_model=ChatbotResponse)
def read_chatbot_start():
    # chatbot_response = ChatbotService.start_chat()
    # return chatbot_response
    return {"message": "안녕하세요! 포트폴리오 챗봇입니다!"}

@router.post("/", response_model=ChatbotResponse)
async def read_chatbot(request: ChatRequest):
    # chatbot_response = await ChatbotService.get_chatbot_response(request.guest_id, request.prompt)
    return {"message": "안녕하세요! 포트폴리오 챗봇입니다!"}