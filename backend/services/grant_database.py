import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "grants.json")


def load_grants():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def search_grants(domain="", country="", stage=""):

    grants = load_grants()

    results = []

    for grant in grants:

        if domain.lower() in grant["sector"].lower() \
                or country.lower() in grant["country"].lower() \
                or stage.lower() in grant["stage"].lower():

            results.append(grant)

    return results