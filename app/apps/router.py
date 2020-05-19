from fastapi import APIRouter

from app.apps.services import controller as services
from app.apps.user import controller as user

router = APIRouter()

router.include_router(services.router, prefix='/service', tags=['SERVICES'])
router.include_router(user.router, prefix='/service', tags=['USER OPTIONS'])
