from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from databases.database import get_db
from schemas import lotto_schemas
from service import lotto_service

router = APIRouter()

global_url = '/api/v1/lotto'

@router.get(f'{global_url}/result', response_model=list[lotto_schemas.Lotto])
async def get_all(db: Session = Depends(get_db)):
    return await lotto_service.get_all_lotto_info(db)

@router.post(f'{global_url}/result', status_code=201)
async def create_lotto(lotto: lotto_schemas.LottoCreate, db: AsyncSession = Depends(get_db)):
    await lotto_service.create_lotto(db=db, lotto=lotto)

@router.get(f'{global_url}/analytics/vertical')
async def get_vertical_chart(db: AsyncSession = Depends(get_db)):
    result = await lotto_service.get_vertical_chart(db=db)
    return result
    
@router.get(f'{global_url}/analytics/horizontal')
async def get_horizontal_chart(db: Session = Depends(get_db)):
    result = await lotto_service.get_horizontal_chart(db=db)
    return result
    
@router.get(f'{global_url}/analytics/pie')
async def get_pie_chart(db: Session = Depends(get_db)):
    result = await lotto_service.get_pie_chart(db=db)
    return result

@router.get(f'{global_url}/analytics/odd_even')
async def get_odd_even_analytics(db: Session = Depends(get_db)):
    return await lotto_service.get_odd_even_chart(db=db)