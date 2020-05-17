from fastapi import APIRouter

from app.controllers import services

router = APIRouter()

router.include_router(services.router, prefix='/service', tags=['SERVICES'])
