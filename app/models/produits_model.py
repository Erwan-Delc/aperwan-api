from sqlalchemy import Column, Integer, String, DECIMAL, Enum, Boolean, Text
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    type = Column(Enum("vin", "bière", "fromage", "charcuterie", "autre", name="product_types"), nullable=False)
    description = Column(Text, nullable=True)
    prix = Column(DECIMAL(6, 2), nullable=False)
    stock = Column(Integer, default=0)
    image_url = Column(String(255), nullable=True)
    actif = Column(Boolean, default=True)