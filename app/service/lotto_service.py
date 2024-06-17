from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from entities import models
from schemas import lotto_schemas
from utils import lotto_dataframe
import datetime

async def create_lotto(db: Session, lotto: lotto_schemas.LottoCreate):
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    db_lotto = models.LottoDrawData(**lotto.model_dump(), create_at=time)
    db.add(db_lotto)
    await db.commit()
    await db.refresh(db_lotto)


def get_all_lotto_info(db: Session):
    return db.query(models.LottoDrawData).all()

async def get_lotto_info(db: Session):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ))
    
    lotto_current_result = await lotto_dataframe.sort_lotto(index, data)
    return lotto_current_result.head()
    
async def get_vertical_chart(db: AsyncSession):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ))
    result = await lotto_dataframe.get_vertical_chart(index, data)
    return {'result': result}
    
async def get_horizontal_chart(db: Session):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ))
    
    result = await lotto_dataframe.get_lotto_result_by_group(index, data)
    return {'result': result}

async def get_pie_chart(db: Session):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ))
    
    result = await lotto_dataframe.get_lotto_result_by_group(index, data)
    return {'result': result}

async def get_odd_even_chart(db: Session):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ))
    
    result = await lotto_dataframe.get_odd_even(index, data)
    return {'result': result}

async def get_recommend_lotto_number(db: Session):
    # index = db.query(models.LottoDrawData.id).all()
    # data =  db.query(
    #     models.LottoDrawData.first_number,
    #     models.LottoDrawData.second_number,
    #     models.LottoDrawData.third_number,
    #     models.LottoDrawData.fourth_number,
    #     models.LottoDrawData.fifth_number,
    #     models.LottoDrawData.sixth_number,
    # ).all()
    pass
    
    