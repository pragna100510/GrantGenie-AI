from fastapi import APIRouter, HTTPException

from schemas.startup import StartupIdea
from agents.profile_agent import analyze_startup

router = APIRouter(tags=["Profile Agent"])


@router.post("/analyze")
def analyze(data: StartupIdea):

    try:
        result = analyze_startup(data.description)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )