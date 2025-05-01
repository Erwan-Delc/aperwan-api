from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.sous_categories_schema import SousCategorie, SousCategorieCreate
from app.crud.sous_categories_crud import get_sous_categories, create_sous_categorie
from app.auth.auth_bearer import get_current_user
from app.schemas.users_schema import User

router = APIRouter(prefix="/sous-categories", tags=["Sous-catégories"])

@router.get("/", response_model=list[SousCategorie])
def list_sous_categories(db: Session = Depends(get_db)):
    return get_sous_categories(db)

@router.post("/", response_model=SousCategorie)
def create(data: SousCategorieCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_sous_categorie(db, data)
