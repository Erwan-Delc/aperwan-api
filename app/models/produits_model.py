from sqlalchemy import Column, Integer, String, DECIMAL, Enum, Boolean, Text
from app.db.base import Base
from sqlalchemy import ForeignKey

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    categorie_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    sous_categorie_id = Column(Integer, ForeignKey("sous_categories.id"), nullable=True)
    description = Column(Text, nullable=True)
    prix = Column(DECIMAL(6, 2), nullable=False)
    stock = Column(Integer, default=0)
    image_url = Column(String(255), nullable=True)
    actif = Column(Boolean, default=True)