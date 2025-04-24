from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.commandes_schema import Commande, CommandeCreate
from app.crud.commandes_crud import (
    get_commandes_by_user, get_commande, create_commande, delete_commande
)
from app.db.session import get_db
from app.api.users import oauth2_scheme
from app.core.security import decode_access_token

router = APIRouter()

def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    payload = decode_access_token(token)
    return int(payload.get("sub"))

@router.get("/commandes", response_model=list[Commande], tags=["Commandes"])
def read_commandes(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return get_commandes_by_user(db, user_id)

@router.get("/commandes/{commande_id}", response_model=Commande, tags=["Commandes"])
def read_commande_by_id(commande_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    commande = get_commande(db, commande_id)
    if not commande or commande.user_id != user_id:
        raise HTTPException(status_code=404, detail="Commande non trouvée ou non autorisée")
    return commande


@router.post("/commandes", response_model=Commande, tags=["Commandes"])
def create(commande: CommandeCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    return create_commande(db, commande, user_id)

@router.delete("/commandes/{commande_id}", tags=["Commandes"])
def delete(commande_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    commande = get_commande(db, commande_id)
    if not commande or commande.user_id != user_id:
        raise HTTPException(status_code=404, detail="Commande non trouvée ou non autorisée")
    delete_commande(db, commande_id)
    return {"ok": True}
