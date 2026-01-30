from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.router import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

def create_app() -> FastAPI:
    app = FastAPI(
        title="Team-Project-API",
        version="0.1.0",
        lifespan=lifespan
    )
    app.include_router(api_router)

    return app

app = create_app()