from src.entity.base import Base
from sqlalchemy import Column, Integer, String, DateTime, func, UniqueConstraint

class Recruiter(Base):
    """
    인사담당자 정보를 관리하는 엔티티입니다.
    """
    __tablename__ = "recruiter_table"

    id = Column(Integer, primary_key=True, autoincrement=True)

    organization = Column(String(50), nullable=False)
    enc_email = Column(String(255), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint("organization", "enc_email", name="_org_email_uc"),
    )