from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import auth
from app.api.routes import account
from app.api.routes import dashboard


app = FastAPI(title="Crypto Dashboard API")

app.include_router(auth.router)
app.include_router(account.router)
app.include_router(dashboard.router)


# Autoriser le frontend à appeler l’API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # à restreindre plus tard
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}
