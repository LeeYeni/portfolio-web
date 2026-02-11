from src.repository.credential_repository import CredentialRepository
from src.schema.credential_schema import CredentialResponse
from typing import List

class CredentialService:
    @staticmethod
    def get_all() -> List[CredentialResponse]:
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        results = CredentialRepository.get_all()
        return [CredentialResponse(**r) for r in results]

    @staticmethod
    def get_by_category(category: str) -> List[CredentialResponse]:
        """
        특정 분야의 증명 가능한 이력을 조회합니다.
        """
        results = CredentialRepository.get_by_category(category)
        return [CredentialResponse(**r) for r in results]