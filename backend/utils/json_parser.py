import json


def extract_json(text: str):
    """
    Extract the first complete JSON object OR JSON array from a model response.
    """

    if not text:
        return None

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    # Decide whether response starts with an object or an array
    obj_start = text.find("{")
    arr_start = text.find("[")

    if obj_start == -1 and arr_start == -1:
        return None

    if arr_start != -1 and (obj_start == -1 or arr_start < obj_start):
        start = arr_start
        open_char = "["
        close_char = "]"
    else:
        start = obj_start
        open_char = "{"
        close_char = "}"

    depth = 0

    for i in range(start, len(text)):

        if text[i] == open_char:
            depth += 1

        elif text[i] == close_char:
            depth -= 1

            if depth == 0:
                return text[start:i + 1]

    return None


def parse_json(text: str):

    json_text = extract_json(text)

    if json_text is None:
        raise ValueError("No JSON found in model response.")

    return json.loads(json_text)