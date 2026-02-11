from src.entity.base import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class GuestBook(Base):
    """
    방문록을 관리하는 엔티티입니다.
    """
    __tablename__ = "guestbook_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    guest_id = Column(Integer, ForeignKey("guest_table.id", ondelete="CASCADE"), nullable=False)
    message = Column(String(500), nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # .guest 하나로 방문자 정보에 즉시 접근 가능.
    guest = relationship("Guest", back_populates="guestbooks")