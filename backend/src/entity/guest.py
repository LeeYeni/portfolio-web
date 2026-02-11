from src.entity.base import Base
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

class Guest(Base):
    """
    방문자 정보를 익명으로 관리하는 엔티티입니다.
    """
    __tablename__ = "guest_table"

    id = Column(Integer, primary_key=True, autoincrement=True)

    uuid = Column(String(36), nullable=False, unique=True, index=True)  # uuid
    nickname = Column(String(20), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    guestbooks = relationship("GuestBook", back_populates="guest", cascade="all, delete-orphan")