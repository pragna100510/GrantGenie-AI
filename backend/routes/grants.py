from fastapi import APIRouter

from schemas.startup import StartupProfile
from agents.grant_agent import recommend_grants

router = APIRouter(tags=["Grant Agent"])


@router.post("/grants")
def get_grants(profile: StartupProfile):

    result = recommend_grants(profile.model_dump())

    return {
        "recommended_grants": result
    }