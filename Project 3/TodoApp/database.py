# sqlalchemy 라이브러리: 파이썬에서 SQL 사용하기 위한 강력한 ORM(Object Relatinoal Mapper)
# ORM: 객체와 DB 테이블 간의 매핑 제공 -> 객체 지향 프로그래밍 스타일로 DB 다룰 수 있게 해줌
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite DB 파일 경로
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# connect_args={'check_same_thread': False}
# SQLite DB 사용 시 스레드 안정성 조절하는 옵션
# 일반적으로 개발 및 테스트 환경에서 사용
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# engine: sqlalchemy 엔진 객체/ DB와 상호 작용 담당
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base: sqlalchemy 모델을 선언하기 위한 기본 클래스
# 이 클래스 상속 받아 모델 클래스 정의 가능
Base = declarative_base()
