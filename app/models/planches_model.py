from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean
from app.db.base import Base

class Planche(Base):
    __tablename__ = "planches"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    prix = Column(DECIMAL(6, 2), nullable=False)
    personnalisable = Column(Boolean, default=False)
