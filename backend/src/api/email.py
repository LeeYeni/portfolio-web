from fastapi import APIRouter, Depends
from src.schema.email_schema import EmailRequest, EmailResponse
from src.service.email_service import EmailService

router = APIRouter(
    prefix = "/api/email",
    tags = ["Email"]
)

# 싱글톤 인스턴스
email_service = EmailService()

# 의존성 주입을 위한 함수
def get_email_service() -> EmailService:
    return email_service

@router.post("/", response_model=EmailResponse)
async def send_mail(
    request: EmailRequest,
    service: EmailService = Depends(get_email_service)
):
    """
    인사담당자에게 포트폴리오 요약본을 메일로 발송합니다.
    """
    await service.save_info_and_send_mail(request.organization, request.email)
    return EmailResponse(message="성공적으로 메일을 전송했습니다.")