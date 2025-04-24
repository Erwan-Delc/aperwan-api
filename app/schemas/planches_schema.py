from pydantic import BaseModel
from typing import Optional

class PlancheBase(BaseModel):
    nom: str
    description: Optional[str] = None
    prix: float
    personnalisable: bool = False

class PlancheCreate(PlancheBase):
    pass

class Planche(PlancheBase):
    id: int

    class Config:
        from_attributes = True
