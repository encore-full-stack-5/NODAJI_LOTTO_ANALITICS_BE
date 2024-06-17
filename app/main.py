from fastapi import FastAPI
from databases.create_table import init_db
from routers.lotto import router

app = FastAPI()

# init_db()

@app.get('/')
def get_default():
    return 'hello world'

app.include_router(router)
