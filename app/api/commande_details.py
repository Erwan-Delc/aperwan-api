from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.commande_details_schema import CommandeDetail, CommandeDetailCreate
from app.crud.commande_details_crud import (
    create_detail, get_by_commande, delete_detail, get_detail
)
from app.crud.commandes_crud import get_commande
from app.db.session import get_db
from app.auth.auth_bearer import get_current_user
from app.schemas.users_schema import User

router = APIRouter()

@router.get("/commande-details/{commande_id}", response_model=list[CommandeDetail], tags=["CommandeDetails"])
def read_details(commande_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    commande = get_commande(db, commande_id)
    if not commande or commande.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Non autorisé à consulter cette commande")
    return get_by_commande(db, commande_id)

@router.post("/commande-details", response_model=CommandeDetail, tags=["CommandeDetails"])
def create(detail: CommandeDetailCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not detail.produit_id and not detail.planche_id:
        raise HTTPException(status_code=400, detail="Il faut fournir soit un produit_id soit un planche_id.")
    
    commande = get_commande(db, detail.commande_id)
    if not commande or commande.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Non autorisé à modifier cette commande")
    
    return create_detail(db, detail)

@router.delete("/commande-details/{detail_id}", tags=["CommandeDetails"])
def delete(detail_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    detail = get_detail(db, detail_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Détail non trouvé")
    
    commande = get_commande(db, detail.commande_id)
    if not commande or commande.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Non autorisé à supprimer ce détail")
    
    delete_detail(db, detail_id)
    return {"ok": True}
