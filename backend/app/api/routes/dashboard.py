from fastapi import APIRouter, Depends
from typing import Dict, Any
from app.api.dependencies import get_current_user, get_db

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/", response_model=Dict[str, Any])
def get_dashboard(current_user=Depends(get_current_user)):
    # Données simulées
    return {
        "total_balance": 1234.56,
        "currency": "EUR",
        "assets": [
            {"symbol": "BTC", "amount": 0.05, "value": 2000.0},
            {"symbol": "ETH", "amount": 0.5, "value": 1000.0}
        ],
        "last_refresh": "2025-06-07T22:00:00Z"
    }
