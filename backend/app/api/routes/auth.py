from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt
from app.schemas.auth import LoginRequest, TokenResponse
from app.core.security import create_access_token
from app.models.user import User
from app.db.session import get_db
from app.core.deps import get_current_user


router = APIRouter()

@router.post("/auth/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == payload.username).first()
    if not user or not bcrypt.checkpw(payload.password.encode(), user.password_hash.encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/auth/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": str(current_user.id),
        "username": current_user.username,
        "created_at": current_user.created_at,
    }
