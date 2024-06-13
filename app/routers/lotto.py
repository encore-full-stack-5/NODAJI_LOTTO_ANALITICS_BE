from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from databases.database import get_db
from schemas import lotto_schemas
from service import lotto_service

router = APIRouter()

global_url = '/api/v1/lotto'

@router.get(f'{global_url}/result', response_model=list[lotto_schemas.Lotto])
async def get_all(db: Session = Depends(get_db)):
    return lotto_service.get_all_lotto_info(db)

@router.post(f'{global_url}/result', status_code=201)
def create_lotto(lotto: lotto_schemas.LottoCreate, db: Session = Depends(get_db)):
    lotto_service.create_lotto(db=db, lotto=lotto)