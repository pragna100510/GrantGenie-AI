from pydantic import BaseModel


class GrantRecommendation(BaseModel):
    grant_name: str
    match_score: str
    reason: str
    funding: str
    deadline: str
    website: str