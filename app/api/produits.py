from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.db.session import get_db
from app.crud.produits_crud import (
    get_produits, get_produit, create_produit, update_produit, delete_produit
)
from app.models.produits_model import Product
from app.schemas.produits_schema import Product as ProductSchema, ProductCreate
from app.schemas.users_schema import User
from app.auth.auth_bearer import get_current_user

router = APIRouter()

# ✅ GET /produits avec filtres facultatifs
@router.get("/produits", response_model=list[ProductSchema], tags=["Produits"])
def read_produits(
    skip: int = 0,
    limit: int = 100,
    categorie_id: Optional[int] = None,
    sous_categorie_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Product)

    if categorie_id:
        query = query.filter(Product.categorie_id == categorie_id)
    if sous_categorie_id:
        query = query.filter(Product.sous_categorie_id == sous_categorie_id)

    return query.offset(skip).limit(limit).all()

# ✅ POST /produits
@router.post("/produits", response_model=ProductSchema, tags=["Produits"])
def create(
    produit: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_produit(db, produit)

# ✅ PUT /produits/{id}
@router.put("/produits/{produit_id}", response_model=ProductSchema, tags=["Produits"])
def update(
    produit_id: int,
    produit_data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    produit = get_produit(db, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    return update_produit(db, produit, produit_data)

# ✅ DELETE /produits/{id}
@router.delete("/produits/{produit_id}", tags=["Produits"])
def delete(
    produit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    produit = get_produit(db, produit_id)
    if not produit:
        raise HTTPException(status_code=404, detail="Produit non trouvé")
    delete_produit(db, produit)
    return {"ok": True}
