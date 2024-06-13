from pydantic import BaseModel
import datetime

class LottoBase(BaseModel):
    first_number: int
    second_number: int
    third_number: int
    fourth_number: int
    fifth_number: int
    sixth_number: int
    bonus_number: int
    
class LottoCreate(LottoBase):
    pass

class Lotto(LottoBase):
    id: int
    create_at: datetime.datetime
    
    class Config:
        from_attributes = True