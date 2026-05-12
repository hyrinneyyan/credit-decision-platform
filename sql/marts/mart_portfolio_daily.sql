CREATE TABLE mart_portfolio_daily (
    snapshot_date DATE,
    product_type VARCHAR(50),

    total_accounts INT,
    active_accounts INT,

    total_exposure NUMERIC(18,2),
    avg_credit_limit NUMERIC(18,2),

    approval_rate NUMERIC(5,2),

    fpd_rate NUMERIC(5,2),
    dpd30_rate NUMERIC(5,2),
    fraud_rate NUMERIC(5,2),

    avg_aecb_score NUMERIC(5,2),

    created_at TIMESTAMP
);
