from fastapi import APIRouter

from app.schemas.common import MessageResponse

router = APIRouter()


@router.get("/live", response_model=MessageResponse)
async def liveness():
    return {"message": "ok"}


@router.get("/ready", response_model=MessageResponse)
async def readiness():
    return {"message": "ready"}
