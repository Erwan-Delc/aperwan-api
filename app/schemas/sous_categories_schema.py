from pydantic import BaseModel

class SousCategorieBase(BaseModel):
    nom: str
    categorie_id: int

class SousCategorieCreate(SousCategorieBase):
    pass

class SousCategorie(SousCategorieBase):
    id: int
    class Config:
        from_attributes = True
