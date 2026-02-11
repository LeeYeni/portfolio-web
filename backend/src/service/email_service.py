import os
import smtplib
from email.mime.text import MIMEText
import asyncio

class EmailService:
    def __init__(self, recruiter_service):
        self.recruiter_service = recruiter_service
        self.NAVER_ID = os.getenv("NAVER_ID")
        self.NAVER_PASSWORD = os.getenv("NAVER_PASSWORD")

    async def save_info_and_send_mail(self, organization: str, email: str) -> None:
        """
        인사담당자 정보 저장 및 포트폴리오 요약본 전송을 백그라운드에서 처리합니다.
        """
        # 인사담당자 정보 저장
        asyncio.create_task(self.recruiter_service.save(organization, email))

        # 메일 전송
        asyncio.create_task(self.send_mail(organization, email))

    async def send_mail(self, organization: str, email: str) -> None:
        """"""
        # 메시지 구성
        msg = MIMEText(f"{organization} 담당자님, 안녕하세요! 포트폴리오 요약본입니다.")
        msg["Subject"] = f"[{organization}] 이예니 포트폴리오 관련 메일입니다."
        msg["From"] = f"{self.NAVER_ID}@naver.com"
        msg["To"] = email

        def execute():
            with smtplib.SMTP("smtp.naver.com", 587, timeout=10) as server:
                server.starttls()
                server.login(self.NAVER_ID, self.NAVER_PASSWORD)
                server.sendmail(msg["From"], msg["To"], msg.as_string())

        await asyncio.to_thread(execute)