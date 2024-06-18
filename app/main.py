from fastapi import FastAPI
from routers.lotto import router

app = FastAPI()

@app.get('/')
def get_default():
    return 'hello world'

app.include_router(router)
