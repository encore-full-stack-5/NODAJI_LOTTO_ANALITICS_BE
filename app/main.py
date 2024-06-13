from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from databases.database import get_db
from schemas import lotto_schemas
from databases.create_table import init_db
from service import lotto_service
from routers.lotto import router

init_db()

app = FastAPI()

global_url = '/api/v1/lotto'

@app.get('/')
def get_default():
    return 'hello world'

app.include_router(router)
