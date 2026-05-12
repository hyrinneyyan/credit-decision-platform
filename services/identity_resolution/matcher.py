from rapidfuzz import fuzz
from uuid import uuid4

MATCH_THRESHOLD = 80


def normalize_name(name):
    return " ".join(name.lower().strip().split())


def resolve_customer(aecb=None, fraud=None, aml=None, internal=None):

    if aecb and aecb.get("emirates_id"):
        return {
            "canonical_customer_id": internal["customer_id"]
            if internal else str(uuid4()),
            "match_strategy": "EMIRATES_ID",
            "confidence": 1.0
        }
if fraud and internal:
        if (
            fraud["phone"] == internal["phone"]
            and fraud["email"].lower() == internal["email"].lower()
        ):
            return {
                "canonical_customer_id": internal["customer_id"],
                "match_strategy": "PHONE_EMAIL",
                "confidence": 0.95
            }

    if aml and internal:
        similarity = fuzz.ratio(
            normalize_name(aml["name"]),
            normalize_name(internal["full_name"])
        )
if similarity >= MATCH_THRESHOLD and aml["dob"] == internal["dob"]:
            return {
                "canonical_customer_id": internal["customer_id"],
                "match_strategy": "FUZZY_NAME_DOB",
                "confidence": similarity / 100
            }

    return {
        "canonical_customer_id": None,
        "match_strategy": "MANUAL_REVIEW",
        "confidence": 0.0
    }
