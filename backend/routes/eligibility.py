from fastapi import APIRouter

from schemas.eligibility import EligibilityRequest
from agents.eligibility_agent import check_eligibility

router = APIRouter(tags=["Eligibility Agent"])


@router.post("/eligibility")
def eligibility(data: EligibilityRequest):

    result = check_eligibility(
        data.startup_profile,
        data.grant
    )

    return result