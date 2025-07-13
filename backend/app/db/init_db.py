from app.db.session import engine
from app.models import user, account, refresh_log  # importe tous les modèles pour enregistrer les métadonnées
from app.models.user import Base  # ou depuis db.base_class

def init_db():
    Base.metadata.create_all(bind=engine)
