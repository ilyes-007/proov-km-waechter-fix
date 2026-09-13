# test_fleet_report.py
from fleet_report import fleet_summary

SAMPLE = [
    {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
    {"id": "VOS-2210", "odometer": 48400, "last_service_km": 45000},
]


def test_summary_counts_due_cars():
    # Only VOS-4471 is nearly worn, so exactly one car is due.
    assert fleet_summary(SAMPLE)["due"] == 1


def test_summary_does_not_crash_on_missing_reading():
    # A car with no last_service_km must not raise a KeyError — the report must survive.
    # car_wear returns 0.0 for it, and needs_service returns False, so due stays at 1.
    fleet = [
        {"id": "VOS-4471", "odometer": 14900, "last_service_km": 0},
        {"id": "VOS-7788", "odometer": 92000},  # no last_service_km
    ]
    result = fleet_summary(fleet)
    assert "average_wear" in result
    assert result["count"] == 2
    assert result["due"] == 1
