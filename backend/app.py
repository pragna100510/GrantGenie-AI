from fastapi import FastAPI

from routes.profile import router as profile_router
from routes.grants import router as grant_router
from routes.workflow import router as workflow_router

app = FastAPI(
    title="GrantGenie AI",
    version="1.0.0",
    description="AI-powered Grant Discovery using Agentic AI"
)


@app.get("/")
def home():
    return {
        "message": "GrantGenie AI Backend Running"
    }


app.include_router(profile_router)
app.include_router(grant_router)
app.include_router(workflow_router)