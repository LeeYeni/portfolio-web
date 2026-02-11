from pydantic import BaseModel

class ProjectResponse(BaseModel):
    category: str
    name: str
    description: str
    start_date: str
    end_date: str
    notion_url: str
    github_url: str