from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router
from app.core.config import settings
from app.core.exceptions import generic_exception_handler
from app.core.logging import configure_logging
from app.schemas.common import MessageResponse

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    description="StudyNest Demo FastAPI application",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api/v1")
app.add_exception_handler(Exception, generic_exception_handler)


@app.get("/", response_model=MessageResponse)
async def root():
    return {"message": "Hello, World!"}
