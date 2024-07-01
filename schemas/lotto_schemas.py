from pydantic import BaseModel
from datetime import datetime

class LottoBase(BaseModel):
    first: int
    second: int
    third: int
    fourth: int
    fifth: int
    sixth: int
    bonus: int
    
class LottoCreate(LottoBase):
    createAt: datetime
    
    class Config:
        from_attributes = True

class LottoResponse(LottoBase):
    id: int
    createAt: datetime
    
    class Config:
        from_attributes = True