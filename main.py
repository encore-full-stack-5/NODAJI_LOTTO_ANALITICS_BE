from fastapi import FastAPI
from routers.lotto import router
from databases.database import init_db

async def startup(app):
    await init_db()
    yield
    
app = FastAPI(lifespan=startup)


@app.get('/')
def get_default():
    return 'hello world'

app.include_router(router)