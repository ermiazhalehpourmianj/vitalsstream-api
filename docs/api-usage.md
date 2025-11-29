# VitalsStream API – Usage Guide

Base URL (local development):

- `http://127.0.0.1:8000`

Interactive OpenAPI docs:

- `http://127.0.0.1:8000/docs`

## 1. Ingest a reading

**Endpoint**

- `POST /api/v1/devices/{device_id}/readings`

**Example**

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/devices/ECG-001/readings" \
  -H "Content-Type: application/json" \
  -d '{
    "device_id": "ECG-001",
    "patient_id": "P-123",
    "heart_rate": 130,
    "spo2": 90,
    "temperature_c": 38.5,
    "timestamp": "2025-11-28T20:15:00Z"
  }'

- Table: Active alerts by device_id, patient_id, alert_type, severity
- Line chart: heart_rate over time by device_id/patient_id
- Bar chart: alerts by severity

The goal is to demonstrate the full API -> SQL -> dashboard flow
for a medical-device style monitoring scenario.

