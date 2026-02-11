from fastapi import APIRouter
from src.schema.credential_schema import CredentialResponse
from src.service.credential_service import CredentialService
from typing import List

router = APIRouter(
    prefix="/api/credential",
    tags=["Credential"]
)

@router.get("/all", response_model=List[CredentialResponse])
def get_all_credentials():
    """
    증명 가능한 모든 것들을 제공합니다.
    """
    return CredentialService.get_all()

@router.get("/category/{category}", response_model=List[CredentialResponse])
def get_credentials(category: str):
    """
    특정 분야 내에서 증명 가능한 모든 것들을 제공합니다.
    """
    return CredentialService.get_by_category(category)