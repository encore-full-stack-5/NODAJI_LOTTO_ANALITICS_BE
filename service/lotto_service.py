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
        models.LottoDrawData.first,
        models.LottoDrawData.second,
        models.LottoDrawData.third,
        models.LottoDrawData.fourth,
        models.LottoDrawData.fifth,
        models.LottoDrawData.sixth,
    ))
    result = await lotto_dataframe.get_vertical_chart(index, data)
    return {'vertical': result}
    
async def get_horizontal_chart(db: AsyncSession):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first,
        models.LottoDrawData.second,
        models.LottoDrawData.third,
        models.LottoDrawData.fourth,
        models.LottoDrawData.fifth,
        models.LottoDrawData.sixth,
    ))
    
    result = await lotto_dataframe.get_lotto_result_by_group(index, data)
    return {'horizontal': result}

async def get_pie_chart(db: AsyncSession):
    index = await db.execute(select(models.LottoDrawData.id))
    data = await db.execute(select(
        models.LottoDrawData.first,
        models.LottoDrawData.second,
        models.LottoDrawData.third,
        models.LottoDrawData.fourth,
        models.LottoDrawData.fifth,
        models.LottoDrawData.sixth,
    ))
    
    result = await lotto_dataframe.get_lotto_result_by_group(index, data)
    return {'pie': result}

async def get_odd_even_chart(db: AsyncSession):
    result = await db.execute(
        select(models.LottoDrawData)
        .order_by(desc(models.LottoDrawData.id))
        .limit(50)
    )
    print(result)
    
    rows = result.scalars().all()
    result_data = [
        lotto_schemas.LottoResponse(
            id= row.id,
            first= row.first,
            second= row.second,
            third= row.third,
            fourth= row.fourth,
            fifth= row.fifth,
            sixth= row.sixth,
            createAt= row.createAt
        )
        for row in rows
    ]
    return result_data