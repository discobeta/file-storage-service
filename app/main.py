from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
from .routes import healthcheck
from app.lib.config import configuration

app = FastAPI(
    title=configuration.app_slug,
    description=configuration.app_description,
    version=configuration.app_version,)

app.add_middleware(
    CORSMiddleware,
    allow_origins=configuration.web_server.get('allow_origins', []),
    allow_credentials=True,
    allow_methods=configuration.web_server.get('allow_methods', []),
    allow_headers=configuration.web_server.get('allow_headers', [])
)

""" Static files """
app.mount("/static", StaticFiles(directory=configuration.static_files), name="static")

""" Health check route used by K8"""
app.include_router(healthcheck.router)

""" Storage routes """
from app.routes import storage





