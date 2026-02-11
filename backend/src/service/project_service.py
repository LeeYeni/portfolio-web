from src.repository.project_repository import ProjectRepository
from src.schema.project_schema import ProjectResponse
from typing import List

class ProjectService:
    @staticmethod
    def get_all() -> List[ProjectResponse]:
        """
        모든 프로젝트를 조회합니다.
        """
        results = ProjectRepository.get_all()
        return [ProjectResponse(**r) for r in results]

    @staticmethod
    def get_by_category(category: str) -> List[ProjectResponse]:
        """
        특정 분야의 프로젝트를 조회합니다.
        """
        results = ProjectRepository.get_by_category(category)
        return [ProjectResponse(**r) for r in results]