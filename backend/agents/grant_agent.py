import json

from ibm_client import model
from services.grant_database import search_grants


def recommend_grants(profile):

    domain = profile.get("domain", "")
    country = profile.get("country", "")
    stage = profile.get("startup_stage", "")

    grants = search_grants(
        domain=domain,
        country=country,
        stage=stage
    )

    prompt = f"""
You are an expert funding advisor.

Startup Profile:

{json.dumps(profile, indent=2)}

Available Grants:

{json.dumps(grants, indent=2)}

Recommend ONLY the best grants.

Return JSON only.

Format:

[
 {{
   "grant_name":"",
   "match_score":"",
   "reason":"",
   "funding":"",
   "deadline":"",
   "website":""
 }}
]
"""

    response = model.generate_text(prompt=prompt)

    response = response.replace("```json", "").replace("```", "").strip()

    return response