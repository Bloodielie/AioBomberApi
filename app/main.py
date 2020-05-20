import os
import sys

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.split(dir_path)[0])

from app.apps.router import router
from app.config import TITLE, DEBUG
from app.events import start_app_handler, stop_app_handler

app = FastAPI(title=TITLE, debug=DEBUG)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )

app.include_router(router, prefix='/api/v1')
app.add_event_handler("startup", start_app_handler())
app.add_event_handler("shutdown", stop_app_handler())

if __name__ == "__main__":
    import uvicorn

    port = os.environ.get('PORT')
    file_name = os.path.splitext(os.path.basename(__file__))[0]
    if port is None:
        uvicorn.run(f"{file_name}:app")
    else:
        uvicorn.run(f"{file_name}:app", host="0.0.0.0", port=int(port), log_level="info")
