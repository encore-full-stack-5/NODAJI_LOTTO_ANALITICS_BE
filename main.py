from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.lotto import router
from databases.database import init_db

async def startup(app):
    await init_db()
    yield
    
app = FastAPI(lifespan=startup)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # cookie 포함 여부를 설정한다. 기본은 False
    allow_methods=["*"],    # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다.
    allow_headers=["*"],	# 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.
)

@app.get('/')
def get_default():
    return 'hello world'

app.include_router(router)