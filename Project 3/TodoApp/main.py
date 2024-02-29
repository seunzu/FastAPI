from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

import models
from models import Todos
from database import engine, SessionLocal
from routers import auth

app = FastAPI()

# todos.db가 없을 때만 실행
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

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

# TodoRequest: 클라이언트가 전송한 데이터
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found.')

@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    # TodoRequest 모델에서 가져온 데이터 기반으로 새로운 Todos 모델 객체 생성
    todo_model = Todos(**todo_request.dict())

    # DB 세션에 새로운 모델 객체 추가
    db.add(todo_model)
    # 모든 변경 사항 커밋 -> 영구적으로 저장
    db.commit()

@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency,
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()

# app.include_router(auth.router)
# app.include_router(todos.router)
# app.include_router(admin.router)
# app.include_router(users.router)

