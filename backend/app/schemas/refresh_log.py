# backend/app/schemas/refresh_log.py

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class RefreshLogRead(BaseModel):
    """Schema for refresh log entries returned by the API."""

    id: UUID
    provider: str
    success: bool
    raw_data: str
    created_at: datetime

    class Config:
        orm_mode = True
