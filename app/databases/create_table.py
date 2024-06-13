from .database import engine, Base


# 데이터베이스 테이블 생성
def init_db():
    Base.metadata.drop_all(bind=engine)
    print("모든 테이블이 성공적으로 삭제되었습니다.")
    
    Base.metadata.create_all(bind=engine)
    print("테이블이 성공적으로 생성되었습니다.")

if __name__ == "__main__":
    init_db()