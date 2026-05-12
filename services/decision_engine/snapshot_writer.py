import json
import uuid
from datetime import datetime


def build_snapshot(customer, aecb, fraud, aml, features):

    return {
        "decision_id": str(uuid.uuid4()),
        "decision_ts": datetime.utcnow().isoformat(),
        "customer_snapshot": customer,
        "aecb_snapshot": aecb,
        "fraud_snapshot": fraud,
        "aml_snapshot": aml,
        "feature_snapshot": features,
        "score_version": "v1.0",
        "policy_version": "policy_2025_q2"
    }
