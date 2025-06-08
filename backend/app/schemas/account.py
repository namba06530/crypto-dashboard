# backend/app/schemas/account.py

from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum
from datetime import datetime

class AccountType(str, Enum):
    wallet = "wallet"
    exchange = "exchange"

class AccountCreate(BaseModel):
    name: str
    type: AccountType
    address: str

class AccountRead(AccountCreate):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
