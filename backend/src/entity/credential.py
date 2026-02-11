from src.entity.base import Base
from sqlalchemy import Column, Integer, Enum, String, Date, Text
import enum

class CredentialCategory(enum.Enum):
    CERTIFICATE = "Certification"
    AWARD = "Award"
    EDUCATION = "Education"
    LANGUAGE = "Language"  # 어학 성적

class Credential(Base):
    """
    증명 가능한 이력을 관리하는 엔티티입니다.
    """
    __tablename__ = "credential_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    category = Column(Enum(CredentialCategory), nullable=False)
    name = Column(String(100), nullable=False)
    issuer = Column(String(100), nullable=False)  # 발행 기관
    description = Column(Text)

    pdf_url = Column(String(255))
    notion_url = Column(String(255))

    issued_date = Column(Date)
