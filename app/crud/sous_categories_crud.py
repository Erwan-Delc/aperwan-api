from sqlalchemy.orm import Session
from app.models.sous_categories_model import SousCategorie
from app.schemas.sous_categories_schema import SousCategorieCreate

def get_sous_categories(db: Session):
    return db.query(SousCategorie).all()

def create_sous_categorie(db: Session, data: SousCategorieCreate):
    sous_cat = SousCategorie(**data.dict())
    db.add(sous_cat)
    db.commit()
    db.refresh(sous_cat)
    return sous_cat
