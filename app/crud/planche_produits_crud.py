from sqlalchemy.orm import Session
from app.models.planche_produits_model import PlancheProduit
from app.schemas.planche_produits_schema import PlancheProduitCreate

def get_by_planche(db: Session, planche_id: int):
    return db.query(PlancheProduit).filter(PlancheProduit.planche_id == planche_id).all()

def create(db: Session, data: PlancheProduitCreate):
    db_item = PlancheProduit(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, pp_id: int):
    db_item = db.query(PlancheProduit).filter(PlancheProduit.id == pp_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
