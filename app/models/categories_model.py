from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Categorie(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False)
