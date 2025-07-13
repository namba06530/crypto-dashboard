from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import json

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.account import Account
from app.models.refresh_log import RefreshLog
from app.schemas.refresh_log import RefreshLogRead
from app.services.fetchers import FETCHERS

router = APIRouter(tags=["refresh"])


@router.post("/refresh")
def refresh_accounts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    accounts = db.query(Account).filter(Account.user_id == current_user.id).all()
    results = {}
    for account in accounts:
        fetcher = FETCHERS.get(account.type)
        if not fetcher:
            continue
        try:
            data = fetcher.fetch(account)
            results[str(account.id)] = data
            log = RefreshLog(
                user_id=current_user.id,
                provider=fetcher.provider,
                success=True,
                raw_data=json.dumps(data),
            )
        except Exception as e:  # noqa: BLE001
            log = RefreshLog(
                user_id=current_user.id,
                provider=fetcher.provider,
                success=False,
                raw_data=str(e),
            )
        db.add(log)
    db.commit()
    return {"status": "ok", "results": results}


@router.get("/refresh-logs", response_model=List[RefreshLogRead])
def get_refresh_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Return the full refresh history for the authenticated user.

    Example response:
    [
        {
            "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
            "provider": "binance",
            "success": true,
            "raw_data": "{...}",
            "created_at": "2025-06-07T22:00:00Z"
        }
    ]
    """

    return (
        db.query(RefreshLog)
        .filter(RefreshLog.user_id == current_user.id)
        .order_by(RefreshLog.created_at.desc())
        .all()
    )
