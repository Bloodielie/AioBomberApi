from starlette.config import Config

config = Config(".env")

#APP
TITLE = config("TITLE", cast=str, default="AioBomberApi")
DEBUG = config("DEBUG", cast=bool, default=False)

#DATABASE
DATABASE_URL = config("DATABASE_URL", default=None)
