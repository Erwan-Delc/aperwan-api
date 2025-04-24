from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.planche_produits_schema import PlancheProduit, PlancheProduitCreate
from app.crud import planche_produits_crud

router = APIRouter()

@router.get("/planches/{planche_id}/produits", response_model=list[PlancheProduit], tags=["PlancheProduits"])
def get_all(planche_id: int, db: Session = Depends(get_db)):
    return planche_produits_crud.get_by_planche(db, planche_id)

@router.post("/planches/produits", response_model=PlancheProduit, tags=["PlancheProduits"])
def add_product_to_planche(data: PlancheProduitCreate, db: Session = Depends(get_db)):
    return planche_produits_crud.create(db, data)

@router.delete("/planches/produits/{pp_id}", tags=["PlancheProduits"])
def remove_product_from_planche(pp_id: int, db: Session = Depends(get_db)):
    pp = planche_produits_crud.delete(db, pp_id)
    if not pp:
        raise HTTPException(status_code=404, detail="Liaison planche-produit introuvable")
    return {"ok": True}
