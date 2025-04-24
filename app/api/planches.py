from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.planches_schema import Planche, PlancheCreate
from app.crud.planches_crud import get_all, get_by_id, create, delete
from app.db.session import get_db

router = APIRouter()

@router.get("/planches", response_model=list[Planche], tags=["Planches"])
def list_planches(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/planches/{planche_id}", response_model=Planche, tags=["Planches"])
def read_planche(planche_id: int, db: Session = Depends(get_db)):
    planche = get_by_id(db, planche_id)
    if not planche:
        raise HTTPException(status_code=404, detail="Planche non trouvée")
    return planche

@router.post("/planches", response_model=Planche, tags=["Planches"])
def create_planche(planche: PlancheCreate, db: Session = Depends(get_db)):
    return create(db, planche)

@router.delete("/planches/{planche_id}", tags=["Planches"])
def delete_planche(planche_id: int, db: Session = Depends(get_db)):
    if not get_by_id(db, planche_id):
        raise HTTPException(status_code=404, detail="Planche non trouvée")
    delete(db, planche_id)
    return {"ok": True}
