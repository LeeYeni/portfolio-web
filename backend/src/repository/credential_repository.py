from src.database.mysql import get_mysql_db
from src.entity.credential import Credential
from typing import List

class CredentialRepository:
    @staticmethod
    def get_all() -> List[Credential]:
        """
        증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            return db.query(Credential).order_by(Credential.issued_date.asc()).all()
        
    @staticmethod
    def get_by_category(category: str) -> List[Credential]:
        """
        특정 분야에서 증명 가능한 모든 이력을 조회합니다.
        """
        with get_mysql_db() as db:
            return db.query(Credential).filter(Credential.category==category.asc()).all()
        
    @staticmethod
    def create(**kwargs) -> Credential:
        """
        증명 가능한 이력 1개를 추가합니다.
        """
        with get_mysql_db() as db:
            new_credential = Credential(**kwargs)

            db.add(new_credential)
            db.commit()
            db.refresh(new_credential)

            return new_credential

    @staticmethod
    def delete(id: int) -> bool:
        """
        증명 가능한 이력 1개를 삭제합니다.
        """
        with get_mysql_db() as db:
            n_deleted = db.query(Credential).filter(Credential.id==id).delete()

            if n_deleted > 0:
                db.commit()
                return True
            
            return False

    @staticmethod
    def update(id: int, **kwargs) -> Credential:
        """
        증명 가능한 이력 1개를 업데이트합니다.
        """
        with get_mysql_db() as db:
            credential = db.query(Credential).filter(Credential.id==id).first()
            
            for key, value in kwargs.items():
                if hasattr(credential, key) and value is not None:  # 엔티티에 해당 필드가 있는지 확인
                    setattr(credential, key, value)

            db.commit()
            db.refresh(credential)

            return credential