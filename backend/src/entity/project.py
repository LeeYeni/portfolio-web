from src.entity.base import Base
from sqlalchemy import Column, Integer, String, Enum, Date, Text
import enum

class ProjectCategory(enum.Enum):
    FULLSTACK = "Fullstack"
    BACKEND = "Backend"
    DATA_ENGINEERING = "Data Engineering"
    AI = "AI"

class Project(Base):
    """
    포트폴리오 정보를 관리하는 엔티티입니다.
    """
    __tablename__ = "project_table"

    id = Column(Integer, primary_key=True, autoincrement=True)

    category = Column(Enum(ProjectCategory), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(Text)

    github_url = Column(String(100))
    notion_url = Column(String(255))

    start_date = Column(Date)
    end_date = Column(Date)