from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.commandes_schema import Commande, CommandeCreate
from app.crud.commandes_crud import (
    get_commandes_by_user, get_commande, create_commande, delete_commande
)
from app.db.session import get_db
from app.auth.auth_bearer import get_current_user
from app.schemas.users_schema import User

router = APIRouter()

@router.get("/commandes", response_model=list[Commande], tags=["Commandes"])
def read_commandes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_commandes_by_user(db, current_user.id)

@router.get("/commandes/{commande_id}", response_model=Commande, tags=["Commandes"])
def read_commande_by_id(commande_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    commande = get_commande(db, commande_id)
    if not commande or commande.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Commande non trouvée ou non autorisée")
    return commande

@router.post("/commandes", response_model=Commande, tags=["Commandes"])
def create(commande: CommandeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_commande(db, commande, user_id=current_user.id)

@router.delete("/commandes/{commande_id}", tags=["Commandes"])
def delete(commande_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    commande = get_commande(db, commande_id)
    if not commande or commande.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Commande non trouvée ou non autorisée")
    delete_commande(db, commande_id)
    return {"ok": True}
