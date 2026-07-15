from fastapi import FastAPI

from routes.profile import router as profile_router
from routes.grants import router as grant_router
from routes.workflow import router as workflow_router
from routes.eligibility import router as eligibility_router
from routes.proposal import router as proposal_router

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="GrantGenie AI",
    version="1.0.0",
    description="AI-powered Grant Discovery using Agentic AI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "GrantGenie AI Backend Running"
    }


app.include_router(profile_router)
app.include_router(grant_router)
app.include_router(workflow_router)
app.include_router(eligibility_router)
app.include_router(proposal_router)