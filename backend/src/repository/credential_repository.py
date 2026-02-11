from src.database.mysql import get_mysql_db
from src.entity.credential import Credential

class CredentialRepository:
    @staticmethod
    def to_dict(r):
        return {
            "category": r.category,
            "name": r.name,
            "description": r.description,
            "issuer": r.issuer,
            "issued_date": r.issued_date,
            "pdf_url": r.pdf_url,
            "notion_url": r.notion_url
        }

    @classmethod
    def get_all(cls):
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            results = db.query(Credential) \
                .with_entities(
                    Credential.category,
                    Credential.name,
                    Credential.description,
                    Credential.issuer,
                    Credential.issued_date,
                    Credential.pdf_url,
                    Credential.notion_url
                ) \
                .all()
            
            return [cls.to_dict(r) for r in results]
        
    @classmethod
    def get_by_category(cls, category: str):
        """
        특정 분야에서 증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            results = db.query(Credential) \
                .filter(Credential.category==category) \
                .with_entities(
                    Credential.category,
                    Credential.name,
                    Credential.description,
                    Credential.issuer,
                    Credential.issued_date,
                    Credential.pdf_url,
                    Credential.notion_url
                ) \
                .all()
            
            return [cls.to_dict(r) for r in results]