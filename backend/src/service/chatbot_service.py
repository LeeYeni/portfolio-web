from langchain_core.output_parsers import JsonOutputParser
from src.client.gpt_client import GPTClient

class ChatbotService:
    def __init__(self):
        self.gpt_client = GPTClient()

    def start_chat(uuid: str) -> dict:
        """
        초기 환영 메시지를 반환합니다.
        """
        return {
            "message": "안녕하세요! 이예니님의 포트폴리오 AI 호스트입니다. 무엇을 도와드릴까요? ✨"
        }