from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.produits_crud import (
    get_produits, get_produit, create_produit, update_produit, delete_produit
)
from app.schemas.produits_schema import Product, ProductCreate

router = APIRouter()

@router.get("/produits", response_model=list[Product], tags=["Produits"])
def read_produits(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_produits(db, skip=skip, limit=limit)

@router.get("/produits/{produit_id}", response_model=Product, tags=["Produits"])
def read_produit(produit_id: int, db: Session = Depends(get_db)):
    produit = get_produit(db, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return produit

@router.post("/produits", response_model=Product, tags=["Produits"])
def create(produit: ProductCreate, db: Session = Depends(get_db)):
    return create_produit(db, produit)

@router.put("/produits/{produit_id}", response_model=Product, tags=["Produits"])
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
