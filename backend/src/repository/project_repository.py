from src.database.mysql import get_mysql_db
from src.entity.project import Project

class ProjectRepository:
    @staticmethod
    def to_dict(r):
        return {
            "category": r.category,
            "name": r.name,
            "description": r.description,
            "start_date": r.start_date,
            "end_date": r.end_date,
            "notion_url": r.notion_url,
            "github_url": r.github_url
        }

    @classmethod
    def get_all(cls):
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            results = db.query(Project) \
                .with_entities(
                    Project.category,
                    Project.name,
                    Project.description,
                    Project.start_date,
                    Project.end_date,
                    Project.notion_url,
                    Project.github_url,
                ) \
                .all()
            
            return [cls.to_dict(r) for r in results]
        
    @classmethod
    def get_by_category(cls, category: str):
        """
        특정 분야에서 증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            results = db.query(Project) \
                .filter(Project.category==category) \
                .with_entities(
                    Project.category,
                    Project.name,
                    Project.description,
                    Project.start_date,
                    Project.end_date,
                    Project.notion_url,
                    Project.github_url,
                ) \
                .all()
            
            return [cls.to_dict(r) for r in results]