from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal

# from routers import auth, todos, admin, users

app = FastAPI()

# todos.db가 없을 때만 실행
models.Base.metadata.create_all(bind=engine)

# sqlalchemy 같은 웹 애플리케이션에서 DB 세션을 관리하는 방법
# DB 연결 효율적으로 관리, 세션 리소스 누수 방지
def get_db():
    db = SessionLocal()
    try:
        # 제너레이터 함수(yield): 실행 중간에 일시 중단, 나중에 다시 시작 O 함수
        # 메모리 효율적 사용/ 대량의 데이터 처리/ 코드 간결하게 작성
        # 제너레이터 함수에서 값을 생성
        yield db
    finally:
        db.close()

# Annotated: 파이썬의 typing 모듈에서 제공하는 클래스/ 변수에 주석 추가
# => 변수에 DB 세션 객체임을 명시
# Depends: FastAPI에서 제공하는 클래스
# / 해당 함수가 필요한 의존성 제공, 요청 처리 전 해당 함수 실행하여 의존성 해결
# => get_db 함수 호출 -> DB 세션 가져옴
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')

# app.include_router(auth.router)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)

