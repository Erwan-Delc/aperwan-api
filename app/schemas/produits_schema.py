from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    nom: str
    type: str
    description: Optional[str] = None
    prix: float
    stock: int
    image_url: Optional[str] = None
    actif: bool

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True