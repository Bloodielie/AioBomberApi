from typing import Union, Dict, Any

from pydantic import BaseModel


class DefaultJsonSchema(BaseModel):
    name: str
    url: str
    method: str
    header: Union[Dict[str, Any], None]
    static_data: Union[Dict[str, Any], None]
    dynamic_data: Union[Dict[str, Any], None]


class Unsuccessful(BaseModel):
    status: bool = False
    reason: str


class Successful(BaseModel):
    status: bool = True
