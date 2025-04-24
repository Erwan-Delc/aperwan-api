from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.produits_crud import (
    get_produits, get_produit, create_produit, update_produit, delete_produit
)
from app.models.produits_model import Product  # pour la DB
from app.schemas.produits_schema import Product as ProductSchema, ProductCreate

router = APIRouter()

@router.get("/produits", response_model=list[ProductSchema], tags=["Produits"])
def read_produits(
    skip: int = 0,
    limit: int = 100,
    type: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if type:
        allowed_types = ["vin", "bière", "fromage", "charcuterie", "autre"]
        if type not in allowed_types:
            raise HTTPException(status_code=400, detail=f"Type invalide : {type}")
        query = query.filter(Product.type == type)

    return query.offset(skip).limit(limit).all()


@router.post("/produits", response_model=ProductSchema, tags=["Produits"])
def create(produit: ProductCreate, db: Session = Depends(get_db)):
    return create_produit(db, produit)

@router.put("/produits/{produit_id}", response_model=ProductSchema, tags=["Produits"])
def update(produit_id: int, produit_data: ProductCreate, db: Session = Depends(get_db)):
    produit = get_produit(db, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return update_produit(db, produit, produit_data)

@router.delete("/produits/{produit_id}", tags=["Produits"])
def delete(produit_id: int, db: Session = Depends(get_db)):
    produit = get_produit(db, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    delete_produit(db, produit)
    return {"ok": True}
