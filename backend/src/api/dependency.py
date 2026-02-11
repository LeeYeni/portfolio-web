from src.service.email_service import EmailService
from src.service.guest_service import GuestService, GuestBookService
from src.service.recruiter_service import RecruiterService

# 싱글톤 인스턴스
recruiter_service = RecruiterService()
email_service = EmailService(recruiter_service)
guest_service = GuestService()
guestbook_service = GuestBookService()

# 의존성 주입을 위한 함수
def get_email_service() -> EmailService:
    return email_service

def get_guest_service() -> GuestService:
    return guest_service

def get_guestbook_service() -> GuestBookService:
    return guestbook_service

def get_recruiter_service() -> RecruiterService:
    return recruiter_service