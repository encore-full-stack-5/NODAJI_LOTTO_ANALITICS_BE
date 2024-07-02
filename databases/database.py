from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from settings import config

SQLALCHEMY_DATABASE_URL = f'postgresql+asyncpg://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}'

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, class_= AsyncSession, bind=engine)

Base: DeclarativeMeta = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        # print("테이블 삭제")
        await conn.run_sync(Base.metadata.create_all)
        print("테이블 생성")