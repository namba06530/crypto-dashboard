from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.models.user import Base


class RefreshLog(Base):
    __tablename__ = "refresh_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    provider = Column(String, nullable=False)
    success = Column(Boolean, default=True)
    raw_data = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
