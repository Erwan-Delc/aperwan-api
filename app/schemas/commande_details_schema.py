from pydantic import BaseModel

class CommandeDetailBase(BaseModel):
    commande_id: int
    produit_id: int
    quantité: int
    prix_unitaire: float

class CommandeDetailCreate(CommandeDetailBase):
    pass

class CommandeDetail(CommandeDetailBase):
    id: int

    class Config:
        from_attributes = True
