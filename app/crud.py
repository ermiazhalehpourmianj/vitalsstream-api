# app/crud.py

from typing import List, Optional, Dict
from .models import VitalReading
from . import db

def create_reading(reading: VitalReading) -> int:
    """
    Store a single vital reading and return its generated ID.
    """
    return db.save_reading(reading)

def list_readings(device_id: Optional[str] = None) -> List[Dict]:
    """
    Fetch readings, optionally filtered by device_id.
    """
    return db.get_readings(device_id=device_id)

def list_alerts() -> List[Dict]:
    """
    Fetch all generated alerts.
    """
    return db.get_alerts()
