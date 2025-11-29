from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class VitalReading(BaseModel):
    device_id: str = Field(..., example="ECG-001")
    patient_id: str = Field(..., example="P-123")
    heart_rate: int = Field(..., example=122)
    spo2: int = Field(..., ge=0, le=100, example=93)
    temperature_c: float = Field(..., example=38.2)
    timestamp: datetime = Field(..., example="2025-11-28T20:15:00Z")

class Alert(BaseModel):
    reading_id: int
    device_id: str
    patient_id: str
    alert_type: str
    severity: str
    created_at: datetime
    resolved_at: Optional[datetime] = None
