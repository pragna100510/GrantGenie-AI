import json

from ibm_client import model
from services.grant_database import search_grants
from utils.json_parser import parse_json


def recommend_grants(profile):

    domain = profile.get("domain", "")
    country = profile.get("country", "")
    stage = profile.get("startup_stage", "")

    # Search matching grants from local database
    grants = search_grants(
        domain=domain,
        country=country,
        stage=stage
    )

    # Limit to top matches for the model
    grants = grants[:5]

    prompt = f"""
You are an expert funding advisor.

Startup Profile:

{json.dumps(profile, indent=2)}

Available Grants:

{json.dumps(grants, indent=2)}

Recommend ONLY the best matching grants.

Return ONLY valid JSON.

Return in this exact format:

[
  {{
    "grant": {{
      "name": "",
      "country": "",
      "sector": "",
      "stage": "",
      "funding": "",
      "deadline": "",
      "website": "",
      "eligibility": ""
    }},
    "match_score": "",
    "reason": ""
  }}
]

Do not include markdown.
Do not explain anything.
Do not return any text outside the JSON.
"""

    response = model.generate_text(prompt=prompt)

    return parse_json(response)