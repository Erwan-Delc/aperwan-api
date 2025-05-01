from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.categories_schema import Categorie, CategorieCreate
from app.crud.categories_crud import get_categories, create_categorie
from app.auth.auth_bearer import get_current_user
from app.schemas.users_schema import User

router = APIRouter(prefix="/categories", tags=["Catégories"])

@router.get("/", response_model=list[Categorie])
def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)

@router.post("/", response_model=Categorie)
def create(data: CategorieCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_categorie(db, data)
