from pydantic import BaseModel
from entities import models
from typing import List
import datetime

class LottoBase(BaseModel):
    first_number: int
    second_number: int
    third_number: int
    fourth_number: int
    fifth_number: int
    sixth_number: int
    
    
class LottoCreate(LottoBase):
    bonus_number: int
    
    class Config:
        from_attributes = True

class LottoResponse(LottoBase):
    id: int
    create_at: datetime.datetime
    
    class Config:
        from_attributes = True