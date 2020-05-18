from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from tortoise.exceptions import IntegrityError

from app.models.database.user import User
from typing import Union
from app.models.pydantic.models import DefaultJsonSchema, Unsuccessful, Successful
from app.models.database.services import Services

router = APIRouter()

security = HTTPBasic()


async def user_verification(credentials: HTTPBasicCredentials = Depends(security)) -> User:
    default_raise = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    user = await User.get_or_none(user_name=credentials.username)
    if user is None:
        raise default_raise
    password_check = user.user_verification(credentials.password)
    if not password_check:
        raise default_raise
    return user


@router.put("/", response_model=Union[Unsuccessful, Successful])
async def add_service(data: DefaultJsonSchema, verification=Depends(user_verification)):
    try:
        await Services.create(**data.dict())
    except IntegrityError:
        return Unsuccessful(reason="Failed to create object in database")
    return Successful(status=True)


@router.delete("/{service_name}", response_model=Union[Unsuccessful, Successful])
async def delete_service(service_name: str, verification=Depends(user_verification)):
    service = await Services.get_or_none(name=service_name)
    if service:
        await service.delete()
        return Successful()
    else:
        return Unsuccessful(reason="No such service found.")


@router.post("/{service_name}", response_model=Union[Unsuccessful, Successful])
async def update_service(service_name: str, data: DefaultJsonSchema, verification=Depends(user_verification)):
    try:
        await Services.filter(name=service_name).update(**data.dict())
        return Successful()
    except:
        return Unsuccessful(reason='exception')
