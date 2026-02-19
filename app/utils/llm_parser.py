import json
import re


def extract_json_from_text(text: str) -> dict:
    match = re.search(r"\{.*", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in LLM response")

    json_str = match.group()

    if not json_str.strip().endswith("}"):
        json_str = json_str.strip() + "}"

    return json.loads(json_str)
