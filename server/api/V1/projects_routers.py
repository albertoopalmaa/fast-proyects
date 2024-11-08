from typing import Annotated, List

from fastapi import APIRouter, Path, Query

from server.schemas.project_schemas import NewProjectRequest, ProjectReponse, ProjectRequest

router = APIRouter(prefix="/projects")


@router.get(
    "",
    status_code=200,
    responses={
        200: {"description": "Listado de proyectos"},
    },
    description="Retorna una lista paginada con los proyectos del usuario. Si no hay proyectos retorna una lista vacías"
)  # GET /projects
async def get_list(limit:Annotated[int, Query(ge=1, le=1000)] = 10, offset:Annotated[int, Query(ge=0)] = 0) -> List[ProjectReponse]:
    return []


@router.post(
    "",
    status_code=201,
    responses={
        201: {"description": "Proyecto creado"},
    },
    description="Crea un proyecto nuevo por los campos pasados por Body Param. Falla si faltan algunos de los campos obligatorios"
)  # POST/projects
async def create(new_project: NewProjectRequest) -> ProjectReponse:
    #Recibir un objeto
    return new_project


@router.get(
    "/{id}",
    status_code=200,
    responses={
        200: {"description": "Proyecto encontrado"},
        422: {"description": "ID no es un entero válido"},
    },
    description="Retorna un proyecto por ID. Falla si el ID no existe"
)  # GET/projects
async def get_by_id(id: Annotated[int, Path(ge=1)], project: ProjectRequest) -> ProjectReponse:
    return project


@router.patch(
    "/{id}",
    status_code=200,
    responses={
        200: {"description": "Proyecto actualizado"},
        422: {"description": "ID no es un entero válido"},
    },
    description="Actualiza un proyecto con la data del Body Param. Falla si el ID no existe"
)  # PATCH/projects
async def update(id: Annotated[int, Path(ge=1)]) -> ProjectReponse :
    return {"id": id}


@router.delete(
    "/{id}",
    status_code=204,
    responses={
        204: {"description": "Proyecto eliminado"},
        422: {"description": "ID no es un entero válido"},
    },
    description="Elimina un proyecto con id pasado por Path Param. Falla si el ID no existe"
)  # DELETE/projects
async def delete(id: Annotated[int, Path(ge=1)]) -> None:
    return None
