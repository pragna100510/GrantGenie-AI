import json

from ibm_client import model
from utils.json_parser import parse_json


def generate_proposal(profile, grant):

    prompt = f"""
You are an expert grant proposal writer.

Startup Profile:
{json.dumps(profile, indent=2)}

Grant:
{json.dumps(grant, indent=2)}

Generate a concise professional grant proposal.

IMPORTANT:
- Return ONLY valid JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Every value must be a string.
- Keep each section under 80 words.

Return exactly this format:

{{
    "title":"",
    "executive_summary":"",
    "problem_statement":"",
    "solution":"",
    "budget":"",
    "conclusion":""
}}
"""

    response = model.generate_text(prompt=prompt)

    response = response.replace("```json", "").replace("```", "").strip()

    return parse_json(response)