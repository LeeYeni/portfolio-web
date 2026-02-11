from dotenv import load_dotenv
import os
from src.database.mysql import get_mysql_db
from src.entity.recruiter import Recruiter
from cryptography.fernet import Fernet
from sqlalchemy import and_

load_dotenv()
ENC_KEY = os.getenv("ENC_KEY")
cipher_suite = Fernet(ENC_KEY)

class RecuiterRepository:
    @staticmethod
    def store(organization: str, email: str):
        """
        이메일을 암호화하여, 인사담당자 정보를 저장합니다.
        """
        enc_email = cipher_suite.encrypt(email.encode()).decode()

        with get_mysql_db() as db:
            existing = db.query(Recruiter).filter(
                and_(
                    Recruiter.organization == organization,
                    Recruiter.enc_email == enc_email
                )
            ).first()

            if not existing:
                new_recruiter = Recruiter(
                    organization=organization,
                    enc_email=enc_email
                )

                db.add(new_recruiter)
                db.commit()