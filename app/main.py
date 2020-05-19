from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from app.config import DATABASE_URL, TITLE, DEBUG
from app.apps.router import router


app = FastAPI(title=TITLE, debug=DEBUG)
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["app.apps.services.models",
                        "app.apps.user.models"]},
    generate_schemas=True,
    add_exception_handlers=False,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )

app.include_router(router, prefix='/api/v1')

