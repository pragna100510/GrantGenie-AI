from fastapi import FastAPI
from pydantic import BaseModel

from agents.profile_agent import analyze_startup

app = FastAPI(title="GrantGenie AI")


class Startup(BaseModel):
    description: str


@app.get("/")
def home():
    return {"message": "GrantGenie AI Backend Running"}


@app.post("/analyze")
def analyze(data: Startup):
    result = analyze_startup(data.description)
    return {"result": result}