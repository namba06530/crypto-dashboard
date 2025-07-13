from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.models.account import Account
from app.models.refresh_log import RefreshLog
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
