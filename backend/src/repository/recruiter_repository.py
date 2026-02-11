from src.database.mysql import get_mysql_db
from src.entity.recruiter import Recruiter
from sqlalchemy import and_
from typing import List

class RecruiterRepository:
    @staticmethod
    def store(organization: str, enc_email: str) -> None:
        """
        인사담당자 정보를 저장합니다.
        """
        with get_mysql_db() as db:
            existing = db.query(Recruiter).filter(
                and_(
                    Recruiter.organization == organization,
                    Recruiter.enc_email == enc_email
                )
            ).first()

            if not existing:
                new_recruiter = Recruiter(
                    organization=organization,
                    enc_email=enc_email
                )

                db.add(new_recruiter)
                db.commit()

    @staticmethod
    def get_all() -> List[Recruiter]:
        """
        인사담당자 정보를 전부 조회합니다.
        """
        with get_mysql_db() as db:
            return db.query(Recruiter).all()
        
    @staticmethod
    def delete(id: int) -> bool:
        """
        인사담당자 정보를 1개 삭제합니다.
        """
        with get_mysql_db() as db:
            n_deleted = db.query(Recruiter).filter(Recruiter.id==id).delete()

            if n_deleted > 0:
                return True
            
            return False