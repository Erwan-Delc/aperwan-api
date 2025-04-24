from pydantic import BaseModel

class PlancheProduitBase(BaseModel):
    planche_id: int
    produit_id: int
    quantité: int = 1

class PlancheProduitCreate(PlancheProduitBase):
    pass

class PlancheProduit(PlancheProduitBase):
    id: int

    class Config:
        from_attributes = True
