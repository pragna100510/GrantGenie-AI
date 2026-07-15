import json


def extract_json(text: str):
    """
    Extract the first complete JSON object or JSON array
    from an LLM response.
    """

    if not text:
        return None


    # Remove markdown formatting
    text = text.replace("```json", "")
    text = text.replace("```JSON", "")
    text = text.replace("```", "")

    text = text.strip()



    # Find possible JSON starting points

    obj_start = text.find("{")
    arr_start = text.find("[")



    if obj_start == -1 and arr_start == -1:
        return None



    # Decide whether object or array comes first

    if arr_start != -1 and (
        obj_start == -1 or arr_start < obj_start
    ):

        start = arr_start
        open_char = "["
        close_char = "]"

    else:

        start = obj_start
        open_char = "{"
        close_char = "}"



    depth = 0
    inside_string = False
    escape = False



    for i in range(start, len(text)):

        char = text[i]


        # Handle strings
        if char == '"' and not escape:
            inside_string = not inside_string


        # Handle escape characters
        if char == "\\" and not escape:
            escape = True
            continue

        escape = False



        # Ignore brackets inside strings
        if inside_string:
            continue



        if char == open_char:
            depth += 1


        elif char == close_char:

            depth -= 1


            if depth == 0:

                return text[start:i+1]



    return None




def parse_json(text: str):

    json_text = extract_json(text)


    if json_text is None:

        print("\n===== MODEL RESPONSE =====")
        print(text)
        print("==========================\n")

        raise ValueError(
            "No JSON found in model response."
        )



    try:

        return json.loads(json_text)



    except json.JSONDecodeError as e:


        print("\n===== INVALID JSON EXTRACTED =====")
        print(json_text)
        print("==================================\n")


        raise ValueError(
            f"Invalid JSON returned by model: {e}"
        )