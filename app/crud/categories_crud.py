from sqlalchemy.orm import Session
from app.models.categories_model import Categorie
from app.schemas.categories_schema import CategorieCreate

def get_categories(db: Session):
    return db.query(Categorie).all()

def create_categorie(db: Session, data: CategorieCreate):
    cat = Categorie(**data.dict())
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat
