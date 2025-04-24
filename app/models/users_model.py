from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    nom = Column(String(100))
    prénom = Column(String(100))
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    commandes = relationship("Commande", back_populates="utilisateur")
