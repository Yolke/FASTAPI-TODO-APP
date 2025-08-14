from fastapi import APIRouter, HTTPException, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']    
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User,db: Session = Depends(database.get_db)):
    return user.create_user(request,db)

@router.get('/{id}',response_model=schemas.ShowUser)
def get(id:int,db:Session = Depends(database.get_db)):
    return user.get(id,Session)