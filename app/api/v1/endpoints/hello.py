from fastapi import APIRouter

from app.schemas.common import MessageResponse
from app.services.hello_service import get_hello_message

router = APIRouter()


@router.get("/", response_model=MessageResponse)
async def hello():
    return {"message": get_hello_message()}
