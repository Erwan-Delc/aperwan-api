from sqlalchemy.orm import Session
from app.models.commandes_model import Commande
from app.schemas.commandes_schema import CommandeCreate

def get_commandes_by_user(db: Session, user_id: int):
    return db.query(Commande).filter(Commande.user_id == user_id).all()

def get_commande(db: Session, commande_id: int):
    return db.query(Commande).filter(Commande.id == commande_id).first()

def create_commande(db: Session, commande: CommandeCreate, user_id: int):
    db_commande = Commande(**commande.dict(), user_id=user_id)
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande

def delete_commande(db: Session, commande_id: int):
    db_commande = get_commande(db, commande_id)
    if db_commande:
        db.delete(db_commande)
        db.commit()
    return db_commande
