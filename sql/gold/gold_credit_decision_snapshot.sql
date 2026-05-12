CREATE TABLE gold_credit_decision_snapshot (
    decision_id UUID PRIMARY KEY,
    customer_id UUID,

    product_type VARCHAR(50),
    decision_ts TIMESTAMP,

    aecb_snapshot JSONB,
    fraud_snapshot JSONB,
    aml_snapshot JSONB,
    customer_snapshot JSONB,

    feature_snapshot JSONB,

    score_version VARCHAR(20),
    policy_version VARCHAR(20),

    final_decision VARCHAR(20),
    decision_reason_codes TEXT[],

    created_at TIMESTAMP DEFAULT NOW()
);
