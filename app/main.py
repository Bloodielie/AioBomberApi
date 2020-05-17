from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.config import DATABASE_URL
from app.controllers.router import router

app = FastAPI(title="AioBomberApi")
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.models.services"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )

app.include_router(router, prefix='/api/v1')

