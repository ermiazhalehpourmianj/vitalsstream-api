from datetime import datetime
from typing import List, Tuple
from .models import VitalReading, Alert

def evaluate_reading(reading: VitalReading) -> List[Alert]:
    alerts: List[Alert] = []
    issues: List[Tuple[str, str]] = []

    if reading.heart_rate > 120:
        issues.append(("HIGH_HEART_RATE", "high"))
    if reading.spo2 < 92:
        issues.append(("LOW_SPO2", "critical"))
    if reading.temperature_c > 38.0:
        issues.append(("HIGH_TEMPERATURE", "medium"))

    for atype, severity in issues:
        alerts.append(
            Alert(
                reading_id=-1,
                device_id=reading.device_id,
                patient_id=reading.patient_id,
                alert_type=atype,
                severity=severity,
                created_at=datetime.utcnow(),
                resolved_at=None,
            )
        )
    return alerts
