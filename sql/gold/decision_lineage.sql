CREATE TABLE decision_lineage (
    decision_id UUID,
    source_event_id UUID,
    source_system VARCHAR(50),
    payload_hash VARCHAR(64),
    used_in_decision BOOLEAN,
    ingestion_ts TIMESTAMP
);
