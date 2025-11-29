from fastapi import FastAPI, Path, Query
from typing import List, Optional
from .models import VitalReading
from . import db
from .alerts import evaluate_reading

app = FastAPI(
    title="VitalsStream API",
    version="0.1.0",
    description="Ingest medical-device vitals, run anomaly checks, and expose alerts."
)

@app.post("/api/v1/devices/{device_id}/readings", response_model=dict)
def ingest_reading(
    device_id: str = Path(...),
    reading: VitalReading = None,
):
    payload = reading.copy(update={"device_id": device_id})
    reading_id = db.save_reading(payload)
    alerts = evaluate_reading(payload)
    db.save_alerts(reading_id, alerts)
    return {"reading_id": reading_id, "alerts_raised": len(alerts)}

@app.get("/api/v1/readings", response_model=List[dict])
def list_readings(device_id: Optional[str] = Query(None)):
    return db.get_readings(device_id=device_id)

@app.get("/api/v1/alerts", response_model=List[dict])
def list_alerts():
    return db.get_alerts()
