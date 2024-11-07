from fastapi import FastAPI

from .api import api_router

fast_projects = FastAPI()

# incluimos el router principal a instancia de fastApi
fast_projects.include_router(api_router)
