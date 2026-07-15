from pydantic import BaseModel


class StartupIdea(BaseModel):
    description: str


class StartupProfile(BaseModel):
    domain: str
    country: str
    startup_stage: str