from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Commande(Base):
    __tablename__ = "commandes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date_commande = Column(DateTime, default=datetime.utcnow)
    date_retrait = Column(DateTime)
    statut = Column(Enum("en attente", "prête", "retirée", "annulée", name="commande_statut"), default="en_attente")

    utilisateur = relationship("User", back_populates="commandes")
