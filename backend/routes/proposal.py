from fastapi import APIRouter
from pydantic import BaseModel

from agents.proposal_agent import generate_proposal

router = APIRouter()


class ProposalRequest(BaseModel):
    profile: dict
    grant: dict


@router.post("/proposal")
def proposal(data: ProposalRequest):

    return generate_proposal(
        data.profile,
        data.grant
    )