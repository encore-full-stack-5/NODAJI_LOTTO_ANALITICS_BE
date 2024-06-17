from .database import engine, Base, AsyncSessionLocal


async def init_db():
    async with AsyncSessionLocal() as session:
        # 비동기 방식으로 테이블 삭제
        async with session.begin():
            await session.run_sync(Base.metadata.drop_all)
            print("모든 테이블이 성공적으로 삭제되었습니다.")

        # 비동기 방식으로 테이블 생성
        async with session.begin():
            await session.run_sync(Base.metadata.create_all)
            print("테이블이 성공적으로 생성되었습니다.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())