from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.commande_details_schema import CommandeDetail, CommandeDetailCreate
from app.crud.commande_details_crud import (
    create_detail, get_by_commande, delete_detail
)
from app.db.session import get_db

router = APIRouter()

@router.get("/commande-details/{commande_id}", response_model=list[CommandeDetail], tags=["CommandeDetails"])
def read_details(commande_id: int, db: Session = Depends(get_db)):
    return get_by_commande(db, commande_id)

@router.post("/commande-details", response_model=CommandeDetail, tags=["CommandeDetails"])
def create(detail: CommandeDetailCreate, db: Session = Depends(get_db)):
    return create_detail(db, detail)

@router.delete("/commande-details/{detail_id}", tags=["CommandeDetails"])
def delete(detail_id: int, db: Session = Depends(get_db)):
    detail = delete_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    return {"ok": True}
