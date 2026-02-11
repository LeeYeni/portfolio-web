from fastapi import APIRouter, Depends
from src.api.dependency import get_recruiter_service
from src.service.recruiter_service import RecruiterService
from src.service.project_service import ProjectService
from src.service.credential_service import CredentialService
from src.schema.recruiter_schema import DeleteRecruiterResponse
from src.schema.project_schema import (
    ProjectResponse,
    AddProjectRequest,
    UpdateProjectRequest,
    DeleteProjectResponse
)
from src.schema.credential_schema import (
    CredentialResponse,
    AddCredentialRequest,
    UpdateCredentialRequest,
    DeleteCredentialResponse
)

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)

@router.delete("/recruiter/{id}", response_model=DeleteRecruiterResponse)
def delete(
    id: int,
    service: RecruiterService = Depends(get_recruiter_service)
):
    """
    인사담당자 정보를 1개 삭제합니다.
    """
    return service.delete(id)

@router.post("/project", response_model=ProjectResponse)
def add(request: AddProjectRequest):
    """
    프로젝트 1개를 추가합니다.
    """
    return ProjectService.add(request.model_dump())

@router.delete("/project/{id}", response_model=DeleteProjectResponse)
def delete(id: int):
    """
    프로젝트 1개를 삭제합니다.
    """
    return ProjectService.delete(id)

@router.patch("/project", response_model=ProjectResponse)
def update(request: UpdateProjectRequest):
    """
    프로젝트 1개를 업데이트합니다.
    """
    data = request.model_dump(exclude_unset=True)
    id = data.pop("id")
    return ProjectService.update(id, **data)

@router.post("/credential", response_model=CredentialResponse)
def add_credentials(request: AddCredentialRequest):
    """
    증명 가능한 이력을 추가합니다.
    """
    return CredentialService.add(**request.model_dump())

@router.delete("/credential/{id}", response_model=DeleteCredentialResponse)
def delete_credentials(id: int):
    """
    증명 가능한 이력을 삭제합니다.
    """
    return CredentialService.delete(id)

@router.patch("/credential", response_model=CredentialResponse)
def update_credentials(request: UpdateCredentialRequest):
    """
    증명 가능한 이력을 수정합니다.
    """
    data = request.model_dump(exclude_unset=True)
    id = data.pop("id")
    return CredentialService.update(id=id, **data)