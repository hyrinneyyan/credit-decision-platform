CREATE TABLE silver_customer_events (
    canonical_customer_id UUID,
    source_system VARCHAR(50),
    source_record_id VARCHAR(255),

    emirates_id VARCHAR(20),
    phone VARCHAR(20),
    email VARCHAR(255),
    full_name TEXT,
    dob DATE,

    event_ts TIMESTAMP,
    normalized_payload JSONB,

    match_confidence NUMERIC(5,2),
    match_strategy VARCHAR(50),

    ingestion_ts TIMESTAMP
);
