from datetime import datetime

from pydantic import BaseModel


class NewProjectRequest(BaseModel):
    title: str
    status: str = "new"
    description: str = ""


class ProjectRequest(BaseModel):
    title: str | None = None
    status: str | None = None
    description: str | None = None


class ProjectReponse(BaseModel):
    id: int
    title: str
    status: str = "new"
    description: str = ""
    create: datetime
    uodate: datetime
