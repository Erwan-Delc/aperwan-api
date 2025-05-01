from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class SousCategorie(Base):
    __tablename__ = "sous_categories"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
    categorie_id = Column(Integer, ForeignKey("categories.id"))
