from src.repository.recruiter_repository import RecruiterRepository
from src.schema.recruiter_schema import RecruiterResponse, DeleteRecruiterResponse
from cryptography.fernet import Fernet
import os
from typing import List

class RecruiterService:
    def __init__(self):
        ENC_KEY = os.getenv("ENC_KEY")
        self.cipher_suite = Fernet(ENC_KEY)

    def save(self, organization: str, email: str) -> None:
        """
        이메일을 암호화하여 저장합니다.
        """
        enc_email = self.cipher_suite.encrypt(email.encode()).decode()
        RecruiterRepository.store(organization, enc_email)

    def get_all(self) -> List[RecruiterResponse]:
        """
        모든 인사담당자 정보를 가져와 이메일을 복호화합니다.
        """
        recruiters = RecruiterRepository.get_all()

        results = []
        for r in recruiters:
            dec_email = self.cipher_suite.decrypt(r.enc_email.encode()).decode()
            results.append(
                RecruiterResponse(
                    id=r.id,
                    organization=r.organization,
                    email=dec_email,
                    created_at=r.created_at
                )
            )

        return results
    
    def delete(self, id: int) -> DeleteRecruiterResponse:
        """
        인사담당자 정보를 1개 삭제합니다.
        """
        is_deleted = RecruiterRepository.delete(id)
        return DeleteRecruiterResponse(is_deleted=is_deleted)