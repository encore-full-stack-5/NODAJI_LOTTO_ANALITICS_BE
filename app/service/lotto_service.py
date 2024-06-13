from sqlalchemy.orm import Session
from entities import models
from schemas import lotto_schemas
from app.utils import lotto_dataframe
import datetime


def create_lotto(db: Session, lotto: lotto_schemas.LottoCreate):
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    db_lotto = models.LottoDrawData(**lotto.model_dump(), create_at=time)
    db.add(db_lotto)
    db.commit()
    db.refresh(db_lotto)


def get_all_lotto_info(db: Session):
    return db.query(models.LottoDrawData).all()

async def get_lotto_info(db: Session):
    data =  db.query(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ).all()
    index = db.query(models.LottoDrawData.id).all()
    
    lotto_current_result = lotto_dataframe.sort_lotto(index, data)
    return lotto_current_result.head()
    
    
async def get_horizontal_chart(db: Session):
    index = db.query(models.LottoDrawData.id).all()
    data =  db.query(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ).all()

async def get_vertical_chart(db: Session):
    index = db.query(models.LottoDrawData.id).all()
    data =  db.query(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ).all()
    
    get_lotto_result_by_group = lotto_dataframe.get_lotto_result_by_group(index, data)
    return get_lotto_result_by_group

async def get_pie_chart(db: Session):
    index = db.query(models.LottoDrawData.id).all()
    data =  db.query(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ).all()
    
    return lotto_dataframe.get_lotto_result_by_group(index, data)
    

async def get_odd_even_chart(db: Session):
    index = db.query(models.LottoDrawData.id).all()
    data =  db.query(
        models.LottoDrawData.first_number,
        models.LottoDrawData.second_number,
        models.LottoDrawData.third_number,
        models.LottoDrawData.fourth_number,
        models.LottoDrawData.fifth_number,
        models.LottoDrawData.sixth_number,
    ).all()
    
    return lotto_dataframe.get_odd_even(index, data)

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
    
    