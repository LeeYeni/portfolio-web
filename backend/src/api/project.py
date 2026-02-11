from fastapi import APIRouter
from src.service.project_service import ProjectService
from src.schema.project_schema import ProjectResponse
from typing import List

router = APIRouter(
    prefix="/api/project",
    tags=["Project"]
)

@router.get("/all", response_model=List[ProjectResponse])
def read_all_project():
    """
    모든 프로젝트를 제공합니다.
    """
    return ProjectService.get_all()

@router.get("/category/{category}", response_model=List[ProjectResponse])
def read_project(category: str):
    """
    특정 분야의 프로젝트를 제공합니다.
    """
    return ProjectService.get_by_category(category)