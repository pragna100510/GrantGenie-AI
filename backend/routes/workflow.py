from fastapi import APIRouter

from schemas.startup import StartupIdea
from services.orchestrator import run_agent_workflow

router = APIRouter(tags=["Workflow"])


@router.post("/workflow")
def workflow(data: StartupIdea):

    return run_agent_workflow(data.description)