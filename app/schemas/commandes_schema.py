from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommandeBase(BaseModel):
    date_retrait: Optional[datetime] = None

class CommandeCreate(CommandeBase):
    pass

class Commande(CommandeBase):
    id: int
    user_id: int
    date_commande: datetime
    statut: str

    class Config:
        from_attributes = True
