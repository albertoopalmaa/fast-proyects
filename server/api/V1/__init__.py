from fastapi import APIRouter

from .projects_routers import router as projects_routers

#router V1
router_v1 = APIRouter(prefix="/v1")

#agregamos al router v1 las rutas definidas 
router_v1.include_router(projects_routers, tags=["Projects"])