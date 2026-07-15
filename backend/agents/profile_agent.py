from ibm_client import model
from utils.json_parser import parse_json


def analyze_startup(description):

    prompt = f"""
You are an expert startup analyst.

Analyze this startup:

{description}

Return ONLY one JSON object.

Never explain.
Never repeat.
Never use markdown.

JSON format:

{{
    "domain":"",
    "country":"India",
    "startup_stage":"",
    "technology":[],
    "funding_needed":""
}}
"""

    response = model.generate_text(prompt=prompt)

    print("\n===== MODEL RESPONSE =====")
    print(response)
    print("==========================\n")

    return parse_json(response)