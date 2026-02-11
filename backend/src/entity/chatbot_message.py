from src.entity.base import Base
from sqlalchemy import Column, Integer, Enum, String, Text, ForeignKey, DateTime, func
import enum

class Role(enum.Enum):
    user = "user"
    assistant = "assistant"

class ChatbotMessage(Base):
    """
    챗봇 메시지를 관리하는 엔티티입니다.
    """
    __tablename__ = "chatbot_message_table"

    id = Column(Integer, primary_key=True, autoincrement=True)

    thread_id = Column(String(100), nullable=False, index=True)
    guest_id = Column(Integer, ForeignKey("guest_table.id", ondelete="CASCADE"), nullable=False, index=True)
    role = Column(Enum(Role), nullable=False)
    content = Column(Text, nullable=False)

    created_at = Column(DateTime, server_default=func.now(), nullable=False)

