from src.repository.guestbook_repository import GuestBookRepository
from src.repository.guest_repository import GuestRepository
from src.client.gpt_client import GPTClient
from src.schema.guest_schema import GuestBookResponse, NicknameResponse
from langchain_core.output_parsers import JsonOutputParser
from uuid import uuid4
from typing import List
import asyncio

class GuestService:
    def __init__(self):
        self.nickname_service = NicknameService()

    def save_uuid_and_nickname(self, uuid: str, nickname: str) -> None:
        """
        uuid와 닉네임을 저장합니다.
        """
        GuestRepository.save(uuid, nickname)

    async def save_and_get_guest_info(self) -> NicknameResponse:
        """
        uuid와 닉네임을 저장 및 반환합니다.
        """
        uuid = str(uuid4())
        nickname = await self.nickname_service.get_available_nickname()

        # uuid 및 닉네임 캐싱
        self.save_uuid_and_nickname(uuid, nickname)

        return NicknameResponse(
            uuid=uuid,
            nickname=nickname
        )
    


class NicknameService:
    def __init__(self):
        self.gpt_client = GPTClient()

    async def generate_and_cache_nickname(self) -> None:
        """
        닉네임 다섯 개를 생성 후 캐싱합니다.
        """
        # 닉네임 생성
        response = await self.gpt_client.get_response(
            prompt_name="generate_nickname",
            input_data={},
            output_parser=JsonOutputParser
        )

        # 닉네임 캐싱
        nicknames = response.get("nicknames", [])
        if nicknames:
            GuestRepository.save_nicknames(nicknames)

    async def get_available_nickname(self) -> str:
        """
        Valkey(Redis)에서 닉네임을 꺼내옵니다.
        """
        nickname = GuestRepository.pop_nickname()

        # 캐싱된 닉네임이 5개 이하라면, 닉네임 추가 캐싱
        current_count = GuestRepository.get_nickname_count()
        if current_count < 5:
            asyncio.create_task(self.generate_and_cache_nickname())

        # 캐싱된 닉네임이 없는 경우를 대비
        return nickname if nickname else "코딩하는 개발자"

    
    
class GuestBookService:
    @staticmethod
    def save_guestbook_message(uuid: str, message: str) -> None:
        """
        방명록을 저장합니다.
        """
        GuestBookRepository.save(uuid, message)

    @staticmethod
    def get_guestbook_messages() -> List[GuestBookResponse]:
        """
        방명록을 전부 조회합니다.
        """
        results = GuestBookRepository.get_all()
        return [GuestBookResponse.model_validate(r) for r in results]