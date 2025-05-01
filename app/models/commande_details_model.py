from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from app.db.base import Base

class CommandeDetail(Base):
    __tablename__ = "commande_details"

    id = Column(Integer, primary_key=True, index=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"), nullable=False)

    produit_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    planche_id = Column(Integer, ForeignKey("planches.id"), nullable=True)

    quantité = Column(Integer, nullable=False)
    prix_unitaire = Column(DECIMAL(6, 2), nullable=False)
