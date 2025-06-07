# backend/scripts/create_user.py

from dotenv import load_dotenv
import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys

# 🔽 Ajoute le dossier racine /app au path Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.models.user import Base, User

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/crypto_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Créer les tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Créer un utilisateur
username = os.getenv("INIT_USER")
password = os.getenv("INIT_PASSWORD")
hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()

user = User(username=username, password_hash=hashed)
session.add(user)
session.commit()
print("Utilisateur créé.")
