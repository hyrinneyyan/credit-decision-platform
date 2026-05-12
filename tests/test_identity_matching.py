from services.identity_resolution.matcher import resolve_customer


def test_phone_email_match():

    fraud = {
        "phone": "0501234567",
        "email": "test@example.com"
    }

    internal = {
        "customer_id": "123",
        "phone": "0501234567",
        "email": "test@example.com"
    }

    result = resolve_customer(
        fraud=fraud,
        internal=internal
    )

    assert result["match_strategy"] == "PHONE_EMAIL"
