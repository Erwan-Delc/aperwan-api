from sqlalchemy.orm import Session
from app.models.planches_model import Planche
from app.schemas.planches_schema import PlancheCreate

def get_all(db: Session):
    return db.query(Planche).all()

def get_by_id(db: Session, planche_id: int):
    return db.query(Planche).filter(Planche.id == planche_id).first()

def create(db: Session, planche: PlancheCreate):
    db_planche = Planche(**planche.dict())
    db.add(db_planche)
    db.commit()
    db.refresh(db_planche)
    return db_planche

def delete(db: Session, planche_id: int):
    db_planche = get_by_id(db, planche_id)
    if db_planche:
        db.delete(db_planche)
        db.commit()
    return db_planche
