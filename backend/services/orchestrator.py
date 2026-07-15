from agents.profile_agent import analyze_startup
from agents.grant_agent import recommend_grants
import json


def run_agent_workflow(description: str):

    # Step 1 - Profile Agent
    profile = analyze_startup(description)

    # Convert JSON string into Python dictionary if needed
    if isinstance(profile, str):
        profile = profile.replace("```json", "").replace("```", "").strip()
        profile = json.loads(profile)

    # Step 2 - Grant Discovery Agent
    grants = recommend_grants(profile)

    if isinstance(grants, str):
        grants = grants.replace("```json", "").replace("```", "").strip()

        try:
            grants = json.loads(grants)
        except Exception:
            pass

    return {
        "startup_profile": profile,
        "recommended_grants": grants
    }