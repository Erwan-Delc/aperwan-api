from fastapi import FastAPI
from app.api import produits
from app.api import users
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aperwan API")

# Inclusion des routes
app.include_router(produits.router, prefix="")
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Aper'wan 🍷🧀"}