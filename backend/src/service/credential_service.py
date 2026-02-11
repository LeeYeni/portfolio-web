from src.repository.credential_repository import CredentialRepository
from src.schema.credential_schema import CredentialResponse, DeleteCredentialResponse
from typing import List

class CredentialService:
    @staticmethod
    def get_all() -> List[CredentialResponse]:
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        results = CredentialRepository.get_all()
        return [CredentialResponse.model_validate(r) for r in results]

    @staticmethod
    def get_by_category(category: str) -> List[CredentialResponse]:
        """
        특정 분야의 증명 가능한 이력을 조회합니다.
        """
        results = CredentialRepository.get_by_category(category)
        return [CredentialResponse.model_validate(r) for r in results]
    
    @staticmethod
    def add(**data) -> CredentialResponse:
        """
        증명 가능한 이력을 1개 추가합니다.
        """
        new_credential = CredentialRepository.create(**data)
        return CredentialResponse.model_validate(new_credential)
    
    @staticmethod
    def delete(id: int) -> DeleteCredentialResponse:
        """
        증명 가능한 이력을 1개 삭제합니다.
        """
        is_deleted = CredentialRepository.delete(id)
        return DeleteCredentialResponse(is_deleted=is_deleted)
    
    @staticmethod
    def update(id: int, **data) -> CredentialResponse:
        """
        증명 가능한 이력을 1개 업데이트합니다.
        """
        updated_credential = CredentialRepository.update(id, **data)
        return CredentialResponse.model_validate(updated_credential)