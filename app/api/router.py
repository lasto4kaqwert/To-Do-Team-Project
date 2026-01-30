from fastapi import APIRouter
from app.api import routers as RT

api_router = APIRouter(prefix="/api")

api_router.include_router(RT.users.router, prefix="/users", tags=["users"])