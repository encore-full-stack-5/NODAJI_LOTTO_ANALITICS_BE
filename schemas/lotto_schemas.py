from pydantic import BaseModel
from datetime import datetime

class LottoBase(BaseModel):
    first: int
    second: int
    third: int
    fourth: int
    fifth: int
    sixth: int
    
class LottoCreate(LottoBase):
    bonus: int
    createAt: datetime
    
    class Config:
        from_attributes = True

class LottoResponse(LottoBase):
    id: int
    bonus: int
    createAt: datetime
    
    class Config:
        from_attributes = True