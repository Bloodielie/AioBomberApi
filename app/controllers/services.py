from typing import Union

from fastapi import APIRouter

from app.models.pydantic_models import DefaultJsonSchema
from app.models.services import Services

router = APIRouter()


@router.get("/get_json_schema", response_model=Union[DefaultJsonSchema, str])
async def get_json_schema(service_name: str) -> Union[dict, str]:
    """
    Gives a json_schema for one service
    """
    a = await Services.filter(name=service_name).first()
    if a is None:
        return "Invalid name"
    return a.get_json_schema()
