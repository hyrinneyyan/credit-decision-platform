import re

EMIRATES_ID_REGEX = r'^\\d{3}-\\d{4}-\\d{7}-\\d{1}$'


def validate_aecb(record):

    errors = []

    emirates_id = record.get("emirates_id")

    if not emirates_id:
        errors.append("MISSING_EMIRATES_ID")

    elif not re.match(EMIRATES_ID_REGEX, emirates_id):
        errors.append("INVALID_EMIRATES_ID")

    if not record.get("credit_score"):
        errors.append("MISSING_CREDIT_SCORE")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
