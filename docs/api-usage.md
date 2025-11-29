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
Expected response:

{
  "reading_id": 1,
  "alerts_raised": 3
}

2. List readings
curl "http://127.0.0.1:8000/api/v1/readings"
curl "http://127.0.0.1:8000/api/v1/readings?device_id=ECG-001"

3. List alerts
curl "http://127.0.0.1:8000/api/v1/alerts"


Now `docs/` looks deliberate, not empty.

---

### 🔹 `sql/03_seed_sample_devices.sql` – minimal seed data

Just a few rows to show intent:

```sql
-- sql/03_seed_sample_devices.sql

-- Seed sample readings for demo / Power BI dashboard.

INSERT INTO device_readings (
    device_id,
    patient_id,
    heart_rate,
    spo2,
    temperature_c,
    timestamp_utc
)
VALUES
    ('ECG-001', 'P-123', 130, 90, 38.5, SYSUTCDATETIME()),
    ('ECG-001', 'P-123', 95, 98, 36.9, DATEADD(MINUTE, -5, SYSUTCDATETIME())),
    ('PULSE-OX-007', 'P-456', 88, 89, 37.2, SYSUTCDATETIME());


This shows:

You understand how to seed data for dashboards/tests.

You’re thinking about Power BI / analytics.

🔹 powerbi/README.txt – explain the dashboard story

Even without a .pbix file yet, you can show the intended design:

VitalsStream Power BI Dashboard (Planned)

This folder is reserved for a Power BI report that connects to the
SQL Server schema defined in the `sql/` scripts.

Planned visuals:
- Card: Active alerts (COUNT of alerts without resolved_at)
- Table: Active alerts by device_id, patient_id, alert_type, severity
- Line chart: heart_rate over time by device_id/patient_id
- Bar chart: alerts by severity

The goal is to demonstrate the full API -> SQL -> dashboard flow
for a medical-device style monitoring scenario.
