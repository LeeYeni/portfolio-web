from fastapi import APIRouter, Depends
from src.api.dependency import get_recruiter_service
from src.service.recruiter_service import RecruiterService
from src.schema.recruiter_schema import RecruiterResponse, DeleteRecruiterResponse
from typing import List

router = APIRouter(
    prefix="/api/recruiter",
    tags=["Recruiter"]
)

@router.get("/", response_model=List[RecruiterResponse])
def get_all(service: RecruiterService = Depends(get_recruiter_service)):
    """
    인사담당자 정보를 전부 조회합니다.
    """
    return service.get_all()