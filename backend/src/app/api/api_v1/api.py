from fastapi import APIRouter

from ..api_v1.endpoints import users, login


api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
