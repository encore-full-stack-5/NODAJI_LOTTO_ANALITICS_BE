from pydantic import BaseModel
from datetime import datetime

class LottoBase(BaseModel):
    first_number: int
    second_number: int
    third_number: int
    fourth_number: int
    fifth_number: int
    sixth_number: int
    
    
class LottoCreate(LottoBase):
    bonus_number: int
    create_at: datetime
    
    class Config:
        from_attributes = True

class LottoResponse(LottoBase):
    id: int
    create_at: datetime
    
    class Config:
        from_attributes = True