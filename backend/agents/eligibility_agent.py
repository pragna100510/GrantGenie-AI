import json
from urllib import response

from typer import prompt

from ibm_client import model
from utils.json_parser import parse_json


def check_eligibility(profile, grant):

    prompt = f"""
You are an expert grant eligibility evaluator.

Startup Profile:

{json.dumps(profile, indent=2)}

Grant Details:

{json.dumps(grant, indent=2)}

Determine whether the startup is eligible.

Return ONLY ONE JSON object.

Format:

{{
    "grant_name":"",
    "eligible": true,
    "eligibility_score": 95,
    "matched_conditions": [],
    "missing_requirements": [],
    "recommendation":""
}}

Do not explain outside JSON.
"""

    response = model.generate_text(prompt=prompt)

    response = response.replace("```json", "").replace("```", "").strip()

    start = response.find("{")
    end = response.rfind("}")

    if start != -1 and end != -1:
        response = response[start:end+1]


    response = model.generate_text(prompt=prompt)

    return parse_json(response)