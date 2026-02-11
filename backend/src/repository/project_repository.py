from src.database.mysql import get_mysql_db
from src.entity.project import Project
from typing import List

class ProjectRepository:
    @staticmethod
    def get_all() -> List[Project]:
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            return db.query(Project).order_by(Project.start_date.asc()).all()
        
    @staticmethod
    def get_by_category(category: str) -> List[Project]:
        """
        특정 분야에서 증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            return db.query(Project).filter(Project.category==category).order_by(Project.start_date.asc()).all()
        
    @staticmethod
    def create(**kwargs) -> Project:
        """
        프로젝트 1개를 추가합니다.
        """
        with get_mysql_db() as db:
            new_project = Project(**kwargs)

            db.add(new_project)
            db.commit()
            db.refresh(new_project)

            return new_project

    @staticmethod
    def delete(id: int) -> bool:
        """
        프로젝트 1개를 삭제합니다.
        """
        with get_mysql_db() as db:
            n_deleted = db.query(Project).filter(Project.id==id).delete()

            if n_deleted > 0:
                return True
            
            return False

    @staticmethod
    def update(id: int, **kwargs) -> Project:
        """
        프로젝트 1개를 업데이트합니다.
        """
        with get_mysql_db() as db:
            project = db.query(Project).filter(Project.id==id).first()

            for key, value in kwargs:
                if hasattr(key, value) and value is not None:
                    setattr(project, key, value)

            db.commit()
            db.refresh(project)
            
            return project