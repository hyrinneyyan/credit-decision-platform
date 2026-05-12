CREATE TABLE bronze_events (
    event_id UUID PRIMARY KEY,
    source_system VARCHAR(50),
    ingestion_ts TIMESTAMP,
    payload JSONB,
    payload_hash VARCHAR(64),
    source_file_name TEXT,
    schema_version VARCHAR(20)
);
