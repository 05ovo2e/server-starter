"""FastAPI 애플리케이션 진입점."""

from fastapi import FastAPI

from app.api.v1.routes import router as v1_router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

# API v1 라우터 등록
app.include_router(v1_router)


@app.get("/")
async def root():
    """루트 엔드포인트."""
    return {"message": "Server Starter is running"}
