from typing import Union, List

from fastapi import APIRouter

from app.models.pydantic.models import DefaultJsonSchema
from app.models.database.services import Services


router = APIRouter()


@router.get("/get_json_schema", response_model=Union[List[DefaultJsonSchema], str])
async def get_all_json_schema() -> Union[List[dict], str]:
    """
    Gives a json_schema for all service
    """
    services = await Services.all()
    if services is None:
        return "No Services"

    return [service.get_json_schema() for service in services]


@router.get("/get_json_schema/{service_name}", response_model=Union[DefaultJsonSchema, str])
async def get_json_schema(service_name: str) -> Union[dict, str]:
    """
    Gives a json_schema for one service
    """
    service = await Services.filter(name=service_name).first()
    if service is None:
        return "Invalid name"
    return service.get_json_schema()
