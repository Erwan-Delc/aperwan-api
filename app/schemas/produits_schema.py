from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    nom: str
    description: Optional[str] = None
    prix: float
    stock: int
    image_url: Optional[str] = None
    actif: bool
    categorie_id: Optional[int] = None
    sous_categorie_id: Optional[int] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True