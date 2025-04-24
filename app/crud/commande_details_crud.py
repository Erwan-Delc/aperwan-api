from sqlalchemy.orm import Session
from app.models.commande_details_model import CommandeDetail
from app.schemas.commande_details_schema import CommandeDetailCreate

def get_by_commande(db: Session, commande_id: int):
    return db.query(CommandeDetail).filter(CommandeDetail.commande_id == commande_id).all()

def create_detail(db: Session, detail: CommandeDetailCreate):
    db_detail = CommandeDetail(**detail.dict())
    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)
    return db_detail

def delete_detail(db: Session, detail_id: int):
    db_detail = db.query(CommandeDetail).filter(CommandeDetail.id == detail_id).first()
    if db_detail:
        db.delete(db_detail)
        db.commit()
    return db_detail
