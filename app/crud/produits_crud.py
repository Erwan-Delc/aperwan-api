from sqlalchemy.orm import Session
from app.models.produits_model import Product
from app.schemas.produits_schema import ProductCreate

def get_produits(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()

def get_produit(db: Session, produit_id: int):
    return db.query(Product).filter(Product.id == produit_id).first()

def create_produit(db: Session, produit: ProductCreate):
    db_produit = Product(**produit.dict())
    db.add(db_produit)
    db.commit()
    db.refresh(db_produit)
    return db_produit

def update_produit(db: Session, db_produit: Product, data: ProductCreate):
    for key, value in data.dict().items():
        setattr(db_produit, key, value)
    db.commit()
    db.refresh(db_produit)
    return db_produit

def delete_produit(db: Session, db_produit: Product):
    db.delete(db_produit)
    db.commit()
