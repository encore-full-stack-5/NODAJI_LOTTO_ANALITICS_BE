from sqlalchemy import desc
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from entities import models
from schemas import lotto_schemas
from utils import lotto_dataframe

async def create_lotto(db: AsyncSession, lotto: lotto_schemas.LottoCreate):
    db_lotto = models.LottoDrawData(**lotto.model_dump())
    db.add(db_lotto)
    await db.commit()
    await db.refresh(db_lotto)


async def get_all_lotto_info(db: AsyncSession):
    lotto_result = await db.execute(select(models.LottoDrawData))
    return lotto_result.all()

async def get_lotto_info(db: AsyncSession):
    result = await db.execute(
        select(models.LottoDrawData)
        .order_by(desc(models.LottoDrawData.id))  # 원하는 컬럼으로 대체 가능
        .limit(1)
    )
        
    return result.scalar_one_or_none()
    
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
    return {'vetical': result}
    
async def get_horizontal_chart(db: AsyncSession):
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
    return {'horizontal': result}

async def get_pie_chart(db: AsyncSession):
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
    return {'pie': result}

async def get_odd_even_chart(db: AsyncSession):
    result = await db.execute(
        select(models.LottoDrawData)
        .order_by(desc(models.LottoDrawData.id))
        .limit(50)
    )
    
    rows = result.scalars().all()
    result_data = [
        lotto_schemas.LottoResponse(
            id= row.id,
            first_number= row.first_number,
            second_number= row.second_number,
            third_number= row.third_number,
            fourth_number= row.fourth_number,
            fifth_number= row.fifth_number,
            sixth_number= row.sixth_number,
            create_at= row.create_at
        )
        for row in rows
    ]
    return result_data