from pydantic import BaseModel
from typing import Optional

class CommandeDetailBase(BaseModel):
    commande_id: int
    produit_id: Optional[int] = None
    planche_id: Optional[int] = None
    quantité: int
    prix_unitaire: float

class CommandeDetailCreate(CommandeDetailBase):
    pass

class CommandeDetail(CommandeDetailBase):
    id: int

    class Config:
        from_attributes = True

