from tortoise import Tortoise

from app.config import DATABASE_URL


def start_app_handler():
    async def start_app() -> None:
        await Tortoise.init(db_url=DATABASE_URL,
                            modules={
                                "models":
                                    ["app.apps.services.models",
                                     "app.apps.user.models"]
                            })
        await Tortoise.generate_schemas()

    return start_app


def stop_app_handler():
    async def stop_app() -> None:
        await Tortoise.close_connections()

    return stop_app
