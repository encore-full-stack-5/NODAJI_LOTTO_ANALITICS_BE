from sqlalchemy import Integer, DateTime
from sqlalchemy.sql.schema import Column
from databases.database import Base
import datetime

class LottoDrawData(Base):
    __tablename__ = 'lotto_draw_data'
    
    id = Column(Integer, primary_key=True)
    first_number = Column(Integer, nullable=False)
    second_number = Column(Integer, nullable=False)
    third_number = Column(Integer, nullable=False)
    fourth_number = Column(Integer, nullable=False)
    fifth_number = Column(Integer, nullable=False)
    sixth_number = Column(Integer, nullable=False)
    bonus_number = Column(Integer, nullable=False)
    create_at = Column(DateTime, default=datetime.datetime.now)