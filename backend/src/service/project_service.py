from src.repository.project_repository import ProjectRepository
from src.schema.project_schema import ProjectResponse, DeleteProjectResponse
from typing import List

class ProjectService:
    @staticmethod
    def get_all() -> List[ProjectResponse]:
        """
        모든 프로젝트를 조회합니다.
        """
        results = ProjectRepository.get_all()
        return [ProjectResponse.model_validate(r) for r in results]

    @staticmethod
    def get_by_category(category: str) -> List[ProjectResponse]:
        """
        특정 분야의 프로젝트를 조회합니다.
        """
        results = ProjectRepository.get_by_category(category)
        return [ProjectResponse.model_validate(r) for r in results]
    
    @staticmethod
    def add(**data) -> ProjectResponse:
        """
        프로젝트 1개를 추가합니다.
        """
        new_project = ProjectRepository.create(**data)
        return ProjectResponse.model_validate(new_project)
    
    @staticmethod
    def delete(id: int) -> DeleteProjectResponse:
        """
        프로젝트 1개를 삭제합니다.
        """
        is_deleted = ProjectRepository.delete(id)
        return DeleteProjectResponse(is_deleted=is_deleted)
    
    @staticmethod
    def update(id: int, **data) -> ProjectResponse:
        """
        프로젝트 1개를 업데이트합니다.
        """
        project = ProjectRepository.update(id, **data)
        return ProjectResponse.model_validate(project)