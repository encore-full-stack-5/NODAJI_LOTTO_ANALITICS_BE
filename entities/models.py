from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql.schema import Column
from databases.database import Base
import datetime

class LottoDrawData(Base):
    __tablename__ = 'lotto_draw_data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first = Column(Integer, nullable=False)
    second = Column(Integer, nullable=False)
    third = Column(Integer, nullable=False)
    fourth = Column(Integer, nullable=False)
    fifth = Column(Integer, nullable=False)
    sixth = Column(Integer, nullable=False)
    bonus = Column(Integer, nullable=False)
    createAt = Column(DateTime, default=datetime.datetime.now().strftime('%Y-%m-%d'))