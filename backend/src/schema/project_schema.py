from pydantic import BaseModel, HttpUrl, ConfigDict
from src.entity.project import ProjectCategory
from datetime import date
from typing import Optional

class ProjectBase(BaseModel):
    category: ProjectCategory
    name: str
    description: Optional[str] = None
    start_date: date
    end_date: date
    notion_url: Optional[HttpUrl] = None
    github_url: Optional[HttpUrl] = None
    service_url: Optional[HttpUrl] = None

class UpdateProjectRequest(ProjectBase):
    id: int
    category: Optional[ProjectCategory] = None
    name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class AddProjectRequest(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DeleteProjectResponse(BaseModel):
    is_deleted: bool