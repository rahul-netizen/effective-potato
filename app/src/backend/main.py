from argparse import ArgumentParser

import uvicorn
from common.configuration import Configuration
from common.logger import logger
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from health.controller import HealthRestController
from health.manager import HealthServiceManager

parser = ArgumentParser(description="Runs the application server")
parser.add_argument("-e", "--env", help="Path to .env file", default="./etc/.env")
args = parser.parse_args()
load_dotenv(args.env)

# common services

logger.info("Starting application ...")

config = Configuration()
config_env = config.configuration()
app_router = APIRouter()

health_service_manager = HealthServiceManager()
health_rest_contoller = HealthRestController(health_service_manager).prepare(app_router)


app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)
# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router, prefix="/v1/api")

if __name__ == "__main__":
    uvicorn.run("main:app", host=config_env.server_configuration.host, timeout_keep_alive=600, port=int(config_env.server_configuration.port), reload=True)
