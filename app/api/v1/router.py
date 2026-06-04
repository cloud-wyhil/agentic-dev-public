from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.hello import router as hello_router

router = APIRouter()
router.include_router(hello_router, prefix="/hello", tags=["hello"])
router.include_router(health_router, prefix="/health", tags=["health"])
