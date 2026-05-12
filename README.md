# Unified Credit Decision Data Platform
This repository contains the implementation design and sample code for a unified credit decision-input platform supporting:

- Personal Finance
- BNPL
- Credit Card Alternative

The solution is designed for AWS using a medallion architecture and supports:
- Batch + real-time ingestion
- Identity resolution
- Immutable audit trails
- Data quality validation
- Portfolio risk monitoring
## Architecture Layers

### Bronze
Immutable raw ingestion layer

### Silver
Standardization + identity resolution

### Gold
Decision snapshots + portfolio marts
- AWS S3
- AWS Glue
- Airflow
- PostgreSQL
- Python
- SQL
- CloudWatch
- SNS

pip install -r requirements.txt

airflow dags trigger aecb_ingestion

Critical validations include:
- Emirates ID format validation
- AML completion
- Fraud score availability
- Duplicate customer detection
  
- Immutable decision snapshots
- Full audit replay
- SHA256 payload hashing
- Policy/model version tracking
