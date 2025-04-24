from sqlalchemy import Column, Integer, ForeignKey
from app.db.base import Base

class PlancheProduit(Base):
    __tablename__ = "planche_produits"

    id = Column(Integer, primary_key=True, index=True)
    planche_id = Column(Integer, ForeignKey("planches.id"), nullable=False)
    produit_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantité = Column(Integer, nullable=False, default=1)
