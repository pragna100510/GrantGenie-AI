import json


def extract_json(text: str):
    """
    Extract the first complete JSON object from a model response.
    """

    if not text:
        return None

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    start = text.find("{")

    if start == -1:
        return None

    depth = 0

    for i in range(start, len(text)):

        if text[i] == "{":
            depth += 1

        elif text[i] == "}":
            depth -= 1

            if depth == 0:
                return text[start:i + 1]

    return None


def parse_json(text: str):

    json_text = extract_json(text)

    if json_text is None:
        raise ValueError("No JSON found in model response.")

    return json.loads(json_text)