from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from src.api import chatbot, guest, email, project, credential, recruiter, admin
from src.entity.base import init_db
import uvicorn
from dotenv import load_dotenv

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 서버 시작 전 DB 테이블 초기화
    init_db()

    yield

app = FastAPI(
    description="이예니 개발자의 포트폴리오입니다.",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://portfolio.yeni-lab.org",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot.router)
app.include_router(guest.router)
app.include_router(email.router)
app.include_router(project.router)
app.include_router(credential.router)
app.include_router(recruiter.router)
app.include_router(admin.router)

@app.get("/")
def reed_root():
    return {"message": "이예니 포트폴리오에 오신 것을 환영합니다"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)