import json
from ibm_client import model


def analyze_startup(description: str):
    prompt = f"""
You are an AI startup funding advisor.

Analyze the startup idea below.

Startup:
{description}

Return ONLY valid JSON.
Do not include markdown or ```json.

Format:

{{
  "domain": "",
  "startup_stage": "",
  "technology": [],
  "funding_needed": "",
  "possible_grants": []
}}
"""

    response = model.generate_text(prompt=prompt)

    # Remove markdown if present
    response = response.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(response)
    except Exception:
        return {
            "raw_response": response
        }