from fastapi import APIRouter, Depends
from src.schema.guest_schema import GuestBookRequest, GuestBookResponse, NicknameResponse
from typing import List
from src.service.guest_service import GuestService, GuestBookService
from src.api.dependency import get_guest_service, get_guestbook_service

router = APIRouter(
    prefix="/api/guest",
    tags=["Guest"]
)

@router.post("/nickname", response_model=NicknameResponse)
async def read_nickname(service: GuestService = Depends(get_guest_service)):
    """
    인사담당자에게 guest_id, AI가 생성한 닉네임을 제공합니다.
    """
    return await service.save_and_get_guest_info()

@router.post("/guestbook")
def save_guestbook(
    request: GuestBookRequest,
    service: GuestBookService = Depends(get_guestbook_service)
):
    """
    전달받은 guest_id를 기반으로 방명록 메시지를 저장합니다.
    """
    return service.save_guestbook_message(request.uuid, request.message)

@router.get("/", response_model=List[GuestBookResponse])
def read_guestbook(service: GuestBookService = Depends(get_guestbook_service)):
    """
    지금까지 모든 방명록 메시지를 최신순으로 조회합니다.
    """
    return service.get_guestbook_messages()