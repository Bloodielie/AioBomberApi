from fastapi import APIRouter

from app.controllers import services, admin

router = APIRouter()

router.include_router(services.router, prefix='/service', tags=['SERVICES'])
router.include_router(admin.router, prefix='/service', tags=['USER OPTIONS'])
