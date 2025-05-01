from fastapi import FastAPI
from app.api import produits
from app.api import users
from app.api import commandes
from app.api import commande_details
from app.api import planches
from app.api import planche_produits
from app.db.base import Base
from app.db.session import engine
from app.api import categories, sous_categories

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Aperwan API")

# Inclusion des routes
app.include_router(produits.router, prefix="")
app.include_router(users.router)
app.include_router(commandes.router)
app.include_router(commande_details.router)
app.include_router(planches.router)
app.include_router(planche_produits.router)
app.include_router(categories.router)
app.include_router(sous_categories.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API Aper'wan 🍷🧀"}