from typing import List, Dict, Optional
from .models import VitalReading, Alert

readings_store: List[Dict] = []
alerts_store: List[Dict] = []

def save_reading(reading: VitalReading) -> int:
    reading_id = len(readings_store) + 1
    data = reading.dict()
    data["id"] = reading_id
    readings_store.append(data)
    return reading_id

def save_alerts(reading_id: int, alerts: List[Alert]) -> None:
    for a in alerts:
        item = a.dict()
        item["reading_id"] = reading_id
        alerts_store.append(item)

def get_readings(device_id: Optional[str] = None) -> List[Dict]:
    if device_id:
        return [r for r in readings_store if r["device_id"] == device_id]
    return readings_store

def get_alerts() -> List[Dict]:
    return alerts_store
